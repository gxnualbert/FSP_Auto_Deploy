# -*- coding:utf-8 -*-
from django.shortcuts import render
import datetime

from TransferFile import TransferFSPFile as tf
from ModifyConfigFile import MofidyFSPFile as mfsp
from StartService import StartService as ss
from log import AddLog as log

def home(request):
    question={'question':'i can not say it,update it'}
    # return render(request,'firstform/index.html',{'question': question['question']})
    return render(request,'firstform/index.html')
def cleanup(request):
        return render(request, 'firstform/cleanup.html')

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
                execmd1 = "cd /root\nrm -rf sss*"
                b.sshclient_execmd(ip, port, username, password, execmd1)
                execmd2 = "cd /\nrm -rf fsmeeting/"
                b.sshclient_execmd(ip, port, username, password, execmd2)
        return render(request, 'firstform/cleansuccessfully.html')

def search(request):
        request.encoding='utf-8'
        dbHost=request.GET['dbip']
        dbPort =request.GET['dbport']
        dbName =request.GET['tablename']
        dbUser =request.GET['username']
        dbPwd  =request.GET['pwd']
        nginxIP =request.GET['nginx']
        # av =request.GET['av']
        # vnc =request.GET['vnc']
        # whiteboard =request.GET['whiteboard']
        # msg = {}
        # msg['ice_master']=ice_master
        # msg['ice_replica']=ice_replica
        # msg['manager']=manager
        # msg['access1']=access1
        # msg['access2']=access2
        # msg['nginx']=nginx
        # msg['av']=av
        # msg['vnc']=vnc
        # msg['whiteboard']=whiteboard

        t1 = datetime.datetime.now()
        print "start time", t1

        # hostname = "192.168.153.129"
        port = 22
        username = 'root'
        password = '123456'
        basePath = "/fsmeeting/sss"

        # #download package and install

        # '''download the package from the url'''
        packageURL = "http://192.168.5.30:8080/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_sss/263/artifact/sss-1.2.1.1.tar.gz"
        packageName = packageURL.split("/")[-1]  # sss-1.2.2.1.tar.gz
        sss = packageName.split(".tar")[0]  # sss-1.2.2.1

        # sss = "sss-1.2.2.1"

        # DB info
        # dbHost = "192.168.7.105"
        # dbPort = "3306"
        # dbName = "fsp_sss"
        # dbUser = "root"
        # dbPwd = "123456"

        # Access config info
        accessIP1 = request.GET['access1']
        accessPort1 = "10000"
        accessIP2 = request.GET['access2']
        accessPort2 = "10001"
        ListenPort = "22222"

        accessTCPPort1 = "1089"
        accessUDPPort1 = "1089"
        accessServiceInstanceID1 = "access_instance_1"
        accessServiceInstancePassword1 = "access_instance_fsp"


        HTTPServiceListenPort = "3000"


        accessTCPPort2 = "1089"
        accessUDPPort2 = "1089"
        accessServiceInstanceID2 = "access_instance_2"
        accessServiceInstancePassword2 = "access_instance_fsp"

        # ICEMaster config Info
        ICEMasterIP = request.GET['myicemaster']
        ICEMasterPort = "10000"

        # ICEReplicaInfo
        ICEReplicaIP = request.GET['ice_replica']
        ICEReplicaPort = "10001"

        ManagerIP = request.GET['manager']
        ManagerPort = "1089"
        ManagerServiceIPv4Addr = "TCP:" + ManagerIP + ":" + ManagerPort

        # av1 config info
        AVIP1= request.GET['av1']
        AVTCPPort1 = "1089"
        AVUDPort1 = "1089"
        AVInstanceGroupID1 = "1"
        AVServiceInstanceID1 = "av_instance_1"
        AVServiceInstancePassword1 = "av_instance_fsp"

        # av2 config info
        AVIP2 = request.GET['av2']
        AVTCPPort2 = "1089"
        AVUDPort2 = "1089"
        AVInstanceGroupID2 = "1"
        AVServiceInstanceID2 = "av_instance_2"
        AVServiceInstancePassword2 = "av_instance_fsp"

        # av3 config info
        AVIP3 = request.GET['av3']
        AVTCPPort3 = "1089"
        AVUDPort3 = "1089"
        AVInstanceGroupID3 = "0"
        AVServiceInstanceID3 = "av_instance_3"
        AVServiceInstancePassword3 = "av_instance_fsp"

        # av4 config info
        AVIP4 = request.GET['av4']
        AVTCPPort4 = "1089"
        AVUDPort4 = "1089"
        AVInstanceGroupID4 = "0"
        AVServiceInstanceID4 = "av_instance_4"
        AVServiceInstancePassword4 = "av_instance_fsp"

        # av5 config info
        AVIP5 = request.GET['av5']
        AVTCPPort5 = "1089"
        AVUDPort5 = "1089"
        AVInstanceGroupID5 = "0"
        AVServiceInstanceID5 = "av_instance_5"
        AVServiceInstancePassword5 = "av_instance_fsp"


        # vnc config info
        VNCIP1 = request.GET['vnc1']
        VNCPort1 = "1091"
        VNCTCPPort1 = "1089"
        VNCUDPPort1 = "1089"
        VNCInstanceGroupID1 = "1"
        VNCServiceInstanceID1 = "vnc_instance_1"
        VNCServiceInstancePassword1 = "vnc_instance_fsp"

        VNCIP2 = request.GET['vnc2']
        VNCPort2 = "1091"
        VNCTCPPort2 = "1089"
        VNCUDPPort2 = "1089"
        VNCInstanceGroupID2 = "1"
        VNCServiceInstanceID2 = "vnc_instance_2"
        VNCServiceInstancePassword2 = "vnc_instance_fsp"

        VNCIP3 = request.GET['vnc3']
        VNCPort3 = "1091"
        VNCTCPPort3 = "1089"
        VNCUDPPort3 = "1089"
        VNCInstanceGroupID3 = "0"
        VNCServiceInstanceID3 = "vnc_instance_3"
        VNCServiceInstancePassword3 = "vnc_instance_fsp"

        VNCIP4 = request.GET['vnc4']
        VNCPort4 = "1091"
        VNCTCPPort4 = "1089"
        VNCUDPPort4 = "1089"
        VNCInstanceGroupID4 = "0"
        VNCServiceInstanceID4 = "vnc_instance_4"
        VNCServiceInstancePassword4 = "vnc_instance_fsp"

        VNCIP5 = request.GET['vnc5']
        VNCPort5 = "1091"
        VNCTCPPort5 = "1089"
        VNCUDPPort5 = "1089"
        VNCInstanceGroupID5 = "0"
        VNCServiceInstanceID5 = "vnc_instance_5"
        VNCServiceInstancePassword5 = "vnc_instance_fsp"

        WhiteBoardIP1 = request.GET['whiteboard1']
        WhiteBoardPort1 = "1093"

        WBTCPPort1 = "1089"
        WBUDPort1 = "1089"
        WBInstanceGroupID1 = "1"
        WBServiceInstanceID1 = "white_board_instance_1"
        WBServiceInstancePassword1 = "white_board_instance_fsp"

        WhiteBoardIP2 = request.GET['whiteboard2']
        WhiteBoardPort2 = "1093"

        WBTCPPort2 = "1089"
        WBUDPort2 = "1089"
        WBInstanceGroupID2 = "1"
        WBServiceInstanceID2 = "white_board_instance_2"
        WBServiceInstancePassword2 = "white_board_instance_fsp"

        WhiteBoardIP3 = request.GET['whiteboard3']
        WhiteBoardPort3 = "1093"

        WBTCPPort3 = "1089"
        WBUDPort3 = "1089"
        WBInstanceGroupID3 = "0"
        WBServiceInstanceID3 = "white_board_instance_3"
        WBServiceInstancePassword3 = "white_board_instance_fsp"

        WhiteBoardIP4 = request.GET['whiteboard4']
        WhiteBoardPort4 = "1093"

        WBTCPPort4 = "1089"
        WBUDPort4 = "1089"
        WBInstanceGroupID4 = "0"
        WBServiceInstanceID4 = "white_board_instance_4"
        WBServiceInstancePassword4 = "white_board_instance_fsp"

        WhiteBoardIP5 = request.GET['whiteboard5']
        WhiteBoardPort5 = "1093"

        WBTCPPort5 = "1089"
        WBUDPort5 = "1089"
        WBInstanceGroupID5 = "0"
        WBServiceInstanceID5 = "white_board_instance_5"
        WBServiceInstancePassword5 = "white_board_instance_fsp"



        b = tf

        tf.prepareFolder()

        logging = log.Log()

        execmd = "cd /root\nwget " + packageURL + "\ntar -xzvf " + packageName
        # get the install package
        print ("start to get package and tar it on %s",accessIP1)
        b.sshclient_execmd(accessIP1,port,username,password,execmd)

        print ("start to get package and tar it on %s", accessIP2)
        b.sshclient_execmd(accessIP2,port,username,password,execmd)

        print ("start to get package and tar it on %s", ManagerIP)
        b.sshclient_execmd(ManagerIP,port,username,password,execmd)

        print ("start to get package and tar it on %s", AVIP1)
        b.sshclient_execmd(AVIP1,port,username,password,execmd)

        print ("start to get package and tar it on %s", AVIP2)
        b.sshclient_execmd(AVIP2,port,username,password,execmd)

        # install service
        logging.info("start to install access")
        # ipList = ""
        # serviceList = ""
        # for i in range(len(ipList)):
        #         hostname = ipList[i]
        #         for j in range(len(serviceList)):
        #                 if "access" in serviceList[i]:
        #                         b.installAccess(hostname, port, username, password, sss)
        #                         logging.info("start to install av")
        #                 if "av" in serviceList[i]:
        #                         b.installAv(hostname, port, username, password, sss)
        #                         logging.info("start to install ice_master")
        #                 if "ice_master" in serviceList[i]:
        #                         b.installIceMaster(hostname, port, username, password, sss)
        #                         logging.info("start to install ice_replica")
        #
        #                 b.installIceReplica(hostname, port, username, password, sss)
        #                 logging.info("start to install manager")
        #                 b.installManager(hostname, port, username, password, sss)
        #                 logging.info("start to install vnc")
        #                 b.installVnc(hostname, port, username, password, sss)
        #                 logging.info("start to install whiteboard")
        #                 b.installWhiteboard(hostname, port, username, password, sss)
        #                 logging.info("start to install nginx")
        #                 b.installNginx(hostname, port, username, password)

        # Access
        print ("start to install access1")
        b.installAccess(accessIP1, port, username, password, sss)

        print ("start to install access2")
        b.installAccess(accessIP2, port, username, password, sss)

        # fundamental service
        print "av1"
        b.installAv(AVIP1,port,username, password, sss)

        b.installAv(AVIP2,port,username, password, sss)
        b.installAv(AVIP3,port,username, password, sss)
        b.installAv(AVIP4,port,username, password, sss)
        b.installAv(AVIP5,port,username, password, sss)

        b.installVnc(VNCIP1,port,username, password, sss)
        b.installVnc(VNCIP2,port,username, password, sss)
        b.installVnc(VNCIP3,port,username, password, sss)
        b.installVnc(VNCIP4,port,username, password, sss)
        b.installVnc(VNCIP5,port,username, password, sss)

        b.installWhiteboard(WhiteBoardIP1,port,username, password, sss)
        b.installWhiteboard(WhiteBoardIP2,port,username, password, sss)
        b.installWhiteboard(WhiteBoardIP3,port,username, password, sss)
        b.installWhiteboard(WhiteBoardIP4,port,username, password, sss)
        b.installWhiteboard(WhiteBoardIP5,port,username, password, sss)

        # manager service
        b.installManager(ManagerIP,port,username, password, sss)

        # ice service
        b.installIceMaster(ICEMasterIP,port,username, password, sss)
        b.installIceReplica(ICEReplicaIP,port,username, password, sss)

        #because there are many av,vnc,whiteboard conf files, but the program only have one folder,like av,vnc, so we
        # need to download the file, then modify it, and the upload it.
        myMofify = mfsp()
        # download access1 config file
        logging.info("start to download access1 config file,ip is %s",accessIP1)
        b.transferAccessFile(accessIP1, port, username, password, basePath)

        logging.info("start to modify access1 config file")
        myMofify.modifyAccessConfigFile(accessTCPPort1, accessUDPPort1, accessServiceInstanceID1, accessServiceInstancePassword1,
                                        HTTPServiceListenPort, ManagerServiceIPv4Addr, ICEMasterIP, ICEMasterPort,
                                        ICEReplicaIP, ICEReplicaPort)

        logging.info("start to upload access1 config file ip is %s",accessIP1)
        b.transferAccessFile(accessIP1, port, username, password, basePath, "Y")

        #download access2 config file, modify, and upload it

        logging.info("start to download access2 config file")
        b.transferAccessFile(accessIP2, port, username, password, basePath)

        logging.info("start to modify access2 config file")
        myMofify.modifyAccessConfigFile(accessTCPPort2, accessUDPPort2, accessServiceInstanceID2,
                                        accessServiceInstancePassword2,
                                        HTTPServiceListenPort, ManagerServiceIPv4Addr, ICEMasterIP, ICEMasterPort,
                                        ICEReplicaIP, ICEReplicaPort)

        logging.info("start to upload access2 config file")
        b.transferAccessFile(accessIP2, port, username, password, basePath, "Y")

        # download av1 config file, modify, and upload it

        logging.info("start to download av1 config file")
        b.transferAvFile(AVIP1, port, username, password, basePath)

        logging.info("start to modify av1 config file")
        myMofify.modifyAvConfigFile(AVIP1, AVTCPPort1, AVUDPort1, AVInstanceGroupID1, AVServiceInstanceID1,
                                    AVServiceInstancePassword1, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        logging.info("start to upload av1 config file")
        b.transferAvFile(AVIP1, port, username, password, basePath, "Y")

        # download av2 config file, modify, and upload it

        logging.info("start to download av2 config file")
        b.transferAvFile(AVIP2, port, username, password, basePath)

        logging.info("start to modify av2 config file")
        myMofify.modifyAvConfigFile(AVIP2, AVTCPPort2, AVUDPort2, AVInstanceGroupID2, AVServiceInstanceID2,
                                    AVServiceInstancePassword2, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        logging.info("start to upload av2 config file")
        b.transferAvFile(AVIP2, port, username, password, basePath, "Y")

        # download av3 config file, modify, and upload it

        logging.info("start to download av3 config file")
        b.transferAvFile(AVIP3, port, username, password, basePath)

        logging.info("start to modify av3 config file")
        myMofify.modifyAvConfigFile(AVIP3, AVTCPPort3, AVUDPort3, AVInstanceGroupID3, AVServiceInstanceID3,
                                    AVServiceInstancePassword3, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        logging.info("start to upload av3 config file")
        b.transferAvFile(AVIP3, port, username, password, basePath, "Y")
        
        # download av4 config file, modify, and upload it

        logging.info("start to download av4 config file")
        b.transferAvFile(AVIP4, port, username, password, basePath)

        logging.info("start to modify av4 config file")
        myMofify.modifyAvConfigFile(AVIP4, AVTCPPort4, AVUDPort4, AVInstanceGroupID4, AVServiceInstanceID4,
                                    AVServiceInstancePassword4, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        logging.info("start to upload av4 config file")
        b.transferAvFile(AVIP4, port, username, password, basePath, "Y")
        
        # download av5 config file, modify, and upload it

        logging.info("start to download av5 config file")
        b.transferAvFile(AVIP5, port, username, password, basePath)

        logging.info("start to modify av5 config file")
        myMofify.modifyAvConfigFile(AVIP5, AVTCPPort5, AVUDPort5, AVInstanceGroupID5, AVServiceInstanceID5,
                                    AVServiceInstancePassword5, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        logging.info("start to upload av5 config file")
        b.transferAvFile(AVIP5, port, username, password, basePath, "Y")

        # download vnc1 config file, modify, and upload it
        logging.info("start to download vnc1 config file")
        b.transferVncFile(VNCIP1, port, username, password, basePath)

        logging.info("start to modify vnc1 config file")
        myMofify.modifyVncConfigFile(VNCIP1, VNCPort1, VNCTCPPort1, VNCUDPPort1, VNCInstanceGroupID1,
                                     VNCServiceInstanceID1,
                                     VNCServiceInstancePassword1, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload vnc1 config file")
        b.transferVncFile(VNCIP1, port, username, password, basePath, "Y")
        
        # download vnc2 config file, modify, and upload it
        logging.info("start to download vnc2 config file")
        b.transferVncFile(VNCIP2, port, username, password, basePath)

        logging.info("start to modify vnc2 config file")
        myMofify.modifyVncConfigFile(VNCIP2, VNCPort2, VNCTCPPort2, VNCUDPPort2, VNCInstanceGroupID2,
                                     VNCServiceInstanceID2,
                                     VNCServiceInstancePassword2, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload vnc2 config file")
        b.transferVncFile(VNCIP2, port, username, password, basePath, "Y")
        
        # download vnc3 config file, modify, and upload it
        logging.info("start to download vnc3 config file")
        b.transferVncFile(VNCIP3, port, username, password, basePath)

        logging.info("start to modify vnc3 config file")
        myMofify.modifyVncConfigFile(VNCIP3, VNCPort3, VNCTCPPort3, VNCUDPPort3, VNCInstanceGroupID3,
                                     VNCServiceInstanceID3,
                                     VNCServiceInstancePassword3, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload vnc3 config file")
        b.transferVncFile(VNCIP3, port, username, password, basePath, "Y")
        
        # download vnc4 config file, modify, and upload it
        logging.info("start to download vnc4 config file")
        b.transferVncFile(VNCIP4, port, username, password, basePath)

        logging.info("start to modify vnc4 config file")
        myMofify.modifyVncConfigFile(VNCIP4, VNCPort4, VNCTCPPort4, VNCUDPPort4, VNCInstanceGroupID4,
                                     VNCServiceInstanceID4,
                                     VNCServiceInstancePassword4, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload vnc4 config file")
        b.transferVncFile(VNCIP4, port, username, password, basePath, "Y")
        
        # download vnc5 config file, modify, and upload it
        logging.info("start to download vnc5 config file")
        b.transferVncFile(VNCIP5, port, username, password, basePath)

        logging.info("start to modify vnc5 config file")
        myMofify.modifyVncConfigFile(VNCIP5, VNCPort5, VNCTCPPort5, VNCUDPPort5, VNCInstanceGroupID5,
                                     VNCServiceInstanceID5,
                                     VNCServiceInstancePassword5, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload vnc5 config file")
        b.transferVncFile(VNCIP5, port, username, password, basePath, "Y")

        # download whiteboard1 config file, modify, and upload it

        logging.info("start to download white board1 config file")
        b.transferWBFile(WhiteBoardIP1, port, username, password, basePath)

        logging.info("start to modify whiteboard1 config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP1, WhiteBoardPort1, WBTCPPort1, WBUDPort1, WBInstanceGroupID1,
                                            WBServiceInstanceID1, WBServiceInstancePassword1, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload whiteboard1 config file")
        b.transferWBFile(WhiteBoardIP1, port, username, password, basePath, "Y")

        # download whiteboard2 config file, modify, and upload it

        logging.info("start to download white board2 config file")
        b.transferWBFile(WhiteBoardIP2, port, username, password, basePath)

        logging.info("start to modify whiteboard config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP2, WhiteBoardPort2, WBTCPPort2, WBUDPort2, WBInstanceGroupID2,
                                            WBServiceInstanceID2, WBServiceInstancePassword2, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload whiteboard2 config file")
        b.transferWBFile(WhiteBoardIP2, port, username, password, basePath, "Y")
        
        # download whiteboard3 config file, modify, and upload it

        logging.info("start to download white board3 config file")
        b.transferWBFile(WhiteBoardIP3, port, username, password, basePath)

        logging.info("start to modify whiteboard3 config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP3, WhiteBoardPort3, WBTCPPort3, WBUDPort3, WBInstanceGroupID3,
                                            WBServiceInstanceID3, WBServiceInstancePassword3, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload whiteboard3 config file")
        b.transferWBFile(WhiteBoardIP3, port, username, password, basePath, "Y")
        
        # download whiteboard4 config file, modify, and upload it

        logging.info("start to download white board4 config file")
        b.transferWBFile(WhiteBoardIP4, port, username, password, basePath)

        logging.info("start to modify whiteboard4 config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP4, WhiteBoardPort4, WBTCPPort4, WBUDPort4, WBInstanceGroupID4,
                                            WBServiceInstanceID4, WBServiceInstancePassword4, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload whiteboard4 config file")
        b.transferWBFile(WhiteBoardIP4, port, username, password, basePath, "Y")
        
        # download whiteboard config file, modify, and upload it

        logging.info("start to download white board5 config file")
        b.transferWBFile(WhiteBoardIP5, port, username, password, basePath)

        logging.info("start to modify whiteboard5 config file")
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP5, WhiteBoardPort5, WBTCPPort5, WBUDPort5, WBInstanceGroupID5,
                                            WBServiceInstanceID5, WBServiceInstancePassword5, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)

        logging.info("start to upload whiteboard5 config file")
        b.transferWBFile(WhiteBoardIP5, port, username, password, basePath, "Y")

        # download ice_master config file, modify, and upload it

        logging.info("start to download ice_master config file")
        b.transferMasterFile(ICEMasterIP, port, username, password, basePath)

        logging.info("start to modify ice_master config file")
        myMofify.modifyIceMasterConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                           dbName, dbUser, dbPwd)

        logging.info("start to upload ice_master config file")
        b.transferMasterFile(ICEMasterIP, port, username, password, basePath, "Y")

        # download ice_replica config file, modify, and upload it
        logging.info("start to download ice_replica config file")
        b.transferReplicaFile(ICEReplicaIP, port, username, password, basePath)

        logging.info("start to modify ice_replica config file")
        myMofify.modifyIceReplicaConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                            dbName, dbUser, dbPwd)
        logging.info("start to upload ice_replica config file")
        b.transferReplicaFile(ICEReplicaIP, port, username, password, basePath, "Y")

        # download manager config file, modify, and upload it

        logging.info("start to download manager config file")
        b.transferManagerFile(ManagerIP, port, username, password, basePath)

        logging.info("start to modify manager config file")
        myMofify.modifyManagerConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort)
        logging.info("start to upload manager config file")
        b.transferManagerFile(ManagerIP, port, username, password, basePath, "Y")


        logging.info("start to modify nginx config file")
        myMofify.modifyNgixConfigFile(accessIP1, accessPort1, accessIP2, accessPort2, ListenPort)

        # b.transferNginxFile(hostname, port, username, password,"Y")

        # Start Service
        logging.info("start access service")
        ss.startAccess(accessIP1, port, username, password)
        logging.info("start av service")
        ss.startAv(AVIP1, port, username, password, basePath)
        logging.info("start ice_master service")
        ss.startIceMaster(ICEMasterIP, port, username, password, basePath)
        logging.info("start ice_replica service")
        ss.startIceReplica(ICEReplicaIP, port, username, password, basePath)
        logging.info("start manager service")
        ss.startManager(ManagerIP, port, username, password)
        logging.info("start nginx service")
        ss.startNginx(nginxIP, port, username, password)
        logging.info("start vnc service")
        ss.startVnc(VNCIP1, port, username, password, basePath)
        logging.info("start whiteboard service")
        ss.startWhiteBoard(WhiteBoardIP1, port, username, password, basePath)

        t2 = datetime.datetime.now()
        print "end time: ", t2

        tt= t2 - t1

        info={"totaltime":tt}

        return render(request,'firstform/result.html',info)
        # return HttpResponse(message)
def deployv2(request):
        return render(request, 'firstform/installAllService.html')


def installinfo(request):
        request.encoding = 'utf-8'
        machine1 = request.GET['machine1']
        machine2 = request.GET['machine2']
        machine3 = request.GET['machine3']
        machine4 = request.GET['machine4']
        machine5 = request.GET['machine5']

        servicelist1 = request.GET['servicelist1']
        servicelist2 = request.GET['servicelist2']
        servicelist3 = request.GET['servicelist3']
        servicelist4 = request.GET['servicelist4']
        servicelist5 = request.GET['servicelist5']

        portlist1=request.GET['portlist1']
        portlist2=request.GET['portlist2']
        portlist3=request.GET['portlist3']
        portlist4=request.GET['portlist4']
        portlist5=request.GET['portlist5']



        print machine1
        print "service list is ",servicelist1

        return render(request,'firstform/installAllService.html')

def search_form(request):
        return render(request,'firstform/deployinfo.html')


def singleService(request):
        return render(request, 'firstform/installSingleService.html')

def allService(request):
        return render(request, 'firstform/installAllService.html')


# def search_post(request):
# 	ctx ={}
# 	ctx.update(csrf(request))
# 	if request.POST:
# 		ctx['rlt'] = request.POST['q']
# 	return render(request, "post.html", ctx)