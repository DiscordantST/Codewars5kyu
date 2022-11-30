import re

def domain_name(url):
    search_url = re.match("(https?://)?(www\d?\.)?(?P<name>[\w-]+)", url)
    search_tuple = search_url.groups()
    return search_tuple[2]


