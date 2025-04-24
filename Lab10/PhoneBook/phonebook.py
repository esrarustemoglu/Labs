import csv
import psycopg2


conn = psycopg2.connect( 
    host="localhost",
    database="postgres",
    user="postgres",
    password="4511"
)


def insert(first_name, last_name, phone_number):

    command = """INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s)"""

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command, (first_name, last_name, phone_number))
        conn.commit()


def insert_from_csv(csv_file_name):

    command = "INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s)"

    with conn.cursor() as cur:
        # execute the command
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # getting rid of the headers
            for row in csvreader:
                # print(row)
                first_name, last_name, phone_number = row
                # print(name, major, gpa, year)
                cur.execute(command, (first_name, last_name, phone_number))
        conn.commit()


def query_phonebook(filter_type=None, value=None):
    with conn.cursor() as cur:
        if filter_type == "first_name":
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (value,))
        elif filter_type == "last_name":
            cur.execute("SELECT * FROM phonebook WHERE last_name ILIKE %s", (f"%{value}%",))
        elif filter_type == "phone_number":
            cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (value,))
        else:
            cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        for row in rows:
            print(row)

def update_user(first_name, new_first_name=None, new_phone=None):
    with conn.cursor() as cur:
        if new_first_name:
            cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_first_name, first_name))
        if new_phone:
            cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, first_name))
        conn.commit()


def delete_user(first_name=None, phone=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (first_name,))
        elif phone:
            cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
        conn.commit()

#first = input("Enter first name: ")
#last = input("Enter last name: ")
#phone = input("Enter phone number: ")

#insert(first, last, phone)
#insert_from_csv('phonebook.csv')
#insert("Wonwoo", "Jeon", "1234567890")
update_user("Wonwoo", new_phone="987654321")
#query_phonebook("first_name", "Esra")
# delete_user(first_name="Wonwoo")

conn.close()