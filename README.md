# Sauvegarder les données de Mouldahka

1. Cloner le dépôt

```bash
git clone https://github.com/Mouldahka/backup
cd backup
```

2. Lancer le script

```bash
./backup.sh <ssh_user> <ssh_host> <ssh_port>
```

3. La base de données est sauvegardée dans le fichier `data.sql` du répertoire courant
4. Les medias sont sauvegardées dans le dossier `data` du répertoire courant
