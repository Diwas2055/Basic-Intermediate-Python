import click

# ! Argument Parsing: Click uses the python decorators for parsing arguments related to a function.

@click.command()
@click.argument('name')
def greeting(name):
    click.echo("Hello, {}".format(name))
  
if __name__=="__main__":
    greeting()
    
# Command :- python index.py Server  
#!   OR  
# Command :- python -m  index Server

# ! Optional arguments: Click gives the option to include optional parameters in the form of flags.

@click.command()
@click.option('--string', default ='World',
        help ='This is a greeting')
def hello(string):
    click.echo("Hello, {}".format(string))
  
if __name__=="__main__":
    hello()    

# Command :- python index.py --string Dinesh    

# ! Optional arguments: Click gives the option to include optional parameters in the form of flags.
# A decorator that is used to validate the input.

@click.command()
@click.option('--string', type=click.Choice(['Dinesh', 'Suresh', 'Ramesh']),
        help ='This is a choice Type')
def hello(string):
    click.echo("Hello, {}".format(string))
  
if __name__=="__main__":
    hello() 

# Command :- python index.py --string Dinesh    
