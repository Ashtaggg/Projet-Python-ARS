import pymysql

def openDataBase():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='projet_python_ars',
    )

    return conn


def requestDataBase(request):
    conn = openDataBase()

    cur = conn.cursor()
    cur.execute(request)
    conn.commit()
    output = cur.fetchall()
    conn.close()

    return output