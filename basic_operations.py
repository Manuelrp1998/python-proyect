
from pymongo import MongoClient

# Cadena de conexión (asegúrate de usar tus propios detalles)
uri = "mongodb+srv://beldic:Tech1Cash2Club3@techcashclub.akflm9s.mongodb.net/"

# Crear una instancia de MongoClient
client = MongoClient(uri)

# Especificar la base de datos y la colección que deseas usar
db = client['sample_mflix']
collection = db['movies']

# Realizar una consulta simple (encontrar todos los documentos)
for doc in collection.find():
    print(doc)

# Cierra la conexión al finalizar
client.close()
