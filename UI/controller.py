import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        #self._view._lista_visualizzazione.controls.clear()
        try:
            testo = self._view.guadagno_medio_minimo.value
            float(testo)
            self._view._lista_visualizzazione.controls.append(ft.TextField(f'Numero di Hubs:{self._model._num_nodes}'))
            self._view._lista_visualizzazione.controls.append(ft.TextField(f'Numero di Tratte:{self._model._num_edges}'))
            num = 0
            for u,v,data in self._model._G.edges(data=True):
                self._view._lista_visualizzazione.controls.append(ft.TextField(f"{num}) {u} → {v}   (guadagno: {data['weight']}"))
                num += 1
                print(u,v,data)
        except ValueError:
            self._view.guadagno_medio_minimo.error_text = 'inserisci un numero valido'
            self._view.guadagno_medio_minimo.update()

        self._view._lista_visualizzazione.update()


        return
        # TODO

