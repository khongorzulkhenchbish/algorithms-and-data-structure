# 🧠 Last-Minute Meta PE "Cheat Sheet"

### 1. The "Direction" of the Problem

* **Upstream:** Is the Load Balancer/CDN dropping traffic?
* **Local:** Is it a Memory Leak, CPU saturation, or Disk Full?
* **Downstream:** Is the DB, Cache, or a 3rd party API slow?

### 2. The "Three Pillars" of Investigation

* **Metrics:** Look at the "Four Golden Signals": **Latency, Traffic, Errors, and Saturation.**
* **Logs:** Use `tail`, `grep`, and `journalctl`. Look for "Out of memory" or "Timeout."
* **Profiling:** Use `strace` to see what a process is doing and `lsof` to see what it's talking to.

### 3. Meta-Specific Vocabulary

* **Splay/Jitter:** Adding randomness to cron jobs to avoid spikes.
* **Canary:** Deploying to 1% of the fleet first to catch bugs.
* **Drain:** Taking a host out of rotation to inspect it safely.
* **Backoff:** Waiting longer between retries to avoid "hammering" a dying service.

### 4. The "Golden Rule"

**Mitigate first, Debug second.** If a config change caused the issue, revert it immediately. Don't try to "fix" the config while the site is down. Revert → Restore Service → Debug in Staging.

**One final tip for tomorrow:**
When the interviewer gives you a problem, **think out loud.** Meta PEs are hired for their **process**, not just for knowing the right answer. Explain *why* you are running a command.