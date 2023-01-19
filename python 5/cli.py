from random import randint

import click


def log(mask):
    def decorator(func):
        def wrapper(pizza):

            ret = func(pizza)
            print(mask.format(ret))
            return ret

        return wrapper

    return decorator


@log("🍳‍ Приготовили за {}с!")
def bake(pizza):
    """Готовит пиццу"""
    cook_time = pizza.cook_time + randint(1, 5)
    if pizza.size == "XL":
        cook_time *= 2
    return cook_time


@log("🏍 Доставили за {}с!")
def delivery(pizza):
    """Доставляет пиццу"""
    is_big = 0
    if pizza.size == "XL":
        is_big = 1
    sndart_time = randint(1, 10) + is_big * randint(1, 5)
    return sndart_time


# переобозначим функцию т.к. у нас есть option delivery
delivery_alt = delivery


@log("🏡 Забрали за {}с!")
def pickup(pizza):
    """Самовывоз"""
    is_big = 0
    if pizza.size == "XL":
        is_big = 1
    sndart_time = randint(1, 2) + is_big * randint(1, 3)
    return sndart_time


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    # MENU_PIZZA = {'pepperoni': Pepperoni(), 'margherita': Margherita(), 'hawaiian': Hawaiian()}
    ctx.obj["MENU_PIZZA"] = {
        "pepperoni": Pepperoni(),
        "margherita": Margherita(),
        "hawaiian": Hawaiian(),
    }


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--big_size", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
@click.pass_context
def order(ctx, pizza: str, big_size: bool, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza = ctx.obj["MENU_PIZZA"][pizza]
    if big_size:
        pizza.make_big()

    if delivery:
        delivery_alt(pizza)
    else:
        pickup(pizza)
    bake(pizza)


@cli.command()
@click.pass_context
def menu(ctx):
    """Выводит меню"""
    for pizza in ctx.obj["MENU_PIZZA"].values():
        click.echo(pizza.dict())


class PizzaRecipe:
    picture = " 😉: "

    def __init__(self, name, size, recipe, cook_time=1):
        if size not in ["L", "XL"]:
            raise ValueError("Size must be L or XL")
        self.name = name
        self.size = size
        self.cook_time = cook_time
        self.recipe = recipe

    def make_big(self):
        self.size = "XL"

    def dict(self):
        ret = " - " + str(self.name) + self.picture
        ret += ", ".join(self.recipe)
        return ret


class Margherita(PizzaRecipe):
    picture = " 🧀: "

    def __init__(self, size="L"):
        recipe = ["tomato sauce", "mozzarella", "tomatoes"]
        cook_time = 3
        super(Margherita, self).__init__("Margherita", size, recipe, cook_time)


class Pepperoni(PizzaRecipe):
    picture = " 🍕: "

    def __init__(self, size="L"):
        recipe = ["tomato sauce", "mozzarella", "pepperoni"]
        cook_time = 5
        super(Pepperoni, self).__init__("Pepperoni", size, recipe, cook_time)


class Hawaiian(PizzaRecipe):
    picture = " 🍍: "

    def __init__(self, size="L"):
        recipe = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
        cook_time = 7
        super(Hawaiian, self).__init__("Hawaiian", size, recipe, cook_time)


if __name__ == "__main__":
    cli(obj={})
