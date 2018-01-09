import pymysql.cursors
 
conn = pymysql.connect(host='localhost',
        user='gaeul',
        password='alpha',
        db='cafe',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO cafe_information (name, address, latitude, longitude$
        cursor.execute(sql, (123, 'CA94103','12.345','1.2345','010'))
    conn.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
finally:
    conn.close()
