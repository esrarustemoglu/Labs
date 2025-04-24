import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="4511"
)
def search_by_pattern_direct(pattern):
    command = """
    SELECT name, number 
    FROM phonebook2
    WHERE name ILIKE %s
       OR number ILIKE %s;
    """
    with conn.cursor() as cur:
        # Add wildcards for pattern matching
        like_pattern = f"%{pattern}%"
        cur.execute(command, (like_pattern, like_pattern))
        results = cur.fetchall()
        for row in results:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    return results


def insert_list(data_list):
    check_command = "SELECT 1 FROM phonebook2 WHERE name = %s"
    insert_command = "INSERT INTO phonebook2 (name, number) VALUES (%s, %s)"
    
    with conn.cursor() as cur:
        for name, number in data_list:
            cur.execute(check_command, (name,))
            if cur.fetchone() is None:
                cur.execute(insert_command, (name, number))
        conn.commit()

def insert_update(conn, name, number):
    command = """
    DO $$ 
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook2 WHERE name = %s) THEN
            UPDATE phonebook2 SET number = %s WHERE name = %s;
        ELSE
            INSERT INTO phonebook2(name, number) VALUES (%s, %s);
        END IF;
    END $$;
    """

    with conn.cursor() as cur:
        cur.execute(command, (name, number, name, name, number))
        conn.commit()  

def delete_by_name(name):
    command = """DELETE FROM phonebook2 WHERE name = %s"""
    with conn.cursor() as cur:
        cur.execute(command, (name, ))
        conn.commit()  

def delete_by_number(number):
    command = """DELETE FROM phonebook2 WHERE number = %s"""
    with conn.cursor() as cur:
        cur.execute(command, (number, ))
        conn.commit()  

def query(limit, offset):
    command = """SELECT * FROM phonebook2 ORDER BY name ASC LIMIT %s OFFSET %s"""
    with conn.cursor() as cur:
        cur.execute(command, (limit, offset))
        results = cur.fetchall()  
        return results
"""insert_list([
    ("Mert", "1234567890"),
    ("Ari", "9876543210"),
    ("Biber", "5551234567"),
    ("Adrien", "4511451145")
])"""
#insert_update(conn, "Ari", "1112223333")
#delete_by_name("Biber")
#delete_by_number("1234567890")
#results = query(2, 0)
#for r in results:
#   print(r)
search_by_pattern_direct("dri")
