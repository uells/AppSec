## SQLite + Python (`sqlite3`)

### 1) Что это

* SQLite — **файл БД** (`.db`), без сервера.
* `sqlite3` — **встроенный модуль Python** для работы с SQLite.

### 2) Подключение

```python
import sqlite3
conn = sqlite3.connect("app.db")  # создаст файл, если нет
```

### 3) Выполнение SQL

* Один запрос:

```python
conn.execute("CREATE TABLE IF NOT EXISTS t(id INTEGER PRIMARY KEY, x TEXT)")
```

* Через cursor (когда удобно):

```python
cur = conn.cursor()
cur.execute("SELECT * FROM t")
```

### 4) Параметризация (обязательно)

* **Никогда не склеивай строки.**

```python
conn.execute("INSERT INTO t(x) VALUES (?)", ("hello",))
conn.execute("SELECT * FROM t WHERE id = ?", (1,))
```

### 5) Чтение результатов

```python
rows = cur.fetchall()     # все
row = cur.fetchone()      # одна
```

### 6) Транзакции: commit / rollback

* Изменения (INSERT/UPDATE/DELETE) фиксируются только после:

```python
conn.commit()
```

* При ошибке можно:

```python
conn.rollback()
```

### 7) `executemany` для пачки вставок

```python
conn.executemany("INSERT INTO t(x) VALUES (?)", [("a",), ("b",)])
conn.commit()
```

### 8) Сколько строк изменилось

```python
cur.execute("DELETE FROM t WHERE id > ?", (10,))
print(cur.rowcount)
```

### 9) Удобный режим “словарём”

```python
conn.row_factory = sqlite3.Row
cur = conn.execute("SELECT id, x FROM t")
for r in cur:
    print(r["id"], r["x"])
```

### 10) Закрытие и безопасный шаблон

```python
with sqlite3.connect("app.db") as conn:
    conn.execute("...")   # commit автоматически при успехе
```

### 11) Практичные PRAGMA (часто нужно)

```python
conn.execute("PRAGMA foreign_keys = ON;")
conn.execute("PRAGMA journal_mode = WAL;")  # лучше для параллельных чтений/записей
```
