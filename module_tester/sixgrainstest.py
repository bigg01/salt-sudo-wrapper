from __future__ import print_function

known_types = {
    'six_special': int,
    'six_release': str,
    'six_roles': list
}

grains = {
    'six_special': 0,
    'six_release': 'S2016q3',
    'six_roles': ['time']
}

def test(g_item, g_type):
    if grains.has_key(g_item):
        if isinstance(grains.get(g_item), g_type):
            return { g_item: True }
        else:
            return { g_item: False }
    return { g_item: 'no key' }

if __name__ == "__main__":
    for i, t in known_types.iteritems():
        print(test(i, t))
