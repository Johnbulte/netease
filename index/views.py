from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def index_views(request):
    return HttpResponse('这是网站的首页')


def login_views(request):
    return HttpResponse('这是首页中的login访问路径')


def register_views(request):
    return HttpResponse('这是首页中的register访问路径')


# getTemp的视图处理函数
def getTemp_views(request):
    # 1.通过loader加载模板
    t = loader.get_template('01_template.html')
    # 2.将模板转换为字符串
    html = t.render()
    # 3.将字符串响应给客户端
    return HttpResponse(html)


def getTemp1_views(request):
    return render(request, '02_template.html')


def var_views(request):
    # 声明变量字典
    # dic = {
    #     'uname':'殷素素',
    #     'uage':'23',
    #     'hobby':'张翠山',
    # }
    # return render(request,'03_var.html',dic)
    l = ['金毛狮王', '白眉鹰王', '青翼蝠王', '东海龙王']
    t = ('潘金莲', '西门庆', '武大郎')
    dic = {'shz': '水浒传', 'xyj': '西游记', 'hlm': '红楼梦'}
    f = fun(35, 53)
    dogs = Dog()
    print(locals())
    # vars = {
    #     'num':'15',
    #     'str':'模板中的字符串变量',
    #     'tup':t,
    #     'list':l,
    #     'dic':dic,
    # }
    return render(request,'03_var.html',locals())


def fun(num1, num2):
    return num1 + num2


def static_views(request):
    return render(request,'04_static.html')


def show_views(request):
	return HttpResponse('这是音乐中的show视图')



def temp_views(request):
	return render(request,"05_temp.html")


class Dog(object):
    name = '阿拉斯加'

    def eat(self):
        return '吃狗粮'
