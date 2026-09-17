# 🎓 Student Database Management System

A simple **Python-based Student Database Management System** designed to manage and analyze student records through a menu-driven command-line interface.

The system uses **Python dictionaries, functions, loops, conditional statements, and exception handling** to provide basic student record management functionality.

---

## 📌 Overview

The Student Database Management System allows users to:

- Add new students and their marks
- Prevent duplicate student entries
- View all student records
- Search for students by name
- Calculate the class average
- Find the highest marks
- Find the lowest marks
- Identify students with the highest and lowest scores, including ties
- Display grades based on marks
- Handle invalid inputs using exception handling

This project is designed as a beginner-friendly Python application for understanding **data structures, functions, validation, and control flow**.

---

## ✨ Features

### 👨‍🎓 Add Student
- Add a student's name and marks to the database.
- Accepts marks between **0 and 100**.
- Prevents duplicate student names.
- Validates empty names and invalid marks.
- Handles non-integer mark inputs.

### 📋 View Students
- Displays all students currently stored in the database.
- Shows each student's name and marks.
- Displays an appropriate message when the database is empty.

### 🔍 Search Student
- Search for a student using their name.
- Displays the student's marks if found.
- Shows a "Student not found" message when no matching record exists.

### 📊 Calculate Class Average
- Calculates the average marks of all students.
- Handles an empty database without causing an error.
- Displays the average up to two decimal places.

### 🏆 Highest Marks
- Finds the highest mark in the database.
- Displays all students who achieved the highest mark.
- Supports multiple students with the same highest score.

### 📉 Lowest Marks
- Finds the lowest mark in the database.
- Displays all students who achieved the lowest mark.
- Supports multiple students with the same lowest score.

### 🎯 Display Grades
Grades are assigned based on the student's marks:

| Marks | Grade |
|-------|-------|
| 90–100 | O |
| 80–89 | A+ |
| 70–79 | A |
| 60–69 | B+ |
| 50–59 | B |
| Below 50 | Fail |

### 🛡️ Input Validation & Error Handling
- Prevents invalid marks.
- Prevents empty student names.
- Prevents duplicate student records.
- Handles invalid numeric input using `try-except`.
- Prevents calculations on an empty database.

---

## 🛠️ Tech Stack

- **Python**
- **Dictionaries**
- **Functions**
- **Loops**
- **Conditional Statements**
- **Exception Handling**
- **String Formatting**

---

## 📂 Project Structure

```text
Student-Database-Management-System/
│
├── student_database.py
└── README.md
