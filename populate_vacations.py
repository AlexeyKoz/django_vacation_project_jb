import psycopg2
from datetime import datetime


conn = psycopg2.connect(
    dbname="project_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


vacations = [
    (1, "Experience the magic of Paris with its iconic Eiffel Tower, world-class museums, and charming cafes. Enjoy the romantic atmosphere and rich cultural heritage.", "2025-06-12", "2025-06-21", 3630.00, "vacations/france.jpg", "2025-06-12 16:50:18.001147+00:00", "2025-06-12 16:50:18.541694+00:00", 1),
    (2, "Discover the eternal city of Rome with its ancient ruins, Vatican City, and delicious Italian cuisine. Immerse yourself in history and art.", "2025-07-12", "2025-07-18", 1274.00, "vacations/italy.jpg", "2025-06-12 16:50:18.543909+00:00", "2025-06-12 16:50:19.096686+00:00", 2),
    (3, "Enjoy the vibrant city of Barcelona with its unique architecture, beautiful beaches, and lively atmosphere. Perfect for art lovers and food enthusiasts.", "2025-08-11", "2025-08-25", 7080.00, "vacations/spain.jpg", "2025-06-12 16:50:19.100832+00:00", "2025-06-12 16:50:19.714623+00:00", 3),
    (4, "Visit the stunning Santorini with its white-washed buildings, blue domes, and breathtaking sunsets. A perfect romantic getaway.", "2025-09-10", "2025-09-18", 903.00, "vacations/greece.jpg", "2025-06-12 16:50:19.718941+00:00", "2025-06-12 16:50:20.315854+00:00", 4),
    (5, "Explore Tokyo, a fascinating blend of traditional culture and cutting-edge technology. Experience unique cuisine and vibrant city life.", "2025-10-10", "2025-10-16", 1489.00, "vacations/japan.jpg", "2025-06-12 16:50:20.321144+00:00", "2025-06-12 16:50:20.927517+00:00", 5),
    (6, "Relax in Phuket with its pristine beaches, crystal-clear waters, and luxurious resorts. Perfect for beach lovers and water sports enthusiasts.", "2025-11-09", "2025-11-16", 8143.00, "vacations/thailand.jpg", "2025-06-12 16:50:20.931892+00:00", "2025-06-12 16:50:22.245908+00:00", 6),
    (7, "Discover Sydney with its iconic Opera House, beautiful harbor, and stunning beaches. Experience the perfect blend of city and nature.", "2025-12-09", "2025-12-18", 6259.00, "vacations/australia.jpg", "2025-06-12 16:50:22.248063+00:00", "2025-06-12 16:50:23.678495+00:00", 7),
    (8, "Visit New York City, the city that never sleeps. Experience world-famous landmarks, Broadway shows, and diverse cultural attractions.", "2026-01-08", "2026-01-14", 7777.00, "vacations/united_states.jpg", "2025-06-12 16:50:23.682810+00:00", "2025-06-12 16:50:24.254173+00:00", 8),
    (9, "Explore Vancouver with its stunning natural beauty, diverse culture, and outdoor activities. Perfect for nature lovers and adventure seekers.", "2026-02-07", "2026-02-15", 842.00, "vacations/canada.jpg", "2025-06-12 16:50:24.257441+00:00", "2025-06-12 16:50:25.555853+00:00", 9),
    (15, "Explore Berlin with its rich history, vibrant art scene, and diverse cultural attractions. Perfect for history and culture enthusiasts.", "2026-08-06", "2026-08-16", 9441.00, "vacations/germany.jpg", "2025-06-12 16:50:29.197783+00:00", "2025-06-12 16:50:30.529206+00:00", 15)
]


insert_query = """
INSERT INTO vacations (
    id, description, start_date, end_date, price, image, created_at, updated_at, tour_id
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s
);
"""


for vacation in vacations:
    cur.execute(insert_query, vacation)


conn.commit()


cur.close()
conn.close()

print("Data inserted successfully into the vacations table.")
