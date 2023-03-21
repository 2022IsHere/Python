# File: a1.py
# Time: 15.3.2023 klo 16.32
# Author(s): Sebastian Sopola
# Description: Open connection into database. Initialize data which you
#              want to add into database. Implement SQL statement so that
#              data you want into database will be added according to
#              your statement
#              Execute adding information into database with statement + data
#              save added info and close

import sqlite3

""" Database """
db = "devicecontrol.db"


with sqlite3.connect(db) as connection:           
    data = 50.5, 1, "Experimental"                  
    sql_statement  = '''

        UPDATE measurements
        SET amplitude = ?
        WHERE device = ? and treatment = ?;
    
    '''
    connection.execute(sql_statement, data)

    






