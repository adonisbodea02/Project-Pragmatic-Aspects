import logging

import json_lexer
import json_parser

from json_builder import JSONObject

logger = logging.getLogger('json_string_functions')


# Function used for obtaining string object from json string
# Input: string
# Output: python string
def from_json(json_string):
    try:
        assert type(json_string) == str, str(json_string) + ' is not string'
        logger.info('from_json: Received string: ' + json_string)
        tokens = json_lexer.lex(json_string)
        json_object = json_parser.parse(tokens, is_root=True)[0]
        assert type(json_object) == dict, 'Dictionary object was not returned'
        logger.info('from_json: Returned object: ' + str(json_object))
        return json_parser.parse(tokens, is_root=True)[0]
    except AssertionError as e:
        logger.error('from_json: ' + str(e))


def to_json(obj):
    try:
        types = [dict, list, str, int, bool, type(None), JSONObject]
        assert type(obj) in types, str(type(obj)) + ' is not an allowed type'
        logger.info('to_json: Received object: ' + str(obj))
        json_type = type(obj)
        if json_type is dict:
            string = '{'
            dict_len = len(obj)

            if dict_len == 0:
                logger.info('to_json: Returned string: {}')
                return '{}'

            for i, (key, val) in enumerate(obj.items()):
                string += '"{}": {}'.format(key, to_json(val))

                if i < dict_len - 1:
                    string += ', '
                else:
                    string += '}'

            logger.info('to_json: Returned string: ' + string)
            return string
        elif json_type is list:
            string = '['
            list_len = len(obj)

            if list_len == 0:
                logger.info('to_json: Returned string: []')
                return '[]'

            for i, val in enumerate(obj):
                string += to_json(val)

                if i < list_len - 1:
                    string += ', '
                else:
                    string += ']'

            logger.info('to_json: Returned string: ' + string)
            return string
        elif json_type is str:
            return '"{}"'.format(obj)
        elif json_type is bool:
            logger.info('to_json: Returned string: ' + str(obj).lower())
            return 'true' if obj else 'false'
        elif isinstance(obj, type(None)):
            logger.info('to_json: Returned string: null')
            return 'null'
        elif json_type is JSONObject:
            return obj.json

        logger.info('to_json: Returned string: ' + str(obj))
        return str(obj)
    except AssertionError as e:
        logger.error('to_json: ' + str(e))
