import json

from cafe.engine.models.base import AutoMarshallingModel


class FilterRequest(AutoMarshallingModel):

    def __init__(self, type, filter):
        self.type = type
        self.filter = filter

    def _obj_to_json(self):
        body = {
            "type":self.type,
            "filter":self.filter
        }
        body = self._remove_empty_values(body)
        return json.dumps(body)