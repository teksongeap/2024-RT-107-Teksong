import mysql.connector as db
from mysql.connector import Error

# PA - 342.3.1

print("PART 1:")
# Part 1 Create the database
try:
    connection = db.connect(
        # host = localhost,
        user = 'root',
        password = 'password'
    )
    if connection.is_connected():
        # create the magic cursor that does the work for us
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE RegistrationDB")
        print("Database created successfully.")
    else:
        print("Connection failed.")
except Error as e:
    # print out error if any
    print(f"Error: {e}")
finally:
    # close the connection, to save memory
    if connection.is_connected():
        cursor.close()
        connection.close()

# Part 3
print("PART 3:")
def generate_user_table():
    try:
        connection = db.connect(
            database = 'RegistrationDB',
            user = 'root',
            password = 'password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "CREATE TABLE user (email VARCHAR(100) NOT NULL, name VARCHAR(255) NOT NULL,\
            password VARCHAR(30) NOT NULL,\
            PRIMARY KEY (email));"
            cursor.execute(query)
            print("Table created successfully.")
            insert_query = "INSERT INTO user (email, name, password) \
            VALUES ('ywbaek@perscholas.org', 'young', 'letsgomets'), \
                ('mcordon@perscholas.org', 'marcial', 'perscholas'), \
                ('mhaseeb@perscholas.org', 'haseeb', 'platform');"
            cursor.execute(insert_query)
            # commit() required for inserting in python
            connection.commit()
            print(cursor.rowcount, "records inserted successfully into user table")
        else:
            print("Connection failed.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

generate_user_table()

# Part 4
print("PART 4:")
def get_all_users():
    try:
        connection = db.connect(
            database = 'RegistrationDB',
            user = 'root',
            password = 'password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM USER;"
            cursor.execute(query)          
            # get all records using fetchall() returns a list?
            records = cursor.fetchall()   
            for row in records:
                print(row)
        else:
            print("Connection failed.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

get_all_users()

# Part 5
print("PART 5:")
def get_user_by_name(name):
    try:
        connection = db.connect(
            database = 'RegistrationDB',
            user = 'root',
            password = 'password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = f"SELECT * FROM USER WHERE name = '{name}';"
            cursor.execute(query)          
            records = cursor.fetchall()
            if records:
                for row in records:
                    print("Email:", row[0], "Password:", row[2])
            else:
                print(f'User with name: {name} not found.')
        else:
            print("Connection failed.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

get_user_by_name("marcial")

# Part 6
print("PART 6:")
def validate_user(email, password):
    try:
        connection = db.connect(
            database = 'RegistrationDB',
            user = 'root',
            password = 'password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = f"SELECT * FROM USER WHERE email = '{email}' and password = '{password}';"
            cursor.execute(query)          
            # get all records
            records = cursor.fetchall()   
            if records:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
        else:
            print("Connection failed.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

print("User exists:", validate_user('mcordon@perscholas.org','perscholas'))

# Part 7
print("PART 7:")
def update_user(email, name, password):
    try:
        connection = db.connect(
            database = 'RegistrationDB',
            user = 'root',
            password = 'password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = f"UPDATE user SET name = '{name}', password = '{password}' \
            WHERE email = '{email}';"
            cursor.execute(query)          
            connection.commit()
            if cursor.lastrowid:
                print("User updated successfully in user table")
                cursor.close()
                connection.close()
                return True
            else:
                print("User not found or already updated.")
                cursor.close()
                connection.close()
                return False
        else:
            print("Connection failed.")
            cursor.close()
            connection.close()
            return False
    except Error as e:
        print(f"Error: {e}")
        cursor.close()
        connection.close()
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

print("User updated:", update_user('mhaseeb@perscholas.org', 'habibi', 'zzzz'))