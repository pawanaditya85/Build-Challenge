# Intuit Build Challenge – Coding Assessment
---
## Prerequisites

- **Language:** Python 3.8 or higher  
- **Dependencies:** None – this project uses only the Python Standard Library:  
  - `threading`  
  - `queue`  
  - `csv`  
  - `functools`  
  - `unittest`  

This ensures lightweight, dependency-free execution.
---
## Project Structure
````markdown
Build Challenge - Pawan Aditya/
│
├── src/
│   ├── assignment_1.py       # Producer-Consumer implementation
│   └── assignment_2.py       # Functional data analysis implementation
│
├── data/
│   └── sales_data.csv        # Superstore dataset subset
│
├── tests/
│   ├── test_assignment_1.py
│   └── test_assignment_2.py
│
├── Results.pdf               # Screenshots of program execution output
└── README.md
````

## Assignment 1: Producer–Consumer Pattern

**Goal:**
Implement a classic producer–consumer pattern demonstrating thread synchronization and communication.

### Implementation Details

* **Architecture:**
  Simulates concurrent data transfer between a **Producer thread** (reads from a source container) and a **Consumer thread** (stores items in a destination container).

* **Synchronization:**
  Achieved using a **blocking queue** (`queue.Queue`). This provides the wait/notify behavior:

  * Blocks the producer when the queue is full
  * Blocks the consumer when the queue is empty
    This prevents race conditions.

* **Concurrency:**
  Uses the `threading` module to execute tasks simultaneously.

### How to Run

From the project root:

```bash
python src/assignment_1.py
```

### Sample Output

The program logs thread activity to the console with timestamps:

```text
10:15:01 - [PRODUCER] Transferred Record-1 to Queue
10:15:01 - [CONSUMER] Stored Record-1 in Final Destination
10:15:01 - [PRODUCER] Transferred Record-2 to Queue
10:15:02 - [CONSUMER] Stored Record-2 in Final Destination
...
10:15:05 - Transfer Complete. Final Destination Count: 10
```

---

## Assignment 2: Data Analysis

**Goal:**
Perform data analysis on CSV data using functional programming paradigms and stream-like operations.

### Dataset Choices & Assumptions

Per the requirement to select a dataset and document choices:

* **Dataset Selection:**
  A subset of the **Superstore Sales Dataset** (commonly used for retail analytics).

* **Reasoning:**
  The dataset includes hierarchical categorical fields (`Category`, `Region`) and numerical metrics (`Sales`, `Profit`), which are ideal for demonstrating grouping and aggregation logic.

* **Assumptions:**

  * `Sales` and `Profit` columns are treated as floating-point numbers.
  * The solution automatically handles potential BOM (`\ufeff`) characters often present in CSV exports.

### Implementation Details

* **Stream Operations:**
  Implemented using Python generators (`yield`) to lazily load data row by row, providing memory-efficient, stream-like processing.

* **Functional Programming:**
  Aggregations are implemented using:

  * `map()`
  * `filter()`
  * `functools.reduce()`

  with lambda expressions, avoiding mutable state and explicit loops where possible.

### How to Run

Run from the `src` directory so that relative paths resolve correctly:

```bash
cd src
python assignment_2.py
```

### Sample Output

Example console output:

```text
--- Analysis Results ---
Total Sales (Furniture): $2000.33
Average Profit (West Region): $23.9
```

---

## Testing

Comprehensive unit tests are included for:

* Concurrency logic (producer–consumer)
* Data analysis methods

### How to Run Tests

From the project root directory:

```bash
python -m unittest discover tests
```

**Expected Test Output (example):**

```text
..Transfer Complete. Final Destination Count: 5
.
----------------------------------------------------------------------
Ran 3 tests in 0.305s

OK
```

---

## Additional Resources

For visual verification of the program outputs, refer to:

* **[Results.pdf](Results.pdf)** – contains screenshots of the execution results.
