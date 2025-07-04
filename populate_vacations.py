import psycopg2
from datetime import date


conn = psycopg2.connect(
    dbname="project_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


vacations = [
    (1, "Beach vacation on the Mediterranean coast in Tel Aviv", "2025-06-01", "2025-06-15", 1500.00, "tel_aviv.jpg"),
    (2, "Ski resort Bukovel in the Carpathians", "2025-12-20", "2026-01-05", 1200.00, "bukovel.jpg"),
    (3, "Golden Ring of Russia Tour", "2025-07-10", "2025-07-20", 1300.00, "golden_ring.jpg"),
    (4, "French Riviera: Vacation in Nice", "2025-08-01", "2025-08-14", 2000.00, "nice.jpg"),
    (5, "Barcelona and Costa Brava: Beach and cultural tour", "2025-07-15", "2025-07-30", 1800.00, "barcelona.jpg"),
    (6, "Rome and Venice: Excursion tour through Italy", "2025-09-10", "2025-09-25", 2200.00, "rome_venice.jpg"),
    (7, "Miami Beach: A sunny paradise in Florida", "2025-05-05", "2025-05-20", 2500.00, "miami.jpg"),
    (8, "Bavarian Alps: Mountain retreat in Germany", "2025-10-01", "2025-10-15", 1600.00, "bavaria.jpg"),
    (9, "Antalya: Five-star holiday in Turkey", "2025-06-10", "2025-06-25", 1400.00, "antalya.jpg"),
    (10, "Santorini Island: A romantic getaway", "2025-07-01", "2025-07-15", 1700.00, "santorini.jpg"),
    (6, "Tuscany: Wine and gastronomy tour in Italy", "2025-09-01", "2025-09-15", 2000.00, "tuscany.jpg"),
    (5, "Madrid and Seville: Cultural journey through Spain", "2025-10-05", "2025-10-20", 1900.00, "madrid_seville.jpg")
]


insert_query = """
INSERT INTO vacations (tour_id, title, start_date, end_date, price, image)
VALUES (%s, %s, %s, %s, %s, %s);
"""


for vacation in vacations:
    cur.execute(insert_query, vacation)


conn.commit()


cur.close()
conn.close()

print("Data populated successfully.")
