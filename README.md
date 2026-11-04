# Student Course Registration System

A C++ console application that simulates a university course registration workflow. Built as a practical exercise for my Data Structures course to implement core structures in a real-world scenario rather than in isolation.

---

## Data Structures Used

| Structure       | Where used                             | Why                                           |
|-----------------|----------------------------------------|-----------------------------------------------|
| Array           | Course catalog                         | Fixed set of courses; O(1) indexed access     |
| Singly Linked List | Student roster per course           | Dynamic size; efficient add/remove            |
| Queue (FIFO)    | Waitlist when course is full           | First-come, first-served waitlist ordering    |
| Stack (LIFO)    | Enrollment action history (undo)       | Most recent action undone first               |
| Binary Search Tree | Student lookup by ID               | O(log n) average search vs. O(n) for array   |

---

## Features

- View the course catalog with current enrollment numbers
- Enroll a student in a course (moves to waitlist if full)
- Drop a student from a course (automatically promotes from waitlist)
- View the roster and waitlist for any course
- Search for a student by ID using the BST
- View enrollment history
- Undo the most recent enrollment

**Not yet implemented** (marked in the code and planned extensions below):
- Full undo for drop and waitlist actions
- Saving/loading data between sessions
- Input validation beyond basic type checking

---

## Project Structure

```
course-registration-system/
├── src/
│   ├── main.cpp              # Entry point, menu, and application logic
│   ├── course_catalog.h      # Course, StudentRoster (linked list), WaitlistQueue, CourseCatalog (array)
│   ├── student_bst.h         # Student record and BST implementation
│   └── enrollment_stack.h    # EnrollmentRecord and Stack implementation
└── README.md
```

All data structures are implemented from scratch in header files. No STL containers (vector, list, stack, queue, map) are used — the point is to build and understand the structures, not just use them.

---

## Compiling and Running

**Requirements:** A C++ compiler supporting C++11 or later (g++, clang++, or MSVC).

**Compile:**
```bash
g++ -std=c++11 -o registration src/main.cpp
```

**Run:**
```bash
./registration        # Linux / macOS
registration.exe      # Windows
```

---

## Sample Output

```
  ============================================
   Student Course Registration System
  ============================================
  Initializing with sample data...

  ---- Main Menu ----------------------------------------
  1. View course catalog
  2. Enroll student in a course
  ...
  Enter choice: 1

  --------------------------------------------------
  ID        Title                           Seats
  --------------------------------------------------
  CS101     Introduction to Programming     0/30
  CS201     Data Structures                 0/25
  CS301     Algorithms                      0/20
  MATH101   Calculus I                      0/35
  ENG101    English Composition             0/40
  --------------------------------------------------

  Enter choice: 2
  Student ID : S001
  Course ID  : CS201
  Ahmed Ali enrolled in Data Structures.

  Enter choice: 4
  Course ID: CS201

  Course : CS201 — Data Structures
  Seats  : 1 / 25
  Enrolled students:
    1. S001
```

---

## What I Practiced

- Implementing linked lists, stacks, and queues manually with pointers
- Understanding the trade-offs between arrays and linked structures
- BST insertion and search with recursive functions
- Separating data structure logic from application logic using header files
- Memory management with constructors and destructors

---

## Planned Extensions

- [ ] Complete undo support for drop and waitlist actions
- [ ] Graph representation of course prerequisites
- [ ] File I/O to persist data between runs
- [ ] Display all courses a student is enrolled in (reverse lookup)
- [ ] Self-balancing BST (AVL tree) to replace the current unbalanced implementation
