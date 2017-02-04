#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.context_processors import csrf
# Create your views here.
import datetime,time
import sys,os

import logging
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

        t1 = datetime.datetime.now()
        print "start time", t1

        hostname = "192.168.153.129"
        port = 22
        username = 'root'
        password = '123456'
        basePath = "/fsmeeting/sss"

        # #download package and install

        # '''download the package from the url'''
        packageURL = "http://192.168.5.30:8080/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_sss/lastSuccessfulBuild/artifact/sss-1.2.2.1.tar.gz"
        packageName = packageURL.split("/")[-1]  # sss-1.2.2.1.tar.gz
        sss = packageName.split(".tar")[0]  # sss-1.2.2.1

        # sss = "sss-1.2.2.1"

        # DB info
        dbHost = "192.168.7.105"
        dbPort = "3306"
        dbName = "fsp_sss"
        dbUser = "root"
        dbPwd = "123456"

        # Access config info
        ACTCPPort = "1089"
        ACUDPPort = "1089"
        ACServiceInstanceID = "access_instance_1"
        ACServiceInstancePassword = "access_instance_fsp"
        HTTPServiceListenPort = "3000"
        AccessMasterIP = "192.168.153.128"
        AccessMasterPort = "1089"
        HTTP2ServicePort = "3000"

        # ICEMaster config Info
        ICEMasterIP = ice_master
        ICEMasterPort = "10000"

        # ICEReplicaInfo
        ICEReplicaIP = ice_replica
        ICEReplicaPort = "10001"

        ManagerIP = manager
        ManagerPort = "1089"
        ManagerServiceIPv4Addr = "TCP:" + ManagerIP + ":" + ManagerPort

        # av config info
        AVIP = av
        AVTCPPort = "1089"
        AVUDPort = "1089"
        AVInstanceGroupID = "1"
        AVServiceInstanceID = "av_instance_1"
        AVServiceInstancePassword = "av_instance_fsp"

        # vnc config info
        VNCIP = vnc
        VNCPort = "1091"
        VNCTCPPort = "1089"
        VNCUDPPort = "1089"
        VNCInstanceGroupID = "0"
        VNCServiceInstanceID = "vnc_instance_1"
        VNCServiceInstancePassword = "vnc_instance_fsp"

        WhiteBoardIP = whiteboard
        WhiteBoardPort = "1093"

        WBTCPPort = "1089"
        WBUDPort = "1089"
        WBInstanceGroupID = "1"
        WBServiceInstanceID = "white_board_instance_1"
        WBServiceInstancePassword = "white_board_instance_fsp"

        accessIP1 = access1
        accessPort1 = "10000"
        accessIP2 = access2
        accessPort2 = "10001"
        ListenPort = "22222"














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