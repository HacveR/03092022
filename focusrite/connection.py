import mysql.connector as cnx


class Connection:

    def __init__(self, host, user, password, database):

        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connectionOpen(self):
        try:

            connection = cnx.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            print("New connection established")

        except cnx.Error as err:
            print("Something went wrong: {}".format(err))
        return connection

    def gethost(self):
        return self.host

    def getuser(self):
        return  self.user

