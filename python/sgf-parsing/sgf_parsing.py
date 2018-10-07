from re import search


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
    nodes_list = []
    node_parse = {}

    if invalid_syntax(input_string) or invalid_content(input_string):
        raise ValueError('Invalid input. Piece with no properties.')

    if empty_move(input_string):
        return SgfTree()

    for pos, character in enumerate(list(input_string)):
        if character == ';':  # Each ';' indicates the presence of one piece
            str_parse = extract_info(input_string, pos)  # String starts after ';' and go to next ';' or ')'

            node_key = str_parse[:str_parse.index('[')]  # Node Key ends before '['
            if invalid_uppercase(node_key):
                raise ValueError('Invalid input, problem with pieces.')

            node_values = split_node_values(str_parse)  # Node values start after '['

            node_parse[node_key] = node_values.copy()  # Build Nodes
            nodes_list.append(node_parse.copy())  # Build Nodes Dict

            node_values.clear()
            node_parse.clear()

    if len(nodes_list) == 1:
        return SgfTree(properties=nodes_list[0])

    children_list = list()
    for c in range(1, len(nodes_list)):
        children_list.append(SgfTree(nodes_list[c]))
    return SgfTree(properties=nodes_list[0], children=children_list)


def invalid_syntax(text):
    return len(text) < 3 or not('(', ')', ';' in text)


def invalid_content(text):
    return search(r'\w', text) and not ('[', ']' in text)


def empty_move(input_string):
    return search(r'\w', input_string) is None


def extract_info(text, reference_number):
    begin_index = end_index = reference_number + 1
    while True:
        if text[end_index] in ';)' or end_index == len(text):
            break
        end_index += 1
    return text[begin_index: end_index]


def split_node_values(text):
    node_values = list()
    begin_index = end_index = text.index('[') + 1

    while True:
        if (begin_index or end_index) >= len(text) - 1:
            break

        if text[begin_index] not in '[':  # Find first position for node value
            while True:
                if text[end_index] == '\\':  # Find final position for node value
                    end_index += 2
                    if end_index > len(text):
                        break
                elif text[end_index] == ']':
                    break
                else:
                    end_index += 1
            node_values.append(escape_special_chars(text[begin_index: end_index]))  # Node value ignoring special chars
            begin_index = end_index + 1
        else:
            begin_index += 1
            end_index = begin_index

    return node_values


def invalid_uppercase(text):
    return not(text.isupper())


def escape_special_chars(text):
    text = text.replace('\]', ']')
    text = text.replace('\:', ':')
    text = text.replace('\\t', ' ')
    text = text.replace('\\n', '\n')
    return text
