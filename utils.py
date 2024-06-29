def merge_dicts(dict1, dict2):
    """ Merge two dicts with inner fields

    Exmpl:
        dict1 = {
            'a': 1,
            'b': {
                'c': 2,
                'd': 3
            },
            'e': 4
        }

        dict2 = {
            'b': {
                'c': 20,
                'f': 30
            },
            'g': 50
        }

        merge_dicts(dict1, dict2) = {
            'a': 1,
            'b': {
                'c': 20,
                'd': 3,
                'f': 30
            },
            'e': 4,
            'g': 50
        }


    """
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dicts(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1
