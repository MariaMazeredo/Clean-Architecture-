from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler: #essa classe encapsula toda a lógica da conexão com banco

    def __init__(self) -> None: #construtor da classe
        self.__connection_string = "{}://{}:{}@{}:{}/{}" .format( #string de conexão com o banco
            'mysql+pymysql', #banco e driver usados
            'root', #usuário
            'myPassword',
            'localhost', #host
            '3306', #porta
            'clean_database'
        )
        self.__engine = self.__create_database_engine () #cria a engine de conexão
        self.session = None


    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self): #chama a engine
        return self.__engine 
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        