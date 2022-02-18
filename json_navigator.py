"""
TASK 2
Navigate through json file
"""
import json


def read_data(path: str):
    """
    Read json file and return data.
    """
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def navigator(data):
    """
    Navigate through json file.
    """
    if isinstance(data, list):
        if data:
            print('\nThis is a list.',
                  f'Available indexes are from 0 to {len(data)-1}')
            try:
                index = int(
                    input('\nType the index of the element you want to see: '))
            except ValueError:
                index = len(data)
            while index not in range(0, len(data)):
                try:
                    index = int(input('\nIndex out of range. Try again: '))
                except ValueError:
                    pass
            new_data = data[index]
            print(new_data)
            navigator(new_data)
        else:
            print('\nThis is an empty list. There is nothing to do anymore.')

    elif isinstance(data, dict):
        print(
            f'\nThis is a dictionary. Here are the available keys:\n{list(data.keys())}')
        key = input('\nType the key the value of which you want to see: ')
        while key not in data.keys():
            key = input('\nThere is no such key. Try again:')
        new_data = data[key]
        print(new_data)
        navigator(new_data)
    else:
        print('\nThere is nothing to do anymore.')


def navigate_in_json(path: str):
    """
    Read json file and navigate through it.
    """
    data = read_data(path)
    navigator(data)


def main():
    """
    Main function.
    """
    path_to_json = input('Type path to the json file: ')
    navigate_in_json(path_to_json)


if __name__ == '__main__':
    main()
