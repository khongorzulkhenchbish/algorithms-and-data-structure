### Your metrics indicate that there are sporadic issues that are impacting user experience

This scenario is a classic "intermittent issue" problem. These are harder than "hard down" scenarios because you have to catch the system in the act or find the pattern in the noise.

The following is a simulated interview guide for the "Synchronized Cron Job" scenario, a favorite at Meta to test if you can correlate time-series data with system resources.

# 🤝 Interview Simulation: The "Periodic Latency Spike"

**Context:** You are the Candidate (PE). The Interviewer is the system.
**Goal:** Identify why the `feed-service` is having sporadic user experience issues.

## Phase 1: Scoping (Defining "Sporadic")

**Interviewer:** "Our monitoring shows that the `feed-service` is triggering a 'High Latency' alert. It’s not constant, but user reports say the app feels 'stuttery' sometimes. How do you troubleshoot this?"

**Candidate:** "First, I need to define 'sporadic.' Is it random, or is there a pattern? And does it affect all hosts or just a few?"

**Interviewer:** "Good question. Looking at the aggregate graphs, it affects **all hosts** in the fleet simultaneously. It seems to happen roughly once an hour and lasts for about 2 minutes."

**Candidate:** "If it affects all hosts at the same time, it's likely not a random hardware failure or a 'bad apple' host. It sounds like a synchronized event. I suspect a scheduled task or a 'thundering herd' of traffic.
I want to look at the **Latency Graph** overlayed with **Error Rates**."

## Phase 2: Verification (Catching the Ghost)

**Candidate:** "I see the spikes at XX:15 every hour. I want to SSH into one of the hosts and observe it *during* that 15-minute mark. I'll wait for the next occurrence."
*(Simulating the wait... the clock hits XX:15)*
"Okay, the issue is happening now. I'll run `top` to check the system vitals."

```bash
top -n 1
```

**Interviewer:** "You see the following:

  * **User CPU:** 10%
  * **System CPU:** 5%
  * **Idle:** 0%
  * **Wait (%wa):** **85%**"

**Candidate:** "That's the smoking gun\! `85% wa` means **I/O Wait**. The CPU is sitting idle waiting for the Disk to finish reading/writing. The application is slow not because it's working hard, but because it's blocked waiting for the disk.
I need to find *what* is eating the disk I/O."

## Phase 3: Root Cause Analysis

**Candidate:** "I'll use `iotop` to see which process is consuming the disk bandwidth."

```bash
sudo iotop -oPa
```

**Interviewer:** "You see a process named `/usr/bin/backup_logs.sh` at the top, writing at 200MB/s."

**Candidate:** "So, there is a backup script running. Since this happens on *all* hosts at the same time, I suspect a **cron job** that was deployed to the entire fleet with a fixed time."
"I'll check the cron schedule."

```bash
cat /etc/cron.d/backup-job
```

**Interviewer:** "It reads: `15 * * * * root /usr/bin/backup_logs.sh`."

**Candidate:** "There it is. Every hour at minute 15, *every single server* in our fleet wakes up and tries to compress/ship logs. This saturates the disk I/O, causing the main application (which also needs to log or read DBs) to hang waiting for the disk."

## Phase 4: Remediation (The "Splay" Fix)

**Candidate:**
**Immediate Fix:** Stop the current backup process if it's impacting production traffic severely.

**Long-Term Engineering Fix:**
The problem is synchronization. We need to introduce **Jitter** (randomness) or **Splay**.
Instead of running at `15 * * * *` (hardcoded minute 15), we should use a randomized sleep or a systemd timer with `RandomizedDelaySec`.

**Example Fix (Systemd Timer):**

```ini
[Timer]
OnCalendar=hourly
RandomizedDelaySec=600  # Spread the start time over 10 minutes
```

This ensures that while all servers back up once an hour, they don't all smash their disks at the exact same second.

-----

# 🧠 Interview Cheatsheet: "Sporadic" Issues

When the problem comes and goes, **Look for the Pattern**.

1.  **The "One Bad Apple":** If the error rate is low (e.g., 1%), it might be **one single host** failing.
      * *Check:* Is the error grouped by HostID?
2.  **The "Cron Job":** If the error is periodic (every hour, every day at midnight).
      * *Check:* `top` for **%wa** (IO Wait) or `cron` logs.
3.  **The "Garbage Collection":** If the latency spikes are frequent but short (milliseconds/seconds) and random.
      * *Check:* Language runtime metrics (Java/Go GC pause times).

**Metric to watch:** **`%wa` (I/O Wait)**. It is the silent killer of latency. If your CPU is low but the app is slow, it's almost always Disk I/O or Network I/O.