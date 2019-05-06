from cVisitor import cVisitor
# from cParser import cParser


HEAD_CSS = '''
<link rel=\"stylesheet\" type=\"text/css\" href=\"{}\">
'''


class Org2Html(cVisitor):
    def __init__(self):
        self.html = '<html>'

    def visitCss(self, ctx):
        path = ctx.path().getText()
        self.html = self.html + "<head>" + HEAD_CSS.format(path)

    def visitTitle(self, ctx):
        title = ctx.one().getText()
        if ctx.params():
            a, b = self.visit(ctx.params())
        else:
            a = 'id'
            b = 'xxx'
        title = "<title {}=\"{}\">{}</title></head>".format(a, b, title)
        self.html = self.html + title + '\n'
        print(self.html)

    def visitPara(self, ctx):
        # need return by all level
        return self.visit(ctx.exprlist())

    def visitExpr(self, ctx):
        a = ctx.ID(0).getText()
        b = ctx.ID(1).getText()
        print(a, b)
        return a, b

    def visitHeader1(self, ctx):
        header1 = ctx.one().getText()
        if ctx.params():
            a, b = self.visit(ctx.params())
            self.html += '''<h2 {}="{}">{}</h2>'''.format(a, b, header1)
        else:
            self.html += '''<h2>{}</h2>'''.format(header1)

    def visitHeader2(self, ctx):
        header2 = ctx.one().getText()
        if ctx.params():
            a, b = self.visit(ctx.params())
            self.html += '''<h3 {}="{}">{}</h3>'''.format(a, b, header2)
        else:
            self.html += '''<h3>{}</h3>'''.format(header2)

    def visitHeader3(self, ctx):
        header3 = ctx.one().getText()
        if ctx.params():
            a, b = self.visit(ctx.params())
            self.html += '''<h4 {}="{}">{}</h4>'''.format(a, b, header3)
        else:
            self.html += '''<h4>{}</h4>'''.format(header3)

    def visitCon(self, ctx):
        p = ''
        # ctx.content() is a list
        p += '<br>'.join([i.getText() for i in ctx.content()])
        p = p.replace(' ', '&nbsp;')
        self.html += '''<p id="org11d7e18">{}</p>'''.format(p)

    def visitNewline(self, ctx):
        pass
