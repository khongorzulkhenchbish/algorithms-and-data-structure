# Google Coding Interview Improvement Playbook (L3 Focus)

Use this before each practice session and before real interviews.

## 1) Session Script (Run Every Time)

### Step 1: Problem framing (5 minutes)
- Restate the problem in your own words.
- Ask 2-4 clarifying questions (constraints, ordering, input size, edge behavior).
- Name 2 candidate patterns and explain why you choose one.
- State target time/space complexity before coding.

### Step 2: Timed implementation (20-25 minutes)
- Code in "Google Doc mode": no autocomplete assumptions.
- Talk while thinking: narrate trade-offs and invariants.
- If stuck for more than 4 minutes, ask for one hint, then adapt clearly.

### Step 3: Post-mortem (10 minutes)
- Where was first correctness risk introduced?
- Which assumption did you make without confirming?
- Was complexity tight and defensible?
- Did you provide a minimal test plan before finishing?

### Step 4: Immediate redo (10 minutes)
- Re-implement same problem from memory, cleaner and shorter.
- Goal: fewer branches, stronger invariants, clearer communication.

---

## 2) Weekly Practice Structure

- 6-8 timed problems per week.
- Suggested distribution:
  - 2x Binary Search on Answer
  - 2x Sliding Window / Hash Map
  - 1-2x Graph (BFS/DFS/Union-Find)
  - 1x DP shape drill
- Do mock-style rounds, not only random untimed solving.

---

## 3) Non-Negotiable Interview Behaviors

Before coding, always state:
- Why this pattern over alternatives
- Complexity target (time + space)
- Key invariant(s)
- Minimal test plan (at least 3 cases)

During coding:
- Keep naming clear and readable.
- Avoid over-engineering.
- Integrate hints quickly and explicitly.

After coding:
- Re-check corner cases.
- Re-state complexity precisely.
- Explain why your solution is correct (invariant + boundary reasoning).

---

## 4) Top Mistakes to Eliminate

- Hand-wavy "this is optimal" without proof.
- Silent assumptions (constraints not confirmed).
- Extra branches that do not change correctness and hurt clarity.
- Delayed pivoting when interviewer hint suggests a better direction.

---

## 5) Your Current Focus (Based on Recent Rounds)

- Strengths:
  - Fast adaptation to feedback
  - Good pattern recognition
  - Improved solution structure

- Improvement targets:
  - Give tighter complexity wording from first attempt
  - State invariants out loud before implementation
  - Remove redundant logic immediately after proving bounds

---

## 6) Pre-Interview 2-Minute Checklist

- Did I restate the problem clearly?
- Did I ask clarifying questions?
- Did I justify pattern choice over alternatives?
- Did I state time/space complexity before coding?
- Did I identify 1-2 invariants?
- Did I define 3 edge tests?

If any answer is "no", fix it before you start coding.

---

## 7) 15-Minute Emergency Drill (When Time Is Tight)

- Pick one monotonic-feasibility problem (e.g., 875, 1283, 1482).
- 2 minutes: clarifications + complexity target.
- 10 minutes: implement.
- 3 minutes: explain monotonic predicate, bounds, and correctness.

Repeat until explanation feels automatic.
