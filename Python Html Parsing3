from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_tag_attrs(attrs=attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_tag_attrs(attrs=attrs)
    
    def print_tag_attrs(self, attrs):
        [print(f"-> {x[0]} > {x[1]}") for x in attrs]
        
parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(int(input()))]))
