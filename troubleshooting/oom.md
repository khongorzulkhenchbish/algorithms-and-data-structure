# 🤝 Interview Simulation: The "Vanishing Process"

**Context:** You are the Candidate (PE).
**Goal:** Determine why the `thumbnail-service` restarts every 6-8 hours.

## Phase 1: Assessment (Rule out the Application)

**Interviewer:** "We have a background worker, `thumbnail-service`. Every 6 to 8 hours, the monitoring system alerts that the service has restarted. There are no tracebacks or panic messages in the application's standard error logs. It just stops and restarts. How do you investigate?"

**Candidate:** "First, I want to confirm it is actually restarting and not just failing a health check. I'll check the service status."

```bash
systemctl status thumbnail-service

```

**Interviewer:** "The output shows `Active: active (running)` but the `uptime` is only 20 minutes. The `Restart Count` is high."

**Candidate:** "Okay, so the process is definitely terminating. Since you mentioned there are no stack traces in the app logs, it suggests the application isn't crashing due to a bug in its own code (like a NullPointer). It’s being **killed** by something external.
I suspect the OS is killing it. I need to check the Kernel logs."

## Phase 2: Verification (The "OOM" Hunter)

**Candidate:** "I'll check `dmesg` or the system logs for signals sent by the kernel."

```bash
dmesg -T | grep -i "kill"
# OR
grep -i "oom" /var/log/syslog

```

**Interviewer:** "You see several entries like this:
`[Wed Oct 11 14:00:00] Out of memory: Kill process 12345 (thumbnail-svc) score 850 or sacrifice child`."

**Candidate:** "That's it. The **OOM (Out of Memory) Killer** is terminating the process. The application is consuming more memory than is available (or allowed by its Cgroup), and the Linux Kernel is stepping in to save the system by killing the biggest consumer."

## Phase 3: Root Cause Analysis (Leak vs. Capacity)

**Candidate:** "Now I know *how* it's dying, but I need to know *why*. Is the service just under-provisioned, or is there a memory leak?"

"I would ask to see a graph of Memory Usage over time for this container/host."

**Interviewer:** "Here is the graph. . It starts at 500MB, steadily climbs to 4GB over 6 hours, drops to zero (the crash), and starts over."

**Candidate:** "The 'Sawtooth' pattern is the signature of a **Memory Leak**. If it were just under-provisioned, it would hit the limit immediately upon processing a large image. The steady climb over hours proves the application is failing to release memory after processing tasks."

## Phase 4: Remediation

**Candidate:**

### 1. Immediate Mitigation (Stabilize)

"We can buy time by increasing the memory limit for the service (if physical RAM allows) or configuring the service to restart gracefully *before* it hits the limit (e.g., restart every 4 hours)."

### 2. Engineering Fix (The Real Solution)

"We need to profile the code to find the leak.

* **Tooling:** Use a memory profiler (like `pprof` for Go, or `Valgrind` for C++) to inspect the heap.
* **Fix:** Identify the object or buffer that isn't being garbage collected and fix the logic."

---

# 🧠 Interview Cheatsheet: The "Silent Crash"

If an app dies without saying "Goodbye" (no logs):

1. **The Suspect:** It's almost always **The Kernel**.
2. **The Command:** `dmesg` (Display Message) is your best friend. It shows what the Kernel is thinking.
3. **The Keyword:** `grep -i oom` or `grep -i kill`.
4. **The Pattern:**
* **Flat line at max memory:** Under-provisioned (needs more RAM).
* **Diagonal line up (Sawtooth):** Memory Leak (needs code fix).



**Bonus Knowledge (Linux Internals):**
The interviewer might ask: *"How does Linux decide who to kill?"*
**Answer:** Linux assigns every process an `oom_score`. The badness heuristic points higher scores to processes using a lot of RAM. You can protect critical processes (like `sshd`) by setting their `oom_score_adj` to a negative number, effectively making them invisible to the OOM killer.