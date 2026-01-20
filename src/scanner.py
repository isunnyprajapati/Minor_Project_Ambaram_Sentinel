import os

import h5py
import numpy as np
import psycopg2

db = {
    "dbname": "weather_db",
    "user": "postgres",
    "password": "2118",
    "host": "127.0.0.1",
    "port": "5757",
}


def f():
    b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = os.path.join(b, "data")

    if not os.path.exists(d):
        return

    c = psycopg2.connect(**db)
    cur = c.cursor()
    cur.execute("DELETE FROM weatheralert")

    fl = [f for f in os.listdir(d) if f.endswith(".h5")]

    for n in fl:
        p = os.path.join(d, n)
        try:
            with h5py.File(p, "r") as h:
                if "IMG_TIR1" in h:
                    t = h["IMG_TIR1"][()]
                elif "IMG_TIR1_TEMP" in h:
                    t = h["IMG_TIR1_TEMP"][()]
                else:
                    continue

                if t.ndim == 1:
                    t = t.reshape((1024, 1024))
                elif t.ndim == 3:
                    t = t[0]

                r_ct, c_ct = t.shape

                y1, y2 = 28.0, -8.0
                x1, x2 = 68.0, 118.0

                la_v = np.linspace(y1, y2, r_ct)
                lo_v = np.linspace(x1, x2, c_ct)

                r_idx, c_idx = np.where((t < 240) & (t > 0))

                for i in range(0, len(r_idx), 10):
                    r, m = r_idx[i], c_idx[i]
                    la, lo, tp = float(la_v[r]), float(lo_v[m]), float(t[r, m])

                    cur.execute(
                        "INSERT INTO weatheralert (lat, lon, temperature, source_file) VALUES (%s, %s, %s, %s)",
                        (la, lo, tp, n),
                    )
                c.commit()
        except:
            pass

    cur.close()
    c.close()


if __name__ == "__main__":
    f()
