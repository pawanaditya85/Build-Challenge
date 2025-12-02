````markdown
# Intuit Build Challenge - Coding Assessment

## Overview
This repository contains the completed solutions for the Intuit Build Challenge. The project is implemented in **Python** and demonstrates core software engineering competencies including concurrency, thread synchronization, and functional data analysis.

## Prerequisites
* **Language:** Python 3.8 or higher.
* **Dependencies:** None. This project utilizes only the Python Standard Library (`threading`, `queue`, `csv`, `functools`, `unittest`) to ensure lightweight and dependency-free execution.

## Project Structure
Build Challenge- Pawan Aditya/
│
├── src/
│   ├── assignment_1.py   # Producer-Consumer implementation
│   └── assignment_2.py   # Functional Data Analysis implementation
│
├── data/
│   └── sales_data.csv    # Superstore dataset subset
│
├── tests/
│   ├── test_assignment_1.py
│   └── test_assignment_2.py
│
├── Results.pdf           # Screenshots of program execution output
└── README.md

-----

## Assignment 1: Producer-Consumer Pattern

**Goal:** Implement a classic producer-consumer pattern demonstrating thread synchronization and communication.

### Implementation Details

  * **Architecture:** The system simulates concurrent data transfer between a **Producer thread** (which reads from a source container) and a **Consumer thread** (which stores items in a destination container).
  * **Synchronization:** Achieved using a **Blocking Queue** (`queue.Queue`). This inherently handles the **Wait/Notify mechanism**, blocking the producer when full and the consumer when empty, preventing race conditions.
  * **Concurrency:** Utilizes the `threading` module to execute tasks simultaneously.

### How to Run

Execute the script from the project root:

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

-----

## Assignment 2: Data Analysis

**Goal:** Perform data analysis on CSV data using functional programming paradigms and stream-like operations.

### Dataset Choices & Assumptions

*Per the requirement to select a dataset and document choices:*

  * **Dataset Selection:** I utilized a subset of the **Superstore Sales Dataset** (Industry Standard for Retail Analytics).
  * **Reasoning:** This dataset was chosen because its schema contains hierarchical categorical data (`Category`, `Region`) and numerical metrics (`Sales`, `Profit`), which are ideal for demonstrating complex grouping and aggregation logic.
  * **Assumptions:**
      * `Sales` and `Profit` columns are treated as floating-point numbers.
      * The solution automatically handles potential BOM (`\ufeff`) characters common in CSV exports.

### Implementation Details

  * **Stream Operations:** Implemented using Python Generators (`yield`) to lazy-load data row-by-row, ensuring memory efficiency similar to stream processing.
  * **Functional Programming:** All aggregations are performed using **Lambda expressions** inside `map()`, `filter()`, and `functools.reduce()`, avoiding mutable state loops.

### How to Run

Execute the script from the `src` directory to ensure relative paths resolve correctly:

```bash
cd src
python assignment_2.py
```

### Sample Output

The following results are printed to the console upon execution:

```text
--- Analysis Results ---
Total Sales (Furniture): $2000.33
Average Profit (West Region): $23.9
```

-----

## Testing

Comprehensive unit tests are included for all analysis methods and concurrency logic.

### How to Run Tests

From the project root directory, use the unittest discovery command:

```bash
python -m unittest discover tests
```

**Expected Test Output:**

```text
..Transfer Complete. Final Destination Count: 5
.
----------------------------------------------------------------------
Ran 3 tests in 0.305s

OK
```
**Note:** For visual verification of the program outputs, please refer to the included **[Results.pdf](Results.pdf)**.

```
```