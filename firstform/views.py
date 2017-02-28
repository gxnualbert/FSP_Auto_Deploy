# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime

from TransferFile import TransferFSPFile as tf
from ModifyConfigFile import MofidyFSPFile as mfsp
from StartService import StartService as ss
from log import AddLog as log

from models import modleLogic as mLogic


LINUX_USER='root'
LINUX_PWD='123456'
PORT=22
#set a default package path:/root

b = tf
myMofify = mfsp()

tf.prepareFolder()

logging = log.Log()



def home(request):
    question={'question':'i can not say it,update it'}
    # return render(request,'firstform/index.html',{'question': question['question']})
    return render(request,'firstform/index.html')
def cleanup(request):
        return render(request, 'firstform/cleanup.html')


def dwnPkgAndTar(request):
        request.encoding = 'utf-8'
        pkgurl = request.GET['pkgURL']
        singleip = request.GET['singleIP']
        ipdic={}
        ipdic[singleip]="invalid,ingnore this value"
        mLogic.m_DownPkgAndTar(pkgurl,ipdic,PORT,LINUX_USER,LINUX_PWD)
        # packageName = pkgurl.split("/")[-1]  # sss-1.2.2.1.tar.gz
        # sss = packageName.split(".tar")[0]
        #
        # execmd = "cd /root\nwget " + pkgurl + "\ntar -xzvf " + packageName
        # # get the install package
        # print ("start to get package and tar it on %s", singleip)
        # b.sshclient_execmd(singleip, PORT, LINUX_USER, LINUX_PWD, execmd)
        # print "down successfully and tar it"

        return render(request, 'firstform/downpackageandtar.html')

def submitSingleService(request):

        request.encoding = 'utf-8'
        machine1 = request.GET['machine1']
        servicelist1 = request.GET['servicelist1']

        # get the base path
        sss=mLogic.m_BasePath(machine1,PORT,LINUX_USER,LINUX_PWD)
        machine_service = {}
        machine_service[machine1] = servicelist1
        mLogic.m_InstallService(machine_service, sss, LINUX_USER, LINUX_PWD, PORT)
        return render(request, 'firstform/installsuccessfully.html')

def cleanaction(request):
        request.encoding = 'utf-8'
        cleanip1=request.GET['ip1']
        cleanip2=request.GET['ip2']
        cleanip3=request.GET['ip3']
        cleanip4=request.GET['ip4']
        cleanip5=request.GET['ip5']
        iplist=[cleanip1,cleanip2,cleanip3,cleanip4,cleanip5]
        print iplist
        b = tf
        port=22
        username='root'
        password='123456'
        for ip in iplist:
                # execmd1 = "cd /root\nrm -rf sss*"
                # b.sshclient_execmd(ip, port, username, password, execmd1)
                execmd2 = "cd /\nrm -rf fsmeeting/"
                b.sshclient_execmd(ip, port, username, password, execmd2)
        return render(request, 'firstform/cleansuccessfully.html')


def deployv2(request):
        return render(request, 'firstform/installAllService.html')



def submitallserviceinfo(request):
        t1 = datetime.datetime.now()
        print "start time", t1
        request.encoding = 'utf-8'
        packageURL = request.GET['pkgURL']
        packageName = packageURL.split("/")[-1]  # sss-1.2.2.1.tar.gz
        sss = packageName.split(".tar")[0]  # sss-1.2.2.1
        formdata=request.GET
        formdata=dict(formdata._iterlists())
        del formdata['pkgURL']
        iplist=[]
        servicelist=[]
        dbinfo={}
        for k, v in formdata.iteritems():
                if "ip" in k:
                        for i in v:
                                iplist.append(i)
                if "service" in k:
                        for i in v:
                                servicelist.append(i)
                if "dbHost" in k:
                        dbinfo["dbHost"]=v[0]
                if "dbPort" in k:
                        dbinfo["dbPort"]=v[0]
                if "dbName" in k:
                        dbinfo["dbName"]=v[0]
                if "dbUser" in k:
                        dbinfo["dbUser"]=v[0]
                if "dbPwd" in k:
                        dbinfo["dbPwd"]=v[0]
        machine_service = dict(zip(iplist, servicelist))
        # mLogic.m_DownPkgAndTar(packageURL,machine_service,PORT,LINUX_USER,LINUX_PWD)
        mLogic.m_InstallService(machine_service,sss,LINUX_USER,LINUX_PWD,PORT)
        mLogic.m_SetCondifFile(machine_service,sss,LINUX_USER,LINUX_PWD,PORT,dbinfo)
        mLogic.m_StartService(machine_service,LINUX_USER,LINUX_PWD,PORT)

        t2 = datetime.datetime.now()
        print "end time: ", t2

        tt = t2 - t1

        info = {"totaltime": tt}
        return render(request,'firstform/installsuccessfully.html',info)

def search_form(request):
        return render(request,'firstform/deployinfo.html')


def singleService(request):
        return render(request, 'firstform/installSingleService.html')

def allService(request):
        return render(request, 'firstform/installAllService.html')

