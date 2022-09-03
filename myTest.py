#from focusrite.Connection import Connection as Connect
from focusrite.connection import *
from focusrite.crud import *
import mysql.connector

#data to estabilish connection
host = "127.0.0.1"
user = "root"
password = "Spartosc2000$"
database = "focusrite"

#establishing connection
conn = Connection(host, user, password, database)
c = conn.connectionOpen()
crud = Crud(c)




# entry data to add new employee
employeeData = (999,'hhgjhj', 'Vanderkelen', '19770614')

# id of user to be deleted
id = [999]

#  data to be updated for the employee
updateemployeeData = (999,'yYYYy', 'xXXXx', '20000101',999)



# adding new user
crud.addEmployee(employeeData)

#updating new user
crud.updateEmployee(updateemployeeData)

#reading all table records
result = crud.readAllEmployees()
for item in result: print(item)

#deleting user by id
crud.deleteEmployee(id)

#second reading all records
result = crud.readAllEmployees()
for item in result: print(item)


