#!/usr/bin/python3
""" scrip """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    """script that adds all arguments to a Python list
    and then save them to a file"""
    import sys
    filename = "add_item.json"
    try:
        my_obj = load_from_json_file(filename)
    except:
        my_obj = []
    finally:
        for arg in(sys.argv[1:]):
            my_obj.append(arg)
        save_to_json_file(my_obj, filename)
