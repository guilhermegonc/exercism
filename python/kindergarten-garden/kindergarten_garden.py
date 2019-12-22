class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.plants_dct = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        self.students = students if students else ['Alice', 'Bob', 'Charlie', 'David',
                                                   'Eve', 'Fred', 'Ginny', 'Harriet',
                                                   'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def plants(self, child):
        pos_1_3, pos_2_4 = self.set_limits(child)
        rows = self.split_rows()

        first_row = [self.plants_dct[p] for p in rows[0][pos_1_3:pos_2_4]]
        second_row = [self.plants_dct[p] for p in rows[1][pos_1_3:pos_2_4]]

        return first_row + second_row

    def set_limits(self, child):
        position = self.find_child_position(child)
        return position * 2, position * 2 + 2

    def find_child_position(self, child):
        self.students.sort()
        return self.students.index(child)

    def split_rows(self):
        return self.diagram.split('\n')
