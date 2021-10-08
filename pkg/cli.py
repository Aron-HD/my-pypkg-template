import logging
import click
from pkg.subpkg.submodule import ClassName

log = logging.getLogger(__name__)


@click.command()
@click.option(
    '-p', '--path',
    required=True,
    show_default=True,
    default='logs',
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True,
        resolve_path=True
    ),
    help="The directory or file you wish to operate on.",
)
def cli(path):
    """
    Click command line pkg.
    """
    log.debug('\n\n# New run\n')
    log.info(f'cli input: {path}')
    res = ClassName.do_something(1)
    click.echo(click.style(res, fg="yellow"))
