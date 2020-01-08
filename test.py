import unittest

import string_functions
import file_functions
import logging


class TestStringMethods(unittest.TestCase):

    # from json
    def test_from_json_empty_object(self):
        self.assertEqual(string_functions.from_json('{}'), {})

    def test_from_basic_object(self):
        self.assertEqual(string_functions.from_json('{"foo":"bar"}'), {"foo": "bar"})

    def test_from_json_basic_number(self):
        self.assertEqual(string_functions.from_json('{"foo":1}'), {"foo": 1})

    def test_from_json_empty_array(self):
        self.assertEqual(string_functions.from_json('{"foo":[]}'), {"foo": []})

    def test_from_json_basic_array(self):
        self.assertEqual(string_functions.from_json('{"foo":[1,2,"three"]}'), {"foo": [1, 2, "three"]})

    def test_from_json_nested_object(self):
        self.assertEqual(string_functions.from_json('{"foo":{"bar":2}}'), {"foo": {"bar": 2}})

    def test_from_json_true(self):
        self.assertEqual(string_functions.from_json('{"foo":true}'), {"foo": True})

    def test_from_json_false(self):
        self.assertEqual(string_functions.from_json('{"foo":false}'), {"foo": False})

    def test_from_json_null(self):
        self.assertEqual(string_functions.from_json('{"foo":null}'), {"foo": None})

    def test_from_json_basic_whitespace(self):
        self.assertEqual(string_functions.from_json('{ "foo" : [1, 2, "three", 4] }'), {"foo": [1, 2, "three", 4]})

    # to json
    def test_to_json_empty_object(self):
        self.assertEqual(string_functions.to_json({}), '{}')

    def test_to_basic_object(self):
        self.assertEqual(string_functions.to_json({"foo": "bar"}), '{"foo": "bar"}')

    def test_to_json_basic_number(self):
        self.assertEqual(string_functions.to_json({"foo": 1}), '{"foo": 1}')

    def test_to_json_empty_array(self):
        self.assertEqual(string_functions.to_json({"foo": []}), '{"foo": []}')

    def test_to_json_basic_array(self):
        self.assertEqual(string_functions.to_json({"foo": [1, 2, "three"]}), '{"foo": [1, 2, "three"]}')

    def test_to_json_nested_object(self):
        self.assertEqual(string_functions.to_json({"foo": {"bar": 2}}), '{"foo": {"bar": 2}}')

    def test_to_json_true(self):
        self.assertEqual(string_functions.to_json({"foo": True}), '{"foo": true}')

    def test_to_json_false(self):
        self.assertEqual(string_functions.to_json({"foo": False}), '{"foo": false}')

    def test_to_json_null(self):
        self.assertEqual(string_functions.to_json({"foo": None}), '{"foo": null}')


class TestFileMethods(unittest.TestCase):
    # from json
    def test_from_json_basic_array(self):
        self.assertEqual(file_functions.from_file('json_file_basic_array.txt'), {"foo": [1, 2, "three"]})

    def test_from_json_nested_object(self):
        self.assertEqual(file_functions.from_file('json_file_nested_object.txt'), {"foo": {"bar": 2}})

    def test_from_json_true(self):
        self.assertEqual(file_functions.from_file('json_file_true.txt'), {"foo": True})

    def test_from_json_false(self):
        self.assertEqual(file_functions.from_file('json_file_false.txt'), {"foo": False})

    def test_from_json_null(self):
        self.assertEqual(file_functions.from_file('json_file_null.txt'), {"foo": None})


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )
    unittest.main()
