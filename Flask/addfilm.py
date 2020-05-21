import click

@click.command()
@click.option("--film-name")
@click.option("--stars")

def addfilm(film_name, stars):
    with open("filmreviews.txt", 'a') as f:
        f.write(film_name + ', ' + stars + '\n')
        f.close()

addfilm()