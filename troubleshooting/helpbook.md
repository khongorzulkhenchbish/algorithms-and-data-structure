### State = Observations + Questions + Hypotheses + Actions
At any moment, you may have:

- **Observations** – Objective facts (metrics, log lines, error messages, user reports) that you already know or confirm during the investigation. Measured or reported facts (e.g., “P95 latency is 6s,” “Disk is 92% full,” “Only EU users are affected”).
- **Questions** – “Is Redis responding normally?” / “What’s the 5xx rate?”
- **Hypotheses** – “Disk might be full,” “Consumer lag might be growing.”
- **Actions** – Concrete steps to gain evidence or rule something out. A question could also be an action, but here we focus on non-question actions.

Prioritize the **short term** fix. The top priority when an incident occurs is to restore service as quickly as possible to minimize the impact on end users. It will buy you a time to figure out the root cause analysis and implement the long term fix.


Each **action** will give you new data:
- this might support or invalidate your hypothesis.
- it may answer a question, but raise a new one.
- it may change the priority of your next move.

### Proactive Resource Monitoring
#### Set Thresholds & Alerts
Establish clear thresholds and alerts for critical resource metrics. Key metrics to monitor include:
- **CPU usage**: Set alerts for when CPU utilization consistently exceeds a certain percentage (e.g., 80%) for an extended period.
- **Memory usage**: Define thresholds for high memory consumption or low free memory conditions.
- **I/O wait**: Monitor disk I/O wait times and set alerts for when they surpass acceptable levels.
- **Error rates**: Configure alerts for when error rates (e.g., 5xx responses for HTTP services) exceed normal baselines.
- **Latency**: Set up alerts for when request or response latencies consistently exceed targets (e.g., 500ms).

For example, you might configure an alert to trigger when a service's CPU usage exceeds 85% for more than 5 minutes. This would give you an early warning of potential resource saturation and allow you to investigate and take action before it leads to performance degradation or service unavailability.

#### Issue types:
**System resources:** "OOM", "Disk Full", "CPU Saturation", "I/O Wait"

**Service issues:** "Timeout", "5xx Errors", "Latency", "Deadlock"

**Component-specific:** "Database", "Cache", "Queue", "Gateway"

#### How to handle Out-Of-Memory (OOM)?

**Check logs for OOM → Restart service → Temporarily add swap → Increase memory limits → Escalate.**

What It Is

A server's RAM (Random Access Memory) is fully used, forcing Linux's OOM (Out-Of-Memory) killer to terminate processes. This may cause critical services to crash or repeatedly restart.

Red Flags ⚠️

- Sudden service crash without clear application errors.
- Kernel logs with "Out of memory" or "Killed process …" messages.
- Container or service repeatedly restarting (systemctl status).

Quick Confirm

Check for OOM in system logs
    
    dmesg | grep -i "out of memory"
    journalctl -k | grep -i "oom"

Observe free RAM

    free -m  # shows memory in MB
    top      # press M to sort by memory usage

Immediate Mitigation

Restart affected service
    
    sudo systemctl restart <service-name>

Add temporary swap (use fast local SSD or low-latency cloud SSD volumes such as AWS gp3/Azure Premium; avoid high-latency network disks like classic NFS)

    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile

🛑 Creating swap may hide underlying memory leaks. Remove ASAP:
  
    sudo swapoff /swapfile && sudo rm /swapfile

Increase container or VM memory limits

Kubernetes/Docker: adjust resources.limits.memory.

💡 Beginner Tip: If you see "OOM" in kernel logs, restart the killed process and monitor with top to check if memory climbs again.

Long-Term Fix (🚧 Dev Only)

- Diagnose memory leaks:
- Share memory graphs (Grafana, Prometheus) with developers.

C++: provide core dump (snapshot of program's memory); devs run gdb / Valgrind in staging.

Python: use tracemalloc in tests.

Limit unbounded caches: Developers should set a maximum size or TTL (Time-To-Live) on caches.

Refactor large data structures: Replace or offload growing structures to disk.

Configure proper memory limits in containers: Set both resources.requests.memory and resources.limits.memory appropriately in Kubernetes.


### Issue 02 — Out-Of-Disk Space

#### Cheat-line:
#### Check disk usage → Delete/archive logs → Vacuum journals → Escalate.

What It Is

Filesystem or partition is 100% full, preventing new data writes (logs, swap, temporary files). Services fail to log or crash; new swap cannot be allocated.

Red Flags ⚠️

"No space left on device" errors.

/var/log stops growing or shows truncated files.

Symptoms similar to OOM, but plenty of RAM remains.

#### Quick Confirm
Check disk usage

    df -h  # disk usage
    df -i  # inode usage

Find largest directories (du -x -m works on any recent GNU coreutils; BSD/macOS users can use -k or -h instead)
  
    du -x -m /* 2>/dev/null | sort -n -k1,1 | tail

If /var/log is large:

    du -x -m /var/log/* | sort -n -k1,1 | tail

#### Immediate Mitigation

Delete or archive old logs ⚠️

    sudo rm /var/log/myapp/*.old.log

Or archive:

    sudo tar czf /backup/logs-$(date +%F).tgz /var/log/myapp/*.1
  
Truncate safe-to-clear logs ⚠️

    sudo truncate -s 0 /var/log/huge.log

Vacuum systemd journals

    sudo journalctl --vacuum-size=200M

Move logs to larger volume

Attach new disk in cloud, mount (e.g., /mnt/newdisk), move non-critical directories.

#### Long-Term Fix (🚧 Ops/Dev)

- Enable log rotation: Ensure /etc/logrotate.d/myapp retains 7 days and compresses older logs.
- Test rotation:
    
      sudo logrotate --debug /etc/logrotate.d/myapp

- Review app log levels: Set "INFO" or "WARN" in prod, not "DEBUG".
- Adjust partition sizes: Dedicate larger volume for /var/log.
- Automate alerts: Monitor node_filesystem_avail_bytes with Prometheus; alert if <10% free.

#### Issue 03 — CPU Saturation (High Load)

#### Cheat-line:
#### Check CPU load → Pause/kill rogue processes → Scale up instances → Escalate.

What It Is

Server CPU at or near 100%; tasks queue, causing slow responses or timeouts.

Red Flags ⚠️

top or htop shows processes near 100 % CPU and load average higher than the number of CPU cores while %wa (I/O-wait) remains below ~5 %.

CPU usage > 80 % sustained.

Slow responses while memory and disk I/O look normal.

#### Quick Confirm

- Check load average

      uptime  # load averages

  If the 1-/5-/15-minute load averages sit well above the number of CPU cores and %wa (I/O-wait) is low (< 5 %), the host is CPU-bound.High load with elevated %wa (≥ 10 %) instead signals disk-I/O saturation.

- Top CPU consumers
    
      top  # press P to sort by CPU usage

  Or:

      ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head

#### Immediate Mitigation

Pause or terminate rogue process ⚠️

    sudo kill -SIGTERM <PID>

If unresponsive:

    sudo kill -SIGKILL <PID>

⚠️ SIGKILL ungraceful; prefer SIGTERM. For containers, use:

    sudo docker kill <container-id>

Scale out instances

Behind load balancer or orchestrator:
orchestrator-cli scale my-app --replicas=4
Long-Term Fix (🚧 Dev Only)
Profile app code: Provide CPU charts to developers. Use perf (only with approval and perf_event_paranoid=1) or cProfile/py-spy in staging.
Move batch jobs off-peak: Schedule intensive tasks outside peak hours.
Autoscaling & rate limiting: Auto-scale if CPU >80%; throttle surges via API gateway.
Issue 04 — Thread/Process Deadlocks & Resource Contention
Cheat-line:
Identify hung processes → Restart affected service → Escalate.

What It Is
A deadlock occurs when threads or processes each hold a resource the other needs, causing indefinite waiting. Resource contention occurs when processes compete for limited resources, degrading performance.

Red Flags ⚠️
Service seems stuck—requests queued, resources appear normal.
Threads blocked while resources underutilized.
Logs with repeated "could not acquire lock" or processes in uninterruptible sleep.
Quick Confirm
Identify hung processes
ps -eo pid,ppid,stat,cmd | awk '$3 ~ /D|T/'
D: uninterruptible sleep, typically I/O or lock waits.
T: stopped or traced.
Check file locks
sudo lsof | grep "<resource_name_or_path>"
Immediate Mitigation
Restart affected service
sudo systemctl restart <service-name>
Remove hung node from load balancer
Temporarily stop routing traffic to the affected instance.
Kill specific hung process (last resort) ⚠️
sudo kill -9 <PID>
⚠️ SIGKILL ungraceful—may leave partial state.

Long-Term Fix (🚧 Dev Only)
Enforce lock ordering: Always acquire locks in a consistent order.
Minimize lock scope: Use smaller critical sections or finer-grained locks.
Use try-lock with timeout: Replace standard locks with timeout-based locks (e.g., std::timed_mutex).
Tune resource pools: Set reasonable maximum pool sizes and connection timeouts.

## Issue 05 — Database Latency / Performance Degradation
### Cheat-line:
#### Check slow queries → Kill slow queries → Scale up DB → Escalate.

### What It Is
Slow database responses causing downstream timeouts or latency due to missing indexes, lock contention, or resource saturation.

### Red Flags ⚠️
- P95/P99 query latency spikes.
- Logs show "SQL query timed out" or similar errors.
- Connection count at maximum.

### Quick Confirm

1. Check slow-query log (MySQL)

        sudo tail -n 50 /var/log/mysql/mysql-slow.log

2. Inspect active connections

        mysql -e "SHOW STATUS LIKE 'Threads_connected';"
3. Observe resource usage

        top
        vmstat 1 5

- High %iowait suggests disk saturation.

### Immediate Mitigation

1. Kill long-running queries ⚠️

        mysql -e "SHOW PROCESSLIST;"
        mysql -e "KILL <Id>;"
        # or: KILL CONNECTION <Id>

2. Temporarily scale up or add read replicas

- Direct read traffic to replicas if available; increase resources on primary.

3. Use rolling restart or read-only mode (last resort) 🛑
Avoid full systemctl restart mysqld; use rolling restarts or read-only mode.

### Long-Term Fix (🚧 Dev/DBA)

- **Optimize indexes**: Use EXPLAIN to analyze slow queries and add missing indexes.
- **Review transactions**: Break large updates/deletes into batches.
- **Tune connection pools**: Adjust max_connections cautiously.
- **Scale resources**: Plan scaling if CPU or I/O is consistently high.

Issue 06 — Service Timeouts (Inter-service Calls)
Cheat-line:
Check timeout logs → Increase timeout → Implement fallback → Escalate.

What It Is
Service A calls Service B with a timeout. If B takes longer, A returns an error while B may still finish.

Red Flags ⚠️
Logs show "request timed out" or "504 Gateway Timeout."
Service B logs indicate completion after Service A timeout.
Quick Confirm
Check timeout messages
sudo grep -R "timeout" /var/log/service-A/
Test downstream latency
time curl -s http://service-B.internal.local/api/health
Check P95/P99 in monitoring (e.g., Grafana)
Immediate Mitigation
Increase timeout in Service A (if allowed)
# /etc/service-A/config.yaml
timeout_ms: 1000  # increased from original value
Throttle traffic or queue inbound requests to Service B
Implement cached or fallback responses
Long-Term Fix (🚧 Dev Only)
Align timeouts with SLAs: Ensure Service A's timeout exceeds Service B's typical response.
Optimize Service B performance: Use profiling (cProfile, gdb) to fix slow endpoints.
Implement exponential backoff: Avoid retries hammering Service B.
Add circuit breakers/bulkheads: Prevent cascading failures.
Issue 07 — High Error Rates / Spike in 5xx Responses
Cheat-line:
Check logs for 5xx → Rollback deploy → Scale/restart → Escalate.

What It Is
A sudden increase in server-side HTTP errors (5xx). Causes include code bugs, resource exhaustion, or failing dependencies.

Red Flags ⚠️
Monitoring shows a sudden spike in 5xx errors.
Clients report "Internal Server Error."
Logs reveal new stack traces or repeated failures.
Quick Confirm
Filter logs for 5xx codes
sudo grep -R "HTTP/1\.[01]\" 5[0-9][0-9]" /var/log/myservice/
Check health endpoint
curl -I http://localhost:8080/health
"200 OK" is healthy; "500+" indicates issues.
Check downstream dependencies
sudo grep -R -e "connection refused" -e "timeout" /var/log/myservice/
Immediate Mitigation
Rollback recent deployment
Revert to last stable version.
Scale out or restart instances
Redeploy or restart services to distribute load.
Throttle or redirect traffic
Temporarily reduce load via load balancer (return 503).
Long-Term Fix (🚧 Dev)
Resolve code bugs: Reproduce errors in staging, attach debuggers (gdb, pdb).
Address resource exhaustion: Examine CPU/RAM usage (free -m, top) during errors.
Fix dependencies: Check logs (/var/log/mysql/error.log, /var/log/redis/redis-server.log) and tune queries or scale out.
Implement retry logic: Prevent immediate retry storms with backoff and jitter.
Issue 08 — Cache Invalidation / Cache Stampede
Cheat-line:
Check cache metrics → Serve stale data → Throttle requests → Escalate.

What It Is
Many cache entries expire simultaneously, causing clients to bypass the cache and overload the backend.

Red Flags ⚠️
Cache hit ratio drops significantly.
Database load spikes dramatically.
Logs filled with cache misses in short intervals.
Quick Confirm
Check cache hit/miss metrics
Use cache dashboard or CLI to verify hit/miss ratio.
Watch database metrics
top
vmstat 1 5
High I/O wait or CPU indicates overload due to cache misses.
Check application logs
grep -R "cache miss key=" /var/log/myservice/cache.log
Immediate Mitigation
Serve stale cache entries (if supported)
Temporarily serve expired entries to mitigate load.
Throttle traffic
Apply rate limits at API gateway.
Extend cache TTL temporarily
# Extend TTL on hot keys
redis-cli EXPIRE <key> 3600  # Example: add 1 hour
Long-Term Fix (🚧 Dev)
Scatter key expirations: Add jitter to TTL values.
Implement request coalescing: Ensure only one request rebuilds cache entry on miss.
Adopt write-through/write-behind caching: 💡 Write-behind caching reduces backend load but may risk data loss. Enable only if tolerable or pair with Redis AOF (appendonly everysec).
Monitor cache health: Alert on high cache miss ratios (>20% for 2+ mins).
Issue 09 — Disk I/O Bottlenecks (Slow Reads/Writes)
Cheat-line:
Check I/O wait → Move logs off volume → Upgrade disk → Escalate.

What It Is
Poor disk performance causing service slowness. High I/O wait indicates CPU idle time spent waiting on disk.

Red Flags ⚠️
High I/O wait (%wa ≥ 20% in top).
Logs report disk I/O timeouts.
Slow database queries that normally perform well.
Quick Confirm
Check I/O wait
top
vmstat 1 5
Review disk usage and type
lsblk
df -h
Identify slow or nearly full disks.
Immediate Mitigation
Offload logs to different volume
sudo systemctl stop rsyslog
sudo systemctl stop systemd-journald   # flush & stop journal writes
sudo mv /var/log /mnt/newdisk/var_log
sudo ln -s /mnt/newdisk/var_log /var/log
sudo systemctl start systemd-journald
sudo systemctl start rsyslog
# ⚠️ Test on a non-critical node first; boot scripts may expect /var/log early.
Pause high-I/O jobs
ps -eo pid,cmd | grep backup-script.sh
sudo kill <pid>
Upgrade disk performance
Switch to SSD or provisioned IOPS.
Long-Term Fix (🚧 Dev/DBA)
Migrate critical data to SSD or provisioned IOPS.
Optimize database I/O: Ensure indexes fit memory, archive old data.
Reduce log verbosity: Set appropriate log levels.
Shard or partition large tables: Spread large datasets across multiple disks.
Issue 10 — Latency Spikes / Elevated P95 & P99 Latencies
Cheat-line:
Check latency logs → Scale out service → Enable caching → Escalate.

What It Is
Sudden jumps in request-response time, particularly affecting the 95th and 99th percentiles (P95/P99), causing intermittent but significant delays.

Red Flags ⚠️
Monitoring dashboards show spikes in P95/P99 latency.
Users report intermittent slow responses.
Logs occasionally indicate high request completion times.
Quick Confirm
Inspect latency logs
grep -R "request completed in" /var/log/myservice/ | awk '{print $NF}' | sort -n | tail -n 10
Correlate with system metrics
top
vmstat 1 5
High CPU or I/O wait during latency spikes indicates resource contention.
Profile slow functions (advanced) 💡
Use profiling tools (cProfile, perf) in staging to pinpoint slow code paths.
Immediate Mitigation
Scale out or add capacity
Increase the number of service replicas to distribute the load.
Enable short-lived caching
Cache expensive database or API calls briefly to prevent repeated expensive operations.
Drain or evict unhealthy instances
Temporarily remove instances showing high latency (e.g., due to garbage collection pauses).
Long-Term Fix (🚧 Dev Only)
Investigate hot code paths: Profile and optimize slow operations.
Tune memory management: Consider faster allocators or periodic process restarts.
Optimize external calls: Implement proper indexing and timeout settings.
Adjust connection pools: Match concurrency with appropriate pool sizes and timeouts.
Section II – Common Component-Level Issues
2.1 API Gateway / Ingress Controllers
Issue 2.1.1 — Rate-Limit Misconfiguration
Cheat-line:
Check logs for HTTP 429 → Increase rate limit → Whitelist trusted IPs → Escalate.

What It Is
Gateway rate limiter incorrectly blocking legitimate traffic or allowing excessive load downstream.

Red Flags ⚠️
Sudden HTTP 429 "Too Many Requests" responses.
Resource starvation downstream due to insufficient rate limiting.
Quick Confirm
Search logs for HTTP 429
sudo grep -R '" 429 ' /var/log/api-gateway/access.log
Test with curl
for i in {1..20}; do curl -s -o /dev/null -w "%{http_code}\n" http://gateway.example.com/api/health; done
Monitor gateway metrics 💡
Check gateway metrics dashboards for spikes in HTTP 429 responses.
Immediate Mitigation
Raise rate-limit temporarily
rateLimit:
  requestsPerMinute: 2000  # previously 500
Whitelist trusted clients
Add trusted client IPs or API keys to bypass rate limits.
Use Retry-After header
Inform clients when to retry after receiving a 429 response.
Long-Term Fix (🚧 Dev & Ops)
Align limits with traffic patterns: Adjust limits based on historical peak load.
Implement client-specific limits: Use API keys or user IDs for granular control.
Adaptive rate limiting: Use burst allowances for handling traffic spikes.
Monitoring & alerting: Alert if HTTP 429 responses exceed 1% for over 5 minutes.
2.1.2 — Payload Size Limits
Cheat-line:
Check logs for HTTP 413 → Increase payload limit → Request compression → Escalate.

What It Is
Gateway rejects large payloads, responding with HTTP 413 "Payload Too Large."

Red Flags ⚠️
Clients report HTTP 413 errors.
Logs show payload rejection after config changes.
Quick Confirm
Check logs for HTTP 413
sudo grep -R '" 413 ' /var/log/api-gateway/access.log
Reproduce error with curl
dd if=/dev/zero bs=1M count=2 of=/tmp/bigfile
curl -i -X POST -H "Content-Type: application/octet-stream" \
  --data-binary @/tmp/bigfile http://gateway.example.com/api/upload
Immediate Mitigation
Temporarily increase payload size
bodySizeLimit: 5m  # previously 1m
Request client compression
Advise clients to gzip payloads to reduce size.
Long-Term Fix (🚧 Dev & Ops)
Set per-endpoint payload limits: Assign limits according to endpoint needs.
Validate payloads upstream: Implement checks to handle oversized payloads gracefully.
Document limits clearly: Inform clients via API documentation.
Monitor payload sizes: Alert on unexpected payload size increases.
2.2 Message Queues / Streaming Platforms
Issue 2.2.1 — Broker OOM or Disk Full → Partitions Offline
Cheat-line:
Check disk/memory → Free resources → Restart broker → Escalate.

What It Is
Queue brokers run out of memory (OOM) or disk space, causing partitions or topics to go offline.

Red Flags ⚠️
Logs indicate "OutOfMemoryError" or "No space left on device."
Producers fail to write data.
Quick Confirm
Check disk usage
df -h | grep /var/lib/queue-broker
Check memory usage
top
dmesg | grep -i "out of memory"
Immediate Mitigation
Free disk space ⚠️
sudo rm /var/log/queue-broker/*.old.log
Add temporary swap (fast local SSD only) ⚠️
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
Restart broker process
sudo systemctl restart queue-broker
Long-Term Fix (🚧 Dev & Ops)
Increase disk/memory capacity: Expand resources permanently.
Configure log rotation/retention: Avoid disk saturation.
Set memory limits: Tune JVM flags (e.g., -Xmx, -Xms).
Monitor resources: Alert early on high usage.
Issue 2.2.2 — Consumer Lag Spikes
Cheat-line:
Check consumer lag → Scale consumers → Pause producers → Escalate.

What It Is
Consumers fall behind message production, increasing lag.

Red Flags ⚠️
Monitoring shows consumer lag spikes.
Logs warn "fetch timeout" or "processing backlog."
Quick Confirm
Check consumer lag
queue-cli lag --consumer-group analytics-workers --topic events
Inspect consumer logs
sudo grep -R "fetch timeout" /var/log/consumer-worker/
Immediate Mitigation
Restart consumer
sudo systemctl restart consumer-worker
Temporarily scale consumers
orchestrator-cli scale consumer-worker --replicas=4
Pause or throttle producers
Temporarily reduce message production.
Long-Term Fix (🚧 Dev)
Optimize consumer code: Refactor slow processing logic.
Increase parallelism: Add partitions or threads.
Tune batch settings: Adjust consumer batch sizes.
Monitor latency: Alert if processing latency grows significantly.
Issue 2.2.3 — Partition Rebalancing Storms
Cheat-line:
Check rebalance logs → Throttle rebalancing → Add capacity → Escalate.

What It Is
Broker cluster reassigns partitions, causing temporary high latency.

Red Flags ⚠️
Logs show frequent rebalance or replica sync issues.
High CPU and disk I/O across brokers.
Quick Confirm
Check broker logs for rebalancing
sudo grep -R "rebalance" /var/log/queue-broker/broker.log
Monitor broker metrics
top
iostat -x 1 5
Immediate Mitigation
Throttle rebalance
queue-cli alter-config --throttle-rebalance 5MB/s
Restart broker cautiously ⚠️
Restart broker with "no-auto-rebalance" if supported.
Add temporary capacity
Introduce additional brokers to reduce load.
Long-Term Fix (🚧 Ops)
Stagger rebalancing: Limit partition movements per step.
Use rack-aware assignments: Minimize cross-rack traffic.
Automate throttling: Set default rebalance speeds.
Monitor ISR: Alert if replicas fall below minimum sync count.
2.3 Database Issues
Issue 2.3.1 — Connection Pool Exhaustion
Cheat-line:
Check connections → Kill idle connections → Increase max connections → Escalate.

What It Is
Database connections exceed the maximum allowed, causing new connections to fail.

Red Flags ⚠️
Logs show "Too many connections" or "Connection timeout."
Monitoring indicates connections at maximum capacity.
Quick Confirm
Check active connections (MySQL)
mysql -e "SHOW STATUS LIKE 'Threads_connected';"
Scan for idle connections
mysql -e "SHOW PROCESSLIST;" | grep Sleep
Immediate Mitigation
Kill idle connections ⚠️
mysql -e "SELECT id FROM information_schema.PROCESSLIST WHERE COMMAND='Sleep' AND TIME > 300;"
mysql -e "KILL <id>;"
Increase max_connections temporarily
Edit /etc/mysql/my.cnf:

[mysqld]
max_connections = 2000
Then restart:

sudo systemctl restart mysqld
Restart application (if connection leaks suspected)
Long-Term Fix (🚧 Dev & DBA)
Tune connection pool settings: Set proper pool size and idle timeouts.
Enable leak detection: Add warnings if connections aren't returned.
Implement health checks: Auto-restart pods if pool usage stays high.
Monitor usage: Alert if connections approach 80% of max.
Issue 2.3.2 — Lock Contention
Cheat-line:
Inspect locks → Kill blocking transactions → Restart queries → Escalate.

What It Is
Long transactions holding locks cause delays for other database operations.

Red Flags ⚠️
Database logs show transaction lock waits or deadlocks.
Application logs record "Lock wait timeout" errors.
Quick Confirm
Inspect InnoDB status
mysql -e "SHOW ENGINE INNODB STATUS\G" | grep -A15 "LATEST DETECTED DEADLOCK"
List lock waits
mysql -e "SELECT r.trx_id AS waiting_trx, r.trx_query AS waiting_query, b.trx_id AS blocking_trx, b.trx_query AS blocking_query FROM information_schema.innodb_lock_waits w JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id;"
Immediate Mitigation
Kill blocking transaction ⚠️
mysql -e "KILL <blocking_thread>;"
Retry or abort waiting queries
Long-Term Fix (🚧 Dev & DBA)
Break large transactions: Use smaller batch updates/deletes.
Add appropriate indexes: Minimize locked rows.
Implement retry logic: Retry queries after short delays.
Monitor lock wait time: Alert on average waits exceeding 500ms.
2.4 Other Issues
Cache-Related Issues (TTL too small, Stale Reads due to Lag or Weak Consistency)
Cheat-line:

Check cache hit rates → Temporarily increase TTL → Implement read-after-write/monotonic reads → Escalate.

What It Is
Cache entries expire too soon, causing frequent database hits or stale data reads due to replication lag or weak consistency models (no guaranteed read-after-write or monotonic reads).

Red Flags ⚠️
Sudden drop in cache hit rates, spike in database load.
Logs frequently show "cache miss".
Users experience stale or inconsistent data.
Quick Confirm
Check cache metrics
redis-cli INFO stats | grep -E 'keyspace_hits|keyspace_misses'
Inspect TTLs on frequently accessed keys
redis-cli TTL <key>
Verify replication or consistency model
Check if system uses asynchronous replication or eventual consistency, causing potential lag.
Immediate Mitigation
Increase cache TTL temporarily
# Extend TTL on hot keys
redis-cli EXPIRE <key> 3600  # Example: add 1 hour
Serve stale entries (if supported)
Configure cache to serve slightly stale entries during TTL resets.
Throttle traffic if database overloaded
Long-Term Fix (🚧 Dev & Ops)
Adjust TTL strategy: Increase default TTL or add jitter.
Implement read-after-write: Ensure cache updates synchronously with writes.
Ensure monotonic reads: Route client requests consistently to the same data store instance to avoid stale reads.
Monitor and alert: Set alerts for cache miss ratios and replication lag.
Clock Drift Issues
Cheat-line:

Check system clock → Sync clocks (timedatectl/chrony) → Restart dependent services → Escalate.

What It Is
System clocks across nodes are unsynchronized, leading to authentication failures (JWT/OAuth) and inaccurate timestamps.

Red Flags ⚠️
"JWT token expired/not yet valid" authentication errors.
Log timestamps inconsistent across nodes.
Quick Confirm
Check NTP synchronization
sudo timedatectl status
Manually compare system clocks
date +"%Y-%m-%d %H:%M:%S"
ssh other-node date +"%Y-%m-%d %H:%M:%S"
Immediate Mitigation
Synchronize clocks immediately
sudo timedatectl set-ntp true
Restart dependent services (JWT/OAuth)
sudo systemctl restart service-A
Long-Term Fix (🚧 Dev & Ops)
Automate NTP synchronization: Ensure chrony or systemd-timesyncd is enabled.
Monitor clock drift: Alert on drift exceeding thresholds.
Validate time synchronization in deployments: Embed time checks in CI/CD pipelines.
Use UTC for all timestamps: Ensure universal consistency across environments.
Glossary
A
API Gateway / Ingress: A service that handles incoming traffic, applies policies like rate limiting or authentication, and routes requests to internal services.
Autoscaling: Automatically adjusting the number of running instances based on current demand (e.g., CPU usage or request volume).
awk: A command-line tool used for pattern scanning, reporting, and text processing.
B
Batch Jobs: Scheduled non-interactive workloads (like reports, data migration, or backups), usually run during off-peak hours.
Block I/O (%iowait): The percentage of CPU time waiting for disk I/O to complete; high values indicate disk bottlenecks.
Body-Size / Payload Limit: The maximum allowed size for an incoming HTTP request body; exceeding it results in HTTP 413 errors.
Bulkhead / Circuit Breaker: Resilience strategies to isolate failures and prevent a domino effect when one component becomes slow or unresponsive.
C
Cache Hit / Miss: A hit means the data was found in the cache; a miss means it had to be fetched from the backend.
Cache Stampede: A situation where many cache entries expire at once, overwhelming the backend with regeneration requests.
Chrony / systemd-timesyncd: Services that keep system clocks in sync with network time servers.
Connection Pool: A pool of reusable database connections to avoid the overhead of establishing new ones frequently.
Core Dump: A file containing a snapshot of a program's memory when it crashes; used for post-mortem debugging.
CPU Load Average: The number of tasks either running or waiting for CPU time; values above the number of cores indicate overload.
cProfile, py-spy: Python tools used for profiling application performance to identify CPU-intensive code paths.
D
Deadlock: A situation where two or more processes are waiting on each other's resources, preventing forward progress.
df -h / df -i: Commands to check disk space (-h) and inode usage (-i).
dmesg: Shows kernel logs, including messages about hardware, memory errors, or OOM kills.
Docker / Kubernetes (K8s): Docker is a container runtime; Kubernetes is an orchestration platform for managing containerized workloads.
du -x -m: A disk usage command that shows the size of directories in megabytes, excluding other filesystems.
E
Elastic / Adaptive Rate Limiting: Dynamically adjusts traffic limits based on observed patterns rather than fixed thresholds.
Eventual Consistency: A data replication model where changes propagate asynchronously, leading to temporary stale reads.
EXPLAIN (SQL): A command that shows how a database query will be executed, useful for identifying slow operations.
F
Fast Local SSD: High-performance disk attached directly to the instance, suitable for swap or I/O-intensive workloads.
FIFO-Style Log Rotation: A mechanism that keeps the most recent log files and deletes or compresses older ones to manage disk space.
fallocate: A fast method to create files of a specific size without writing data; commonly used to create swap files.
G
Grafana / Prometheus: Tools used for monitoring and visualization; Prometheus collects metrics, Grafana displays them.
gdb, Valgrind: Tools for debugging and analyzing native (e.g., C/C++) applications to find memory or threading bugs.
H
Health Endpoint: An API route (e.g., /health) that responds with 200 OK if the service is functioning properly.
HTTP 429 / 413 / 5xx: Standard HTTP error codes—429 means too many requests, 413 means payload too large, 5xx indicates server-side errors.
htop: An advanced, interactive system monitor that shows real-time CPU, memory, and process stats.
I
InnoDB: The default MySQL storage engine that supports transactions and row-level locking.
Inode: A filesystem structure representing metadata about files; disk can run out of inodes even if it has free space.
J
Jitter (TTL Jitter): Adding randomness to TTL values to avoid simultaneous cache expiration.
JWT (JSON Web Token): A token format for stateless authentication that includes timestamps for expiration and validity.
journalctl / Journald Vacuum: Tools for viewing and cleaning up system logs managed by systemd.
K
kill -SIGTERM / -SIGKILL: Signals used to terminate processes—SIGTERM is graceful; SIGKILL is forceful and immediate.
L
Latency P95/P99: The latency threshold below which 95% or 99% of requests fall—useful for understanding tail latency.
Load Balancer Drain / Evict: Temporarily stop sending new traffic to a node (drain), or remove it completely (evict).
Log Level (DEBUG/INFO/WARN/ERROR): Controls verbosity of application logs; DEBUG is most verbose, ERROR is most severe.
Logrotate: A Linux tool to rotate, compress, and manage log file growth over time.
M
Memory Leak: When a process allocates memory but never releases it, gradually consuming all available RAM.
mkswap / swapon / swapoff: Commands to set up and manage swap space in Linux.
Monotonic Reads: Guarantees that a read will not return older data than a previous read, even in eventually consistent systems.
MySQL Slow-Query Log: A log file that records SQL queries that take longer than a configured threshold.
N
NTP (Network Time Protocol): A protocol used to synchronize system clocks across machines.
O
OOM Killer: Linux kernel mechanism that forcefully kills processes when the system runs out of memory.
Orchestrator-CLI: Placeholder for your service orchestrator's CLI (e.g., kubectl, nomad, etc.).
P
Percent Idle Wait (%wa): CPU time spent waiting for disk I/O; high values indicate a disk performance issue.
Perf / perf_event_paranoid: Linux performance analysis tool; kernel setting determines who can access it.
Process State D / T: In ps output: D = uninterruptible sleep (usually I/O), T = stopped or traced (e.g., by a debugger).
Prometheus node_filesystem_avail_bytes: A metric indicating available disk space; used for setting alerts.
R
Rate Limit: Restriction on the number of requests a client can send in a given time window.
Read Replica: A read-only copy of a database used to offload read queries from the primary DB.
Rollback Deployment: Reverting to a previous software version after a faulty release.
S
SIGTERM vs. SIGKILL: SIGTERM asks a process to exit cleanly; SIGKILL forces it to stop immediately.
Slow-Query Threshold: Configuration setting that determines which queries get logged as "slow."
Swap: Disk space used as overflow for RAM when memory runs low; significantly slower than actual RAM.
System Load: Number of processes waiting for CPU or I/O; values higher than CPU cores suggest saturation.
Systemd Service (systemctl): A tool to manage background services (start, stop, restart, etc.) in modern Linux.
T
Tail Latency: The slowest response times (e.g., P99), which can severely impact user experience.
Throttle (Traffic / Producer): Intentionally slowing down traffic or message publishing to avoid overload.
Throughput vs. Latency: Throughput measures total work done per time unit; latency is how long a single task takes.
Timeout Budget / SLA Alignment: Ensuring your timeout settings match the expected response time + buffer of downstream services.
TLS / SSL Termination: Where HTTPS (encrypted) traffic is decrypted—often at the gateway or load balancer.
Top (M, P sort): A real-time process monitor; press M to sort by memory or P by CPU usage.
TTL (Time To Live): Duration after which a cache or DNS record expires.
U
Uninterruptible Sleep (D state): A process is stuck waiting on I/O and can't be killed until the wait completes.
UTC: Coordinated Universal Time; standard timezone used in logging to avoid daylight savings issues.
V
Valgrind: A tool for detecting memory leaks and threading issues in compiled code.
vmstat: Reports memory, CPU, and I/O usage statistics at intervals (e.g., vmstat 1 5 for 5 samples at 1s each).
W
%wa (Percent Idle Wait): The percentage of CPU time spent waiting for I/O (disk) operations to complete.
Reported by tools like top and vmstat.
A high %wa (e.g., ≥ 10 %) indicates the CPU is often idle because it’s blocked on disk reads/writes, suggesting a disk I/O bottleneck. -->
