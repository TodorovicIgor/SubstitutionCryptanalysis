from util import mapping


class Key:

    def __init__(self, key=None):
        if key is None:
            # initial guess is without encryption
            self.key = mapping.freq
        else:
            self.key = key

    def swap(self, index1, index2):
        lst = list(self.key)
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return ''.join(lst)

