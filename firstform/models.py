from __future__ import unicode_literals
from TransferFile import TransferFSPFile as tf
from ModifyConfigFile import MofidyFSPFile as mfsp
from StartService import StartService as ss
from log import AddLog as log
from django.db import models
import MySQLdb


# Create your models here.
b = tf()
myMofify = mfsp()

tf.prepareFolder()

logging = log.Log()



remotePath="/fsmeeting/sss"
accessHTTP2ListenPort="3000"

class modleLogic(object):
    def __init__(self):
        pass


    # iplist, service_port, port, username, password, package_path
    '''
    function name:m_installallservice, m means Model,
    servicePort: the combination of service and port, e.g:av,1089
    ip_service:store ip and service, one ip corresponding to several service. key is ip , and value is service and port
    '''

    @classmethod
    def m_InstallService(self,ip_service, pkgPath,username, password, port):
        """Install the service according to the dic of ip and service

        :param ip_service:this is a dic, key is ip, and value is service and port
        :param pkgPath: /fsmeeting/sss
        :param username:the username that login to machine
        :param password:the password using to login machine
        :param port:the port that login to machine
        :return:
        """

        for k,v in ip_service.items():
            #install service
            servicePort = v.split(";")
            for i in servicePort:
                service=i.split(",")[0]
                if "av" in service.lower():
                    b.installAv(k,port,username,password,pkgPath)
                elif "vnc" in service.lower():
                    b.installVnc(k,port,username,password,pkgPath)
                elif "whiteboard" in service.lower():
                    b.installWhiteboard(k,port,username,password,pkgPath)
                elif "access" in service.lower():
                    b.installAccess(k,port,username,password,pkgPath)
                elif "manager" in service.lower():
                    b.installManager(k,port,username,password,pkgPath)
                elif "ice_master" in service.lower():
                    b.installIceMaster(k,port,username,password,pkgPath)
                elif "ice_replica" in service.lower():
                    b.installIceReplica(k,port,username,password,pkgPath)
    @classmethod
    def m_DownPkgAndTar(self,pkgURL,machineIps,port,username,password):
        """ download package from jenkins url and tar it on target machine

        :param self:
        :param pkgURL: the url that using to download the fsp ackage
        :param machineIps: the machines which using to install service, this is a dic
        :param port: port for login machine
        :param username: username for login machine
        :param password: password for login machine
        :return:
        """
        packageName = pkgURL.split("/")[-1]
        execmd = "cd /root\nwget " + pkgURL + "\ntar -xzvf " + packageName
        for k, v in machineIps.items():
            b.sshclient_execmd(k, port,username,password,execmd)

    @classmethod
    def m_BasePath(self,hostname,port,username,password):
        """get the package name from the machine

            :return return the package name, e.g: sss-1.2.3.0
        """
        execmd="cd /root\nls"
        result=b.sshclient_execmd(hostname,port,username,password,execmd)
        result=result.split("\n")
        for i in result:
            if "sss" in i and "tar" not in i:
                return i

    @classmethod
    def m_AccessFileConfig(self,accessIP1,port, username, password, basePath,accessTCPPort1, accessUDPPort1, accessServiceInstanceID1,
                                        accessServiceInstancePassword1,
                                        HTTPServiceListenPort, ManagerServiceIPv4Addr, ICEMasterIP, ICEMasterPort,
                                        ICEReplicaIP, ICEReplicaPort):
        """ This function is used to download the access config file and then modify it, and upload it at last

        :param accessIP1: the ip for access machine
        :param port: the port for login access machine
        :param username: the username for login access machine
        :param password: the password for login access machine
        :param basePath: basePath = "/fsmeeting/sss" the path that fsp install
        :param accessTCPPort1: the tcp port in access ServiceXML config file
        :param accessUDPPort1: the UDP port in access ServiceXML config file
        :param accessServiceInstanceID1: the ServiceInstanceID in access config file
        :param accessServiceInstancePassword1: the ServiceInstancePassword in access config file
        :param HTTPServiceListenPort:
        :param ManagerServiceIPv4Addr:the manager service ip,e.g: <ManagerServiceIPv4Addr>TCP:192.168.7.74:1089</ManagerServiceIPv4Addr>
        :param ICEMasterIP: the ice master machine ip, e.g: <DBServer>192.168.7.160</DBServer>
        :param ICEMasterPort:
        :param ICEReplicaIP:the ice replica machine ip, e.g: <DBServer>192.168.7.72</DBServer>
        :param ICEReplicaPort:
        :return:
        """

        b.transferAccessFile(accessIP1, port, username, password, basePath)
        myMofify.modifyAccessConfigFile(accessTCPPort1, accessUDPPort1, accessServiceInstanceID1,
                                        accessServiceInstancePassword1,
                                        HTTPServiceListenPort, ManagerServiceIPv4Addr, ICEMasterIP, ICEMasterPort,
                                        ICEReplicaIP, ICEReplicaPort)
        b.transferAccessFile(accessIP1, port, username, password, remotePath, "Y")

    @classmethod
    def m_AvFileConfig(self,AVIP1,port,username,password,basePath,AVTCPPort1,AVUDPort1,AVInstanceGroupID1,AVServiceInstanceID1,
                       AVServiceInstancePassword1,ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr
                       ):
        b.transferAvFile(AVIP1, port, username, password, remotePath)
        myMofify.modifyAvConfigFile(AVIP1, AVTCPPort1, AVUDPort1, AVInstanceGroupID1, AVServiceInstanceID1,
                                    AVServiceInstancePassword1, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                    ICEReplicaPort,
                                    ManagerServiceIPv4Addr)

        b.transferAvFile(AVIP1, port, username, password, remotePath, "Y")


    @classmethod
    def m_VncFileConfig(self,VNCIP1, port, username, password, basePath, VNCTCPPort1, VNCUDPPort1, VNCInstanceGroupID1,
                                     VNCServiceInstanceID1,
                                     VNCServiceInstancePassword1, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr):
        b.transferVncFile(VNCIP1, port, username, password, remotePath)
        print "finished download vnc file, start to modify it"
        myMofify.modifyVncConfigFile(VNCIP1, VNCTCPPort1, VNCUDPPort1, VNCInstanceGroupID1,
                                     VNCServiceInstanceID1,
                                     VNCServiceInstancePassword1, ICEMasterIP, ICEMasterPort, ICEReplicaIP,
                                     ICEReplicaPort, ManagerServiceIPv4Addr)
        b.transferVncFile(VNCIP1, port, username, password, remotePath, "Y")

    @classmethod
    def m_WhiteBoardFileConfig(self,WhiteBoardIP1, port, username, password, basePath, WBTCPPort1, WBUDPort1, WBInstanceGroupID1,
                                            WBServiceInstanceID1, WBServiceInstancePassword1, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr):
        b.transferWBFile(WhiteBoardIP1, port, username, password, remotePath)
        myMofify.modifyWhiteBoardConfigFile(WhiteBoardIP1,WBTCPPort1, WBUDPort1, WBInstanceGroupID1,
                                            WBServiceInstanceID1, WBServiceInstancePassword1, ICEMasterIP,
                                            ICEMasterPort,
                                            ICEReplicaIP, ICEReplicaPort, ManagerServiceIPv4Addr)
        b.transferWBFile(WhiteBoardIP1, port, username, password, remotePath, "Y")

    @classmethod
    def m_Ice_MasterFileConfig(self,ICEMasterIP, port, username, password, basePath,ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                           dbName, dbUser, dbPwd):
        b.transferMasterFile(ICEMasterIP, port, username, password, remotePath)
        myMofify.modifyIceMasterConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                           dbName, dbUser, dbPwd)
        # myMofify.modifyIceMasterConfigFile(ICEMasterIP,)
        b.transferMasterFile(ICEMasterIP, port, username, password, remotePath, "Y")

    @classmethod
    def m_Ice_ReplicaFileConfig(self,ICEReplicaIP, port, username, password, basePath,ICEMasterIP,
                                ICEMasterPort,ICEReplicaPort,
                                dbHost, dbPort,
                                dbName, dbUser, dbPwd
                                ):
        b.transferReplicaFile(ICEReplicaIP, port, username, password, remotePath)
        myMofify.modifyIceReplicaConfigFile(ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort, dbHost, dbPort,
                                            dbName, dbUser, dbPwd)
        b.transferReplicaFile(ICEReplicaIP, port, username, password, remotePath, "Y")

    @classmethod
    def m_ManagerFileConfig(self,ManagerIP, port, username, password,ICEMasterIP, ICEMasterPort, ICEReplicaIP, ICEReplicaPort,ManagerTCPPort,ManagerUDPPort):
        b.transferManagerFile(ManagerIP, port, username, password, remotePath)
        myMofify.modifyManagerConfigFile(ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerTCPPort,ManagerUDPPort)
        b.transferManagerFile(ManagerIP, port, username, password, remotePath, "Y")

    @classmethod
    def m_SetCondifFile(self,ip_service, pkgPath,username, password, port,dbinfo):
        iceInfo={}
        managerInfo={}
        accessServiceInfo={}
        avServiceInfo={}
        vncServiceInfo={}
        whiteboardServiceInfo={}
        for k,v in ip_service.items():
            servicePortList = v.split(";")

            for i in servicePortList:
                if i:
                    service = i.split(",")[0]
                    servicePort=i.split(",")[1]
                    if "ice_master" in service:
                        iceInfo['iceMasterIp']=k
                        iceInfo['iceMasterPort']=servicePort
                    if "ice_replica" in service:
                        iceInfo['iceReplicaIp']=k
                        iceInfo['iceReplicaPort']=servicePort
                    if "manager" in service:
                        managerInfo['managerIp']=k
                        managerInfo['managerPort']=servicePort

        ManagerServiceIPv4Addr="TCP:" + managerInfo['managerIp'] + ":" + managerInfo['managerPort']
        avFlag=1
        vncFlag=1
        whiteboardFlag=1
        accessFlag=1
        for k,v in ip_service.items():
            #install service
            servicePortList = v.split(";")
            for i in servicePortList:
                if i:
                    service=i.split(",")[0]
                    servicePort=i.split(",")[1]
                    if "av" in service.lower():
                        if "m" in service:
                            InstanceGroupID="1"
                        else:
                            InstanceGroupID="0"
                        ServiceInstanceID="auto_av_instance_"+str(avFlag)
                        ServiceInstancePassword="auto_av_instance_pwd_"+str(avFlag)
                        avServiceInfo[ServiceInstanceID]=ServiceInstancePassword
                        self.m_AvFileConfig(k,port,username,password,pkgPath,servicePort,servicePort,InstanceGroupID,ServiceInstanceID,
                                            ServiceInstancePassword,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],iceInfo['iceReplicaIp'],
                                            iceInfo['iceReplicaPort'],ManagerServiceIPv4Addr)
                        print k,ServiceInstancePassword,"finished"
                        avFlag=avFlag+1

                        tf.prepareFolder()
                    elif "vnc" in service.lower():
                        if "m" in service:
                            InstanceGroupID="1"
                        else:
                            InstanceGroupID="0"
                        ServiceInstanceID = "auto_vnc_instance_" + str(vncFlag)
                        ServiceInstancePassword = "auto_vnc_instance_pwd_" + str(vncFlag)
                        vncServiceInfo[ServiceInstanceID]=ServiceInstancePassword
                        self.m_VncFileConfig(k,port,username,password,pkgPath,servicePort,servicePort,InstanceGroupID,ServiceInstanceID,
                                             ServiceInstancePassword,
                                             iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],iceInfo['iceReplicaIp'],
                                             iceInfo['iceReplicaPort'],
                                             ManagerServiceIPv4Addr)
                        print k,ServiceInstancePassword,"finished"
                        vncFlag=vncFlag+1
                        tf.prepareFolder()
                    elif "whiteboard" in service.lower():
                        if "m" in service:
                            InstanceGroupID="1"
                        else:
                            InstanceGroupID="0"
                        ServiceInstanceID = "auto_whiteboard_instance_" + str(whiteboardFlag)
                        ServiceInstancePassword = "auto_whiteboard_instance_pwd_" + str(whiteboardFlag)
                        whiteboardServiceInfo[ServiceInstanceID]=ServiceInstancePassword
                        self.m_WhiteBoardFileConfig(k,port,username,password,pkgPath,servicePort,servicePort,InstanceGroupID,ServiceInstanceID,
                                                    ServiceInstancePassword,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],iceInfo['iceReplicaIp'],
                                                    iceInfo['iceReplicaPort'],ManagerServiceIPv4Addr)
                        print k, ServiceInstancePassword, "finished"
                        whiteboardFlag=whiteboardFlag+1
                        tf.prepareFolder()
                    elif "access" in service.lower():
                        ServiceInstanceID = "auto_access_instance_" + str(accessFlag)
                        ServiceInstancePassword = "auto_access_instance_pwd_" + str(accessFlag)
                        accessServiceInfo[ServiceInstanceID]=ServiceInstancePassword
                        self.m_AccessFileConfig(k,port,username,password,pkgPath,servicePort,servicePort,ServiceInstanceID,ServiceInstancePassword,
                                                accessHTTP2ListenPort,ManagerServiceIPv4Addr,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],
                                                iceInfo['iceReplicaIp'],iceInfo['iceReplicaPort'])
                        print k,ServiceInstancePassword,"finished"
                        accessFlag=accessFlag+1
                        tf.prepareFolder()
                    elif "manager" in service.lower():
                        # self.m_ManagerFileConfig(k,port,username,password,pkgPath,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],iceInfo['iceReplicaIp']
                        #                          ,iceInfo['iceReplicaPort'])
                        self.m_ManagerFileConfig(k,port,username,password,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],
                                                 iceInfo['iceReplicaIp'],iceInfo['iceReplicaPort'],servicePort,servicePort)
                        print "mananger finished config"
                        tf.prepareFolder()
                    elif "ice_master" in service.lower():
                        self.m_Ice_MasterFileConfig(iceInfo['iceMasterIp'],port,username,password,pkgPath,iceInfo['iceMasterPort'],iceInfo['iceReplicaIp'],
                                                    iceInfo['iceReplicaPort'],dbinfo["dbHost"],dbinfo["dbPort"],dbinfo["dbName"],
                                                    dbinfo["dbUser"],dbinfo["dbPwd"])
                        # self.m_Ice_MasterFileConfig(iceInfo['iceMasterIp'],)
                        print "ice master finished config"
                        tf.prepareFolder()
                    elif "ice_replica" in service.lower():
                        self.m_Ice_ReplicaFileConfig(k,port,username,password,pkgPath,iceInfo['iceMasterIp'],iceInfo['iceMasterPort'],
                                                     iceInfo['iceReplicaPort'],dbinfo["dbHost"],dbinfo["dbPort"],dbinfo["dbName"],
                                                    dbinfo["dbUser"],dbinfo["dbPwd"])
                        print "ice replica finished config"
                        # empty folder, or next time download file, the file is empty
                        tf.prepareFolder()



        db = MySQLdb.connect(dbinfo["dbHost"], dbinfo["dbUser"], dbinfo["dbPwd"], dbinfo["dbName"])
        cursor = db.cursor()

        #empty the table
        sql = "DELETE from t_service_info"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print "Error: unable to fecth data"

        #update database
        sql="insert into t_service_info(service_id,service_instance_id,service_instance_password) VALUES (%s,%s,%s);"
        serviceTuple=(accessServiceInfo,avServiceInfo,vncServiceInfo,whiteboardServiceInfo)
        for i in range(len(serviceTuple)):
            for k, v in serviceTuple[i].iteritems():
                cursor.execute(sql, (i, k, v))
                db.commit()

        db.close()



    @classmethod
    def m_StartService(self,ip_service,username,password,port):

        for k,v in ip_service.items():

            servicePortList = v.split(";")
            print k
            for i in servicePortList:
                if i:
                    service=i.split(",")[0]
                    print service
                    if "manager" in service.lower():
                        ss.startManager(k, port, username, password)

                    elif "access" in service.lower():
                        ss.startAccess(k, port, username, password)
                    elif "vnc" in service.lower():
                        ss.startVnc(k, port, username, password, remotePath)
                    elif "whiteboard" in service.lower():
                        ss.startWhiteBoard(k, port, username, password, remotePath)

                    elif "av" in service.lower():
                        ss.startAv(k, port, username, password, remotePath)

                    elif "ice_master" in service.lower():
                        ss.startIceMaster(k, port, username, password, remotePath)

                    elif "ice_replica" in service.lower():
                        ss.startIceReplica(k, port, username, password, remotePath)








class serviceInfo(models.Model):

    service_id=models.IntegerField(default=0)
    service_instance_id=models.CharField(primary_key=True,max_length=64,default='access_instance_1')
    service_instance_password=models.CharField(max_length=32,null=True)
    service_token=models.CharField(max_length=38,null=True)
    service_addr=models.CharField(max_length=256,null=True)
    service_application_id=models.IntegerField(null=True)

    adaptor_addr=models.CharField(null=True,max_length=256)

    adaptor_application_id=models.IntegerField(null=True)
    instance_group_id=models.IntegerField(null=True)
    flowrate_overload_threshold=models.IntegerField(null=True)

