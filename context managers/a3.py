# File: a3.py
# Time: 20.3.2023 klo 9.41
# Author(s): Sebastian Sopola
# Description: Update database and check succesfulity of that

import sqlite3

def update(connection, amplitude, device, treatment):
    # form sql statement
    sql_statement = '''
            UPDATE measurements
            SET amplitude = ?
            WHERE device= ? and treatment=?;
            '''
    # form data
    data = amplitude, device, treatment
    # call execute_statement
    result = execute_statement(connection, sql_statement, data)
    # return result
    return result


def execute_statement(connection: sqlite3.Connection, sql_statement, data):
    # create cursor object with cursor method
    cursor = connection.cursor()
    # execute statement
    cursor.execute(sql_statement, data)
    # commit changes to database
    connection.commit()
    # return number of rows affected by update
    return cursor.rowcount


if __name__ == "__main__":
    data_set = {
        1: (50.5, 1, "Experimental"),
        2: (50.5, 1, 'Finished'),
    }

    for i in range(1,3):
        try:
            db = "devicecontrol.db"
            connection = sqlite3.connect(db)

            # check, is update succesfull
            rows_affected = update(connection, data_set[i][0], data_set[i][1], data_set[i][2])
            if ( rows_affected < 1 ):
                print(f"Update failed - {rows_affected} row(s) affected")
            else:
                print(f"Update succesfull - {rows_affected} row(s) affected")
        except Exception as error:
            print('Something went wrong.... ', error)

        finally:
            connection.close()
    



























