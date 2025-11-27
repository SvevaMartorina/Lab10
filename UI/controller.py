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
        self._view._lista_visualizzazione.controls.clear()

        valore = self._view.guadagno_medio_minimo.value
        try:
            float(valore)
        except ValueError:
            self._view.guadagno_medio_minimo.error_text = 'inserisci un numero valido'
            self._view.guadagno_medio_minimo.update()

        self._model.costruisci_grafo(valore)
        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        self._view._lista_visualizzazione.controls.append(ft.TextField(f'Numero di Hubs:{num_nodi}'))
        self._view._lista_visualizzazione.controls.append(ft.TextField(f'Numero di Tratte:{num_archi}'))

        num = 1
        for u, v, data in self._model._G.edges(data=True):
            guadagno = data.get("weight", 0)

            #prendo gli oggetti Hub direttamente dal grafo
            hub_u = self._model._G.nodes[u]["hub"]
            hub_v = self._model._G.nodes[v]["hub"]

            self._view._lista_visualizzazione.controls.append(
                ft.Text(f"{num}) [{hub_u.nome}({hub_u.stato}) → {hub_v.nome}({hub_v.stato})]--guadagno Medio Per Hub: {guadagno:.2f} €")
            )
            num += 1

        self._view._lista_visualizzazione.update()
        return
        # TODO

