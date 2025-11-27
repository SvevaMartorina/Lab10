from dataclasses import dataclass

@dataclass
class Tratta:
    id_hub_origine: int
    id_hub_destinazione: int
    guadagno_medio : float

    def __eq__(self, other):
        return (self.id_hub_origine == other.id_hub_origine and
                self.id_hub_destinazione == other.id_hub_destinazione)

    def __hash__(self):
        return hash(self.id_hub_origine + self.id_hub_destinazione)

    def __lt__(self, other):
        return self.guadagno_medio < other.guadagno_medio

    def __repr__(self):
        return f':From{self.id_hub_origine} to:{self.id_hub_destinazione} - Guadagno medio per spedizione {self.guadagno_medio}'


