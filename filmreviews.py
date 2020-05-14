import click

@click.command()
@click.option("--filmname")
@click.option("--stars")
def addfilm(filmname, stars):
    with open("filmreviews.txt", 'a') as f:
        f.write(filmname + ', ' + stars + '\n')
        f.close()

addfilm()