import json
import keyword


class json2py():


    def __init__(self):
        self.mass = list()

    def keys(self, dct, pred_str=''):
        for key in dct.keys():
            if not isinstance(dct[key], dict):
                self.mass.append([pred_str + str(key), dct[key]])
            else:
                self.mass.append([pred_str + str(key), dct[key]])
                # self.keys(dct[key], pred_str= pred_str + str(key)+'.')
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


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self):
        title = super().__getattribute__('title')
        price = super().__getattribute__('price')
        temp = f'\033[1;{ColorizeMixin.repr_color_code};01m' + f'{title} | {price} ₽' + '\033[0;38;01m'
        return temp


@object_correct
class Advert(ColorizeMixin):
    def __init__(self, lesson: dict):
        mass_attr = json2py().keys(lesson)
        for pred_attr in mass_attr:
            name_attr = pred_attr[0]
            if keyword.iskeyword(name_attr):
                name_attr = name_attr + '_'
            setattr(self, name_attr, pred_attr[1])

    # def setter(self, name_attr, val):
    #     object.__setattr__(self, name_attr.split('.')[-1], val)

    def __getattribute__(self, attr):
        t = super().__getattribute__(attr)
        if type(t) is not dict:
            print(t)
        else:
            return Advert(t, check_value=False)

    # def __repr__(self):
    #     title = super().__getattribute__('title')
    #     price = super().__getattribute__('price')
    #     return f'{title} | {price} ₽'


if __name__ == '__main__':
    lesson_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }  
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # lesson_ad.price
    lesson_ad.title
    lesson_ad.location.address
    print(lesson_ad)
    lesson_ad.title
    print('100')
    lesson_ad.class_
    # lesson_ad.class_
