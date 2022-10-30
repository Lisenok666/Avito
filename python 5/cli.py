import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if delivery:
        click.echo('Work')
    click.echo('Syncing1')


def correct_init(cls):
    def wrapper(name, size):
        if size not in ['L', 'XL']:
            raise ValueError('Size must be L or XL')
        return cls.__call__(name, size)
    return wrapper


@correct_init
class pizza_recipe():
    def __init__(self, name, size):
        self.name = name
        self.size = size


@cli.command()
def menu():
    """Выводит меню"""
    click.echo('- Margherita : tomato sauce, mozzarella, tomatoes')
    click.echo('- Pepperoni : tomato sauce, mozzarella, pepperoni')
    click.echo('- Hawaiian : tomato sauce, mozzarella, chicken, pineapples')


if __name__ == '__main__':
    pizza_recipe('ajks', 'L')
    cli()
