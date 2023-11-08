words={
    'ə': 'e',
    'Ə': 'E',
    'I': 'I',
    'ö': 'o',
    'Ö': 'O',
    'ğ': 'g',
    'Ğ': 'G',
    'ü': 'u',
    'Ü': 'U',
    'ş': 's',
    'Ş': 'S',
    'ç': 'c',
    'Ç': 'C',
    ' ': '-',
    ',': '',
    '.': '',
    ':': '',
    ';': '',
    '!': '',
    '?': '',
    '(': '',
    ')': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    '""':'',
    '`': '',
    '_': '',

}

def generate_slug(title):
    for key,value in words.items():
        title=title.replace(key,value)
    return title.lower()
