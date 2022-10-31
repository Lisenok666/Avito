import click
from random import randint


def correct_init(init):
    def wrapper(self, name, size, recipe):
        if size not in ['L', 'XL']:
            raise ValueError('Size must be L or XL')
        return init(self, name, size, recipe)

    return wrapper


def log(mask):
    def decorator(func):
        def wrapper(pizza):
            print(mask.format(randint(1, 10)))
            return func

        return wrapper

    return decorator


@log('🍳‍ Приготовили за {}с!')
def bake(pizza):
    """Готовит пиццу"""
    pass


@log('🏍 Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""
    pass


# переобозначим функцию т.к. у нас есть option delivery
delivery_alt = delivery


@log('🏡 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    pass


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    MENU_PIZZA = {'pepperoni': Pepperoni(), 'margherita': Margherita(), 'hawaiian': Hawaiian()}
    ctx.obj['MENU_PIZZA'] = {'pepperoni': Pepperoni(), 'margherita': Margherita(), 'hawaiian': Hawaiian()}


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.pass_context
def order(ctx, pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza = ctx.obj['MENU_PIZZA'][pizza]
    if delivery:
        delivery_alt(pizza)
    else:
        pickup(pizza)
    bake(pizza)


@cli.command()
@click.pass_context
def menu(ctx):
    """Выводит меню"""
    click.echo(Margherita().dict)
    click.echo(Pepperoni().dict)
    click.echo(Hawaiian().dict)


class pizza_recipe():
    picture = ' \N{winking face}: '

    @correct_init
    def __init__(self, name, size, recipe):
        self.name = name
        self.size = size
        self.recipe = recipe

    def dict(self):
        ret = ' - ' + str(self.name) + self.picture
        ret += ', '.join(self.recipe)
        return ret


class Margherita(pizza_recipe):
    picture = ' 🧀: '

    def __init__(self, size='L'):
        recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
        super(Margherita, self).__init__('Margherita', size, recipe)


class Pepperoni(pizza_recipe):
    picture = ' 🍕: '

    def __init__(self, size='L'):
        recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
        super(Pepperoni, self).__init__('Pepperoni', size, recipe)


class Hawaiian(pizza_recipe):
    picture = ' 🍍: '

    def __init__(self, size='L'):
        recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        super(Hawaiian, self).__init__('Hawaiian', size, recipe)


if __name__ == '__main__':
    cli(obj={})
