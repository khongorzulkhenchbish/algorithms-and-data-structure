# Before Interview Check

Day-of packet for Google coding interviews. No cramming — trust patterns, communicate clearly, execute calmly.

See also: [GOOGLE_INTERVIEW_IMPROVEMENT_PLAYBOOK.md](GOOGLE_INTERVIEW_IMPROVEMENT_PLAYBOOK.md) for weekly practice structure.

---

## 60-Second Interview Script

Say this out loud before you code on every problem:

1. **Clarify** (30 sec): input size? duplicates? sorted? negative values? empty input?
2. **Pattern** (15 sec): "This looks like X because constraint Y."
3. **Complexity target** (10 sec): "Aiming for O(…) time, O(…) space because n ≤ …"
4. **Invariant** (15 sec): one sentence for what your state means
5. **Test plan** (15 sec): 3 cases — empty/single, typical, adversarial

If you do only this, you jump from Lean Hire → Hire territory.

---

## Pattern Trigger Card

| Signal | Pattern | Complexity target |
|--------|---------|-------------------|
| Sorted array, find X | Binary search | O(log n) |
| Subarray/substring, sum/count constraint | Sliding window or prefix sum + hashmap | O(n) |
| Contiguous max/min sum | Kadane (`ending_here` vs `best_so_far`) | O(n) |
| Grid, connected components, flood | BFS/DFS | O(m×n) |
| Shortest path, unweighted | BFS | O(V+E) |
| Dependencies, prerequisites | Topological sort / DFS cycle detect | O(V+E) |
| Top K / median stream | Heap | O(n log k) |
| Intervals overlapping | Sort + merge / sweep | O(n log n) |
| Tree path / subtree | DFS + return value to parent | O(n) |
| "Can we achieve?" with monotonic feasibility | Binary search on answer | O(n log range) |
| Design class with state (bookshelf, cache) | Clear interface, invariants, test transitions | — |

---

## Your 2 Blockers (Fix These Today)

From prior rounds — these are what cost Hire signals:

### 1. State vs answer

Every DP/Kadane problem uses two variables with two jobs:

- **State**: best ending here
- **Answer**: best anywhere

Say it before coding. Interviewers love this.

### 2. OOP / design rounds (bookshelf-style)

If the round includes design/OOP, lead with:

- **What objects exist?** (Book, Shelf, Library — not vague "manager")
- **What state does each hold?**
- **What invariants must always hold?** (e.g. "book id unique", "shelf capacity not exceeded")
- **What operations mutate state?** List them before implementing.

Do not jump to code. Sketch interfaces first.

---

## 90-Minute Morning Warm-Up

Do **3 problems max**, talk through each aloud:

| Time | Problem | Why |
|------|---------|-----|
| 20 min | LC 200 Number of Islands | BFS/DFS muscle memory |
| 20 min | LC 53 Maximum Subarray | Kadane invariant drill |
| 20 min | LC 560 Subarray Sum Equals K | Prefix sum + hashmap — very Google |
| 15 min | Design: Min Stack or Bookshelf | State boundaries |

**Rule:** If stuck > 8 min, say the pattern + complexity out loud and move on. Do not spiral.

---

## Complexity Cheat Sheet

Avoid "it's linear" without naming n.

| Technique | Time | Space |
|-----------|------|-------|
| BFS/DFS on grid | O(rows × cols) | O(rows × cols) queue/recursion worst case |
| Binary search | O(log n) | O(1) |
| Heap of size k over n items | O(n log k) | O(k) |
| Sorting-based | O(n log n) | O(1) or O(n) |
| Kadane / sliding window | O(n) | O(1) or O(k) |
| Prefix sum + hashmap | O(n) | O(n) |

Always say the **dominant term** and **why** from constraints.

---

## Python Day-Of Reminders (Google Style)

```python
def solve(nums: list[int]) -> int:
    if not nums:
        return 0  # clarify expected behavior first
```

- Descriptive names: `ending_sum`, `best_sum`, not `dp`, `ans` unless standard
- Early returns for empty/single
- Extract helpers when logic repeats
- Test with 3 cases before saying "done"

---

## When You Are Stuck in the Interview

1. **Restate the problem** in your own words
2. **Brute force first** — "O(n²) check all pairs" — then optimize
3. **Ask** "Can I use extra space for a hashmap?" — often unlocks O(n)
4. **Narrow the pattern** — "Is this graph, array, or tree?"
5. **Do not go silent** — thinking aloud beats 2 minutes of silence

Recovering from a wrong turn with clear reasoning = Hire signal.

---

## Logistics Checklist

- [ ] Quiet space, charger, water
- [ ] Google Doc or CoderPad ready — know your environment
- [ ] Pen + paper for examples
- [ ] Breathe before each problem — 10 seconds
- [ ] Treat follow-ups as new problems: re-clarify, do not patch silently

---

## Quick Self-Check (2 min each)

**Q1:** LC 53 — why two variables?  
**A:** `ending_here` can reset; `best` must not forget past peaks.

**Q2:** LC 200 — BFS vs DFS?  
**A:** Both O(m×n). BFS for shortest path; DFS simpler for "count islands."

**Q3:** LC 560 — key insight?  
**A:** `prefix[j] - prefix[i] = k` → store prefix counts in hashmap.

**Q4:** Bookshelf design — first question?  
**A:** "What operations? add, remove, get, list? Capacity per shelf?"

If you nailed 3/4, you are ready.

---

## What NOT to Do Today

- Do not grind hard problems you have never seen
- Do not memorize solutions — patterns only
- Do not skip clarifying questions to code faster
- Do not claim "optimal" without complexity proof
- Do not panic on one stumble — packet is multiple rounds

---

## Optional Live Drills

Pick one for a 15-minute mock:

1. **Coding:** Number of Islands — explain approach, push on edge cases
2. **Coding:** Merge Intervals — classic Google
3. **Design:** Implement a bookshelf with add/remove/search — OOP focus
4. **Pattern drill:** Given constraints, name pattern + complexity only (no code)

---

## Final Mindset

**Today's goal:** not perfection — clear reasoning + working code + recovery when stuck.

**One habit:** Say the invariant out loud before every loop.

Trust the patterns. Communicate constantly.
