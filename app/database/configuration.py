from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine



#datos para la conexion a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"


#creo el motor de conexion a la base de datos
Engine = create_engine(dataBaseConnection)

#abrir la sesion con la base de datos


#para que no haga peticiones 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
