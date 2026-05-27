from sqlmodel import create_engine

databasse_URL = "mysql+pymysql://root:root@localhost:3306/challenge" #creamos en nombre del archivo der la base de datos
mysql_path = (databasse_URL) # creamos la ruta de la base de datos pasando como argumento quie va a hcer con un motor de base de datos de mysql

connect_args = {"check_same_thread": False} # guardamos en una variablke lo que se coonoce como el multi-hilo para que en caso tal de que una ssola requeste requiera usa r mas de un hilo
engine = create_engine(mysql_path, connect_args=connect_args) 