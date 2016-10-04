import json

from cafe.engine.models.base import AutoMarshallingModel


class CreateRequest(AutoMarshallingModel):

    def __init__(self, cdt_type, opportunity_type, name, data_load_id):
        self.cdt_type = cdt_type
        self.opportunity_type = opportunity_type
        self.name = name
        self.data_load_id = data_load_id

    def _obj_to_json(self):
        body = {
            "cdt_id": self.cdt_type,
            "type": self.opportunity_type,
            "name": self.name,
            "data_load_id": self.data_load_id
        }
        body = self._remove_empty_values(body)
        return json.dumps(body)


class DeleteRequest(AutoMarshallingModel):

    def __init__(self, opportunity_ids):
        self.opportunity_ids = opportunity_ids

    def _obj_to_json(self):
        body = {
            "opportunity_ids":self.opportunity_ids
        }
        body = self._remove_empty_values(body)
        return json.dumps(body)