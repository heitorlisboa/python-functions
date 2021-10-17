def extract_dictionary_keys_values(dictionary: dict) -> tuple[list, list]:
    dict_keys: list = []
    dict_values: list = []

    for key, value in dictionary.items():
        if not isinstance(value, dict):
            dict_keys.append(key)
            dict_values.append(value)

        else:
            dict_keys = [*dict_keys, *extract_dictionary_keys_values(value)[0]]
            dict_values = [*dict_values, *extract_dictionary_keys_values(value)[1]]

    return dict_keys, dict_values

if __name__ == "__main__":
    MY_DICT = {
        "name": "Heitor",
        "parents": {
            "dad": "dad's name",
            "mom": "mom's name",
        },
        "level1": {
            "level2": {
                "level3": "random value"
            }
        }
    }

    MY_DICT_KEYS, MY_DICT_VALUES = extract_dictionary_keys_values(MY_DICT)

    print(MY_DICT_KEYS)
    print(MY_DICT_VALUES)
