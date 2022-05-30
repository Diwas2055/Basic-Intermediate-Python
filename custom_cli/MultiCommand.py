import click
import os

# Creating a path to the folder where the commands are stored.
plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

# It's a subclass of click.MultiCommand that allows you 
# to create a CLI with multiple subcommands
class MyCLI(click.MultiCommand):

    """
    It returns a list of all the files in the plugin folder, minus the .py extension
    
    :param ctx: The context as the command was invoked. This is the only required parameter
    :return: A list of all the files in the plugin folder that end in .py and are not __init__.py
    """
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """
        It reads the file named `name.py` in the `plugin_folder` directory, compiles it, and returns the
        `cli` function defined in the file
        
        :param ctx: The context object that is passed to the command
        :param name: The name of the command
        :return: The function that is being returned is the cli function.
        """
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')

if __name__ == '__main__':
    cli()
    

# A decorator that is used to create a command line interface.
@click.command(cls=MyCLI)
def cli():
    pass