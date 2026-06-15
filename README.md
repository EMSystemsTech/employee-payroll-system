# Employee Payroll System

## Overview

This project demonstrates the evolution of a payroll processing application from a traditional Java console program into a modern FastAPI backend service.

The original application was designed to manage employee payroll calculations, overtime processing, tax deductions, and payroll summaries using structured business logic and operational workflows.

The project was later refactored into a RESTful API architecture to support automation, service integration, data persistence, and future Human Resource Management System (HRMS) expansion.

---

# Original Java Payroll System

## Features

* Employee payroll processing
* Overtime pay calculations
* Tax deduction calculations
* Employee data management
* Nested data structure handling
* Currency formatting
* Structured workflow processing
* Console-based user interaction

## Technologies Used

* Java
* ArrayList
* ListIterator
* Scanner
* NumberFormat
* Conditional Logic
* Loops and Iteration

## Project Structure

```text
CalculatePayProgram5App.java
```

### Purpose

This project was originally created to demonstrate payroll processing, financial calculations, workflow automation, and structured business application development using Java.

---

# FastAPI Payroll Refactor

## Overview

The original Java payroll application was refactored into a FastAPI backend service to demonstrate modern API development, backend automation, service-oriented design, and payroll processing workflows.

The refactored solution uses employee_id as a reference to employee records maintained by the Employee Management System (EMS).

For portfolio and open-source demonstration purposes, this repository includes a local employee data file used during development and testing.

## Current Features

### Payroll Processing

* Employee lookup by employee_id
* Hourly wage retrieval from employee data
* Payroll processing using employee_id and hours_worked
* Regular hours calculation
* Overtime hours calculation
* Gross pay calculation
* Payroll deduction calculation
* Net pay calculation

### Data Management

* JSON payroll persistence
* Auto-incrementing payroll_id values
* Auto-generated payroll check numbers (001, 002, 003, etc.)

### API Features

* FastAPI backend
* Swagger API documentation
* GET all payroll records
* GET payroll record by payroll ID
* POST payroll processing endpoint

## API Routes

```text
GET /
GET /payroll
GET /payroll/id/{payroll_id}
POST /payroll
```

## Swagger Documentation

```text
http://localhost:8000/docs
```

## Example POST Request

```json
{
    "employee_id": 1001,
    "hours_worked": 45
}
```

## Example Response

```json
{
    "message": "Payroll processed successfully"
}
```

---

# Architecture Notes

The Payroll service is being developed as part of a larger Human Resource Management System (HRMS) SaaS platform.

The production architecture separates functionality into individual modules while maintaining shared employee data across services.

```text
HRMS SaaS
│
├── Employee Management System
├── Payroll
├── Attendance & Scheduling
└── Shared Services
```

To keep the public repository focused on payroll functionality, only the Payroll module and supporting demonstration data are included here.

---

# Future Enhancements

## Payroll Enhancements

* Deduction breakdown by line item
* Search payroll by check number
* Payroll reporting endpoints
* PATCH payroll records
* DELETE payroll records

## HRMS Expansion

* Attendance & Scheduling module
* Shared service integration
* Cross-module API communication
* HRMS SaaS platform expansion

```
```
