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
    ordered_ids = [r.record_id for r in records]
    parent_ids = [c.parent_id for c in records]

    validate_tree_structure(ordered_ids)
    nodes_tree = list(map(build_node_tree, records))

    parent_child = zip(parent_ids[1:], nodes_tree[1:])
    nodes_list = build_node_relations(nodes_tree, parent_child)

    if len(nodes_list) <= 0:
        return None
    return nodes_list[0]


def validate_tree_structure(lst_of_record_ids):
    if len(lst_of_record_ids) <= 0:
        return
    if lst_of_record_ids[0] != 0:
        raise ValueError('Tree must start with id 0')
    if lst_of_record_ids[-1] != len(lst_of_record_ids) - 1:
        raise ValueError('Tree must be continuous')


def validate_precedence(record_obj):
    if record_obj.record_id == record_obj.parent_id and record_obj.record_id != 0:
        raise ValueError('Tree is a cycle')
    if record_obj.record_id < record_obj.parent_id:
        raise ValueError('Parent id must be lower than child id')


def build_node_tree(record):
    validate_precedence(record)
    return Node(record.record_id)


def build_node_relations(nodes, relations):
    for n_id, c in relations:
        nodes[n_id].children.append(c)
    return nodes
