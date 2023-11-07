import pymysql
import tkinter as tk




cuicui = tk.Tk()
cuicui.title("Cuicui")
cuicui.geometry("1920x1080")











def mysqlconnect(request):

    # To connect MySQL database. Change the database name as per requirement

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='projet_python_ars',
    )

    

    #Change the name of the table as per requirement

    cur = conn.cursor()

    cur.execute(request)

    output = cur.fetchall()

    print(output)



    # To close the connection

    conn.close()






    