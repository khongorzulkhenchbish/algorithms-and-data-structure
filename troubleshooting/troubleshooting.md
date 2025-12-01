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

