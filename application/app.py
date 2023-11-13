from services.db import create_db
from models.people import People
from models.employee import Employee
from models.place import Place
from models.gym_class import GymClass

create_db()

People.create_person('Johan', '09447520977', '997957929', '2005-01-05') #1 query
People.create_person('Felipe', '09847310957', '907057929', '2004-07-20') #2 query
People.create_person('Giuseppe', '02856510988', '917957929', '1998-02-02') #3 query
People.create_person('Andre', '03547210473', '927957929', '2006-11-023') #4 query
People.create_person('Juca', '06847510932', '937554329', '2007-06-029') #5 query

#6 query
i = 1
while People.get_person_by_id(i) is not None: 
    person = People.get_person_by_id(i)
    print(f'ID:{person.id}, Nome: {person.person_name}')
    i += 1

#7 query
People.update_person(5, 'Amanda',None,'997977929')

#8 query
person = People.get_person_by_id(5)
print(f'ID:{person.id}, Nome: {person.person_name}, Celular: {person.phone}')

#9 - 10 query
Place.create_place('SuperFit Bacacheri', 3000, '82510-70', '35561740', 'Curitiba', 'Bacacheri', 'Rua Holanda', 'Parana') 
Place.create_place('SuperFit Cabral', 4200, '80540-90', '35562835', 'Curitiba', 'Cabral', 'Av Anita Garibaldi', 'Parana') 

#11 - 12 query
Employee.create_employee('Trainer', 3500, 1, 1)
employee = Employee.get_employee_by_id(1) 
print(f'ID:{employee.id}, Nome: {employee.position}, Cargo: {employee.salary}')

#12 - 13 query
Employee.update_employee(1, 'Senior Trainer', 5500)
employee = Employee.get_employee_by_id(1)
print(f'ID:{employee.id}, Nome:{employee.position}, Cargo:{employee.salary}')

#14 - 17 query
GymClass.create_gym_class('2023-11-01 10:30:00', '1', '80')  
GymClass.create_gym_class('2023-11-05 12:00:00', '2', '50')  
GymClass.create_gym_class('2023-11-10 11:30:00', '3', '60')  
GymClass.create_gym_class('2023-11-15 10:30:00', '1', '80')  

# 18 query
class_info = GymClass.get_gym_class_by_id(1)
print(f'ID: {class_info.id}, Data: {class_info.class_datetime}, Local: {class_info.class_type}, Capacidade: {class_info.price}')

# 19 - 20 query
GymClass.update_gym_class(2, '2023-11-08 10:30:00', '2', '70')
class_info = GymClass.get_gym_class_by_id(2)
print(f'ID: {class_info.id}, Data: {class_info.class_datetime}, Local: {class_info.class_type}, Capacidade: {class_info.price}')

