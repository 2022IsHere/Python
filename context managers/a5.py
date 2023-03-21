# File: a5.py
# Time: 20.3.2023 klo xx.xx
# Author(s): Sebastian Sopola
# Description: Use custom  context manager class to derive open database connection and possible errors raised during entire process until closing of database connection

import sqlite3
from contextlib import closing

class DataBaseManager:
    # initialize database and connection
    def __init__(self, database: str):
        self.database = database
        self.connection = None
    # open connection to database
    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.database)
        # raise error if connection can not be opened
        except sqlite3.Error as error:
            # call error handling function to deal with error
            self.handle_exception(error)
            self.__exit__()
        # return connection to database
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if issubclass(exc_type, sqlite3.Error):
                self.handle_exception(exc_val)
                #  return True if exception was handled gracefully
                return True
            else:
                # return False if exception was not handled
                return False
        else:
            # save and close connection to database
            self.connection.commit()
            self.connection.close()

    def handle_exception(self, error):
        print('Something went wrong.... ', error)
        self.connection.rollback()


def _show_content(connection: sqlite3.Connection):
        # form sql statement
        sql_statement = """
            SELECT *
            FROM measurements;
        """
        # create cursor object of db connection
        cursor = connection.cursor()
        # call execute command with sql_statement ( statement calls information from database )
        cursor.execute(sql_statement)
        # store information into result variable
        results = cursor.fetchall()
        # loop through rows of datatable to show information from the database
        for row in results:
            print(row)
        # remember to close cursor object
        cursor.close()


def _execute_statement(connection: sqlite3.Connection, sql_statement, data):
        # create cursor object with cursor method
        cursor = connection.cursor()
        # execute statement
        cursor.execute(sql_statement, data)
        # commit changes to database
        connection.commit()
        # return number of rows affected by update
        return cursor.rowcount
    
def _update(connection: sqlite3.Connection, amplitude: float, device: int, treatment: str):
        # form sql statement
        sql_statement = '''
                UPDATE measurements
                SET amplitude = ?
                WHERE device= ? and treatment=?;
                '''
        # form data
        data = amplitude, device, treatment
        # call execute_statement
        result = _execute_statement(connection, sql_statement, data)
        # return result
        return result    


        """ Action loop to demonstrate added functionality to databases with context managers """
def main(database: str):
        # form dataset
        data_set = {
            1: (50.5, 1, "Experimental"),
            2: (50.5, 1, 'Finished'),
        }
        # open connection to database with context manager and assign it to 'connection' keyword
        with DataBaseManager(database) as connection:
            # loop through dataset items
            for i in range(1, 3):
                try:
                    # check, is update succesfull
                    rows_affected = _update(connection, data_set[i][0], data_set[i][1], data_set[i][2])
                    print(f"{rows_affected} row(s) affected")
                except Exception as error:
                    print('Something went wrong.... ', error)
            # call show function to show content of database
            _show_content(connection)


if __name__ == '__main__':
    db = "devicecontrol.db"
    main(db)


















