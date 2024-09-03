import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuración del nombre y directorio del archivo de base de datos SQLite
sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

# URL de la base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Creación del motor de la base de datos
engine = create_engine(database_url, echo=True)

# Creación de la sesión de base de datos
Session = sessionmaker(bind=engine)

# Creación de la base declarativa
Base = declarative_base()
