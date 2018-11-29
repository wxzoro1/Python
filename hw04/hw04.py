# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,x):
        #判断捕获变量
        x = 9 if x == None else  int(x)
        y = int(self.get_argument('n',10))
        if  0<y<10:
            x = y
        #html结构
        html = '''
        <html>
        <body>
        '''
        for a in range(x,0,-1):
            for b in range (a,0,-1):
                if a*b>=10:
                    html += '<td>' + str("%d*%d=%-100d" % (a,b,a*b)) + '&nbsp;&nbsp;' + '</td>'              
                else:
                    html += '<td>' + str("%d*%d=%-100d" % (a,b,a*b)) + '&nbsp;&nbsp;&nbsp;&nbsp;' + '</td>'
            html += '</br>'
        html += '''      
        </body>
        </html>'''
        #写入
        self.write(html)

application = tornado.web.Application([
    (r"/([0-9])?", MainHandler)
    ], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

