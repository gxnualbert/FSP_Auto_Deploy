#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.context_processors import csrf
# Create your views here.
def hello(request):
    question={'question':'i can not say it,update it'}
    # return render(request,'firstform/index.html',{'question': question['question']})
    return render(request,'firstform/index.html',question)

def search(request):
        request.encoding='utf-8'
        # if 'ice_master' in request.GET:
        #     ice_master = request.GET['ice_master'].encode('utf-8')
        # elif 'ice_replica' in request.GET:
        #     ice_replica = request.GET['ice_replica'].encode('utf-8')
        # elif 'manager' in request.GET:
        #     manager = request.GET['manager'].encode('utf-8')
        # elif 'access1' in request.GET:
        #     access1 = request.GET['access1'].encode('utf-8')
        # elif 'access2' in request.GET:
        #     access2 = request.GET['access2'].encode('utf-8')
        # elif 'nginx' in request.GET:
        #     nginx =request.GET['nginx'].encode('utf-8')
        # elif 'av' in request.GET:
        #     av =request.GET['av'].encode('utf-8')
        # elif 'vnc' in request.GET:
        #     vnc =request.GET['vnc'].encode('utf-8')
        # elif 'whiteboard' in request.GET:
        #     whiteboard =request.GET['whiteboard'].encode('utf-8')
        #
        # else:
        #     message = '你提交了空表单'

        ice_master = request.GET['ice_master'].encode('utf-8')
        ice_replica = request.GET['ice_replica'].encode('utf-8')
        manager = request.GET['manager'].encode('utf-8')
        access1 = request.GET['access1'].encode('utf-8')
        access2 = request.GET['access2'].encode('utf-8')
        nginx =request.GET['nginx'].encode('utf-8')
        av =request.GET['av'].encode('utf-8')
        vnc =request.GET['vnc'].encode('utf-8')
        whiteboard =request.GET['whiteboard'].encode('utf-8')
        msg = {}
        msg['ice_master']=ice_master
        msg['ice_replica']=ice_replica
        msg['manager']=manager
        msg['access1']=access1
        msg['access2']=access2
        msg['nginx']=nginx
        msg['av']=av
        msg['vnc']=vnc
        msg['whiteboard']=whiteboard

        return render(request,'firstform/search.html',{'confInfo':msg})
        # return HttpResponse(message)

def search_form(request):
        return render(request,'firstform/search_form.html')


# 接收POST请求数据
# def search_post(request):
# 	ctx ={}
# 	ctx.update(csrf(request))
# 	if request.POST:
# 		ctx['rlt'] = request.POST['q']
# 	return render(request, "post.html", ctx)