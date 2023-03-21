# File: a2.py
# Time: 15.3.2023 klo 7.59
# Author(s): Sebastian Sopola
# Description: SQL update is done in 'Update' function where context manager handles the commit to sql database

import sqlite3

def update(database: str, sql_statement: str, data: tuple):
    with sqlite3.connect(database) as connection:
        connection.execute(sql_statement, data)


if __name__=="__main__":

    try:
        """ Database """
        db = "devicecontrol.db"

        """Test the function with """

        data = 50.5, 1,  "Experimental"  #  ok

        sql_statement = '''
            UPDATE measurements
            SET amplitude = ?
            WHERE device= ? and treatment=?;
            '''

        update(db, sql_statement, data)

        data = 50.5, 1, "Finished"  # fails
        
        update(db, sql_statement, data)

    except Exception as error:
        print("Something went wrong....")

    
    
    

























