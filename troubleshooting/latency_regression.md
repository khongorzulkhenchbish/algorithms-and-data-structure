### an alert fires that shows a sustained latency regression.

This is a classic scenario that tests your ability to correlate **Time** with **Change Events**. In a sustained regression (unlike a spike), something changed in the system state and *stayed* that way.

Here is the simulation for **"The Feature Flag Regression."**

---

# 🤝 Interview Simulation: "The Invisible Change"

**Context:** You are the Candidate (PE).
**Goal:** Identifying why the `search-ranking-svc` got 30% slower starting at 2:00 PM and hasn't recovered.

## Phase 1: Assessment (Characterize the Regression)

**Interviewer:** "Alerts fired at 2:00 PM. P99 Latency for `search-ranking-svc` jumped from 200ms to 350ms. It has been a flat line at 350ms for the last 2 hours. Traffic volume is normal. Error rate is normal. Just slow. Go."

**Candidate:** "A sudden, sustained jump usually implies a specific 'Step Function' change, like a deployment or a configuration update.
First, did a code deployment happen at 2:00 PM?"

**Interviewer:** "No. The last code deployment was 3 days ago."

**Candidate:** "Okay, no code change. Did the traffic mix change? For example, did we suddenly get a influx of 'heavy' requests (like a scraper)?"

**Interviewer:** "Traffic looks identical to yesterday. Same endpoints, same volume."

**Candidate:** "If code is same and traffic is same, the environment must have changed.

1. **Downstream:** Did a dependency (like the Database or a Cache) get slower?
2. **Config:** Was there a `Config` or `Feature Flag` update?"

**Interviewer:** "Good thinking.

1. **Downstream:** The Database P99 latency is flat. No change there.
2. **Config:** Yes, a developer updated a dynamic configuration key `enable_advanced_scoring` to `True` at 2:00 PM."

## Phase 2: Verification (The "Kill Switch" Mentality)

**Candidate:** "That's a strong correlation. A config change exactly matches the latency jump. The new `advanced_scoring` logic is likely CPU intensive or doing extra work.
To verify this **and** mitigate the impact immediately, I want to revert that config change. Can I toggle `enable_advanced_scoring` back to `False`?"

**Interviewer:** "You revert the config. Within 30 seconds, the latency drops back down to 200ms."

**Candidate:** "Great, we have mitigated the incident. The root cause is the `enable_advanced_scoring` feature. Now we need to understand *why* it's slow so the dev can fix it. Is it doing extra I/O or just burning CPU?"

## Phase 3: Deep Dive (Profiling)

**Candidate:** "I'll re-enable the feature on a **single canary host** (if possible) or look at the data from the incident window. I want to see a **CPU Profile** (Flame Graph) of the service while the flag was on."

**Interviewer:** "You pull up the profile. You see that `ScoringFunction()` is now taking 40% of the CPU cycles, specifically in a regex parsing function."

**Candidate:** "It looks like the new feature parses a text field using a heavy regex on every request. This is CPU bound.
**Recommendation:** The developer needs to optimize the regex (or pre-compile it) before re-enabling this feature."

---

# 🧠 Interview Cheatsheet: Sustained Regression

When a graph goes up and stays up (Step Function):

1. **The "What Changed?" Rule:** Systems don't just get slower for no reason.
* **Code:** Was there a deploy?
* **Config:** Was there a Feature Flag/Env Var change? (Very common at Meta).
* **Infrastructure:** Did we lose a cache node? (Cache Miss storm).


2. **The "Upstream/Downstream" Check:**
* If **Your Service** is slow, but **Your Database** is fast -> The problem is in **Your Code** (CPU/Logic).
* If **Your Service** is slow, and **Your Database** is slow -> The problem is the **Database**.


3. **The "Mitigation" First:**
* Don't debug the regex while the site is burning. **Revert first**, debug later.



**Visual Guide for the Interview:**
Imagine the latency graph:

* `_______|-------` (Step up) -> **Change Event** (Deploy/Config).
* `_______/\______` (Spike) -> **Transient Event** (Cron job/Network blip).
* `_______/-------` (Gradual Ramp) -> **Resource Leak** (Memory leak/Connection pool saturation).