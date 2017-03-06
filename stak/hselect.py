"""
Hselect class, use to collate FITS header information

"""

# STDLIB
from six import iteritems, string_types
import operator
import argparse
import pyparsing as pyp

# THIRD-PARTY
import numpy as np
from stsci.tools import parseinput
from astropy.io import fits
from astropy.table import Table


__all__ = ['Hselect']


class Hselect(object):
    """Hselect is a hselect IRAF replacement.  You can use Hselect on a
    collection of FITS files to pull out selected header keywords and save
    them to an astropy table.  You can also pre-filter the table results using
    an assertion expression on the keyword values.

    Parameters
    ----------
    filename_list : string or iterable
        String of filename(s), comma separated. Can also provide an iterable
        with individual filename strings. Can use wildcards and IRAF file
        syntax. ex: "file1.fits,file2.fits" or ("file1.fits","file2.fits")

    keywords : string
        String of comma separated keywords to search for in headers, Can use
        the `*` wildcard character. ex: "DATE-OBS, NAXIS*"

    extension : tuple, optional
        Tuple of requested header extensions to search. Default is empty tuple,
        which will search all header extensions.

    expression : string, optional
        Assertion expression to evaluate keyword values for inclusion in final
        table.  This can include combination of expressions using "AND" and
        "OR" (not case sensitive), and each evaluation can be one of the set
        (=,>=,<=,>,<).  Can use parenthesis to denote order of evaluation.
        ex: "BUNIT='ELECTRONS' OR BUNIT='ELECTRONS/SECOND'")


    Attributes
    ----------
    table : Astropy Table
        The Astropy Table that stores the header search results.  If a
        searched header does not contain the desired header keyword, that
        value will be masked in the output Table, denoted by a '-'.

    Examples
    --------
    ::

        $ myObj = Hselect("*.fits","BUNIT,TIME-OBS",extension=(0,1,2,3),
                          expression="BUNIT='ELECTRONS'")

        $ myObj = Hselect("jcz8*raw.fits","BUNIT,TIME-OBS",
                          expression="BUNIT='ELECTRONS' AND
                          (TIME-OBS < 10 OR TIME-OBS > 100")
    """

    def __init__(self, filename_list, keywords, extension=(),
                 expression="None"):
        """
        set initial parameters, call class functions for preforming selection
        and formatting to masked astropy table.

        """

        self.filename_list = parseinput.parseinput(filename_list)[0]
        self.final_key_dict = {}
        self.keyword_list = keywords.split(",")
        self.final_key_set = set()

        if not isinstance(extension, tuple):
            raise ValueError("extension parameter must be a tuple")
        self.extension = extension
        if self.extension == ():
            self.all_ext = True
        else:
            self.all_ext = False

        self.expr = expression
        self.table = Table()

        self._select()
        self._dict_to_table()

    def _select(self):
        """Perform hselect like query on provided file names, inputs were
        setup in init, and output is stored in self.final_key_dict
        """

        # loop through all files, find requested keywords
        for filename in self.filename_list:
            with fits.open(filename) as hdulist:

                if self.all_ext:
                    self.extension = range(len(hdulist))

                for ext in self.extension:

                    try:
                        header = hdulist[ext].header
                    except IndexError:
                        continue
                    outer_key = '{}-{}'.format(filename, ext)

                    # check for expressions, will not make dictionary entry if
                    # expression false would be nice to use interpreter
                    # pattern here for more advanced expressions, but for now
                    # I'll stick with just 'AND's. check is expr is valid only
                    # once, earlier in code.

                    if self.expr != "None" and not depth_parse(
                            expr_pyparse(self.expr), header):
                        continue

                    self.final_key_dict[outer_key] = {}

                    for search_keyword in self.keyword_list:
                        # have to do regular expression matching for keywords
                        if '*' in search_keyword:
                            matches = wildcard_matches(header, search_keyword)
                            for match in matches:
                                self.final_key_dict[outer_key][match] = \
                                    header[match]

                                self.final_key_set.add((match,
                                                        type(header[match])))

                        else:
                            if search_keyword in header:
                                self.final_key_dict[outer_key][search_keyword]\
                                    = header[search_keyword]
                                self.final_key_set.add((
                                    search_keyword,
                                    type(header[search_keyword])))

                    if not self.final_key_dict[outer_key]:
                        del self.final_key_dict[outer_key]

                hdulist.close()


    def _dict_to_table(self):
        """Format the final dictionary of keyword matches into a masked
        astropy table.

        """

        # need to setup all numpy arrays first, then put into table, adding
        # columns is apparently slow
        file_ext_list = self.final_key_dict.keys()
        num_rows = len(file_ext_list)
        final_keyword_list = list(self.final_key_set)

        array_list = [[elem.split('-')[0] for elem in file_ext_list],
                      [int(elem.split('-')[1]) for elem in file_ext_list]]
        col_names = ['Filename', 'Ext']
        data_types = ['S80', int]
        # the bool mask array list will be off by index of 2
        mask_list = []
        dumb_indx_dict = {}

        # make initial empty data and bool arrays
        for indx, key_tuple in enumerate(final_keyword_list):
            # make dumb keyword index dict, probably a better way to do this
            dumb_indx_dict[key_tuple[0]] = indx
            if key_tuple[1] == str:
                data_type = 'S68'
            else:
                data_type = key_tuple[1]

            array_list.append(np.zeros(num_rows, dtype=data_type))
            mask_list.append(np.ones(num_rows, dtype=bool))
            col_names.append(key_tuple[0])
            data_types.append(data_type)

        # now fill in arrays and mask arrays
        for indx, efile in enumerate(file_ext_list):
            for (ikeyword, value) in iteritems(self.final_key_dict[efile]):
                ikeyword_indx = dumb_indx_dict[ikeyword]
                array_list[ikeyword_indx+2][indx] = value
                mask_list[ikeyword_indx][indx] = False

        # put arrays and masks together into one masked array
        for indx, mask_arr in enumerate(mask_list):
            array_list[indx+2] = np.ma.array(array_list[indx+2], mask=mask_arr)

        # put everything into an astropy table
        self.table = Table(array_list, names=tuple(col_names),
                           dtype=tuple(data_types))
        self.table.sort(['Filename', 'Ext'])


def eval_keyword_expr(list_expr, header):
    """Translate the input string expression into True or False on given header.
    This function takes the smallest chunk of the expression in a list format,
    i.e. [keyword, operator, value].

    Parameters
    ----------
    list_expr : list
        a list of three elements, keyword, operator, value

    header : fits header
        input header to test keyword value against

    Returns
    -------
    boolean : boolean

    """

    operator_dict = {'=': operator.eq, '<': operator.lt, '<=': operator.le,
                     '>': operator.gt, '>=': operator.ge}

    if len(list_expr) == 3:
        eval_function = operator_dict[list_expr[1]]

        # check for keyword
        if list_expr[0] not in header.keys():
            return False

        # turn value to float if not string, if string strip extra quotes
        if list_expr[2][0] == '"' and list_expr[2][-1] == '"':
            right_side = list_expr[2].lstrip('"').rstrip('"')
        elif list_expr[2][0] == "'" and list_expr[2][-1] == "'":
            right_side = list_expr[2].lstrip("'").rstrip("'")
        else:
            right_side = float(list_expr[2])

        # now check condition
        return eval_function(header[list_expr[0]], right_side)
    else:
        # should add exception catching here
        return False


def wildcard_matches(header, wildcard_key):
    """Take wildcard keyword and return all keyword name matches found in
    header. Throwing out COMMENT and HISTORY cards.

    Parameters
    ----------
    header : header object

    wildcard_key : str

    Returns
    -------
    matches : list
    """

    header_keys = header.keys()
    if 'COMMENT' in header_keys:
        header_keys.remove('COMMENT')
    if 'HISTORY' in header_keys:
        header_keys.remove('HISTORY')
    matches = header[wildcard_key].keys()
    return matches


def expr_pyparse(full_expr):
    """
    Run the full string evaluation expression through initial parsing.
    This should be some combination of AND,ORs using appropriate parenthesis,
    and the evaluation statement should looks like so: KEYWORD = "value" for
    strings, KEYWORD = value for integer/float values.  Example of full
    expression: "(BUNIT = 'UNITLESS' and NAXIS1 = 1014) OR BUNIT='ELECTRONS/S'"
    Can use lower or upper case for or/and argument, and spaces around
    operators not required.

    Parameters
    ----------
    full_expr : string

    Returns
    -------
    list
        nested list of expression elements, where inner list has
        [keyword, operator, value]

    """

    # Setup "word" patterns
    and_ = pyp.CaselessLiteral('and')
    or_ = pyp.CaselessLiteral('or')
    keyword = pyp.Word(pyp.alphanums+'_'+'-')
    value = (pyp.Word(pyp.nums + '.') | pyp.Word(pyp.alphanums + "'" + '"'))
    expr = pyp.Word('=<>')

    searchTerm = pyp.Group(keyword + expr + value)
    searchExpr = pyp.operatorPrecedence(searchTerm,
                                        [(and_, 2, pyp.opAssoc.LEFT),
                                         (or_, 2, pyp.opAssoc.LEFT)])
    # change this to catch exception, this is most likely where parsing
    # exception will happen from bad user input
    return searchExpr.parseString(full_expr, parseAll=True).asList()


def depth_parse(input_list, header):
    """Take an input nested list built from pyparsing and deconstruct
    recursively to evaluate expressions.

    Parameters
    ----------
    input_list: nested list

    header: fits header
        fits header to evaluate expression on

    Returns
    -------
    result : boolean
    """

    bool_dict = {'and': operator.and_, 'or': operator.or_}

    # first pass from pyparse output will be single element list
    if len(input_list) == 1:
        return depth_parse(input_list[0], header)
    # list should have three elements, if inner elements also list, use boolean
    # parsing
    elif (len(input_list) == 3) and (isinstance(input_list[0], list)):
        bool_func = bool_dict[input_list[1]]
        result = bool_func(depth_parse(input_list[0], header),
                           depth_parse(input_list[2], header))
        return result
    # list should have three elements, if inner elements strings, use keyword
    # evaluation
    elif (len(input_list) == 3) and (isinstance(input_list[0], string_types)):
        return eval_keyword_expr(input_list, header)
    else:
        raise ValueError("no deconstruction match found for list: {}".format(
            input_list))


def main(args=None):

    parser = argparse.ArgumentParser(description='''Select and print FITS
    header keywords to the screen. Works like IRAF Hselect.''',
                                     epilog='''Examples:
        $hselect hselect *.fits BUNIT,TIME-OBS
        $hselect file1.fits NAXIS1 -e 1,2 -x 'NAXIS1=1014 AND BUNIT="SECONDS"' ''',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', nargs='+', help='''Name(s) of FITS files to
        search. Arguments can be multiple white-space separated filenames.
        Wildcard characters and IRAF filename syntax is accepted.''')
    parser.add_argument('keywords', help='''Requested keyword(s) for output
        table, comma separated, no spaces. The '*' wildcard is also accepted.''')
    parser.add_argument('-e', '--ext', help='''Extension number(s) to search,
        comma separated, no white-space. Defaults to all.''')
    parser.add_argument('-x', '--expression', help='''Assertion expression to
        run on the output table, The expression can be defined using
        =,>,<,>=,<= operators in a "keyword operator value" combination. These
        inner expressions can then be combined using AND/OR
        (case insensitive). Enclose your full expression in quotes, and any
        string values in the alternate quote style ` or ". If necessary, use
        parenthesis to notate order of evaluation.''')

    try:
        parsed = parser.parse_args()

        if parsed.ext:
            extension_list = parsed.ext.split(',')
            # attempt to change input extensions names to ints
            for i, elem in enumerate(extension_list):
                try:
                    extension_list[i] = int(elem)
                except ValueError:
                    continue

        if parsed.ext and parsed.expression:
            hsel = Hselect(parsed.filename, parsed.keywords,
                           extension=tuple(extension_list),
                           expression=parsed.expression)

        elif parsed.ext and not parsed.expression:
            hsel = Hselect(parsed.filename, parsed.keywords,
                           extension=tuple(extension_list))

        elif not parsed.ext and parsed.expression:
            hsel = Hselect(parsed.filename, parsed.keywords,
                           expression=parsed.expression)

        else:
            hsel = Hselect(parsed.filename, parsed.keywords)

        print(hsel.table)

    except SystemExit:
        pass
