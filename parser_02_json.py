import json
from parser_02 import *


def build_json_parser():
    return Terminal("json")


def main():
    json_parser = build_json_parser()

    test_object = {"name": "John", "age": "25", "cats": ["tommy", "fluffy", "rex"]}
    test_string = json.dumps(test_object)
    result = json_parser.parse(test_string)
    parsed_object = result[1]

    print("\nTest String:")
    print(f"'{test_string}'")

    print("\nParsed:")
    print(parsed_object)

    print("\nExpected:")
    print(test_object)

    print("\nResult:")
    print(test_object == parsed_object)


if __name__ == '__main__':
    main()
