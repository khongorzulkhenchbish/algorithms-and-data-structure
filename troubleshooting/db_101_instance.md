### **Interview Scenario: The "One Bad Instance" Mystery**

**Context:** You are the Candidate (PE). The Interviewer is the system.
**Goal:** Identify why 1 instance out of 101 is failing and fix it.

-----

### **Phase 1: Assessment & Isolation**

*The goal here is to narrow down the scope. Is it the code? The network? The host?*

**Interviewer:** "We have a service called `inventory-svc`. It has 101 instances behind a load balancer. Metrics show that exactly **one** instance is consistently returning 500 errors to customers. All other 100 are fine. How would you troubleshoot this?"

**Candidate:** "First, I want to isolate the problem. Is it always the *same* instance failing, or does it move around?"

**Interviewer:** "It is always the same host: `inventory-svc-101`."

**Candidate:** "Since all instances run the same code, I suspect a local environment issue on that specific host. I’ll SSH into `inventory-svc-101` and check the application logs to see the specific error message."

> **Meta Tip:** Don't just guess "reboot it." Engineers need to know *why* it failed so it doesn't happen again.

-----

### **Phase 2: Verification & Evidence**

*The goal is to find the "smoking gun" error message.*

**Candidate:** "I'm on the box. I’ll check the service logs. I’ll assume they are in `/var/log/inventory-svc/`."

```bash
tail -f /var/log/inventory-svc/error.log
# returns the last 10 lines of the log
```

**Interviewer:** "You see a repeating error every time a request comes in: `Error: Connection to database failed. Fatal: sorry, too many clients already`."

**Candidate:** "Interesting. 'Too many clients' suggests the database is rejecting the connection, not that the network is down.
To confirm this isn't an application library bug, I want to try connecting to the DB manually from this host using the command line."

```bash
# Simulating a manual connection attempt
# Manual DB connect
# psql -h [host] -U [user]
psql -h db.production.com -U inventory_user -d inventory_db
```

**Interviewer:** "The command hangs for a moment and then returns: `psql: FATAL: sorry, too many clients already`."

**Candidate:** "Okay, this confirms it’s not the application code; the Database Server itself is rejecting new connections. Since only *this* instance is failing, and the others are working, the DB is likely at its connection limit."

-----

### **Phase 3: Root Cause Analysis (The "Aha\!" Moment)**

*The goal is to match the configuration to the reality.*

**Candidate:** "I need to check the database configuration to see what the connection limit is. Do I have access to the DB, or can I check the config file?"

**Interviewer:** "You have read access to the DB."

**Candidate:** "I'll check the `max_connections` setting."

```sql
SHOW max_connections;
```

**Interviewer:** "The output is `100`."

**Candidate:** "That explains it. We have **101** application instances. If every instance opens a persistent connection to the database (which is standard for backend services), we need 101 connections. But the DB is configured to allow only **100**.
The first 100 instances grabbed a slot. The 101st instance (this one) is being locked out because the pool is full."

-----

### **Phase 4: Remediation (Short & Long Term)**

*Meta PEs are expected to fix the fire NOW, but also prevent it FOREVER.*

**Candidate:** "I have a two-part plan."

#### **1. Immediate Fix (The Band-Aid)**

"I need to increase `max_connections` on the database to accommodate the current fleet size plus a buffer. I'll increase it to **120** to be safe."

  * *Action:* Update `postgresql.conf` (or equivalent) and reload the config.
  * *Verification:* Restart the failing application instance. It should now connect.

#### **2. Long-Term Fix (Engineering the Solution)**

"Simply increasing the limit isn't scalable. If we auto-scale to 200 instances tomorrow, we'll crash again.

  * **Implement Connection Pooling:** We should use a sidecar proxy like `PgBouncer` or a library-level pool so 101 instances can share, say, 50 DB connections.
  * **Add Monitoring:** We need an alert for `DB Connection Usage > 80%` so we know *before* we hit the limit.
  * **Deployment Check:** Add a pre-flight check in our deployment pipeline that fails the build if `Replica Count > DB Max Connections`."

-----

### **Summary of the Guide for Your Interview**

If you get this question, follow this mental map:

1.  **Scope it:** Is it network? Code? Config? (It's config).
2.  **Prove it:** Don't just say "It's probably the DB." **Prove** it by running `psql` or `mysql` manually from the failing box. *This is the step that gets you hired.*
3.  **Do the Math:** Compare `App Instances` vs `DB Config`. (101 vs 100).
4.  **Fix it twice:** Fix the outage now, fix the architecture for later.

#### **Cheatsheet of Commands to remember:**

  * **Check Logs:** `tail -f /var/log/myapp.log` or `journalctl -u myapp`
  * **Check Connections (Net):** `netstat -an | grep 5432` (Postgres port)
  * **Manual DB Connect:** `psql -h [host] -U [user]`
  * **Check DB Config:** `SHOW max_connections;` (Postgres) or `SHOW VARIABLES LIKE 'max_connections';` (MySQL)

src: https://www.youtube.com/watch?v=MRzAWUAhgkw
