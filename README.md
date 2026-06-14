Employee Payroll System

Overview

This project is a Java-based payroll processing system designed to demonstrate employee data management, financial calculations, operational workflows, and structured backend processing logic.

The application allows users to enter employee payroll information, calculate overtime pay, process tax deductions, and generate formatted payroll summaries using structured data handling and workflow-based programming techniques.

---

Features

- Employee payroll processing
- Overtime pay calculations
- Tax deduction calculations
- Employee data management
- Nested data structure handling
- Currency formatting
- Structured workflow processing
- Console-based user interaction

---

Technologies Used

- Java
- ArrayList
- ListIterator
- Scanner Input Handling
- NumberFormat
- Conditional Logic
- Loops & Iteration

---

Project Structure

- "CalculatePayProgram5App.java" → Main payroll processing and employee management application

---

Concepts Demonstrated

This project demonstrates several foundational software engineering and operational systems concepts:

- Payroll calculation logic
- Financial processing workflows
- Nested data structures
- Employee data management
- Operational backend processing
- Workflow automation logic
- Input handling
- Structured program design

---

Purpose

This project was created as part of a systems design and programming learning journey focused on building operational business applications and workflow-oriented backend systems using Java.


## Payroll FastAPI Refactor

This project refactors the original Java console-based payroll program into a FastAPI backend service. The original version required users to manually enter employee name, hours worked, and pay rate. The refactored version uses `employee_id` as a foreign-key style reference to the Employee Management System data.

Payroll currently references EMS employee data.
For local testing a copy of employees.json was used.
Future versions will connect directly to EMS services.

### Current Features

* FastAPI backend
* Swagger documentation
* JSON payroll persistence
* Auto-incremented `payroll_id`
* Auto-generated check numbers such as `001`, `002`, and `003`
* Employee lookup by `employee_id`
* Hourly wage pulled from EMS employee data
* Payroll processing using only `employee_id` and `hours_worked`
* Regular hours calculation
* Overtime hours calculation
* Gross pay calculation
* Deduction calculation
* Net pay calculation
* GET all payroll records
* GET payroll record by payroll ID
* POST payroll processing route

### API Routes

* `GET /`
* `GET /payroll`
* `GET /payroll/id/{payroll_id}`
* `POST /payroll`

### Example POST Request

```json
{
    "employee_id": 1001,
    "hours_worked": 45
}
```

### Next Enhancements

* Deduction breakdown by line item
* Search payroll by check number
* Payroll reports
* PATCH payroll records
* DELETE payroll records
* Attendance module
* Shared HRMS/SaaS folder structure connecting EMS, Payroll, and future modules
