

from faker import Faker
import random 
from faker.providers import BaseProvider


fake = Faker()


x = range(100)

first_name = fake.first_name()
last_name = fake.last_name()
other_name = fake.first_name()
phone_number = fake.phone_number()
email = fake.email()
occupation = fake.job()
address = fake.address()
bank = fake.aba()
staff_category = ['Teaching Staff', 'Non-Teaching staff']
marital_status = ['Single', 'Married']
Salary = [30000, 25000, 40000, 45000]



print("INSERT INTO parent(first_name, surname, other_name, phone_number, email, occupation, address)VALUES")
for n in range(85):
	print("(%s, %s, %s, %s, %s, %s, %s)," %(f" \'{fake.first_name()}\'", f" \'{fake.last_name()}\'", 
											f" \'{fake.first_name()}\'", f" \'{fake.phone_number()}\'", 
											f" \'{fake.email()}\'", f" \'{fake.job()}\'", f" \'{fake.address()} \'" ))



# print("INSERT INTO users(email, password)VALUES")
# for n in range(50):
# 	print("(%s, %s)," %(f" \'{fake.first_name()}\'",f" \'{fake.first_name()}\'"))



# print("INSERT INTO staff(first_name, surname, othername, staff_category, email, phone_number, marital_status, Account_number, Salary) VALUES")
# for n in range(50):
# 	print("(%s, %s, %s, %s, %s, %s, %s, %s, %s)," %(f" \'{fake.first_name()}\'", 
# 		f" \'{fake.last_name()}\'", f" \'{fake.first_name()}\'", f" \'{random.choice(staff_category)}\'", 
# 		f" \'{fake.email()}\'", f" \'{fake.phone_number()}\'", f" \'{random.choice(marital_status)}\'", 
# 		f" \'{fake.aba()}\'", f" \'{random.choice(Salary)}\'"))




