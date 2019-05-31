class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def __repr__(self):
        return f'r.id: {self.record_id}'


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self):
        return f'n.id: {self.node_id}'


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    ordered_id = [r.record_id for r in records]
    parent_id = [c.parent_id for c in records]

    validate_tree_structure(ordered_id)
    tree = build_node_tree(records)

    parent_child = zip(parent_id[1:], tree[1:])
    lst_of_nodes = build_node_relations(tree, parent_child)

    root = None
    if len(lst_of_nodes) > 0:
        root = lst_of_nodes[0]

    return root


def validate_tree_structure(lst_of_record_ids):
    if len(lst_of_record_ids) > 0:
        if lst_of_record_ids[0] != 0:
            raise ValueError('Tree must start with id 0')
        if lst_of_record_ids[-1] != len(lst_of_record_ids) - 1:
            raise ValueError('Tree must be continuous')
    pass


def validate_precedence(record_obj):
    if record_obj.record_id == 0 and record_obj.parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    if record_obj.record_id < record_obj.parent_id:
        raise ValueError('Parent id must be lower than child id')
    if record_obj.record_id == record_obj.parent_id and record_obj.record_id != 0:
        raise ValueError('Tree is a cycle')
    pass


def build_node_tree(records):
    tree = []
    for r in records:
        validate_precedence(r)
        node = Node(r.record_id)
        tree.append(node)
    return tree


def build_node_relations(nodes, relations):
    for i, c in relations:
        nodes[i].children.append(c)
    return nodes
