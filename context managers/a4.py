# File: a4.py
# Time: 20.3.2023 klo xx.xx
# Author(s): Sebastian Sopola
# Description: use main loop to handle all actions regarding database handling and context manager use

import sqlite3
# import closing to close database connection when other commands are done
from contextlib import closing

""" Action loop to demonstrate added functionality to databases with context managers """
def main(database):
    # form dataset
    data_set = {
        1: (50.5, 1, "Experimental"),
        2: (50.5, 1, 'Finished'),
    }
    # open connection to database with context manager and assign it to 'connection' keyword
    with closing(sqlite3.connect(database)) as connection:
        # loop through dataset items
        for i in range(1,3):
            try:
                # check, is update succesfull
                rows_affected = _update(connection, data_set[i][0], data_set[i][1], data_set[i][2])
                if ( rows_affected < 1 ):
                    print(f"Update failed - {rows_affected} row(s) affected")
                else:
                    print(f"Update succesfull - {rows_affected} row(s) affected")
            except Exception as error:
                print('Something went wrong.... ', error)


def _show_content(connection):
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


def _update(connection, amplitude, device, treatment):
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


def _execute_statement(connection: sqlite3.Connection, sql_statement, data):
    # create cursor object with cursor method
    cursor = connection.cursor()
    # execute statement
    cursor.execute(sql_statement, data)
    # commit changes to database
    connection.commit()
    # return number of rows affected by update
    return cursor.rowcount


if __name__ == "__main__":

    db = "devicecontrol.db"
    main(db)




















