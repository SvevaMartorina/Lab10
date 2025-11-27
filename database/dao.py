from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def spedizione():
        cnx = DBConnect().get_connection()
        result = []
        cursor = cnx.cursor()
        query = ('''SELECT * FROM spedizione S ''', )
        cursor.execute(query)

        for row in cursor:
            spedizione = Spedizione(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            result.append(spedizione)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def compagnia():
        cnx = DBConnect().get_connection()
        result = []
        cursor = cnx.cursor()
        query = '''SELECT * FROM compagnia'''
        cursor.execute(query)

        for row in cursor:
            compagnia = Compagnia(row[0], row[1], row[2])
            result.append(compagnia)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def hub():
        cnx = DBConnect().get_connection()
        result = []
        cursor = cnx.cursor()
        query = '''SELECT * FROM hub'''
        cursor.execute(query)

        for row in cursor:
            hub = Hub(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            result.append(hub)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def tratta():
        cnx = DBConnect().get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = '''
            SELECT id_hub_origine, id_hub_destinazione, AVG(valore_merce) as guadagno_medio
            FROM spedizione S
            GROUP BY id_hub_origine, id_hub_destinazione
            '''

        cursor.execute(query)
        for row in cursor:
            tratta = Tratta(row['id_hub_origine'], row['id_hub_destinazione'], row['guadagno_medio'])
            result.append(tratta)

        cursor.close()
        cnx.close()
        return result


    # TODO
