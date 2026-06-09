# YRAL – Rust Developer – 3–4 Years Experience

## Overview

* **Company**: YRAL (hiring through an agency)
* **Role**: Rust Developer
* **Location**: India · Remote
* **Interview Date**: Aug, 2024
* **Experience Level**: 4–7 years of software development, strong focus on Rust
* **Application Source**: LinkedIn

---

## Interview Process

### Round 1 – Technical Interview

* **Duration**: ~30 minutes
* **Format**: Discussion + Output-based Questions

**Questions & Topics Discussed**

* Profile and experience discussion.
* Five output-based Rust questions — predict the output or explain the behavior:

```rust
use std::mem;

fn main() {
    let a;
    let a = a = true;
    print!("{}", mem::size_of_val(&a));
}
```

```rust
trait Trait {
    fn f(&self);
}

impl<'a> dyn Trait + 'a {
    fn f(&self) {
        print!("1");
    }
}

impl Trait for bool {
    fn f(&self) {
        print!("2");
    }
}

fn main() {
    Trait::f(&true);
    Trait::f(&true as &dyn Trait);
    <_ as Trait>::f(&true);
    <_ as Trait>::f(&true as &dyn Trait);
    <bool as Trait>::f(&true);
    <dyn Trait as Trait>::f(&true as &dyn Trait);
}
```

```rust
fn return1() { print!("1"); return; }
fn return2() { print!("2"); return; }
fn break1() { loop { print!("1"); break; } }
fn break2() { loop { print!("2"); break; } }
fn f() {}
fn g() {}

fn main() {
    let pf = f as fn();
    let pg = g as fn();
    print!("{}", (pf == pg) as u8);
    return1();
    return2();
    break1();
    break2();
}
```

```rust
macro_rules! x {
    ($n:expr) => {
        let a = X($n);
    };
}

struct X(u64);

impl Drop for X {
    fn drop(&mut self) {
        print!("{}", self.0);
    }
}

fn main() {
    let a = X(1);
    x!(2);
    print!("{}", a.0);
}
```

```rust
use std::fmt::{self, Display};

struct S;

impl Display for S {
    fn fmt(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
        formatter.write_str("1")
    }
}

impl Drop for S {
    fn drop(&mut self) {
        print!("2");
    }
}

fn f() -> S { S }

fn main() {
    let S = f();
    print!("{}", S);
}
```

---

## Key Topics Covered

* Core Rust concepts: functions, memory management, traits, lifetimes
* Drop order and destructors
* Trait object dispatch vs concrete type dispatch
* Macros and scoping
* Rust compilation process

---

## Outcome

* **Result**: Rejected
* **Feedback Received**: No
* **Reflections**: I was able to answer 3 out of 5 questions with proper explanation, but got rejected. These kinds of tricky output questions can catch you off-guard even if you're strong in Rust fundamentals.

---

## Tips for Future Candidates

* Focus on core concepts, and expect the unexpected — tricky output-based questions are common at companies that want deep language knowledge.
* Practice explaining drop order, trait dispatch, and macro hygiene out loud.
* Study edge cases in Rust's type system and trait resolution — not just day-to-day patterns.
