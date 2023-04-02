class Printer:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ok(values) -> None:
    print(Printer.OKGREEN + values.__str__() + Printer.ENDC)

def fail(values) -> None:
    print(Printer.FAIL + values.__str__() + Printer.ENDC)

def warn(values) -> None:
    print(Printer.WARNING + values.__str__() + Printer.ENDC)
