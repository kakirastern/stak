#!/usr/bin/env python
import os
import shutil
import sys
import tempfile
from . import version

try:
    from urllib.request import urlopen
except ImportError:
    # Python 2.x compat
    from urllib import urlopen

CFG = dict(name='stak-notebooks',
           repo='https://github.com/spacetelescope',
           rev=version.__version__,
           ext='.tar.gz')

def download(url, destdir):
    bsize = 4096
    filename = os.path.join(destdir, os.path.basename(url))

    with open(filename, 'w+b') as ofp:
        with urlopen(url) as data:
            chunk = data.read(bsize)
            while chunk:
                ofp.write(chunk)
                chunk = data.read(bsize)

    return filename


def main():
    import argparse
    global verbose

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--latest', action='store_true', help='Ignore current release and download the latest available')
    parser.add_argument('-o', '--output-dir', action='store', type=str, default='.')
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing notebook directory')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    if args.latest:
        CFG['rev'] = 'master'

    verbose = args.verbose
    args.output_dir = os.path.abspath(args.output_dir)
    expected = os.path.abspath(os.path.join(args.output_dir, '-'.join([CFG['name'], CFG['rev']])))

    if os.path.exists(expected) and not args.force:
        print('{} exists.\nUse --force to overwrite.'.format(expected), file=sys.stderr)
        exit(1)

    with tempfile.TemporaryDirectory() as tdir:
        url = '/'.join([CFG['repo'], CFG['name'], 'archive', CFG['rev'] + CFG['ext']])

        if verbose:
            print('Retrieving {}'.format(url))

        archive = download(url, tdir)

        if verbose:
            print('Unpacking {} to {}'.format(archive, args.output_dir))

        shutil.unpack_archive(archive, args.output_dir)




