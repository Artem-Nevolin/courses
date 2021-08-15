

class Vector:
    def __init__(self, *args):
        self.value = list(args)
        # если в value сохранить словарь, то item ключем.

    def __repr__(self):
        return str(self.value)

    def __getitem__(self, item):
        # сам метод позволяет делать доступ к значению
        # item является индексом в списке,
        # если value - это список, а если value - это словарь,
        # то item - это ключ к словарю
        if 0 < item <= len(self.value):
            return self.value[item]
        else:
            raise IndexError('Индекс лежит за пределами нашей коллекции')

    def __setitem__(self, key, value):
        # метод позволяет изменять значения в списки или словаре
        # key - индекс,
        # value - значение, которое хотим изменить.
        if 0 < key <= len(self.value):
            self.value[key] = value
        else:
            raise IndexError('Индекс лежит за пределами нашей коллекции')

    def __delitem__(self, key):
        # метод удаляет значение из коллекции по ключу
        if 0 < key < len(self.value):
            del self.value[key]
        else:
            raise IndexError('Индекс лежит за пределами нашей коллекции')
