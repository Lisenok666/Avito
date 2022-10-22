import json
import keyword


class JsonToPy():

    def __init__(self):
        self.mass = list()

    def keys(self, dct, pred_str=''):
        for key in dct.keys():
            if not isinstance(dct[key], dict):
                self.mass.append([pred_str + str(key), dct[key]])
            else:
                self.mass.append([pred_str + str(key), dct[key]])
        return self.mass


def object_correct(cls):
    def wrapper(lesson, check_value=True):
        if 'title' not in lesson and check_value:
            raise ValueError('Object without key Title')
        if 'price' not in lesson and check_value:
            lesson['price'] = 0
        # может не быть ключа price в dict
        if check_value and lesson['price'] < 0:
            raise ValueError('must be >= 0')
        return cls.__call__(lesson)
    return wrapper
    #return wrapper


class ColorizeMixin:
    def __init__(self):
        self.repr_color_code = 33



@object_correct
class Advert(ColorizeMixin):
    repr_color_code = 38

    def __init__(self, lesson: dict):
        super().__init__()
        mass_attr = JsonToPy().keys(lesson)
        self.price = 0
        for pred_attr in mass_attr:
            name_attr = pred_attr[0]
            if keyword.iskeyword(name_attr):
                name_attr = name_attr + '_'
            setattr(self, name_attr, pred_attr[1])

    def __getattribute__(self, attr):
        t = super().__getattribute__(attr)
        if not isinstance(t, dict):
            return t
        else:
            return Advert(t, check_value=False)

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};01m' + f'{self.title} | {self.price} ₽' + '\033[0;38;01m'


if __name__ == '__main__':
    lesson_str = """{
    "title": "Вельш-корги",
    "price": 100,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }  
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    lesson_ad.price
    print(lesson_ad.title)
    print(lesson_ad.location.address)
    print(lesson_ad)
    lesson_ad.title
    print(lesson_ad.price)
    print(lesson_ad.class_)
