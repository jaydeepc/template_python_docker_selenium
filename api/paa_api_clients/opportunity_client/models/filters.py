import json

from marshest.marshmodels import MarshModel


class FilterRequest(MarshModel):

    def __init__(self, type, filter):
        self.type = type
        self.filter = filter

    def _object_to_json(self):
        body = {
            "type":self.type,
            "filter":self.filter
        }

        return json.dumps(body)