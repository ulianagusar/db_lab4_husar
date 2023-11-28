import psycopg2



username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'



query_1 = """
SELECT method, COUNT(*) AS death_count
FROM Deaths
GROUP BY method
ORDER BY death_count DESC;
"""

query_2 = """
SELECT location, COUNT(*) AS death_count
FROM Deaths
GROUP BY location;
"""

query_3 = """
SELECT C.house_name, COUNT(*) AS death_count
FROM Characters C
JOIN Deaths D ON C.name = D.killed_name
GROUP BY C.house_name
ORDER BY death_count DESC;
"""


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
                       
    cur = conn.cursor()

    print('\nЗагальна кількість смертей за кожним методом, впорядковуючи їх від найчастішого до найрідшого:')
    cur.execute(query_1)

    for row in cur:
       print(row)

    print('\nкількість смертей у кожному місці, але без впорядкування за кількістю:')
    cur.execute(query_2)

    for row in cur:
       print(row)

    print('\nкількість смертей для кожного дому, розташовуючи їх від найбільшої кількості смертей до найменшої:')
    cur.execute(query_3)

    for row in cur:
       print(row)