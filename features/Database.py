from sqlite3 import *
import os, time
from features.User import User

DATABASE_NAME = "banco.db"


class DataMethods:

    @classmethod
    def create_connection(cls):
        connection = connect(f'{DATABASE_NAME}')
        return connection

    # Metodo para executar querys
    @classmethod
    def execute_query(cls, query):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    # Metodo para identificar se o banco ja existe ou nao
    @classmethod
    def initialize(cls):
        print("Inicializando banco")
        if os.path.exists(f'./{DATABASE_NAME}'):
            print('Banco existe')
        else:
            print('Banco não existe')
            print('Criando banco de dados')
            cls.execute_query(f'CREATE TABLE IF NOT EXISTS usuarios('
                              f'id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'nome TEXT NOT NULL,'
                              f'email TEXT UNIQUE NOT NULL,'
                              f'cpf TEXT UNIQUE NOT NULL,'
                              f'senha TEXT NOT NULL,'
                              f'data_nascimento TEXT NOT NULL,'
                              f'sexo TEXT NOT NULL,'
                              f'telefone INTEGER NOT NULL,'
                              f'tipo_sanguineo TEXT NOT NULL,'
                              f'altura REAL NOT NULL,'
                              f'peso REAL    NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS remedio('
                              f'id_remedio INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_remedio TEXT NOT NULL,'
                              f'desc_remedio TEXT,'
                              f'intervalo_uso TEXT,'
                              f'primeiro_uso TEXT NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS consulta('
                              f'id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_consulta TEXT NOT NULL,'
                              f'desc_consulta TEXT,'
                              f'hora_consulta TEXT NOT NULL,'
                              f'data_consulta TEXT NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS exame('
                              f'id_exame INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_exame TEXT NOT NULL,'
                              f'desc_exame TEXT,'
                              f'hora_exame TEXT NOT NULL,'
                              f'data_exame TEXT NOT NULL)')

            connection = connect(f'{DATABASE_NAME}')  # Replace with your database filename
            cursor = connection.cursor()
            try:

                # Execute the trigger creation query directly using cursor.execute()
                cursor.execute("""
                            CREATE TRIGGER validar_insercao_users
                            BEFORE INSERT ON usuarios
                            WHEN length(new.cpf) <> 11
                            BEGIN
                                SELECT RAISE(ABORT, 'CPF deve ter 11 digitos');
                            END;
                        """)
                connection.commit()
                print("Trigger 'validar_insercao_users' criado com sucesso!")
            except Error as e:
                print(f"Error creating trigger: {e}")

            try:
                # cls.execute_query("""INSERT INTO usuarios(nome, email, cpf, senha, data_nascimento, sexo, telefone , tipo_sanguineo, altura, peso) VALUES('Arthur', 'a', '52716328811', 'a', '24/08/2004', 'M', 19995128382, 'A+', 1.72, 80.0)""")
                User.add_users('Arthur', 'a', "52716328811", 'a', '24/08/2004', 'M', 19995128382, 'A+', 1.72, 80.0)
                # print(connection.execute("SELECT * from usuarios").fetchall())
            except Error as e:
                print(f"Error: {e}")

            # time.sleep(20)

            try:
                cursor.execute("""
                    CREATE VIEW users_view as SELECT * FROM usuarios
                """)
                connection.commit()
            except Error as e:
                print(f"Error: {e}")
            finally:
                connection.close()




    # Metodo para verificar login
    @classmethod
    def verify_login(cls, email: str, senha: str) -> bool:
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM usuarios')
        data = cursor.fetchall()
        for user in data:
            if user[2] == email:
                if user[4] == senha:
                    return True
                else:
                    return False
            else:
                continue
        connection.close()
        return False
