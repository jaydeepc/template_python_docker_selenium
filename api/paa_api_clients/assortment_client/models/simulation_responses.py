import json

from marshest.marshmodels import MarshModel


class Simulation(MarshModel):

    def __init__(self, simulation_id):
        self.simulation_id = simulation_id

    @classmethod
    def _json_to_object(cls, serialized_str):
        return Simulation(simulation_id=serialized_str.decode("utf-8"))
