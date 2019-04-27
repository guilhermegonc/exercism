import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):

    if invalid_basic_syntax(input_string):
        raise ValueError('Invalid input. Check for \'(\'\';\'\')\' in your input.')

    if empty_move(input_string):
        return SgfTree()

    node = {}
    n_list = []
    moves = [match.group() for match in re.finditer(r'(;\w*)+((\[)+((\w+)|(\s+)|(\\|\])*)+(]))+', input_string)]

    if len(moves) == 0:
        raise ValueError('Node without information.')

    for m in moves:
        action = split_move_from_prop(m)
        action_props = [escape_special_chars(match.group()[1:-1])
                        for match in re.finditer(r'((\[)+((\w+)|(\s+)|(\\|\])*)+(]))', m)]

        node[action] = action_props[:]
        n_list.append(node.copy())

        action_props.clear()
        node.clear()
    child = [SgfTree(np) for np in n_list[1:]]
    return SgfTree(properties=n_list[0], children=child)


def invalid_basic_syntax(text):
    return re.search(r'(\(;(.|\s)*\)$)', text) is None


def empty_move(input_string):
    return re.search(r'\w', input_string) is None


def split_move_from_prop(m):
    action = re.search(f';\w*', m).group()
    action = re.sub(';', '', action)

    if not (action.isupper()):
        raise ValueError('Invalid Input. Piece must be all uppercase.')

    return action


def escape_special_chars(text):
    text = text.replace('\]', ']')
    text = text.replace('\t', ' ')
    text = text.replace('\\n', '\n')
    return text
