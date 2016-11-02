import json

from marshest.marshmodels import MarshModel


class SimulationRequest(MarshModel):

    def __init__(self, cdt_id, delisted_products_ids, data_load_id):
        self.cdt_id = cdt_id
        self.delisted_products_ids = delisted_products_ids
        self.data_load_id = data_load_id

    def _object_to_json(self):
        body = {
            "cdt_id": self.cdt_id,
            "delisted_products": self.delisted_products_ids,
            "data_load_id": self.data_load_id
        }

        return json.dumps(body)
