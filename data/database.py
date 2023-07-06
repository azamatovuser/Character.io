import sqlite3


class Database:
    def __init__(self, db_name):
        # Создание подключения к базе данных SQLite
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Создание таблицы users, если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY UNIQUE,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_date TEXT
            )
        ''')
        self.conn.commit()

        # Создание таблицы user_question, если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_question (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                question TEXT,
                answer TEXT
            )
        ''')
        self.conn.commit()

        # Создание таблицы answer, если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS character (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                character TEXT
            )
        ''')
        self.conn.commit()

    def insert_user(self, user_id, username, first_name, last_name):
        # Вставка данных в таблицу users
        self.cursor.execute('''
            INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, created_date)
            VALUES (?, ?, ?, ?, datetime('now'))
        ''', (user_id, username, first_name, last_name))
        self.conn.commit()

    def insert_user_question_answer(self, user_id, question, answer):
        # Вставка данных в таблицу user_question
        self.cursor.execute('''
            INSERT INTO user_question (user_id, question, answer)
            VALUES (?, ?, ?)
        ''', (user_id, question, answer))
        self.conn.commit()


    def insert_character(self, user_id, character):
        # Вставка данных в таблицу answer
        self.cursor.execute('''
            INSERT INTO answer (user_id, character)
            VALUES (?, ?)
        ''', (user_id, character))
        self.conn.commit()

    def close_connection(self):
        # Закрытие подключения к базе данных
        self.cursor.close()
        self.conn.close()
