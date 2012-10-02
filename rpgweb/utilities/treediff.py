from types import NoneType
from datetime import datetime, timedelta



"""

opcodes:

add (paths, key) value
replace (paths, key) value
delete (paths, key) None


WARNING - ATM immutable types are not supported.

"""

ATOMIC_TYPES = (basestring, long, int, float, bool, set, tuple, NoneType, datetime, timedelta)
LOOKUP_TYPES = (dict, list) # other are considered as instances, with editable attributes



def _recurse_tree_diff(a, b, current_paths, final_opcodes):

    if a.__class__ != b.__class__:
        final_opcodes.append(("replace", current_paths, b))

    elif isinstance(a, ATOMIC_TYPES):
        if a != b:
            final_opcodes.append(("replace", current_paths, b))
    else:
        # we transform a and b into mappings
        if isinstance(a, dict):
            pass # a and b unchanged
        elif isinstance(a, (list, tuple)):
            a = dict(enumerate(a))
            b = dict(enumerate(b))
        else: # any other kind of object
            a = a.__dict__
            b = b.__dict__

        for key in sorted(a.keys()):
            new_current_paths = current_paths + [key]
            if key not in b:
                final_opcodes.append(("delete", new_current_paths, None))
            else:
                _recurse_tree_diff(a[key], b[key], new_current_paths, final_opcodes)

        for key in sorted(set(b.keys()) - set(a.keys())):
            new_current_paths = current_paths + [key]
            final_opcodes.append(("add", new_current_paths, b[key]))


def generate_tree_diff(a, b):
    final_opcodes = []
    _recurse_tree_diff(a, b, [], final_opcodes)
    return final_opcodes






def _extract_object(root, paths):
    leaf = root
    for path_item in paths:
        if isinstance(leaf, LOOKUP_TYPES):
            leaf = leaf[path_item]
        else:
            leaf = getattr(leaf, path_item)
    return leaf

def _apply_operation(op, leaf, key, value):
    if op in ("add", "replace"):
        if isinstance(leaf, LOOKUP_TYPES):
            if isinstance(leaf, list) and len(leaf) <= key:
                assert key == len(leaf), (op, leaf, key) # by construction!!
                leaf.append(value)
            else:
                leaf[key] = value
        else:
            setattr(leaf, key, value)
    elif op == "delete":
        if isinstance(leaf, LOOKUP_TYPES):
            if isinstance(leaf, list):
                list.pop() # by construction, it'll work!!
            else:
                del leaf[key]
        else:
            delattr(leaf, key)
    else:
        raise ValueError("Unrecognized opcode %s" % op)


def apply_tree_diff(root, opcodes):

    # special case - we replace the root object by another
    if len(opcodes) == 1 and not opcodes[0][1]:
        if opcodes[0][0] != "replace":
            raise ValueError("Operation on root object can be nothing but a 'replace'")
        return opcodes[0][2]

    for (op, paths, value) in opcodes:
        assert paths
        leaf = _extract_object(root, paths[:-1])
        _apply_operation(op, leaf, paths[-1], value)

    return root




if __name__ == "__main__":

    class TestClass(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
        def __eq__(self, other):
            return self.__class__ == other.__class__ and self.__dict__ == other.__dict__

    a = dict(cat=True,
             dog=[22, 33],
             bird=None,
             stuffs=TestClass(obj=u"hello"),
             missing=set((1, 2, 3)))

    b = dict(cat=True,
             dog=[11, 33, 99],
             bird=False,
             stuffs=TestClass(obj="hello", objbis=77),
             added=122.11)

    opcodes = generate_tree_diff(a, b)
    #for code in opcodes: print code

    assert opcodes == [
        ('replace', ['bird'], False),
        ('replace', ['dog', 0], 11),
        ('add', ['dog', 2], 99),
        ('delete', ['missing'], None),
        ('replace', ['stuffs', 'obj'], 'hello'),
        ('add', ['stuffs', 'objbis'], 77),
        ('add', ['added'], 122.11),
        ]


    new_b = apply_tree_diff(a, opcodes)
    assert a == b


    # root difference
    opcodes = generate_tree_diff(2, True)
    assert apply_tree_diff(2, opcodes) == True



