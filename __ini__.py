import tornado.ioloop
import tornado.web



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("数据出书","test")
        # Response.AddHeader("Access-Control-Allow-Origin", "*");
        self.set_header("Access-Control-Allow-Origin","*");
        # self.set_header("Content-Type","text/html");
        self.write("{'nihao':'hello the wrolr'}")

def make_app():
    # 怎么拦截所有的请求
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()