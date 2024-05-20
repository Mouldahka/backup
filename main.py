import psycopg2, os, requests, time, random

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port="6543"
)

cur = con.cursor()

os.system("cat data.sql | docker exec -i backup_db psql -U postgres > /dev/null 2>&1")

cur.execute("SELECT id, title, url FROM database_meme")
memes = cur.fetchall()

for meme in memes:
    id, title, url = meme
    print(f"Chargement du meme \"{title}\"...", end=" ")
    response = requests.get(url, headers={"User-Agent": user_agent})
    extension = url.split(".")[-1].split("?")[0]
    with open(f"data/{id}.{extension}", "wb") as f:
        f.write(response.content)
    print("Terminé")
    sleep_time = random.randint(1, 10)
    print(f"Délai de {sleep_time}s avant le prochain téléchargement...")
    time.sleep(sleep_time)

con.close()