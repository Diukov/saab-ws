import re

def parse_comment(parser):
    comment_match = re.match(r"<!--(.*?)-->", parser.html[parser.position:], re.DOTALL)
    if comment_match:
        comment_content = comment_match.group(1).strip()
        parser.output['comments'].append(comment_content)
        parser.position += comment_match.end()
    else:
        parser.position += 4
