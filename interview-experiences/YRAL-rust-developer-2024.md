# YRAL – Rust Developer – 3-4 Years Experience

## Overview
- **Company**: YRAL (hiring through some agency)
- **Role**: Rust Developer
- **Location**: India, Remote
- **Interview Date**: August, 2024
- **Experience Level**: 4-7 years of professional experience in software development with a strong focus on Rust.
- **Application Source**: LinkedIn

## Interview Process
1. **Round 1 – Output based questions**
   - **Duration**: 30 minutes
   - **Format**: Discussion
   - **Topics Covered**: Rust concepts.
   - **Details**:
     - The round involved discuss around profile, experience and three random output based questions were asked.

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
      fn return1() {
         print!("1");
         return;
      }

      fn return2() {
         print!("2");
         return;
      }

      fn break1() {
         loop {
            print!("1");
            break;
         }
      }

      fn break2() {
         loop {
            print!("2");
            break;
         }
      }

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

      fn f() -> S {
         S
      }

      fn main() {
         let S = f();
         print!("{}", S);
      }
      ```

## Key Rust Topics Covered
- Rust core concepts like functions, memory management, traits, lifetimes.
- Compilation process in detail.

## Outcome
- **Result**: Rejected
- **Feedback Received**: No
- **Personal Reflections**: I was able to answer 3/5 questions with proper explaination, but got rejected.

## Tips for Future Candidates
- Focus on core concepts, and expect the unexpected that these kind of questions can also be asked.