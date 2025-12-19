# Zzazz – Rust Developer (3–6 Years)

## Overview

* **Company**: Zzazz
* **Role**: Rust Developer
* **Location**: India
* **Interview Date**: 2025
* **Experience Level**: Atleast 1 year of experience in Rust
* **Application Source**: HR Outreach

---

## Interview Process

### 1. **Round 1 – MCQ Test**

* **Duration**: ~60 minutes
* **Format**: MCQ + Live problem-solving (screen sharing)
* **Conducted By**: HR
* **Details**:
  * A form containing **<a href="../assets/zzazz-mcq-questions.md">50 MCQs</a>** focused on **Rust basics** 

  * Answers were selected while sharing the screen.

* **Coding Questions Asked**:
  * **Valid Parentheses**
    👉 [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
  * **Valid Anagram**
    👉 [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

* **Focus Areas**:
  * Rust syntax and fundamentals
  * Basic DSA concepts

---

### 2. **Round 2 – Technical Interview**

* **Duration**: ~60 minutes
* **Format**: Deep technical discussion + problem-solving
* **Questions Asked**:

  * How Rust is different from other programming languages.
  * Ownership, borrowing, and their rules.
  * `Copy` vs `Move` traits and where memory is allocated.
  * Lifetimes and why they are required.
  * Zero-cost abstractions.

    * Comparison between a manual loop (`10^3` summation) vs `iter().sum()` and performance implications.
  * Difference between **Concurrency** and **Parallelism**.
  * What is **Tokio** and why it is required.
  * Difference between `std::thread` and Tokio tasks.
  * Error handling in Rust (`Option`, `Result`).
  * Pattern matching in Rust.
  * Smart pointers: `Box`, `Rc`, `Arc`.
  * Interior mutability:
    * Why it is required.
    * How borrow rules are enforced in `RefCell`.
  * Channels in Rust and use cases.

* **Coding / Design Tasks**:

  * **Password Strength Classification**:

    * Write a Rust function that classifies a password as:

      * `"High-secure"`
      * `"Medium-secure"`
      * `"Low-secure"`
    * Conditions (lowercase, uppercase, digit, special character) were **not explicitly given**.
    * Expected to **assume and define** rules for classification.
  * Discussion on **TDD in Rust**.
  * Reverse a string:
    * Clean up spaces and punctuation.
    * Ignore case.
    * Check if the result is a palindrome.

---

### 3. **Round 3 – Technical Interview**

* **Duration**: ~30 minutes
* **Format**: Technical discussion
* **Questions Asked**:

  * How Rust manages memory safely without a garbage collector.
  * Interior mutability pattern in Rust.
  * Tokio and its necessity.
  * Database consistency question:

    * What happens if a record exists in a table but not in the index, or vice versa?
  * Discussion on work experience and since when I started coding in Rust.
  * Detailed discussion on `Rc` vs `Arc`.

---

## Key Rust Topics Covered

* Ownership, Borrowing, and Lifetimes
* Copy vs Move semantics
* Zero-cost abstractions
* Async Rust (`Tokio`, tasks, channels)
* Smart pointers (`Box`, `Rc`, `Arc`)
* Interior mutability (`RefCell`)
* Error handling and pattern matching
* TDD and problem-solving in Rust

---

## Outcome

* **Result**: Neutral / Not Selected
* **Feedback Received**: Neutral assessment communicated
* **Personal Reflections**:

  * Interviews were **Rust-heavy and conceptually deep**.
  * Some problem statements were intentionally open-ended to test design thinking.
  * Despite multiple rounds and solid discussions, the final outcome was neutral.

---

## Tips for Future Candidates

* Be prepared for **very deep Rust internals**, not just surface-level knowledge.
* Expect open-ended design problems where requirements are intentionally vague.
* Revise async Rust thoroughly, especially Tokio vs standard threading.
* Brush up on database fundamentals alongside Rust concepts.
* MCQ rounds may still test practical Rust understanding, not just theory.
