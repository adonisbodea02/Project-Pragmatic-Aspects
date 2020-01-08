import logging
from copy import deepcopy


logger = logging.getLogger('json_builder')


class JSONObject(object):
    def __init__(self):
        self.json = ''

    @staticmethod
    def builder():
        return JSONObjectBuilder()


class JSONObjectBuilder(object):

    def __init__(self):
        self.fields = {}

    def put_list(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_string: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, list):
                raise TypeError("put_list: Value " + str(value) + " is not list!")
            types = [JSONObject, str, int, float, bool, type(None)]
            for i in value:
                if type(i) not in types:
                    raise TypeError("put_list: List item " + str(i) + " is not of suitable type!")
                if isinstance(i, str):
                    if "'" in i or '"' in i:
                        raise ValueError("put_string: Potential Injection Attack in value: " + i)
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def put_object(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_object: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, JSONObject):
                raise TypeError("put_object: Value " + str(value) + " is not JSONObject!")
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def put_null(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_null: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, type(None)):
                raise TypeError("put_null: Value " + str(value) + " is not None!")
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def put_bool(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_bool: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, bool):
                raise TypeError("put_bool: Value " + str(value) + " is not bool!")
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def put_number(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_number: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, int):
                raise TypeError("put_number: Value " + str(value) + " is not number!")
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def put_string(self, key, value):
        memento = deepcopy(self)
        try:
            if not isinstance(key, str):
                raise TypeError("put_string: Key " + str(key) + " is not string!")
            if "'" in key or '"' in key:
                raise ValueError("put_string: Potential Injection Attack in key: " + key)
            if not isinstance(value, str):
                raise TypeError("put_string: Value " + str(value) + " is not string!")
            if "'" in value or '"' in value:
                raise ValueError("put_string: Potential Injection Attack in key: " + value)
            memento.fields[key] = value
            del self
            return memento
        except (TypeError, ValueError) as e:
            logger.error(str(e))
            return self

    def build(self) -> JSONObject:
        jo = JSONObject()
        import string_functions
        jo.json = string_functions.to_json(self.fields)
        return jo
