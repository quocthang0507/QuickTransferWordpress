from termcolor import cprint
from urllib.parse import urljoin, urlsplit


def print_red(x: str): return cprint(x, 'red')


def print_blue(x): return cprint(x, 'blue')


def get_host_name(url: str):
    return "{0.scheme}://{0.netloc}/".format(urlsplit(url))
