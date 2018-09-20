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
    nodes_list = list()
    node_parse = dict()

    validate_syntax(input_string)
    validate_content(input_string)

    if search(r'\w', input_string) is None:
        return SgfTree()

    for pos, character in enumerate(list(input_string)):
        if character == ';':
            str_parse = extract_info(input_string, pos)  # String selection

            node_key = str_parse[0: str_parse.index('[')]  # Node Key
            validate_uppercase(node_key)

            node_values = split_node_values(str_parse)  # Node Values

            node_parse[node_key] = node_values.copy()  # Build Nodes
            nodes_list.append(node_parse.copy())  # Build Nodes Dict

            node_values.clear()
            node_parse.clear()

    if len(nodes_list) == 1:
        return SgfTree(properties=nodes_list[0])
    else:
        children_list = list()
        for c in range(1, len(nodes_list)):
            children_list.append(SgfTree(nodes_list[c]))
        return SgfTree(properties=nodes_list[0], children=children_list)


def validate_syntax(text):
    if len(text) >= 3 and ('(' and ')' and ';' in text):
        return
    raise ValueError('Invalid values, check the pieces and its properties.')


def validate_content(text):
    if search(r'\w', text) and not ('[' and ']' in text):
        raise ValueError('Invalid input. Piece with no porperties.')
    else:
        return


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
        elif text[begin_index] not in '[]':
            while True:
                if text[end_index] == '\\':
                    end_index += 2
                    if end_index > len(text):
                        break
                elif text[end_index] == ']':
                    break
                else:
                    end_index += 1
            node_values.append(escape_special_chars(text[begin_index: end_index]))
            begin_index = end_index + 1
        else:
            begin_index += 1
            end_index = begin_index
    return node_values


def validate_uppercase(text):
    if not (text.isupper()):
        raise ValueError('Invalid input, problem with pieces.')
    return


def escape_special_chars(text):
    text = ''.join(text)
    text = text.replace('\]', ']')
    text = text.replace('\:', ':')
    text = text.replace('\\t', ' ')
    text = text.replace('\\n', '\n')
    return text
