"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def read_csv(data):
    """Функция для чтения файла .csv"""
    with open(data, encoding='utf-8') as file:
        # Создаем объект reader, указываем символ-разделитель ","
        reader_object = csv.reader(file, delimiter=",")
        # Счетчик для подсчета количества строк и пустой список для кортежей
        count = 0
        tup = []
        # Считывание данных из CSV файла
        for r in reader_object:
            if count == 0:
                count += 1
                continue
            else:
                r = tuple(r)
                tup.append(r)
    return tup


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='123456')
try:
    employees_data = read_csv('north_data/employees_data.csv')  # Достаем информацию из employees_data.csv и добавляем в БД
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", vars_list=employees_data)

            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)

    customers_data = read_csv('north_data/customers_data.csv')  # Достаем информацию из customers_data.csv и добавляем в БД
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", vars_list=customers_data)

            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            for row in rows:
                print(row)

    orders_data = read_csv('north_data/orders_data.csv')  # Достаем информацию из orders_data.csv и добавляем в БД
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", vars_list=orders_data)

            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()
