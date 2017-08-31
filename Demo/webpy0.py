# coding=utf-8
import web

urls = (
    '/index','index', #URL完全匹配
    '/blog/\d+','blog', #URL模糊匹配
    '/(.*)', 'hello', #URL带组匹配，放最后
)
# 请求参数获取 web.input()
# 请求头获取 web.ctx.env
# 模板文件读取 render.index("参数")
# 结果数据获取 model.select("sql")
# URL跳转 web.seeother("/")
app = web.application(urls, globals())
class index:
    def GET(self):
        query = web.input()
        return query

class blog:
    def GET(self):
        return 'blog'
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        return web.ctx.env

class hello:
    def GET(self,name):
        return open(r'1.html').read()


if __name__ == "__main__":
    app.run()
