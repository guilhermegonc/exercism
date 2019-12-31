class Garden:
    def __init__(self, diagram, students=None):
        self.plants_dct = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        self.diagram = diagram.replace('\n', '')
        self.row_size = len(self.diagram) / 2
        self.students = sorted(students) if students else ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                                                           'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def plants(self, child):
        first_row, second_row = self.set_positions(child)
        plants_list = [self.diagram[first_row], self.diagram[first_row + 1],
                       self.diagram[second_row], self.diagram[second_row + 1]]
        return [self.plants_dct[p] for p in plants_list]

    def set_positions(self, child):
        reference = self.find_child_position(child)
        first_row = int(reference * 2)
        second_row = int(first_row + self.row_size)
        return first_row, second_row

    def find_child_position(self, child):
        return self.students.index(child)
