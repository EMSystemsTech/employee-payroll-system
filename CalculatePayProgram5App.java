/**
 * Calculate Pay Program - Week 1 Assignment
 * Ebony Morrow
 * CPT 307 Data Structures and Algorithms
 * Professor Joel Short
 * November 26, 2024
 */

import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.ListIterator;
import java.util.Scanner;

public class CalculatePayProgram5App {
	
	//Start of the Calculate Pay Program version 5
	public static void main(String[] args) {
		//Opens scanner to read user input
		Scanner scanner = new Scanner(System.in);

		//Arrays to list employee information and the final count printed
		ArrayList<ArrayList<String>> fullEmployeeList = new ArrayList<>();
		ArrayList<String> employeeList = new ArrayList<>();

		
		// Runs the loop to add three employees
		int i = 0;
		
		while (i < 3) {
			
			/**
			 * Helps remove white space so the scanner can 
			 * keep reading employees after the first input
			 * employee in the program.
			 */
			scanner.useDelimiter(System.lineSeparator());
			
			//Ensures a space between each added employee
			System.out.println();
			
			//User input start for name, hours, and payRate.
			String name;
			System.out.print("Enter your first and last name: ");
			name = scanner.next().toUpperCase().trim();
			
			int hours= 0;
			System.out.print("Enter total hours worked: "); // Request input for hours worked.
			hours = scanner.nextInt();			
			
			double payRate = 0;
			System.out.print("Enter your pay rate: "); // Request input for hourly pay rate.
			payRate = (scanner.nextDouble());
			
			scanner.nextLine();
			
			//Calculating gross pay amount and checking for overtime pay.
			double grossPaid = 0;
			int overtime= 0;

			if (hours <= 40) {
				double normal = hours * payRate;
				grossPaid = normal;
			} else {
				overtime = hours - 40;
				double overtimePay = (overtime * (payRate * 1.5)) + (40 * payRate);
				grossPaid = overtimePay;
			}
						
			//Performing the operation for grossPaid - deductions
			final double federalTaxRate = 0.15d; // 15%
			final double stateTaxRate = 0.0307d; // 3.07%
			final double medicareRate = 0.0145d; // 1.45%
			final double socialSecurityRate = 0.062d; // 6.2%
			final double unemploymentInsuranceRate = 0.0007d; // 0.07%
        
			final double federalTaxAmount = federalTaxRate * grossPaid;
			final double stateTaxAmount = stateTaxRate * grossPaid;
			final double medicareAmount = medicareRate * grossPaid;
			final double socialSecurityAmount = socialSecurityRate * grossPaid;
			final double unemploymentInsuranceAmount = unemploymentInsuranceRate * grossPaid;
			
			
			// Final Deduction amount
			double deductions;
			deductions = federalTaxAmount + stateTaxAmount + medicareAmount + socialSecurityAmount + unemploymentInsuranceAmount;
			
			// Actual Income received
			double netPay;
			netPay = grossPaid - deductions;
			
			// Changing original line type to String and formatting.
			NumberFormat currency = NumberFormat.getCurrencyInstance();

			String resultUserPayRate = currency.format(payRate);
			String resultGrossPaid = currency.format(grossPaid);
			String resultDeductions = currency.format(deductions);
			String resultNetPay = currency.format(netPay);
        
			String resultUserHours = String.valueOf(hours);
			String resultOvertime = String.valueOf(overtime);
			
			//List of employee's as a nested array
			employeeList.add(name);
			employeeList.add(resultUserPayRate);
			employeeList.add(resultUserHours);
			employeeList.add(resultOvertime);
			employeeList.add(resultGrossPaid);
			employeeList.add(resultDeductions);
			employeeList.add(resultNetPay);
			
			//Saving the current loops employee information to the main list.
			fullEmployeeList.add(employeeList);
			
			i++;
			System.out.println();
		}
		
			//Changing the employeeList to a String to iterate over with custom print statements
			ListIterator<String> indexFullEmployeeList = employeeList.listIterator();
			while(indexFullEmployeeList.hasNext()) {
				System.out.println("Employee Name: " + indexFullEmployeeList.next());
				System.out.println("Rate of Pay: " + indexFullEmployeeList.next());
				System.out.println("Hours Worked: " + indexFullEmployeeList.next());
				System.out.println("Overtime Worked: " + indexFullEmployeeList.next());
				System.out.println("Gross Pay: " + indexFullEmployeeList.next());
				System.out.println("Total Amount of Deductions: " + indexFullEmployeeList.next());
				System.out.println("Net Pay: " + indexFullEmployeeList.next());
				System.out.println();
			}
		
		String result = "Employees Printed: " + fullEmployeeList.size();
		System.out.println(result);
		scanner.close();
	}
}