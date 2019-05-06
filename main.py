import sys
from antlr4 import CommonTokenStream, FileStream
from antlr4.InputStream import InputStream
from cLexer import cLexer
from cParser import cParser
from org2html import Org2Html

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = cLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = cParser(token_stream)
    tree = parser.org()

    visitor = Org2Html()
    visitor.visit(tree)

    html = visitor.html + '</html>'

    print(html)
    f = '{}.html'.format(''.join(sys.argv[1].split('.')[:-1]))
    with open(f, 'w') as f:
        f.write(html)
