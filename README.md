# Rust Interview Questions & Answers

### Table of Contents

<details open>
<summary>
Hide/Show table of contents
</summary>

| No. | Questions                                                                                                  |
| --- | ---------------------------------------------------------------------------------------------------------- |
|     | <b>Fundamentals</b>          |
| 1   | [What is Rust, and where is it mostly used?](#what-is-rust-and-where-is-it-mostly-used)                    |
| 2   | [What are ownership and borrowing in Rust?](#what-are-ownership-and-borrowing-in-rust)                     |
| 3   | [What are lifetimes in Rust?](#what-are-lifetimes-in-rust)                                                 |
| 4   | [How is memory allocated for a `String` type in Rust?](#how-is-memory-allocated-for-a-string-type-in-rust) |
| 5   | [What is `&str` in Rust, and where is it stored?](#what-is-str-in-rust-and-where-is-it-stored)             |
|     | <b>Concurrency & Asynchronous Programming </b>          |
| 6   | [What are `async` and `await` in Rust?](#what-are-async-and-await-in-rust)                            |
| 7   | [Explain Tokio and where it is used.](#explain-tokio-and-where-it-is-used)                            |
| 8   | [What is pinning in Rust, and why is it important?](#what-is-pinning-in-rust-and-why-is-it-important) |
| 9   | [How do we handle errors in Rust?](#how-do-we-handle-errors-in-rust)                                                  |
|     | <b>Error Handling & Unsafe Code</b>          |
| 10  | [How does the `?` operator simplify error handling in Rust?](#how-does-the--operator-simplify-error-handling-in-rust) |
| 11  | [What is unsafe Rust? Explain with an example.](#what-is-unsafe-rust-explain-with-an-example)                         |
|     | <b>Advanced Concepts</b>          |
| 12  | [What are generics in Rust?](#what-are-generics-in-rust)                               |
| 13  | [How do you implement inheritance in Rust?](#how-do-you-implement-inheritance-in-rust) |
| 14  | [What is Zero-Cost Abstraction?](#what-is-zero-cost-abstraction)                       |
|     | <b>Memory Management & Smart Pointers</b>          |
| 15  | [What is the possibility of memory leaks in Rust?](#what-is-the-possibility-of-memory-leaks-in-rust)      |
| 16  | [What are Smart Pointers? Explain about Box, Rc, Arc.](#what-are-smart-pointers-explain-about-box-rc-arc) |

</details>

---

## Fundamentals

### 1. What is Rust, and where is it mostly used?

Rust is a modern, general-purpose systems programming language designed with a strong emphasis on performance, memory safety, and concurrency. Unlike traditional systems languages like C or C++, Rust eliminates entire classes of bugs at compile time—such as null pointer dereferencing, buffer overflows, and data races—without relying on a garbage collector.

Rust achieves this through its innovative ownership model, borrow checker, and strict compile-time checks, which enforce safe memory access while still enabling fine-grained control over system resources.

Rust is used in below areas,

**Systems Programming:** Operating systems, device drivers, and system utilities.

**Embedded Systems:** Microcontroller firmware and real-time applications with minimal runtime overhead.

**WebAssembly (Wasm):** Performance-critical code compiled to run in browsers or on edge devices.

**Cloud Infrastructure:** Networking stacks, container runtimes, and service frameworks.

**Command-Line Tools:** Tools like ripgrep, bat, and exa are written in Rust for speed and reliability.

**Concurrent Systems:** Thanks to fearless concurrency, Rust is well-suited for building multithreaded servers and distributed systems.

---

### 2. What are ownership and borrowing in Rust?

**Ownership** and **borrowing** are foundational concepts in Rust that allow it to manage memory safely and efficiently without the need for a garbage collector.

#### **Ownership**

* In Rust, **each value has a single owner**—a variable that holds responsibility for the value’s memory.
* **Only one owner** exists for a variable or memory location at any given point in time.
* When the **owner goes out of scope**, Rust automatically deallocates the associated memory. This deterministic model ensures memory safety and eliminates leaks.

#### **Borrowing**

* Rust allows variables to be **borrowed** by creating references to them.
* There can be:

  * **Multiple immutable (`&T`) references** at a time (read-only access).
  * **Only one mutable (`&mut T`) reference** at a time (write access).
* This restriction prevents **data races** and enforces safe concurrent access.
* **Immutable and mutable references cannot coexist** in the same scope, ensuring clear access semantics.

To guarantee the validity of these references, Rust uses a concept called **lifetimes**, which ensures that a reference never outlives the data it points to.

By enforcing these strict but predictable rules at compile time, Rust ensures **memory safety**, **thread safety**, and **efficient resource management**—all without runtime overhead.

---

### 3. What are lifetimes in Rust?

**Lifetimes** are annotations used by Rust’s type system to track how long references are valid. They ensure that references do not outlive the data they point to, preventing **dangling references** at compile time.

Rust enforces strict borrowing rules for safety, but it often **infers lifetimes automatically** through a feature called **lifetime elision**. In simple cases, explicit lifetime annotations aren’t needed. However, in more **complex or ambiguous cases**, such as when multiple references are involved, the compiler requires explicit lifetimes to determine how the data should be borrowed.

#### Why Lifetimes Matter

When a function returns a reference, Rust needs to know whether the returned reference is tied to one of the input references. If it’s unclear, the compiler will ask for lifetime annotations to make the relationship explicit.

##### Example

```rust
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

fn main() {
    let str1 = String::from("Rust");
    let str2 = String::from("Programming");

    let result = longest(&str1, &str2);
    println!("The longest string is: {}", result);
}
```

Here, we annotate the function with a lifetime `'a`, stating that the returned reference is valid for **at least as long as** both `s1` and `s2`. This tells the compiler that the returned reference won't outlive either input.


Lifetimes don’t change how long a value lives at runtime—they're only used during **compile time** to check validity of references. They're a key part of what makes Rust **memory-safe without garbage collection**.

---

### 4. How is memory allocated for a `String` type in Rust?

```rust
todo!()
```
---

### 5. What is `&str` in Rust, and where is it stored?

```rust
todo!()
```

---

## Concurrency & Asynchronous Programming

### 6. What are `async` and `await` in Rust?

Rust’s `async` and `await` keywords enable **asynchronous programming**, allowing tasks to be performed **concurrently** without blocking the thread.

* When you declare a function as `async`, it **does not run immediately**. Instead, it returns a **`Future`**—a value representing a computation that may complete in the future.
* When you call `.await` on a `Future`, you **pause** the current task until the future is ready, but the thread itself is **not blocked**. Instead, other tasks can continue executing on the same thread.

This model is built around **polling**: the runtime (such as [Tokio](https://tokio.rs/) or [async-std](https://async.rs/)) repeatedly polls the future to check if it's ready to produce a result. Meanwhile, other futures can be polled and progressed.

#### Key Benefits:

* Enables **non-blocking I/O**.
* Improves **throughput and responsiveness**, especially in applications that deal with many I/O-bound tasks (e.g., web servers, APIs).
* Offers **fine-grained control** over task scheduling and performance.

Rust’s async model is **zero-cost**, meaning you don’t pay extra at runtime for these abstractions—they compile down to efficient state machines.

---

### 7. Explain Tokio and where it is used.

```rust
todo!()
```

---

### 8. What is pinning in Rust, and why is it important?

```rust
todo!()
```

---
### 9. How do we handle errors in Rust?

Rust categorizes errors into two types:

#### Recoverable Errors

Handled using the `Result<T, E>` and `Option<T>` types. These allow the program to gracefully respond to unexpected conditions.

#### Irrecoverable Errors

Handled using the `panic!` macro, which **immediately terminates** the program. This is reserved for bugs or unrecoverable states, such as indexing out of bounds.

### Recoverable Error Handling in Rust

* **`Result<T, E>`** is used when an operation might succeed (`Ok(T)`) or fail (`Err(E)`).
* **`Option<T>`** is used when a value may or may not be present (`Some(T)` or `None`).

These types encourage **explicit error handling** through `match`, `if let`, or the `?` operator.

#### Example:

```rust
fn divide(numerator: f64, denominator: f64) -> Result<f64, String> {
    if denominator == 0.0 {
        Err(String::from("Cannot divide by zero"))
    } else {
        Ok(numerator / denominator)
    }
}

fn get_value(val: Option<i32>) -> i32 {
    match val {
        Some(x) => x,
        None => 0,
    }
}

fn main() {
    match divide(4.0, 2.0) {
        Ok(result) => println!("Result: {}", result),
        Err(err) => println!("Error: {}", err),
    }

    let val = Some(10);
    println!("Value: {}", get_value(val));
}
```

In this example:

* `divide()` uses `Result` to indicate a possible failure (division by zero).
* `get_value()` handles the absence of a value using `Option`.

---

## Error Handling & Unsafe Code

### 10. How does the `?` operator simplify error handling in Rust?

The `?` operator in Rust is a **convenient shorthand** for **propagating errors** in functions that return a `Result` or `Option`.

Instead of explicitly matching on the result of a fallible operation, the `?` operator:

* **Unwraps the value** if it's `Ok` or `Some`.
* **Returns early** from the function if it's `Err` or `None`, forwarding the error or absence to the caller.

This removes boilerplate and makes error-handling code **more concise and readable**.

### Without `?` Operator

```rust
fn read_file(path: &str) -> Result<String, std::io::Error> {
    let file = std::fs::read_to_string(path);
    match file {
        Ok(content) => Ok(content),
        Err(e) => Err(e),
    }
}
```

### With `?` Operator

```rust
fn read_file(path: &str) -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string(path)?; // returns early if Err
    Ok(content)
}
```

> Note: The function must return a `Result` (or `Option` when using `?` on `Option`) for `?` to work.


By using `?`, developers can **avoid deep nesting** and **focus on the success path**, while still correctly handling errors. This contributes to **cleaner and more maintainable** Rust code.

---
### 11. What is unsafe Rust? Explain with an example.

**Unsafe Rust** allows developers to perform low-level operations that bypass Rust's usual safety guarantees. This includes operations like:

* Dereferencing raw pointers
* Calling unsafe functions
* Accessing mutable static variables
* Implementing unsafe traits

Unsafe Rust is necessary in scenarios where **performance and control are critical**, such as interacting with hardware, building abstractions like custom allocators, or interfacing with C code via **FFI (Foreign Function Interface)**.

```rust
fn main() {
    let value: i32 = 42;

    // Create raw pointer
    let raw_pointer = &value as *const i32;

    unsafe {
        // Dereference the raw pointer
        println!("Value at raw pointer: {}", *raw_pointer);
    }

    /*
    Raw pointers (*const T or *mut T) bypass Rust's safety checks.
    Dereferencing a raw pointer is unsafe because it can lead to undefined behavior
    if the pointer is invalid.
    */
}
```
---

## Advanced Concepts

### 12. What are generics in Rust?

**Generics** are a powerful feature in Rust that allow you to write flexible, reusable, and type-safe code. They enable you to define **functions, structs, enums, and traits** with **placeholders for types**, which are filled in with concrete types when used.

This means you can write code that works with **multiple data types** without duplicating logic.


### Key Concepts

* **Placeholders**: Represented with angle brackets (e.g., `<T>`, `<K, V>`), they act as stand-ins for actual data types.
* **Type Parameters**: You can define multiple type parameters for flexibility.
* **Generic Definitions**: You can use generics in functions, structs, enums, and traits.

##### Example: Generic Addition Function

```rust
fn add_numbers<T>(a: T, b: T) -> T
where
    T: std::ops::Add<Output = T>,
{
    a + b
}

fn main() {
    let int_num1: u64 = 10;
    let int_num2: u64 = 20;
    let result_int = add_numbers(int_num1, int_num2);
    println!("The sum of u64 is: {}", result_int);

    let float_num1: f64 = 10.5;
    let float_num2: f64 = 20.75;
    let result_float = add_numbers(float_num1, float_num2);
    println!("The sum of f64 is: {}", result_float);
}
```

### Trait Bounds

Trait bounds (e.g., `T: Add<Output = T>`) **restrict** the types that can be used with generics. This ensures that only types which implement the specified traits can be substituted, enabling type-safe operations like `+`, `==`, etc.

---
### 13. How do you implement inheritance in Rust?

In many object-oriented languages like Java or C++, **inheritance** allows a class to inherit fields and methods from another class. This enables code reuse and establishes an `is-a` relationship between classes. For example, a `Dog` class might inherit from an `Animal` class, automatically gaining all properties and behaviors of `Animal`.

**Rust, however, does not support classical inheritance.** Instead, Rust uses a powerful and flexible mechanism called **traits** to achieve polymorphism and code reuse.

#### How is Rust’s approach different?

* **No class hierarchy:** Rust has no classes or subclassing. Instead, it has structs for data and traits for behavior.
* **Trait inheritance:** Traits can inherit from other traits, meaning one trait can require the functionality of another trait.
* **Composition over inheritance:** You compose behavior by implementing traits rather than inheriting from a parent class.
* **Explicit implementation:** Each type explicitly implements traits to provide specific behaviors.

This avoids some common pitfalls of classical inheritance, such as the fragile base class problem and deep inheritance hierarchies, while still allowing polymorphic behavior.


##### Example: Trait inheritance in Rust

```rust
// Define a base trait with a common behavior
trait Animal {
    fn speak(&self);
}

// Define a trait that inherits from Animal
trait Mammal: Animal {
    fn walk(&self);
}

// Struct representing a Dog
struct Dog;

// Implement the Animal trait for Dog
impl Animal for Dog {
    fn speak(&self) {
        println!("Woof!");
    }
}

// Implement the Mammal trait for Dog
impl Mammal for Dog {
    fn walk(&self) {
        println!("Dog is walking.");
    }
}

fn main() {
    let dog = Dog;

    // Dog can speak because it implements Animal
    dog.speak();

    // Dog can walk because it implements Mammal, which inherits from Animal
    dog.walk();
}
```
---
### 14. What is Zero-Cost Abstraction?

**Zero-Cost Abstractions** means that the high-level abstractions Rust provides, such as iterators, closures, traits, and pattern matching, compile down to code that is as efficient as manually written low-level code. In other words, **you don’t pay any runtime performance penalty for using these abstractions** — the compiler optimizes them away.

Rust's abstractions provide safety, expressiveness, and convenience **without sacrificing performance**.

#### Example:

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4];

    // Using iterators and closures (high-level abstraction)
    let doubled: Vec<i32> = numbers.iter()
        .map(|&x| x * 2)
        .filter(|&x| x > 4)
        .collect();

    println!("{:?}", doubled); // Output: [6, 8]
}
```

### Why is this zero-cost?

* The iterator chain (`iter()`, `map()`, `filter()`) is lazy and composed of small functions.
* At compile time, Rust **inlines** and **optimizes** this chain so it performs **no more work** than an equivalent `for` loop written by hand.
* No intermediate collections are created during iteration; it all happens efficiently in one pass.

### Equivalent manual implementation (no abstraction):

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4];
    let mut doubled = Vec::new();

    for &x in &numbers {
        let val = x * 2;
        if val > 4 {
            doubled.push(val);
        }
    }

    println!("{:?}", doubled); // Output: [6, 8]
}
```

Both programs produce the **same machine code** after optimizations, but the first version is much more expressive and concise.

Zero-cost abstraction means **using idiomatic Rust abstractions doesn’t cost you runtime performance**, because the compiler generates highly optimized code equivalent to what you’d write manually.

---

## Memory Management & Smart Pointers

### 15. What is the possibility of memory leaks in Rust?

```rust
todo!()
```

---
### 16. What are Smart Pointers? Explain `Box`, `Rc`, `Arc`.

**Smart Pointers** in Rust are types that not only act like regular pointers but also have additional capabilities, such as automatic memory management, reference counting, or thread safety.

Unlike raw pointers, smart pointers:

* Manage **ownership** of the data they point to.
* **Automatically deallocate** memory when no longer used.
* Provide **type safety** and **abstractions** over manual memory management.

## `Box<T>` – Heap Allocation and Single Ownership

* `Box<T>` stores data **on the heap**.
* It has **exclusive ownership**—only one `Box` can own the data at a time.
* It is ideal for:

  * Storing large data on the heap instead of the stack.
  * Enabling recursive types like linked lists or trees.

```rust
fn main() {
    let b = Box::new(42); // heap allocation
    println!("Value = {}", b); // Deref happens automatically
} // memory is freed when `b` goes out of scope
```

Use `Box<T>` when:

* You need heap allocation with single ownership.
* You want to move heap-allocated data across scopes.


## `Rc<T>` – Reference Counting (Single-threaded Shared Ownership)

* `Rc` stands for **Reference Counted**.
* Allows **multiple ownership** of heap-allocated data.
* Keeps a **reference count** of how many `Rc` pointers point to the same allocation.
* **Not thread-safe**—only for use in **single-threaded** contexts.

```rust
use std::rc::Rc;

fn main() {
    let rc1 = Rc::new(5);
    let rc2 = Rc::clone(&rc1);

    println!("rc1 count = {}", Rc::strong_count(&rc1)); // 2
    drop(rc1); // count decreases
    println!("rc2 count = {}", Rc::strong_count(&rc2)); // 1
} // memory deallocated when count reaches 0
```

Use `Rc<T>` when:

* You need shared read-only access to data in a single-threaded context.
* You want multiple owners but don't need mutation or thread safety.

## `Arc<T>` – Atomic Reference Counting (Thread-safe Shared Ownership)

* `Arc` stands for **Atomic Reference Counted**.
* Like `Rc<T>`, but **safe to share across threads**.
* Internally uses atomic operations to update the reference count.
* Often combined with `Mutex` or `RwLock` to enable **shared mutability** across threads.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..5 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result = {}", *counter.lock().unwrap()); // 5
}
```

Use `Arc<T>` when:

* You need to share data between threads safely.
* You're working in a concurrent/multithreaded environment.
---
