import click


# A decorator that tells click that this function is a command line group.
@click.group()
def cli():
    pass

@cli.group()
def lunch():
    pass

@cli.group()
def dinner():
    pass

@click.command()
def burger():
    click.echo("I am a burger")


# Adding the burger command to both lunch and dinner.
lunch.add_command(burger)
dinner.add_command(burger)


if __name__=="__main__":
    cli()