import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'

query_methods = """
SELECT method, COUNT(*) AS death_count
FROM Deaths
GROUP BY method
ORDER BY death_count DESC;
"""

query_locations = """
SELECT location, COUNT(*) AS death_count
FROM Deaths
GROUP BY location;
"""

query_houses = """
SELECT C.house_name, COUNT(*) AS death_count
FROM Characters C
JOIN Deaths D ON C.name = D.killed_name
GROUP BY C.house_name
ORDER BY death_count DESC;
"""

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_methods)
    methods = []
    method_counts = []

    for row in cur:
        methods.append(row[0])
        method_counts.append(row[1])

    cur.execute(query_locations)
    locations = []
    location_counts = []

    for row in cur:
        locations.append(row[0])
        location_counts.append(row[1])

    cur.execute(query_houses)
    houses = []
    house_counts = []

    for row in cur:
        houses.append(row[0])
        house_counts.append(row[1])

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    ax[0].bar(methods, method_counts, color='skyblue')
    ax[0].set_title('Deaths by Method')
    ax[0].set_xlabel('Method')
    ax[0].set_ylabel('Number of Deaths')
    ax[0].tick_params(axis='x', rotation=45)

    ax[1].pie(location_counts, labels=locations, autopct='%1.1f%%', startangle=140)
    ax[1].set_title('Distribution of Deaths by Location')

    ax[2].plot(houses, house_counts, color='skyblue', marker='o')
    ax[2].set_title('Number of Deaths by House')
    ax[2].set_xlabel('House')
    ax[2].set_ylabel('Number of Deaths')
    ax[2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
