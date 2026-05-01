# Patterns

## 1. Prefix sum

### Fast recognition checklist

Think **prefix sum candidate** when you see any of these:

- Repeated queries about **sum/count over subarray** ranges.
- Need to find a subarray with a target like **sum = k**, **sum divisible by k**, **equal 0/1 count**, etc.
- Language like **“continuous subarray”**, **“range”**, **“between i and j”**.
- Brute force is obvious **O(n²)** by checking every start/end, and constraints suggest **O(n)** or **O(n log n)**.
- You can rewrite the condition on subarray `[l..r]` as:

  `prefix[r] - prefix[l - 1] = target`

If that algebra appears, prefix sums are likely central.

### Pattern variants

- **Static range sums** — build a prefix array once; answer each range in **O(1)**.
- **Count subarrays with property** — prefix + hash map frequency (`sum → count`).
- **Longest/shortest subarray with property** — prefix + first-occurrence map or monotonic structure.
- **2D matrix region sums** — 2D prefix sums (inclusion–exclusion).
- **Parity / modulo constraints** — prefix modulo bucket (`prefix % k`).

### Interview heuristic (~30 seconds)

Ask yourself:

1. Can I express the subarray condition as a **difference of two prefixes**?
2. Do I need to evaluate **many ranges** quickly?
3. Is there a hash map state keyed by **`prefix`** or **`prefix % k`** that avoids nested loops?

If **yes** to two or more of these, push prefix sum early.

Positive and negative integers + Not Sorted + Contiguous subarray + Non-empty => Prefix sum

## 2. Sliding Window

Positive integers + Not Sorted + Contiguous subarray + Non-empty => Sliding window

