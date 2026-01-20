import psycopg2

db = {
    "dbname": "weather_db",
    "user": "postgres",
    "password": "2118",
    "host": "127.0.0.1",
    "port": "5757",
}


def s():
    c = psycopg2.connect(**db)
    cur = c.cursor()

    cur.execute("DROP TABLE IF EXISTS weatheralert")

    q = """
    CREATE TABLE weatheralert (
        id SERIAL PRIMARY KEY,
        lat FLOAT,
        lon FLOAT,
        temperature FLOAT,
        source_file TEXT,
        t_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cur.execute(q)
    c.commit()
    cur.close()
    c.close()


if __name__ == "__main__":
    s()
