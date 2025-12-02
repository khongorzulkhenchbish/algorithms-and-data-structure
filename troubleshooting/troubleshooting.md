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

