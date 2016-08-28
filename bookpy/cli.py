import os

import click

from .version import __version__
from .bookpy import rename_files


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def get_files(directory, recursive=False):
    for parent, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(parent, f)
        if not recursive:
            raise StopIteration()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
@click.argument('srcs', nargs=-1)
@click.option(
    '-r', '--recursive', is_flag=True,
    help="Get all files recursively from a directory."
)
@click.option(
    '-t', '--template', default=None,
    help="Specify a template with which the books are renamed.\n"
         "Default template is '{short_title} - {main_author} ({year})'"
)
def bookpy(**kwargs):
    """ Renames your e-books for better organization.

    SRCS are the books sources (individual files or a directory).
    If any source is given, the current directory will be taken.
    """
    recursive = kwargs['recursive']
    srcs = kwargs['srcs']
    template = kwargs['template']

    if not srcs:
        srcs = get_files(os.getcwd(), recursive)

    files = []
    for s in srcs:
        if os.path.isdir(s):
            files.extend(get_files(s, recursive))
        else:
            files.append(s)
    rename_files(files, template)
