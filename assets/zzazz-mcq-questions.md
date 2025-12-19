## Round 1 – MCQ Test (Rust Fundamentals – 50 Questions)

### Memory Safety & Ownership

1. Which Rust feature ensures memory safety without a garbage collector?

   * A. Box<T>
   * B. Rc<T>
   * C. Borrow Checker
   * D. Cell<T>

2. How does Rust guarantee memory safety without a garbage collector?

   * A. Explicit deallocation
   * B. Ownership, borrowing, and lifetimes
   * C. Reference counting everywhere
   * D. Automatic memory compaction

3. What mechanism ensures references do not outlive their owners?

   * A. Garbage Collector
   * B. Mutex
   * C. Lifetimes
   * D. Channels

4. What does the `Copy` trait imply for a Rust type?

   * A. It can be duplicated without heap allocation
   * B. It uses reference counting
   * C. It enables interior mutability
   * D. It disables ownership transfer

5. What happens when you try to mutate data borrowed immutably?

   * A. Runtime panic
   * B. Compilation error
   * C. Undefined behavior
   * D. Silent failure

6. How does Rust prevent dangling pointers?

   * A. Garbage collection
   * B. Ownership and borrow checking
   * C. Reference counting
   * D. Runtime checks

---

### Smart Pointers & Interior Mutability

7. Which smart pointer provides heap allocation with single ownership?

   * A. Rc<T>
   * B. Arc<T>
   * C. Box<T>
   * D. RefCell<T>

8. What is the main difference between `Rc<T>` and `Arc<T>`?

   * A. Arc is thread-safe
   * B. Rc is atomic
   * C. Rc supports Mutex
   * D. No difference

9. When is interior mutability required?

   * A. To bypass ownership
   * B. To mutate data through immutable references
   * C. To enable async execution
   * D. To improve performance

10. How does `RefCell<T>` enforce borrowing rules?

    * A. Compile-time checks
    * B. Runtime checks
    * C. Unsafe blocks
    * D. Atomic counters

11. Which type allows safe mutation of static variables?

    * A. RefCell<T>
    * B. Arc<Mutex<T>>
    * C. Cell<T>
    * D. Box<T>

---

### Concurrency & Parallelism

12. Which Rust construct is best for shared mutable state across threads?

    * A. Rc<T>
    * B. RefCell<T>
    * C. Mutex<T>
    * D. Cell<T>

13. What does the `Send` trait guarantee?

    * A. Safe transfer across threads
    * B. Automatic cloning
    * C. Async execution
    * D. Interior mutability

14. What does “fearless concurrency” mean in Rust?

    * A. No locks needed
    * B. Compiler prevents data races
    * C. Automatic deadlock recovery
    * D. Runtime thread scheduling

15. What happens if a thread panics while holding a Mutex?

    * A. Deadlock
    * B. Mutex poisoning
    * C. Automatic unlock without impact
    * D. Program termination

16. Which type should be used for read-only shared data across threads?

    * A. Rc<T>
    * B. Arc<T>
    * C. RefCell<T>
    * D. Cell<T>

---

### Async Rust & Tokio

17. What is the primary purpose of the `async` keyword?

    * A. Spawn threads
    * B. Convert function into a Future
    * C. Improve compile time
    * D. Enable unsafe execution

18. Why is Tokio required in async Rust?

    * A. Garbage collection
    * B. Async runtime and scheduler
    * C. Memory allocation
    * D. Thread pooling

19. What is the difference between Tokio tasks and OS threads?

    * A. Tasks are lighter-weight
    * B. Tasks block threads
    * C. Threads are async
    * D. No difference

20. How can multiple independent futures run concurrently?

    * A. `.await` sequentially
    * B. `tokio::join!`
    * C. Mutex on futures
    * D. Rc<Future>

21. Which function should be used for blocking work inside Tokio?

    * A. std::thread::spawn
    * B. tokio::spawn
    * C. tokio::task::block_in_place
    * D. async {}

---

### Error Handling

22. What does the `?` operator do?

    * A. Converts types
    * B. Propagates errors
    * C. Panics on error
    * D. Breaks loops

23. What happens when `unwrap()` is called on `None`?

    * A. Returns default
    * B. Compilation error
    * C. Runtime panic
    * D. Silent failure

24. Why are `Result` and `Option` preferred over exceptions?

    * A. Faster execution
    * B. Explicit error handling
    * C. Automatic recovery
    * D. Less boilerplate

25. Which macro reduces error-handling boilerplate?

    * A. println!
    * B. try!
    * C. unwrap!
    * D. anyhow!

---

### Traits, Iterators & Abstractions

26. What is a zero-cost abstraction in Rust?

    * A. Traits
    * B. Garbage collection
    * C. Rc<T>
    * D. RefCell<T>

27. Which iterator method returns a new collection?

    * A. map()
    * B. for_each()
    * C. filter()
    * D. collect()

28. What does the `move` keyword do in closures?

    * A. Forces cloning
    * B. Transfers ownership
    * C. Prevents mutation
    * D. Enables async

29. What does `Cow<T>` represent?

    * A. Atomic counter
    * B. Borrowed or owned data
    * C. Unsafe pointer
    * D. Heap-only data

30. Which trait allows equality comparison?

    * A. Hash
    * B. Eq
    * C. Display
    * D. Clone

---

### Strings, Collections & Utilities

31. How do you efficiently convert `String` to `&str`?

    * A. &String
    * B. as_str()
    * C. clone()
    * D. from_utf8_lossy()

32. Which iterator method applies a function and returns results?

    * A. filter()
    * B. map()
    * C. for_each()
    * D. collect()

33. What does `std::mem::replace` do?

    * A. Swap values
    * B. Extract value leaving default
    * C. Allocate heap memory
    * D. Manage threads

---

### Web, Database & Tooling

34. Which crate is best for async PostgreSQL with pooling?

    * A. diesel
    * B. rusqlite
    * C. tokio
    * D. sqlx

35. Which crate is commonly used for JSON handling?

    * A. regex
    * B. serde_json
    * C. tokio
    * D. diesel

36. Which library is used to build JSON REST APIs?

    * A. warp
    * B. std::net
    * C. hyper (raw)
    * D. serde_yaml

37. Which tool profiles CPU usage in Rust?

    * A. rustfmt
    * B. cargo flamegraph
    * C. clippy
    * D. cargo audit

38. Which tool detects race conditions and UB?

    * A. Miri
    * B. rustfmt
    * C. tokio-console
    * D. cargo audit

---

### Unsafe & Low-Level Rust

39. When should `unsafe` be used?

    * A. To improve speed
    * B. To bypass borrow checker
    * C. When compiler cannot prove safety
    * D. For async code

40. What happens when dereferencing a null raw pointer?

    * A. Compilation error
    * B. Runtime panic
    * C. Undefined behavior
    * D. Safe no-op

---

### Advanced Concepts

41. What is the purpose of `derive`?

    * A. Auto-implement traits
    * B. Convert structs to enums
    * C. Declare traits
    * D. Generate unsafe code

42. Which atomic type supports lock-free counters?

    * A. Mutex
    * B. RefCell
    * C. AtomicUsize
    * D. Cell

43. How is deterministic cleanup achieved?

    * A. Garbage collection
    * B. Drop trait
    * C. Unsafe blocks
    * D. Yielding threads

44. Which library is used for secure hashing?

    * A. ring
    * B. regex
    * C. std::hash
    * D. tokio

45. Which keyword makes a function private by default?

    * A. pub
    * B. mod
    * C. private
    * D. No keyword

---

### Code Behavior & Reasoning

46. What happens when cloning `Rc<T>`?

    * A. Deep copy
    * B. Ref count increments
    * C. Runtime panic
    * D. Ownership transfer

47. What happens if an immutable borrow exists and mutation is attempted?

    * A. Runtime panic
    * B. Compilation error
    * C. Undefined behavior
    * D. Silent failure

48. Which method converts `Result<T,E>` to `Option<T>`?

    * A. unwrap()
    * B. map()
    * C. ok()
    * D. expect()

49. Which library is used for low-level HTTP handling?

    * A. hyper
    * B. actix-web
    * C. warp
    * D. reqwest

50. Which keyword allows other async tasks to run while waiting?

    * A. await
    * B. async
    * C. move
    * D. sync

---
