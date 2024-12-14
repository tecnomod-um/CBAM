from neotime import DateTime
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, DateTime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)