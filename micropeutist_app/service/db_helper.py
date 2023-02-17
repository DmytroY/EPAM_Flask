'''Procedures for work with MySQL DB'''

import mysql.connector as mysql
from service.config import config


def execute_query(sql_file):
    '''Procedure for execute MySQL script file'''
    try:
        params = config()
        conn = mysql.connect(**params)
        cursor = conn.cursor()

        feedback = []
        sql_file = "sql/" + sql_file

        with open(sql_file) as f:
            query = " ".join(f.readlines())
        print('=== readed query:', query)

        query_list = query.split(";")
        print('=== splited query:', query_list)

        for item in query_list[:-1]:
            cursor.execute(item)
            feedback.append(cursor.fetchall())
            conn.commit()
            print("=== commited query:", item)

        conn.close()
        print("=== connection closed, conn value:", conn)
        return feedback
    
    except Exception as error:
        print(error)

    finally:
            conn.close()


    
