#Archivo de entrada

import click
from clients import commands as clients_commands

CLIENTS_TABLE = ".clients.csv"

#declarar que esta sera la entrada
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj["clients_table"] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
