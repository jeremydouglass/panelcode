#!/usr/bin/env python
"""
paneler.py
Render panelcode files into image collections

1.  Accepts a list of one or more file paths. Within those paths (recursive):
2.  All text files matching pattern (*.txt by default) are processed

v0.1 2017-09-12
"""

#pylint: disable=line-too-long

## IMPORT

## Python 2-3 compatible code
from __future__ import print_function

from context import panelcode

## argument parsing
import argparse
from argparse import RawDescriptionHelpFormatter
## logging
import logging
## time the script
from datetime import datetime
## file handling, matching, writing
import os
import fnmatch
import csv
## working with lists and indexes
import itertools
import operator
## comparing files and strings
import difflib
import filecmp

## INFO

__author__ = "Jeremy Douglass"
__copyright__ = "copyright 2017"
__license__ = "GPL"
__version__ = "1.6"
__email__ = "jeremydouglass@gmail.com"

## LOGGING

#pylint: disable=logging-format-interpolation
logger = logging.getLogger()  #pylint: disable=invalid-name

## FUNCTIONS

def fname_to_fstr(fname, linebreaks=0, whitespace=0):
    """
    Filename to filestring:
    Take file name, return text contents as string.

    By default filters linebreaks and whitespace.
    """
    with open(fname, "r") as fhandle:
        if linebreaks == 0 and whitespace == 0:
            fstr = " ".join(fhandle.read().split())   ## remove linebreaks and reduce whitespace
        elif linebreaks == 0:
            fstr = fhandle.read().replace('\n', ' ')  ## remove linebreaks only
        elif whitespace == 0:
            fstr = fhandle.read().translate(None, ' \n\t\r')
        else:
            fstr = fhandle.read()
    fhandle.close()
    return fstr

def fnamelist_pairs(fname_list):
    """
    Filename list pairs:
    Takes a filename list; returns a sorted set of filename pair combinations (AB AC AD BC BD CD ....)

    Uses itertools.combinations.
    """
    fpairs = itertools.combinations(sorted(set(fname_list)), 2)
    for fpair in fpairs:
        yield fpair

def fnamelist_to_strgen(fname_list, linebreaks=0, whitespace=0):
    """
    Filename list to string generator:
    Take a list of file names, return a generator of file content strings which will load on-demand.
    """
    for fname in fname_list:
        yield fname_to_fstr(fname, linebreaks, whitespace)

def fpath_to_fnamelist(fpath, fnpattern):
    """
    Filepath to filename list:
    Take a directory and pattern, return a list of file paths.

    fnpattern filters results use Unix shell-style wildcards: (*, ?, [abc], [!abc])
    Uses fnmatch.filter.
    """
    return [os.path.join(dirpath, f)
            for dirpath, _dirnames, files in os.walk(fpath)
            for f in fnmatch.filter(files, fnpattern)]

def fpaths_to_fnamelist(fpaths, filepattern, mergepaths):
    """"
    Filepaths to filename list:
    Accept a list of filepaths, a list of tuples:
        [(path, [filelist]), (path, [filelist])]
    Mergepaths option returns a single tuple:
        [('', [filelist])]

    NOTES:
    Batch wrapper for fpath_to_fnamelist.
    Returns sorted filelists.
    """
    path_fnamelists = []
    filelist = []
    if mergepaths == 1:
        for path in set(fpaths): ## suppress duplicate path processing
            filelist += fpath_to_fnamelist(path, filepattern)  ## combine lists
        path_fnamelists = [('', sorted(filelist))]
    else:
        for path in fpaths:
            filelist = fpath_to_fnamelist(path, filepattern)
            path_fnamelists.append((path, sorted(filelist)))  ## append lists
    return path_fnamelists

def main_logging(args):
    """
    Configure global logger.
    """
    ## SET UP OUTPUT
    outdir = os.path.dirname(args.log)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(args.log)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(console_handler)

def main(args):
    """
    Main loop through comparison filesets -- either per-path or in one merged batch.
    Manages csv file writing and timing.
    """
    main_logging(args)
    logger.info('\n###  '+os.path.basename(__file__)+'  ###')

    ## TIMING
    start_time = datetime.now().replace(microsecond=0)
    logger.info('Start time: {}\n'.format(start_time))

    ## SET UP OUTPUT
    if not os.path.exists(args.outpath):
        os.makedirs(args.outpath)
    outdir = os.path.dirname(args.outputfile)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    csvfile = open(args.outputfile, 'w') ## a/ab = add to existing csv, w/wb = write (clobber) new csv. a/w both py2 and py3 compatible.
    resultwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # resultwriter.writerow(['identical', 'tf-idf', 'sequence', 'jaccard', 'file1', 'file2', 'str1', 'str2', datetime.now()])

    count_total_hits = 0
    path_filelists = fpaths_to_fnamelist(args.inputpaths, args.filepattern, args.mergepaths)
    logger.info('{} path filelists.\n'.format(len(path_filelists)))

    count_hits = 0
    # for filestring in fnamelist_to_strgen(path_filelists)
    for path, filelist in path_filelists:
        logger.info('Filelist:\n{}\n'.format(filelist))
        logger.info('...in path: {}'.format(path))
        logger.info('  {} {} files found'.format(str(len(filelist)), args.filepattern))

        for filename in filelist:
            print('FILENAME: ')
            print(os.path.splitext(filename)[0])
            ## create separate output folder for each file
            fileoutdir = os.path.join(args.outpath,os.path.splitext(os.path.basename(filename))[0])
            print(fileoutdir)
            if not os.path.exists(fileoutdir):
                os.makedirs(fileoutdir)

            test_string = fname_to_fstr(filename, linebreaks=1, whitespace=1)
            # test_string = panelcode.pstr_clean(panelcode_test_string) # strip all kinds of bad behavior
                
            test_string = test_string.replace("~", "0") # replace uncoded page markers as empty pages
            test_string = test_string.replace(";", "\n") # split pages into lines
                
                    ## this function needs to be replaced with pyparser output,
                    ## but temporarily cleaning the input in-place during testing
            
            thumbsfilestring = ""
            try:
                thumbsfilestring = fname_to_fstr(filename+'.thumbs', linebreaks=1, whitespace=1)
                print(thumbsfilestring)
            except:
                pass
            
            if(thumbsfilestring!=""):
                        ## RUN THIS FOR PANELCODE PLUS THUMBNAILS
                panelcode.app_batch_svg(test_string, thumbsfilestring.split('\n'), outpath=fileoutdir)
            else:
                        ## RUN THIS FOR JUST PANELCODE IMAGES
                panelcode.app_batch_svg(test_string, outpath=fileoutdir)

    logger.info('\n' + 'Done.')
    logger.info('Elapsed time: {}'.format(datetime.now().replace(microsecond=0) - start_time))
    logger.info('Output in: {}\n'.format(args.outputfile))
    logger.info('')


## ENTRY POINT

if __name__ == '__main__':

    ## COMMAND LINE ARGUMENT PARSING

    PARSER = argparse.ArgumentParser(description='Simple interface for panelcode. Accepts a path or list of paths and an optional filepattern for panelcode files; optionally copies output into to a new directory.', epilog='EXAMPLE:\n  python '+os.path.basename(__file__)+'-i ./data/ -f "*.txt" -o ./output\n \n', formatter_class=RawDescriptionHelpFormatter)
    PARSER.add_argument('-i', '--inputpaths', nargs='*', default=['./'], help='input source paths for files to compare, default is current directory')   ## e.g.  ['./'] ... or ['./data1/', './data2/']
    PARSER.add_argument('-m', '--mergepaths', default=0, help='all files in all paths')
    PARSER.add_argument('-f', '--filepattern', default="*.panelcode.txt", help='input source path for files')
    PARSER.add_argument('-O', '--outpath', default='./output/', help='results output file')
    PARSER.add_argument('-o', '--outputfile', default='./log/out.txt', help='results output file')
    PARSER.add_argument('-v', '--verbose', default='1', help='verbose mode')
    PARSER.add_argument('-l', '--log', default='./log/'+os.path.basename(__file__)+'.log', help='write log to file')

    CL_ARGS = PARSER.parse_args()

    main(CL_ARGS)
