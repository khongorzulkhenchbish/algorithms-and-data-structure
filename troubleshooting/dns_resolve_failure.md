### user report suggest that your service has an outage, but your team hasn't received any alerts.

This is a high-level "Blind Spot" scenario. It’s a favorite at Meta because it tests two things: your ability to think outside the "service bubble" and your understanding of the **entire request lifecycle** (DNS → Load Balancer → Service).

If your service is "down" but your internal metrics are "green," the problem is almost certainly happening **before** the request reaches your application logic.

---

# 🤝 Interview Simulation: The "Invisible Outage"

**Context:** You are the Candidate (PE).
**Goal:** Figure out why users can’t reach the service even though the internal dashboard shows 100% success.

## Phase 1: Scoping the "Silent" Failure

**Interviewer:** "Our Customer Support team is flooded with reports that users cannot access `messenger-web`. However, your service dashboard shows 0% error rates and healthy CPU/Memory. In fact, traffic volume on your dashboard looks slightly lower than usual. What do you do?"

**Candidate:** "This is a classic 'monitoring blind spot.' If my service thinks it's 100% healthy but users can't get in, the requests aren't reaching my service. I need to check the **edge** of our network.
First: Are the users seeing a specific error? (e.g., 'Connection Refused', 'DNS Probe Finished', or a '404'?)"

**Interviewer:** "Users are reporting 'Site cannot be reached' and 'DNS_PROBE_FINISHED_NXDOMAIN'."

**Candidate:** "NXDOMAIN! That is a major clue. It means the Domain Name System (DNS) cannot find the IP address for our service. The outage isn't in the code; it’s in the **Routing/Infrastructure** layer. I'll start by testing DNS resolution myself."

```bash
dig messenger-web.meta.com

```

## Phase 2: Identifying the Layer

**Interviewer:** "The `dig` command returns `status: NXDOMAIN` and an empty answer section."

**Candidate:** "Okay, the hostname isn't resolving. This explains why my service metrics are green: if users can't find the IP, they never send the request, so my service never sees an error.
I need to check the **DNS Control Plane**. Was there a recent change to our DNS records or the TTL (Time to Live)?"

**Interviewer:** "Our DNS team says no manual changes were made today. However, we use an automated system that updates DNS records based on Load Balancer health."

**Candidate:** "Interesting. If the automation thinks the Load Balancers are dead, it might have pulled the DNS records. I'll check the health of the **External Load Balancer (ELB)**."

## Phase 3: Root Cause (The Health Check Loop)

**Candidate:** "I'll check the Load Balancer logs or the health check status of the ELB."

**Interviewer:** "You see that the ELB marked all backends as 'Unhealthy' and consequently withdrew the DNS record. But when you look at the backends (your service), they are actually running fine."

**Candidate:** "If the service is fine but the LB thinks it's dead, the **Health Check** itself is the problem. What is the LB using to check health? Is it a simple TCP check or an HTTP endpoint?"

**Interviewer:** "It's an HTTP check on `/health`. You check the logs for `/health` on your service and you see thousands of `404 Not Found` errors starting 10 minutes ago."

**Candidate:** "Wait, if the service is fine but `/health` is 404, did someone move the health check file or change the routing configuration? I'll check the latest config push."

**Interviewer:** "Aha! A developer pushed a change to the Nginx/Envoy config to 'refactor' the paths, and they accidentally renamed `/health` to `/status`, but didn't update the Load Balancer configuration."

## Phase 4: Remediation

**Candidate:**

### 1. Immediate Fix

"We have two choices for a quick fix:

* Revert the Nginx/Envoy config change to restore the `/health` endpoint.
* Update the Load Balancer config to point to the new `/status` endpoint.
**I will revert the config change** as it is the fastest way to get back to a 'known good' state."

### 2. Long-Term Fix

"The 'Blind Spot' happened because we don't monitor **DNS Resolution** or **External Availability** from the user's perspective.

* **External Probing (Canaries):** We need 'Blackbox' monitoring—probes that live outside our network (like in AWS or Google Cloud) and try to hit our public URL every minute. If they fail, we alert, even if internal metrics are green.
* **Config Validation:** Add a CI/CD rule that prevents merging a config change if it deletes or renames a known health-check path."

---

# 🧠 Interview Cheatsheet: The "Invisible Outage"

When "User says Down" but "Dashboard says Up":

1. **Check the "Edge":**
* **DNS:** Is the domain resolving? (`dig`, `nslookup`).
* **CDN/LB:** Is the Load Balancer rejecting traffic before it hits the app?


2. **Look for "Missing Traffic":**
* If your "Total Requests" graph drops suddenly but "Success Rate" stays at 100%, you have lost your connection to the outside world.


3. **The "Blackbox" vs. "Whitebox" Rule:**
* **Whitebox:** Metrics from *inside* the app (CPU, internal logs).
* **Blackbox:** Metrics from *outside* (Can users reach us?).
* *Meta PE Tip:* You need both. This outage was a failure of Whitebox-only monitoring.


**The "NXDOMAIN" Clue:**
In any interview, if the interviewer says "NXDOMAIN," stop looking at the code and start looking at DNS, Domain registrars, or automated Traffic Management (GSLB).