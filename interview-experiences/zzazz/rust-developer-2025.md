# Zzazz – Rust Developer – 3–6 Years Experience

## Overview

* **Company**: Zzazz
* **Role**: Rust Developer
* **Location**: India · Not specified
* **Interview Date**: 2025
* **Experience Level**: At least 1 year in Rust
* **Application Source**: HR Outreach

---

## Interview Process

### Round 1 – MCQ Test

* **Duration**: ~60 minutes
* **Format**: MCQ + Live Problem-solving (screen sharing)
* **Conducted by**: HR

**Questions & Topics Discussed**

* A form containing [50 MCQs](../../assets/zzazz-mcq-questions.md) focused on Rust basics, answered while sharing the screen.

**Coding Problems**

* [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) – LeetCode easy
* [Valid Anagram](https://leetcode.com/problems/valid-anagram/) – LeetCode easy

---

### Round 2 – Technical Interview

* **Duration**: ~60 minutes
* **Format**: Discussion + Problem-solving

**Questions & Topics Discussed**

* How Rust is different from other programming languages.
* Ownership, borrowing, and their rules.
* `Copy` vs `Move` traits and where memory is allocated.
* Lifetimes and why they are required.
* Zero-cost abstractions — comparison between a manual loop (`10^3` summation) vs `iter().sum()` and performance implications.
* Difference between Concurrency and Parallelism.
* What is Tokio and why it is required.
* Difference between `std::thread` and Tokio tasks.
* Error handling in Rust (`Option`, `Result`).
* Pattern matching in Rust.
* Smart pointers: `Box`, `Rc`, `Arc`.
* Interior mutability: why it is required; how borrow rules are enforced in `RefCell`.
* Channels in Rust and use cases.

**Coding Problems**

* Password Strength Classification — write a Rust function that classifies a password as `"High-secure"`, `"Medium-secure"`, or `"Low-secure"`. Conditions were **not given explicitly** — expected to define and justify your own classification rules.
* Reverse a string: clean up spaces and punctuation, ignore case, and check if the result is a palindrome.
* Discussion on TDD in Rust.

---

### Round 3 – Technical Interview

* **Duration**: ~30 minutes
* **Format**: Discussion

**Questions & Topics Discussed**

* How Rust manages memory safely without a garbage collector.
* Interior mutability pattern in Rust.
* Tokio and its necessity.
* Database consistency question: what happens if a record exists in a table but not in the index, or vice versa?
* Discussion on work experience and since when I started coding in Rust.
* Detailed discussion on `Rc` vs `Arc`.

---

## Key Topics Covered

* Ownership, Borrowing, and Lifetimes
* Copy vs Move semantics
* Zero-cost abstractions
* Async Rust (Tokio, tasks, channels)
* Smart Pointers (`Box`, `Rc`, `Arc`)
* Interior mutability (`RefCell`)
* Error handling and pattern matching
* TDD in Rust
* Database fundamentals

---

## Outcome

* **Result**: Neutral
* **Feedback Received**: Yes — neutral assessment communicated.
* **Reflections**: Interviews were Rust-heavy and conceptually deep. Some problem statements were intentionally open-ended to test design thinking. Despite multiple rounds and solid discussions, the final outcome was neutral.

---

## Tips for Future Candidates

* Be prepared for very deep Rust internals — not just surface-level knowledge.
* Expect open-ended design problems where requirements are intentionally vague.
* Revise async Rust thoroughly, especially Tokio vs standard threading.
* Brush up on database fundamentals alongside Rust concepts.
* MCQ rounds can still test practical Rust understanding, not just theory.
