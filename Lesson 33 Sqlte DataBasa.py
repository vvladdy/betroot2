from pprint import pprint

import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'Sqlite connection error {e}')

    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'Sqlite connection error {e}')


def select_querry(connection, querry: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(querry)
        #result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Sqlite connectio error {e}')


def main():
    connection = create_connection('Lesson33_T1.sqlite')

    create_job_title_table = """
    CREATE TABLE IF NOT EXIST job_title (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """

    create_workers_table = """
        CREATE TABLE IF NOT EXIST workers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER,
            gender VARCHAR(8),
            job_title_id INTEGER NOT NULL,
            FOREIGN KEY (job_title_id) REFERENCES job_title (id)
    );
    """

    create_department_table = """
            CREATE TABLE IF NOT EXIST department (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                job_title_id INTEGER NOT NULL,
                FOREIGN KEY (job_title_id) REFERENCES job_title (id)
    );
    """

    execute_query(connection, create_job_title_table)
    execute_query(connection, create_workers_table)
    execute_query(connection, create_department_table)

    create_job_title = """
    INSERT INTO
        job_title (name)
    VALUES 
        ('hr manager'),
        ('recruter'),
        ('sales manager'),
        ('acaunter');
    """

    create_workers = """
    INSERT INTO
        workers (full_name, age, gender, job_title_id)
    VALUES 
        ('Serg Ivanov', 34, 'male', 2),
        ('Snegana Serg', 24, 'female', 1),
        ('Ivan Drugb', 35, 'male', 3),
        ('Ivanna Ludvig', 26, 'female', 4);
    """

    create_department = """
    INSERT INTO
        workers (title, job_title_id)
    VALUES 
        ('Sales dept', 2),
        ('HR Dept', 1),
        ('Sales dept', 3),
        ('HR Dept', 4);
    """

    select_dep_workers = """
    SELECT
        workers.id,
        workers.full_name,
        workers.age,
        department.title
    FROM
        department
    INNER JOIN workers on workers.job_title_id = department.job_title_id        
    """

    department_workers = select_querry(connection, select_dep_workers)
    pprint(department_workers)

    update_worker = 'UPDATE workers SET age = 35 WHERE full_name = "Serg Ivanov"'

    execute_query(connection, update_worker)
    department_workers = select_querry(connection, select_dep_workers)
    pprint(department_workers)

if __name__ == "__main__":
    main()