from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
          if "\n" in data:
              print(">>> Multi-line Comment\n%s"%data)
          else:
              print(">>> Single-line Comment\n%s"%data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data\n%s"%data)
          
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
