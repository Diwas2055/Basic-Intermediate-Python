import click

@click.command
@click.option('--name', default='World', help='The greeting')
def cli(name):
    click.echo('Hello, {}!'.format(click.get_current_context().params['name']))
    
    
# It installs the current directory as an editable package.
# pip install --editable .    