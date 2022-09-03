from focusrite.connection import *



class Crud(Connection):

    #addUser query
    addUser = ("INSERT INTO employees(`emp_no`,`first_name`,`last_name`,`hire_date`) VALUES (%s,%s,%s,%s)")
    #show all users query
    select = ("SELECT * FROM employees")
    # delete user by id query
    delete = ("DELETE FROM employees WHERE emp_no = %s")
    # update query
    updateUser = ("UPDATE employees SET emp_no = %s, first_name = %s, last_name = %s, hire_date = %s WHERE emp_no = %s")


    #constructor
    def __init__(self,conn):
        self.conn = conn


    # add employ function
    def addEmployee(self,employeeData):
        cursor = self.conn.cursor()
        cursor.execute(self.addUser, employeeData)
        self.conn.commit()
        #self.conn.close()


    # read all resoults from the  table
    def readAllEmployees(self):
            # Executing the query
        cursor = self.conn.cursor()
        cursor.execute(self.select)
            # Fetching 1st row from the table
        result = cursor.fetchall();
        #self.conn.close()
        return result



    # update employee selected by id
    def updateEmployee(self,employeeData):
        cursor = self.conn.cursor()
        cursor.execute(self.updateUser, employeeData)
        self.conn.commit()
        # self.conn.close()


    # removing employee by id
    def deleteEmployee(self,id):

        cursor = self.conn.cursor()
        try:
            # Execute the SQL command
            cursor.execute(self.delete, id)

            # Commit your changes in the database
            self.conn.commit()
        except:
            # Roll back in case there is any error
            self.conn.rollback()
            print("Delete unsuccessful")
        #self.conn.close()

    def addEmployesFromCSV(self):
