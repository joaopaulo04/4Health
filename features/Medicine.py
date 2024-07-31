from sqlite3 import *

DATABASE_NAME = "banco.db"


class Medicine:

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
    def show_remedios(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM remedio WHERE id_usuario = {id_usuario}')
        remedio = cursor.fetchall()
        connection.close()
        return remedio

    @classmethod
    def add_remedio(cls, id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        cls.execute_query(
            f"INSERT INTO remedio(id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso) VALUES("
            f"{id_usuario},"
            f"'{nome_remedio}',"
            f"'{desc_remedio}',"
            f"'{intervalo_uso}',"
            f"'{primeiro_uso}'"
            f")")

    @classmethod
    def remove_remedio(cls, id_remedio):
        cls.execute_query(f"DELETE FROM remedio WHERE id_remedio = {id_remedio};")

    @classmethod
    def edit_remedio(cls, id_remedio, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        cls.execute_query(f"UPDATE remedio SET nome_remedio = '{nome_remedio}',"
                          f"desc_remedio = '{desc_remedio}',"
                          f"intervalo_uso = '{intervalo_uso}',"
                          f"primeiro_uso = '{primeiro_uso}'"
                          f"WHERE id_remedio = {id_remedio};")
