from beerlog.core import add_beer_to_database
import typer


main = typer.Typer(help="Beer Management Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to the database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 Beer added!!!")
    else:
        print("🚨 - Cannot add beer.")


@main.command("list")
def list_beers(style: str):
    """List beers in database"""
    print(style)
