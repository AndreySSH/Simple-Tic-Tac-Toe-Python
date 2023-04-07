name = input()

replace_dic = {
    'é': 'e',
    'ë': 'e',
    'á': 'a',
    'å': 'aa',
    'œ': 'oe',
    'æ': 'ae',
}

def normalize(string):
    for old, new in replace_dic.items():
        string = string.replace(old, new)
    return string

print(normalize(name))