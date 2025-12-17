In a Meta PE interview, they often use a "progressive" problem—it starts simple and gets harder as you solve each layer. Here is a simulated high-speed learning guide for a classic Meta-specific scenario: **The "Thundering Herd" after a Cache Flush.**

---

# 🤝 Final Interview Prep: The "Thundering Herd" Scenario

**Context:** A service that fetches user profile data is experiencing a massive spike in latency and 5xx errors immediately after a routine maintenance window.

## Phase 1: The Initial Trigger (What happened?)

**Interviewer:** "We just finished a scheduled maintenance on our Memcached tier. We brought the cache back online, but now the `ProfileService` is essentially down. CPU is at 100% on the app servers. What’s your first move?"

**Candidate:** "Maintenance usually involves clearing or restarting the cache. If the cache is empty (cold), the app servers are likely hitting the database for every single request. This is a **Cache Miss Storm** (or Thundering Herd). I’ll check the **Cache Hit Rate** metric."

**Interviewer:** "The Hit Rate dropped from 99% to 2%. The Database is now showing extremely high load and slow queries."

## Phase 2: The "Thundering Herd" (Why is it still failing?)

**Candidate:** "Even if we wait for the cache to fill, the database might be so overwhelmed that it can't respond to the queries needed to *fill* the cache. Multiple app threads are likely requesting the same 'hot' User ID simultaneously."

**Candidate:** "I'll check if we have **Request Collapsing** (or Coalescing). If 100 threads need User A, only one should go to the DB; the other 99 should wait for that one result."

**Interviewer:** "We don't have request collapsing. But even worse, the app servers are now failing health checks and being pulled out of the Load Balancer."

## Phase 3: The Cascading Failure (The Meta Scale)

**Candidate:** "This is a **Cascading Failure**. As the LB pulls 'failed' nodes, the remaining nodes get *more* traffic, which makes them fail faster.
**Action:** I need to stop the bleeding. I will implement **Load Shedding** at the edge. I’ll configure the Load Balancer to drop 50% of traffic (non-critical requests) immediately to allow the remaining 50% to actually succeed and slowly prime the cache."

## Phase 4: The Long-Term Fix (Meta Engineering)

**Interviewer:** "The site is back up after we throttled traffic. How do we prevent this from happening during the next maintenance?"

**Candidate:**

1. **Cache Warming:** Before pointing production traffic to a new cache tier, we should 'warm' it using sampled production logs or a background crawler.
2. **Soft TTLs:** Use a 'Stale-While-Revalidate' approach. If the data is old, serve it anyway while updating the cache in the background.
3. **Adaptive Throttling:** The service should automatically return a `503 Service Unavailable` when its own internal queues are full, rather than trying to process everything and crashing.