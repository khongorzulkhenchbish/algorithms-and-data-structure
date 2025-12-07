### HTTP status codes

- 5xx means something’s broken on the server — check logs, dependencies, resource limits.
- 4xx means the client did something wrong — look at payloads, tokens, permissions.
- 2xx means success — but make sure the outcome matches your expectations.

#### Server side faults 5xx status codes

500 - internal server error, the server encountered an unexpected condition and didn't know how to handle => broke something.

try
- unhandled exceptions, check logs for stack traces
- regression from recent code changes
- edge case configs, null input, unexpected formats
- happening intermittent => examine load conditions or retry logic

501 - not implemented, the server doesn't support the functionality needed for the request.

try
- Review server-side feature flags, installed modules, or framework capabilities.
- Double-check that the client’s HTTP method and requested media types are actually implemented on the server.
- Confirm an API gateway or filter is not downgrading a 405 into 501.

405 Method Not Allowed - when the resource exists but explicitly disallows that particular method.

502 - bad gateway, proxy or gateway received invalid response, or failed to establish connection to upstream service.

try:
- check proxy logs (nginx, envoy) and target service logs
- validate service health and network connectivity
- Investigate whether the service is returning incomplete headers or crashing on startup.

503 — Service Unavailable, due to overload, downtime, maintenance.

- Monitor resource metrics: CPU, memory, database connections, queue depth.
- Inspect autoscaler behavior, rate limiters, or circuit breakers.
- Check if a deployment or maintenance window was in progress.

504 — Gateway Timeout, service acting as gatewat or proxy didn't get a response from upstream service in time.

try
- Look at timeout configurations for proxies, load balancers, and clients.
- Examine the performance of the upstream service.
- Break the request into smaller parts if feasible, or implement async/polling.

#### Client Side faults 4xx

400 — Bad Request, request was malformed, invalid, or couldn't be understood by the server.

try
- Validate the request body, query parameters, and headers.
- Confirm your frontend or client code adheres to the API spec.
- Check whether a misbehaving proxy or transformation layer is corrupting the request.

401 — Unauthorized

- Verify the presence and correct formatting of the Authorization header (e.g., Authorization: Bearer <token>).
- Check token validity: expired timestamps, bad signatures, wrong issuer/audience, missing scopes.
- Ensure the endpoint isn’t behind a mis-configured proxy stripping auth headers.
- Inspect authentication middleware / filters to confirm they run before business logic and return a 401 when creds are absent or invalid.
- When using session cookies, confirm the cookie isn’t HttpOnly- or SameSite-restricted in a way that blocks the client.

403 — Forbidden (Authenticated but not authorized),  doesn’t have permission

try
- Review RBAC (role-based access control) or ABAC policies to see why the principal lacks the required permission.
- Confirm the user’s group / role / scope mapping; refresh tokens can lag behind newly granted roles.
- Examine audit logs or feature-flag rules that might be overriding normal permissions.
- In multi-tenant systems, verify the request is scoped to the correct tenant or namespace.

404 — Not Found

try
- Double-check the route or endpoint path.
- Validate that the resource ID or slug is correct.
- Check if soft deletes or resource hiding (e.g., private posts) are in play.

408 — Request Timeout

The server didn’t receive the full request from the client within the expected time window.

try
- Look into client-side slowness or flaky networks.
- Check for large payloads or inefficient upload flows.
- Increase timeouts where reasonable, but log slow request trends to catch bottlenecks.

409 — Conflict, The request couldn’t be completed due to a conflict with the current state of the resource.

try
- Implement optimistic locking or version control on write operations.
- Return clear error messages to guide clients on how to resolve the conflict.
- Monitor for recurring patterns of conflict to improve UX.

429 — Too Many Requests, client hit a rate limit

try
- Inspect rate-limiting headers such as Retry-After or the newer RateLimit-Remaining, RateLimit-Reset.
- Review client behavior and introduce exponential backoff or batching.
- Consider increasing quotas for legitimate high-usage clients.

#### When Things Work as Expected 2xx

..

202 — Accepted, The request was received and accepted for processing, but the processing is asynchronous and not complete yet.

try
- Ensure there’s a way for the client to check the job’s status (e.g., a /status/{jobId} endpoint).
- Monitor the queue and worker service logs to confirm the job runs as expected.
- Handle timeouts or dropped jobs in long-running workflows.

204 — No Content, The request was successful, but there is no response body.

try
- Clients should be built to gracefully handle empty responses.
- Make sure the action really took effect (e.g., resource was deleted, update applied).
- Avoid using 204 if the client expects data to render — it will lead to errors.

206 — Partial Content, The server is delivering only part of the resource due to a range request.

try
- Verify the Range and Content-Range headers.
- Ensure your backend supports range requests and returns the correct slices.
- Log partial responses if users report incomplete downloads.

#### What About Redirects and Informational Codes?

You may also encounter other categories:

3xx Redirects tell the client to look elsewhere for the resource. They’re useful for caching, load balancing, and SEO, but can cause issues if used improperly (e.g., redirect loops or stale caches). 

Examples include:

- 301 — Moved Permanently
- 302 — Found (Temporary Redirect)
- 304 — Not Modified (used in caching)
- 1xx Informational Codes are rarely seen in modern API development and mostly appear in low-level HTTP handling or protocol switching (like WebSocket upgrades).

- 100 — Continue
- 101 — Switching Protocols
