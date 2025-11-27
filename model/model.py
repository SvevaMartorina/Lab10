from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self._num_nodes = 0
        self._num_edges = 0
        self._G = nx.Graph()


    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        for hub in self._nodes:
            self._G.add_node(hub.id)
        for tratta in self._edges:
            if tratta.guadagno_medio >= threshold:
                self._G.add_edge(tratta.id_hub_origine,
                                 tratta.id_hub_destinazione,
                                 weight=tratta.guadagno_medio)

        self._num_nodes = self._G.number_of_nodes()
        self._num_edges = self._G.number_of_edges()
        return self._G
        # TODO

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        self._num_edges = self._G.number_of_edges()
        return self._num_edges
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        self._num_nodes = self._G.number_of_nodes()
        return self._num_nodes
        # TODO

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        self._edges = DAO.tratta()
        return self._edges

        # TODO

    def get_all_nodes(self):
        """
        Restituisce tutti gli hub (i nodi)
        """
        self._nodes = DAO.hub()
        return self._nodes


