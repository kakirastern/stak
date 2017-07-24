#!/usr/bin/env python
import atexit
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
           ext='.tar.gz',
           tmpdir='',
           verbose=False)


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


@atexit.register
def cleanup():
    tmpdir = CFG['tmpdir']
    if tmpdir and os.path.exists(tmpdir):
        if CFG['verbose']:
            print('Removing {}'.format(tmpdir))
        shutil.rmtree(tmpdir)


def main():
    import argparse
    global CFG
    global verbose

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--latest', action='store_true', help='Ignore current release and download the latest available')
    parser.add_argument('-o', '--output-dir', action='store', type=str, default=os.curdir)
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing notebook directory')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    CFG['verbose'] = args.verbose

    # Pull from HEAD (only useful for active development)
    if args.latest:
        CFG['rev'] = 'master'

    # If the user issues an output directory, create the directory if it does not exist
    args.output_dir = os.path.abspath(args.output_dir)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, mode=0o755)

    # Do not clobber existing notebooks if they exist
    expected = os.path.abspath(os.path.join(args.output_dir, '-'.join([CFG['name'], CFG['rev']])))
    if os.path.exists(expected) and not args.force:
        print('{} exists.\nUse --force to overwrite.'.format(expected), file=sys.stderr)
        exit(1)

    # Create temporary directory and store location in configuration
    CFG['tmpdir'] = tempfile.mkdtemp()

    # Compile URL
    url = '/'.join([CFG['repo'], CFG['name'], 'archive', CFG['rev'] + CFG['ext']])

    # Download archive to temp directory
    if CFG['verbose']:
        print('Retrieving {}'.format(url))
    archive = download(url, CFG['tmpdir'])

    # Extract archive in temp directory
    if CFG['verbose']:
        print('Unpacking {} to {}'.format(archive, args.output_dir))
    shutil.unpack_archive(archive, args.output_dir)

    # NOTE: cleanup() callback method deletes temporary directory


if __name__ == '__main__':
    main()
