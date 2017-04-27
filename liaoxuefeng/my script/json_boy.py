import json


class Boy():
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def __str__(self):
        return '%s(name=%s,age=%s)' % (
            self.__class__.__name__, self.name, self.age)

    def boydefault(obj):
        if isinstance(obj, Boy):
            return {'name': obj.name, 'age': obj.age}
        return obj

    def boyhook(dic):
        print('test')
        if dict['name']:
            return boy(dic['name'], dic['age'])
        return dic


if __name__ == '__main__':
    boy = Boy('jack', 20)
    print('jake:', boy)
    boy_encode_str = json.dumps(boy, default=Boy.boydefault)
    print(boy_encode_str)
