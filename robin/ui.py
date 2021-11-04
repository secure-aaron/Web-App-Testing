import click

"""
This file will hold the styling for our print statements
"""

def success(message): # formats the message put into the function
    click.echo(click.style(str(message), fg="green", bold=True)) # instead of print(), we will use this since its crossplatform way of printing to all terminals with color styling.

def error(message): # formats the message put into the function
    click.echo(click.style(str(message), fg="red", bold=True))  # cast the message to a string in case we try to print a dict

def bar(message): # formats the message put into the function
    click.echo(click.style("-------------------------------------------", fg="green", bold=True)) 



