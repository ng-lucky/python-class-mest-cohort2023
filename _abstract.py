from abc import ABC, abstractmethod


class Payroll(ABC):
    @abstractmethod
    def print_payroll(self):
        pass

class Employee():
    id = 0
    first_name = ''
    last_name = ''
    middle_name = ''
    role = ''
    email = ''
    phone_number = ''
    is_active = True
    salary = 0

class FullTimeEmployee(Employee, Payroll):
    
    def print_payroll(self):
        print(f"Employee Name: {self.first_name}, {self.last_name} ")
        print(f"Net Salary: {self.salary}")

class HourlyEmployee(Employee, Payroll):
    number_of_hours_worked = 0
    hourly_rate = 0
    def print_payroll(self):
        
        self.salary = self.number_of_hours_worked * self.hourly_rate
        print(f"Employee Name: {self.first_name}, {self.last_name}")
        print(f"Net Salary: {self.salary}")
    
full_time = FullTimeEmployee() # Instantiation
full_time.salary = 10000
full_time.first_name = "Peru"
full_time.last_name = "Para"
full_time.middle_name = "Para para para"
full_time.print_payroll()

hourly_employee = HourlyEmployee()
hourly_employee.first_name = "Favor"
hourly_employee.last_name = "Okechukwu"
hourly_employee.middle_name = "Gongon"
hourly_employee.hourly_rate = 50
hourly_employee.number_of_hours_worked = 40
hourly_employee.print_payroll()

