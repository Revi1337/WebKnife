import argparse

def logo():
    print("""
     _  _  _ _______ ______       _     _ __   _ _____ _______ _______
     |  |  | |______ |_____]      |____/  | \  |   |   |______ |______
     |__|__| |______ |_____]      |    \_ |  \_| __|__ |       |______
     
                                                
                                                @Author: revi1337
                                                
    """)

def set_global_options(parser):
    global_options = parser.add_argument_group('Global options')
    # global_options.add_argument('-r', '--radius', type=int, required=True, help='radius of the circle')
    global_options.add_argument('-u', dest='url', metavar='URL', type=str, help='Domain or URL')
    global_options.add_argument('-w', dest='wordlist', metavar='WORDLIST', type=str, help='specify entering valid, unexpected or random data wordlist')
    global_options.add_argument('-X', dest='method', metavar='METHOD', nargs='?', type=str, default='get', help='http method (Default: GET)')
    global_options.add_argument('-b', dest='cookies', nargs='?',
                                action=type('',
                                            (argparse.Action,),
                                            dict(__call__=lambda a, p, n, v, o: getattr(n, a.dest).update(dict([v.split('=')])))
                                            ),
                                default={},
                                help='Cookie Values. (ex. {"cookie1": "cookie1 Value"} )')
    global_options.add_argument('-H', dest='headers', nargs='?',
                                action=type('',
                                            (argparse.Action,),
                                            dict(__call__=lambda a, p, n, v, o: getattr(n, a.dest).update(dict([v.split('=')])))
                                            ),
                                default={},
                                help='Header Values. (ex. {"Header1": "Header1 Value"} )')
    global_options.add_argument('-k', dest='verify_ssl', action='store_true', help='skip ssl certificate')
    return global_options


def parse_arguments():
    logo()
    parser = argparse.ArgumentParser()

    #####################################################################################################################
    # Set Sub Command
    sub_command = parser.add_subparsers(dest = 'sub_commands', title='Sub Command', description='available subcommands (least of one must me specified)', required=True, help='asdf')

    # Set Global Options
    set_global_options(parser)

    #####################################################################################################################
    # Discovery SubCommand Options
    discovery = sub_command.add_parser('discovery', help='Discovery Web Contents')

    set_global_options(discovery)
    filter_options = discovery.add_argument_group('Discovery Options')
    filter_options.add_argument('-fc', dest='fstatus', metavar='CODE', nargs='?', type=int, action='append', help='filter response status code.    (can multiple manipulate ex. -fs 404 -fs 400)')
    filter_options.add_argument('-fs', dest='fsize', metavar='SIZE', nargs='?', type=int, action='append', help='filter response size    (can multiple manipulate ex. -fc 0 -fc 1234)')
    filter_options.add_argument('-mc', dest='mstatus', metavar='CODE', nargs='?', type=int, action='append', help='match response status code    (can multiple manipulate ex. -mc 200 -mc 301)')
    filter_options.add_argument('-ms', dest='msize', metavar='SIZE', nargs='?', type=int, action='append', help='match response size    (can multiple manipulate ex. -ms 222)')
    filter_options.add_argument('--find-string', dest='find_string', metavar='TEXT', help='find a string contained in response.')
    filter_options.add_argument('--regex', dest='regex', metavar='REGEX', help='find a string match with regular expression.')

    #####################################################################################################################
    # Fuzz SubCommand Options
    fuzz = sub_command.add_parser('fuzz', help='Entering valid, unexpected or random data')

    set_global_options(fuzz)

    #####################################################################################################################
    # LFI SubCommand Options

    lfi = sub_command.add_parser('lfi', help='Local File Inclusion Injector')
    set_global_options(lfi)

    lfi_options = lfi.add_argument_group('LFI Options')
    lfi_options.add_argument('-p', metavar='PARAM', help='Parameter')
    lfi_options.add_argument('--encode', help='Select Encoding Data')
    lfi_options.add_argument('--depth', choices=[1,2,3,4,5,6], help='Encoding Depth')

    #####################################################################################################################

    return parser.parse_args(), parser


if __name__ == '__main__':
    parse_arguments()
