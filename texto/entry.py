import click

@click.group()
def cli():
    pass

@click.command()
def install():
    """Installation des dépendances."""
    import os
    click.echo('Installation en cours...')
    os.system('python -m spacy download fr_core_news_md')
    click.echo('Installation réussie !')

@cli.command()
def hello():
    """Juste pour vous dire bonjour."""
    click.echo('Hello!')

cli.add_command(install)
cli.add_command(hello)

if __name__ == '__main__':
    cli()