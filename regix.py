import re


def get_string_info(s):
    pattern = r'.*?(\d+).*'
    replacement = r'\1'
    new_str = re.sub(pattern, replacement, s)
    return int(new_str)


list_of_strings = ['photo_1.png', 'photo_11.png',
                   'photo_129.png', 'photo_8.png',
                   'photo_21.png']

list_of_strings.sort()
print("\n".join(list_of_strings))
print()

list_of_strings.sort(key=get_string_info)
print("\n".join(list_of_strings))
