### Suppose you are working as a deployment eng and your team works on a service which is called XYZ,
### which takes pictures of cars and bikes. There is already one service which is deployed onto the server,
### but one of the developers is trying to upload a new version of this particular service. They've tried 
### multiple times deploying it but when they try to hit the service, they are not getting the newer response.

This is a classic Production Engineering scenario often called "The Phantom Deployment." It tests your understanding of Linux internals (specifically how the OS handles files and processes) rather than just high-level tools.

Here is a simulation of this interview scenario.

# 🤝 Interview Simulation: The "Stale Deployment"

**Context:** You are the Candidate (Deployment Engineer).
**Goal:** Figure out why the `XYZ` service is returning old responses despite a successful deployment of the new version.

## Phase 1: Assessment and Scope

**Interviewer:** So, the developer says the CI/CD pipeline is green. It says "Deployed Successfully" 30 minutes ago. But when they curl the API, they still get the old JSON response. How do you start?

**Candidate:** First, I want to rule out the basics—sanity checks.

1.  Are they hitting the correct environment (e.g., Production vs. Staging)?
2.  Is there a caching layer (like a CDN or Varnish) in front of the service that might be holding onto the old response?

**Interviewer:** Good questions. They are definitely hitting the correct Production IP. We checked the CDN, and we bypassed it using `curl -H "Cache-Control: no-cache"`, but the response is still the old version.

**Candidate:** Okay, so the server itself is serving the old code. Since the pipeline reported success, I need to verify what is actually happening on the server. I'll SSH into one of the instances.

## Phase 2: Verification (Disk vs. Memory)

**Candidate:** I'm on the server. First, I want to verify if the new code artifact actually arrived. I'll check the timestamp of the application file. Let's assume it's a Python application named `server.py` in `/var/www/xyz/`.

```bash
ls -l /var/www/xyz/server.py
```

**Interviewer:** The output shows the file timestamp is **30 minutes ago** (matching the deployment time). The file size is also slightly different from the previous version.

**Candidate:** Okay, this is interesting. The **file on disk is new**. But the **response is old**. This implies the running process is not reading the file I'm looking at.

I need to check the running process. I want to see how long the service process has been running.

```bash
# Check the PID and start time of the service
ps -eo pid,lstart,cmd | grep python
```

**Interviewer:** You see the process for `server.py`. The `lstart` (start time) column shows the process started **25 days ago**.

## Phase 3: Root Cause Analysis (The Linux Internals)

**Candidate:** That’s the smoking gun\! The file on the disk was updated 30 minutes ago, but the process handling requests has been running for 25 days. The process was never restarted.

**Interviewer:** But wait, the deployment script overwrote the file. Why is the old process still running the old code if the file is changed?

**Candidate:** This is a specific behavior of Linux file systems. When a process opens a file, it holds a file descriptor pointing to the **inode** (the physical data on the disk), not the filename.

When the deployment script "overwrote" the file (likely using `cp` or `mv`), it created a *new* inode for the new file and unlinked the old filename. However, because the running process still has the *old* inode open, the OS keeps that old data alive for the process. The process is happily reading the "deleted" file from memory/disk, completely ignoring the new file sitting on the disk with the same name.

## Phase 4: Remediation

**Candidate:** To fix this immediately and prevent it in the future:

### 1\. Immediate Fix

We simply need to restart the service to force it to drop the old file handle and load the new one.

```bash
sudo systemctl restart xyz-service
```

Once restarted, the `ps` command will show a new start time, and the API should return the new response.

### 2\. Long-Term Fix

We need to audit the deployment script. It seems to be doing a file copy but missing the restart signal.

  * **Update Script:** Ensure the script runs `service xyz restart` or sends a `HUP` signal (`kill -HUP [PID]`) after copying the files.
  * **Better Approach:** Move to an "Atomic Deployment" strategy. Deploy the new code to a new directory (e.g., `/release/v2`), then switch a symlink (`/current -> /release/v2`), and *then* restart the service. This ensures consistency.

-----

# 🧠 Interview Cheatsheet: The "Stale Code" Mental Model

If the "Deploy was successful" but "App is old":

1.  **Check the Cache:** Is a CDN/Browser confusing you? (Bypass it).
2.  **Check the Disk:** Did the new file actually arrive? (`ls -l --time-style=long-iso`).
3.  **Check the Process:** Is the app uptime older than the file timestamp? (`ps -ef` or `uptime`).
4.  **The "Why":** Remember that **Linux processes hold inodes, not filenames**. Replacing a file does not magically update a running process.

**Common variation:**

  * **Deleted files filling disk:** Sometimes you delete a huge log file to free space, but `df -h` still says 100% full. Why? Because the process (like Apache/Nginx) is still holding the file open. You must restart the process to actually free the space. This is the exact same Linux principle.