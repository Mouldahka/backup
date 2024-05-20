if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <user> <host> <port>"
    exit 1
fi

ssh -p $(echo $3) $(echo $1)@$(echo $2) "sudo docker exec -i mouldahka_mouldahka_db_1 pg_dump -U mouldahka -h localhost -d mouldahka" > data.sql

docker run --rm --name backup_db -p 6543:5432 -e POSTGRES_PASSWORD=postgres -d postgres:latest

sleep 5

python3 main.py

docker stop backup_db