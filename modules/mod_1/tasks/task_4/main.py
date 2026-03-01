import sqlite3
from security_vulnerabilities_100 import security_vulnerabilities

connection = sqlite3.connect('security_vulnerabilities')

# Создание и вставка строк
def create_and_insert(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vulnerabilities (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                cwe_id TEXT NOT NULL,
                vuln_type TEXT NOT NULL,
                component TEXT,
                endpoint TEXT,
                data_classification TEXT,
                detected_at TIMESTAMP,
                severity INTEGER, 
                is_confirmed BOOLEAN,
                is_exploitable BOOLEAAN,
                area TEXT
                   )
    ''')

    cursor.executemany('''
        INSERT INTO Vulnerabilities (
            id, title, cwe_id, vuln_type, component, endpoint,
            data_classification, detected_at, severity,
            is_confirmed, is_exploitable, area
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', security_vulnerabilities)

    connection.commit()
    return

# Вспомогательная функция для выбора записей
def select(connection, sql: str):
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor

# Вывод результата
def print_table(cursor):
    rows = cursor.fetchall()
    print(f"Число строк = {len(rows)}\n")
    for r in rows:
        print(r)

sql_1 = '''
SELECT * FROM Vulnerabilities WHERE component = 'Admin Panel' OR component = 'Reports' 
'''

print_table(select(connection, sql_1))

connection.close()