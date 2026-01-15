import psycopg2


def wipe():
    conn = psycopg2.connect(
        dbname="weather_db",
        user="postgres",
        password="2118",  # change this
        host="127.0.0.1",
        port="5757",
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM weatheralert")
    conn.commit()
    print("Database cleared. Ready for real data!")
    cur.close()
    conn.close()


wipe()
