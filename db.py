import cx_Oracle

from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()



    def newUser(self, nameStudent,ageStudent):

        cursor = self.db.cursor

        name = cursor.var(cx_Oracle.STRING)
        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("std.new_student", [name, status, nameStudent, ageStudent])

        return name.getvalue(), status.getvalue()

    def deleteStudent(self,nameStudent):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("std.delete_student", [status, nameStudent])

        return status.getvalue()









if __name__ == "__main__":

    helper = UserHelper()
    helper.newUser('hi','33')
