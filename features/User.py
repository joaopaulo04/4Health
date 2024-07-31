from sqlite3 import *

DATABASE_NAME = "banco.db"


class User:

    @classmethod
    def create_connection(cls):
        connection = connect(f'{DATABASE_NAME}')
        return connection

    @classmethod
    def execute_query(cls, query):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    @classmethod
    def show_users(cls):
            connection = cls.create_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            connection.close()
            return usuarios

    @classmethod
    def get_user_by_email(cls, email):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE email='{email}'")
        user = cursor.fetchone()
        connection.close()
        return user

    @classmethod
    def get_user_by_cpf(cls, cpf):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE cpf={cpf}")
        user = cursor.fetchone()
        connection.close()
        return user

    @classmethod
    def add_users(cls, nome, email, cpf, senha, data_nascimento, sexo, telefone, tipo_sanguineo, altura, peso):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO usuarios(nome, email, cpf, senha, data_nascimento, sexo, telefone , tipo_sanguineo, altura, peso) VALUES ("
            f"'{nome}',"
            f"'{email}',"
            f"{cpf},"
            f"'{senha}',"
            f"'{data_nascimento}',"
            f"'{sexo}',"
            f"{telefone},"
            f"'{tipo_sanguineo}',"
            f"{altura},"
            f"{peso}"
            f")")
        connection.commit()
        connection.close()
        return True

    @classmethod
    def remove_users(cls, id_usuario):
        cls.execute_query(f"DELETE FROM usuarios WHERE id_usuario = {id_usuario}")

    @classmethod
    def edit_users(cls, id_usuario, senha, telefone, altura, peso, tipo_sanguineo):
        cls.execute_query(f"UPDATE usuarios SET senha = '{senha}',"
                          f"telefone = {telefone}, "
                          f"altura = {altura}, "
                          f"peso = {peso},"
                          f"tipo_sanguineo = '{tipo_sanguineo}'"
                          f"WHERE id_usuario = {id_usuario};")

    @classmethod
    def edit_password(cls, email: str, senha: str):
        # Criando conexão com o banco
        connection = cls.create_connection()
        cls.execute_query(f"UPDATE usuarios SET senha = '{senha}' WHERE email = '{email}';")
        connection.close()
