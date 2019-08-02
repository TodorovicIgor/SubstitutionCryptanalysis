from util.mapping import freq


class Matrix:

    def __init__(self):
        self.matrix = [[0 for _ in range(26)] for _ in range(26)]
        self.indexes = freq

    def swap_indexes(self, char1, char2):
        lst = list(self.indexes)
        lst[self.indexes.find(char1)], lst[self.indexes.find(char2)] = lst[self.indexes.find(char2)], lst[self.indexes.find(char1)]
        self.indexes = ''.join(lst)

    def swap_matrix(self, char1, char2):
        # self.matrix[:, [self.indexes.find(char1), self.indexes.find(char2)]] = self.matrix[:, [self.indexes.find(char2), self.indexes.find(char1)]]
        # self.matrix[[self.indexes.find(char1), self.indexes.find(char2)], :] = self.matrix[[self.indexes.find(char2), self.indexes.find(char1)],:]
        index1 = self.indexes.find(char1)
        index2 = self.indexes.find(char2)
        for i in range(26):
            temp = self.matrix[i][index1]
            self.matrix[i][index1] = self.matrix[i][index2]
            self.matrix[i][index2] = temp
        temp = self.matrix[index1]
        self.matrix[index1] = self.matrix[index2]
        self.matrix[index2] = temp

    def swap(self, char1, char2):
        self.swap_indexes(char1, char2)
        self.swap_matrix(char1, char2)

    def print(self):
        for i in range(26):
            print(self.matrix[i])


# a = Matrix()
# a.matrix[2][2] = 5
# a.matrix[24][24] = 10
# a.swap('a', 'z')
# a.print()
