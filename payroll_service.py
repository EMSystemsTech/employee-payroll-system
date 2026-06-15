import json

PAYROLL_FILE = "payroll.json"
EMPLOYEES_FILE = "../Shared/data/employees.json"


def load_payroll():
    try:
        with open(PAYROLL_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_payroll(payroll):
    with open(PAYROLL_FILE, "w") as file:
        json.dump(payroll, file, indent=4)


def generate_payroll_id():
    payroll = load_payroll()

    if len(payroll) == 0:
        return 1

    highest_id = max(record["payroll_id"] for record in payroll)

    return highest_id + 1


def generate_check_number(payroll_id):
    return str(payroll_id).zfill(3)


def calculate_regular_hours(hours_worked):
    if hours_worked <= 40:
        return hours_worked

    return 40


def calculate_overtime_hours(hours_worked):
    if hours_worked > 40:
        return hours_worked - 40

    return 0


def calculate_gross_pay(hours_worked, hourly_wage):
    regular_hours = calculate_regular_hours(hours_worked)
    overtime_hours = calculate_overtime_hours(hours_worked)

    regular_pay = regular_hours * hourly_wage
    overtime_pay = overtime_hours * (hourly_wage * 1.5)

    return regular_pay + overtime_pay


def calculate_deductions(gross_pay):
    federal_tax_rate = 0.15
    state_tax_rate = 0.0307
    medicare_rate = 0.0145
    social_security_rate = 0.062
    unemployment_insurance_rate = 0.0007

    deductions = (
        gross_pay * federal_tax_rate
        + gross_pay * state_tax_rate
        + gross_pay * medicare_rate
        + gross_pay * social_security_rate
        + gross_pay * unemployment_insurance_rate)

    return round(deductions, 2)


def calculate_net_pay(gross_pay, deductions):
    return gross_pay - deductions


def create_payroll_record(employee, hours_worked):
    payroll_id = generate_payroll_id()
    check_number = generate_check_number(payroll_id)

    hourly_wage = employee["hourly_wage"]
    regular_hours = calculate_regular_hours(hours_worked)
    overtime_hours = calculate_overtime_hours(hours_worked)
    gross_pay = calculate_gross_pay(hours_worked, hourly_wage)
    deductions = calculate_deductions(gross_pay)
    net_pay = calculate_net_pay(gross_pay, deductions)

    payroll_record = {
        "payroll_id": payroll_id,
        "check_number": check_number,
        "employee_id": employee["employee_id"],
        "name": employee["name"],
        "hourly_wage": hourly_wage,
        "hours_worked": hours_worked,
        "regular_hours": regular_hours,
        "overtime_hours": overtime_hours,
        "gross_pay": round(gross_pay, 2),
        "deductions": deductions,
        "net_pay": round(net_pay, 2)}

    return payroll_record


def get_employee_by_id(employee_id):
    with open(EMPLOYEES_FILE, "r") as file:
        employees = json.load(file)

    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    return None

def get_payroll_by_check_number(check_number):
    payroll_records = load_payroll()

    for payroll in payroll_records:
        if payroll["check_number"] == check_number:
            return payroll

    return None

def get_payroll_by_id(payroll_id):
    payroll_records = load_payroll()

    for payroll in payroll_records:
        if payroll["payroll_id"] == payroll_id:
            return payroll

        return None

def process_payroll(employee_id, hours_worked):
    payroll = load_payroll()
    employee = get_employee_by_id(employee_id)

    if employee is None:
        return None

    payroll_record = create_payroll_record(employee, hours_worked)

    payroll.append(payroll_record)
    save_payroll(payroll)

    return payroll_record


