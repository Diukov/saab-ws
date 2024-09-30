import re
from html import unescape

def parse_attributes(attributes_string):
    attr_matches = re.findall(r'([a-zA-Z]+)="(.*?)"', attributes_string)
    return {key: unescape(value) for key, value in attr_matches}
