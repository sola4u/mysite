'''
Created on 2013-11-21
@author: yihaomen.com
'''
from django.utils.html import escape, strip_tags, remove_tags

html_content = """
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <script>alert("test")</script>
    <title>yihaomen.com test</title>
    <link href="/static/css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
     content
    </body>
    </html>
"""

def escape_html(html):
    return escape(html);

def stript_all_tags(html):
    return strip_tags(html)

def remove_part_tags(html,tags):
    return remove_tags(html, tags)

if __name__ == '__main__':
    print("====escape all tags======")
    print(escape_html(html_content))
    print("====remove all tags======")
    print(strip_tags(html_content))
    print("===remove part tags.=====")
    print(remove_part_tags(html_content,"script html body"))

