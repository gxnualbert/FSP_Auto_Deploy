#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.context_processors import csrf
# Create your views here.
import datetime,time
import sys,os
from TransferFile import TransferFSPFile as tf
from ModifyConfigFile import MofidyFSPFile as mfsp
from StartService import StartService as ss
from log import AddLog as log
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

        ice_master = request.GET['myicemaster'].encode('utf-8')
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

        execmd = "cd /root\nwget " + packageURL + "\ntar -xzvf " + packageName
        b = tf

        tf.prepareFolder()
        # sys.exit()

        # logger.addHandler(zlg_log)
        # logging.info("start to download package and tar it")
        # tf.sshclient_execmd(hostname, port, username, password, execmd)
        # logging.info("finished download package and tar it")

        logging = log.Log()
        # install service


        logging.info("start to install access")
        ipList = ""
        serviceList = ""
        for i in range(len(ipList)):
                hostname = ipList[i]
                for j in range(len(serviceList)):
                        if "access" in serviceList[i]:
                                b.installAccess(hostname, port, username, password, sss)
                                logging.info("start to install av")
                        if "av" in serviceList[i]:
                                b.installAv(hostname, port, username, password, sss)
                                logging.info("start to install ice_master")
                        if "ice_master" in serviceList[i]:
                                b.installIceMaster(hostname, port, username, password, sss)
                                logging.info("start to install ice_replica")

                        b.installIceReplica(hostname, port, username, password, sss)
                        logging.info("start to install manager")
                        b.installManager(hostname, port, username, password, sss)
                        logging.info("start to install vnc")
                        b.installVnc(hostname, port, username, password, sss)
                        logging.info("start to install whiteboard")
                        b.installWhiteboard(hostname, port, username, password, sss)
                        logging.info("start to install nginx")
                        b.installNginx(hostname, port, username, password)

        # download config file
        logging.info("start to download access config file")
        b.transferAccessFile(hostname, port, username, password, basePath)
        logging.info("start to download av config file")
        b.transferAvFile(hostname, port, username, password, basePath)
        logging.info("start to download ice_master config file")
        b.transferMasterFile(hostname, port, username, password, basePath)
        logging.info("start to download ice_replica config file")
        b.transferReplicaFile(hostname, port, username, password, basePath)
        logging.info("start to download manager config file")
        b.transferManagerFile(hostname, port, username, password, basePath)
        logging.info("start to download vnc config file")
        b.transferVncFile(hostname, port, username, password, basePath)
        logging.info("start to download white board config file")
        b.transferWBFile(hostname, port, username, password, basePath)

        # modify config file
        myMofify = mfsp()
        logging.info("start to modify access config file")
        myMofify.modifyAccessConfigFile(ACTCPPort, ACUDPPort, ACServiceInstanceID, ACServiceInstancePassword,
                                        HTTPServiceListenPort, ManagerServiceIPv4Addr, ICEMasterIP, ICEMasterPort,
                                        ICEReplicaIP, ICEReplicaPort)
        logging.info("start to modify av config file")
        myMofify.modifyAvConfigFile(hostname, AVTCPPort, AVUDPort, AVInstanceGroupID, AVServiceInstanceID,
                                    AVServiceInstancePassword, ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort,
                                    ManagerServiceIPv4Addr)
        logging.info("start to modify ice_master config file")
        myMofify.modifyIceMasterConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                           dbName, dbUser, dbPwd)
        logging.info("start to modify ice_replica config file")
        myMofify.modifyIceReplicaConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                            dbName, dbUser, dbPwd)
        logging.info("start to modify manager config file")
        myMofify.modifyManagerConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort)
        logging.info("start to modify nginx config file")
        myMofify.modifyNgixConfigFile(accessIP1, accessPort1, accessIP2, accessPort2, ListenPort)
        logging.info("start to modify vnc config file")
        myMofify.modifyVncConfigFile(VNCIP, VNCPort, VNCTCPPort, VNCUDPPort, VNCInstanceGroupID, VNCServiceInstanceID,
                                     VNCServiceInstancePassword, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)
        logging.info("start to modify whiteboard config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP, WhiteBoardPort, WBTCPPort, WBUDPort, WBInstanceGroupID,
                                            WBServiceInstanceID, WBServiceInstancePassword, ICEMasterIP, ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        # upload file
        logging.info("start to upload access config file")
        b.transferAccessFile(hostname, port, username, password, basePath, "Y")
        print "finished upload access config file"
        logging.info("start to upload av config file")
        b.transferAvFile(hostname, port, username, password, basePath, "Y")
        logging.info("start to upload ice_master config file")
        b.transferMasterFile(hostname, port, username, password, basePath, "Y")
        logging.info("start to upload ice_replica config file")
        b.transferReplicaFile(hostname, port, username, password, basePath, "Y")
        logging.info("start to upload manager config file")
        b.transferManagerFile(hostname, port, username, password, basePath, "Y")
        logging.info("start to upload vnc config file")
        b.transferVncFile(hostname, port, username, password, basePath, "Y")
        logging.info("start to upload whiteboard config file")
        b.transferWBFile(hostname, port, username, password, basePath, "Y")
        # b.transferNginxFile(hostname, port, username, password,"Y")

        # Start Service
        logging.info("start access service")
        ss.startAccess(hostname, port, username, password)
        logging.info("start av service")
        ss.startAv(hostname, port, username, password, basePath)
        logging.info("start ice_master service")
        ss.startIceMaster(hostname, port, username, password, basePath)
        logging.info("start ice_replica service")
        ss.startIceReplica(hostname, port, username, password, basePath)
        logging.info("start manager service")
        ss.startManager(hostname, port, username, password)
        logging.info("start nginx service")
        ss.startNginx(hostname, port, username, password)
        logging.info("start vnc service")
        ss.startVnc(hostname, port, username, password, basePath)
        logging.info("start whiteboard service")
        ss.startWhiteBoard(hostname, port, username, password, basePath)

        t2 = datetime.datetime.now()
        print "end time: ", t2

        print t2 - t1



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