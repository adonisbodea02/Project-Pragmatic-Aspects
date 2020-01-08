import logging

from constants import JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET, JSON_LEFTBRACE, JSON_RIGHTBRACE

logger = logging.getLogger('parser')


# Function used for parsing json array as tokens
# Input: list of tokens
# Output: array
def parse_array(tokens):
    assert type(tokens) == list, "Did not receive list!"
    types = [int, bool, str, float]
    for i in tokens:
        assert type(i) in types, "Did not receive suitable type!"
    logger.info('parse_array: Received tokens: ' + str(tokens))
    json_array = []

    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        logger.info('parse_array: Returned object: ' + str(json_array))
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            logger.info('parse_array: Returned object: ' + str(json_array))
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]


# Function used for parsing json object as tokens
# Input: list of tokens
# Output: python dictionary
def parse_object(tokens):
    assert type(tokens) == list, "Did not receive list!"
    for i in tokens:
        assert type(i) == str or bool or int or float, "Did not receive suitable type!"
    logger.info('parse_object: Received tokens: ' + str(tokens))
    json_object = {}

    t = tokens[0]
    if t == JSON_RIGHTBRACE:
        logger.info('parse_object: Returned object: ' + str(json_object))
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expected string key, got: {}'.format(json_key))

        if tokens[0] != JSON_COLON:
            raise Exception('Expected colon after key in object, got: {}'.format(t))

        json_value, tokens = parse(tokens[1:])

        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            logger.info('parse_object: Returned object: ' + str(json_object))
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after pair in object, got: {}'.format(t))

        tokens = tokens[1:]


# Function used for parsing json string as tokens
# Input: list of tokens
# Output: python objects
def parse(tokens, is_root=False):
    assert type(tokens) == list, "Did not receive list!"
    for i in tokens:
        assert type(i) == str or bool or int or float, "Did not receive suitable type!"
    assert type(is_root) == bool, "Did not receive bool!"
    logger.info('parse: Received tokens: ' + str(tokens) + " is_root = " + str(is_root))
    t = tokens[0]

    if is_root and t != JSON_LEFTBRACE:
        raise Exception('Root must be an object')

    if t == JSON_LEFTBRACKET:
        logger.info('parse: Returned type: ' + str(type([])))
        return parse_array(tokens[1:])
    elif t == JSON_LEFTBRACE:
        logger.info('parse: Returned type: ' + str(type({})))
        return parse_object(tokens[1:])
    else:
        logger.info('parse: Returned type: ' + str(type(t)))
        return t, tokens[1:]
