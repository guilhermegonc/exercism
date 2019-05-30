class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def __repr__(self):
        return f'Record_id: {self.record_id}\nParent_id: {self.parent_id}\n'


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self):
        return f'n.id: {self.node_id} c:{len(self.children)}'


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    ordered_id = [r.record_id for r in records]
    validate_tree_structure(ordered_id)

    trees = []
    for r in records:
        validate_precedence(r)
        node = Node(r.record_id)
        trees.append(node)

    # for o in ordered_id:
    #     for j in ordered_id[:o]:
    #         if records[o].parent_id == j and records[o].record_id != 0:
    #             trees[j].children.append(trees[o])

    for node in trees:
        for r in records:
            if node.node_id == r.parent_id:
                for k in trees:
                    if r.record_id == k.node_id and k.node_id != 0:
                        node.children.append(k)

    root = None
    if len(trees) > 0:
        root = trees

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


# records = [
#             Record(6, 2),
#             Record(0, 0),
#             Record(3, 1),
#             Record(2, 0),
#             Record(4, 1),
#             Record(5, 2),
#             Record(1, 0)
#         ]
#
# print(BuildTree(records))
