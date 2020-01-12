import logging

from json_builder import JSONObjectBuilder, JSONObject
from string_functions import to_json, from_json

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )

    to_json([{"foo": [1, 2, '2']}])
    from_json('{ "foo" : [1, 2, 3, 4] }')

    jo = JSONObject.builder().put_string("JSON1", "Hello World!"). \
        put_string("JSON2", "Hello my World!"). \
        put_string(1, JSONObjectBuilder().put_list("key1", "value1")).\
        put_list("list", [1, 2, True]).\
        put_object('obj', {'k1': 2, 'k2': 3}).\
        put_list('list2', ['1\"']).\
        put_object('obj', JSONObjectBuilder().put_list("key1", []).build()). \
        put_list('list3', [1, JSONObjectBuilder().put_list("key1", []).build()]).\
        put_string('1\\n\\', '1\t2').\
        build()

    print(jo.json)

    from_json([])
