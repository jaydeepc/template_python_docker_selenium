import json

from marshest.marshmodels import MarshModel


class CreateRequest(MarshModel):

    def __init__(self, cdt_type, opportunity_type, name, data_load_id):
        self.cdt_type = cdt_type
        self.opportunity_type = opportunity_type
        self.name = name
        self.data_load_id = data_load_id

    def _object_to_json(self):
        body = {
            "cdt_id": self.cdt_type,
            "type": self.opportunity_type,
            "name": self.name,
            "data_load_id": self.data_load_id
        }

        return json.dumps(body)


class DeleteRequest(MarshModel):

    def __init__(self, opportunity_ids):
        self.opportunity_ids = opportunity_ids

    def _object_to_json(self):
        body = {
            "opportunity_ids":self.opportunity_ids
        }

        return json.dumps(body)