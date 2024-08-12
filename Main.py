import pyodbc

# Chemin vers la base de données Access
db_path = r'C:\chemin\vers\ta\base_de_donnees.accdb'

# Créer une connexion à la base de données
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path)
cursor = conn.cursor()

# Fonction pour insérer un utilisateur
def ajouter_utilisateur(nom, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (nom, email))
    conn.commit()
    print("Utilisateur ajouté avec succès")

# Fonction pour lire les utilisateurs
def lire_utilisateurs():
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row.id}, Nom: {row.name}, Email: {row.email}")

# Exemple d'utilisation
ajouter_utilisateur('Jean Dupont', 'jean.dupont@example.com')
lire_utilisateurs()

# Fermer la connexion
conn.close()
