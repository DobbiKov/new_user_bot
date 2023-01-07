import sqlite3
from data import sqlite_database_file

def create_connection(sqlite_file):
    conn = None
    try: 
        conn = sqlite3.connect(sqlite_file)
        print(f"SQLite: {sqlite3.version}")
    except sqlite3.Error as e:
        show_sqlite_error(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        show_sqlite_error(e)

def create_chats_for_translating_table(conn: sqlite3.Connection):
    sql_create_chats_for_translatings_table = """ CREATE TABLE IF NOT EXISTS chats_for_translation (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        date text,
                                        chat_id integer NOT NULL
                                    ); """
    # new_conn = create_connection(sqlite_database_file)
    if conn is not None:
        create_table(conn, sql_create_chats_for_translatings_table)
    else:
        print("Error! cannot create the database connection.")

def create_chats_for_translating(conn: sqlite3.Connection, chat):
    conn = create_connection(sqlite_database_file)
    """
    Create a new chat into the chats table
    :param conn:
    :param chat:
    :return: chat_db id
    """
    sql = ''' INSERT INTO chats_for_translation(name,date,chat_id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, chat)
    conn.commit()
    return cur.lastrowid

async def select_chat_by_chatid(conn: sqlite3.Connection, chat_id):
    conn = create_connection(sqlite_database_file)
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM chats_for_translation WHERE chat_id=?", (chat_id,))

    rows = cur.fetchall()

    return rows

def show_sqlite_error(message):
    print(f"SQLite error: {message}")
