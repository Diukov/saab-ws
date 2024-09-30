import re
from attribute_parser import parse_attributes

def parse_tag(parser):
    tag_match = re.match(r"<([a-zA-Z0-9]+)([^>]*)>", parser.html[parser.position:])
    end_tag_match = re.match(r"</([a-zA-Z0-9]+)>", parser.html[parser.position:])
    self_closing_match = re.match(r"<([a-zA-Z0-9]+)([^>]*)/>", parser.html[parser.position:])

    if self_closing_match:
        tag_name = self_closing_match.group(1)
        process_self_closing_tag(parser, tag_name)
        parser.position += tag_match.end()

    elif end_tag_match:
        tag_name = end_tag_match.group(1)
        close_tag(parser, tag_name)
        parser.position += end_tag_match.end()

    elif tag_match:
        tag_name = tag_match.group(1)
        attributes = parse_attributes(tag_match.group(2))
        open_tag(parser, tag_name, attributes)
        parser.position += tag_match.end()

    else:
        parser.position += 1

def open_tag(parser, tag_name, attributes):
    if tag_name == "title":
        title_match = re.search(r"<title>(.*?)</title>", parser.html[parser.position:], re.DOTALL)
        if title_match:
            parser.output['title'] = title_match.group(1).strip()
            parser.position += title_match.end()
    elif tag_name in ["h1", "h2"]:
        parser.tags_stack.append(tag_name)
    elif tag_name == "p":
        parser.tags_stack.append("p")
    elif tag_name == "a":
        parser.tags_stack.append({"a": attributes})
    else:
        parser.tags_stack.append(tag_name)

def close_tag(parser, tag_name):
    if parser.tags_stack and (tag_name == parser.tags_stack[-1] or isinstance(parser.tags_stack[-1], dict) and tag_name == "a"):
        parser.tags_stack.pop()
    else:
        pass

def process_self_closing_tag(parser, tag_name):
    if tag_name == "img":
        return
