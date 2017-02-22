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

db = MySQLdb.connect("192.168.7.105","root","123456","fsp_sss" )
cursor = db.cursor()
sql="select service_instance_id,service_instance_password from fsp_sss"
try:
   # excute sql
   cursor.execute(sql)
   # get all records
   results = cursor.fetchall()
   for row in results:
      print row
      # print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
      #        (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"
# close database connection
db.close()

# Access config info
accessPort1 = "10000"
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
ICEMasterPort = "10000"

# ICEReplicaInfo
ICEReplicaPort = "10001"

# ManagerPort = "1089"
# ManagerServiceIPv4Addr = "TCP:" + ManagerIP + ":" + ManagerPort
#
# # av1 config info
# AVTCPPort1 = "1089"
# AVUDPort1 = "1089"
# AVInstanceGroupID1 = "1"
# AVServiceInstanceID1 = "av_instance_1"
# AVServiceInstancePassword1 = "av_instance_fsp"
#
# # av2 config info
# AVIP2 = request.GET['av2']
# AVTCPPort2 = "1089"
# AVUDPort2 = "1089"
# AVInstanceGroupID2 = "1"
# AVServiceInstanceID2 = "av_instance_2"
# AVServiceInstancePassword2 = "av_instance_fsp"
#
# # av3 config info
# AVIP3 = request.GET['av3']
# AVTCPPort3 = "1089"
# AVUDPort3 = "1089"
# AVInstanceGroupID3 = "0"
# AVServiceInstanceID3 = "av_instance_3"
# AVServiceInstancePassword3 = "av_instance_fsp"
#
# # av4 config info
# AVIP4 = request.GET['av4']
# AVTCPPort4 = "1089"
# AVUDPort4 = "1089"
# AVInstanceGroupID4 = "0"
# AVServiceInstanceID4 = "av_instance_4"
# AVServiceInstancePassword4 = "av_instance_fsp"
#
# # av5 config info
# AVIP5 = request.GET['av5']
# AVTCPPort5 = "1089"
# AVUDPort5 = "1089"
# AVInstanceGroupID5 = "0"
# AVServiceInstanceID5 = "av_instance_5"
# AVServiceInstancePassword5 = "av_instance_fsp"
#
# # vnc config info
# VNCIP1 = request.GET['vnc1']
# VNCPort1 = "1091"
# VNCTCPPort1 = "1089"
# VNCUDPPort1 = "1089"
# VNCInstanceGroupID1 = "1"
# VNCServiceInstanceID1 = "vnc_instance_1"
# VNCServiceInstancePassword1 = "vnc_instance_fsp"
#
# VNCIP2 = request.GET['vnc2']
# VNCPort2 = "1091"
# VNCTCPPort2 = "1089"
# VNCUDPPort2 = "1089"
# VNCInstanceGroupID2 = "1"
# VNCServiceInstanceID2 = "vnc_instance_2"
# VNCServiceInstancePassword2 = "vnc_instance_fsp"
#
# VNCIP3 = request.GET['vnc3']
# VNCPort3 = "1091"
# VNCTCPPort3 = "1089"
# VNCUDPPort3 = "1089"
# VNCInstanceGroupID3 = "0"
# VNCServiceInstanceID3 = "vnc_instance_3"
# VNCServiceInstancePassword3 = "vnc_instance_fsp"
#
# VNCIP4 = request.GET['vnc4']
# VNCPort4 = "1091"
# VNCTCPPort4 = "1089"
# VNCUDPPort4 = "1089"
# VNCInstanceGroupID4 = "0"
# VNCServiceInstanceID4 = "vnc_instance_4"
# VNCServiceInstancePassword4 = "vnc_instance_fsp"
#
# VNCIP5 = request.GET['vnc5']
# VNCPort5 = "1091"
# VNCTCPPort5 = "1089"
# VNCUDPPort5 = "1089"
# VNCInstanceGroupID5 = "0"
# VNCServiceInstanceID5 = "vnc_instance_5"
# VNCServiceInstancePassword5 = "vnc_instance_fsp"
#
# WhiteBoardIP1 = request.GET['whiteboard1']
# WhiteBoardPort1 = "1093"
#
# WBTCPPort1 = "1089"
# WBUDPort1 = "1089"
# WBInstanceGroupID1 = "1"
# WBServiceInstanceID1 = "white_board_instance_1"
# WBServiceInstancePassword1 = "white_board_instance_fsp"
#
# WhiteBoardIP2 = request.GET['whiteboard2']
# WhiteBoardPort2 = "1093"
#
# WBTCPPort2 = "1089"
# WBUDPort2 = "1089"
# WBInstanceGroupID2 = "1"
# WBServiceInstanceID2 = "white_board_instance_2"
# WBServiceInstancePassword2 = "white_board_instance_fsp"
#
# WhiteBoardIP3 = request.GET['whiteboard3']
# WhiteBoardPort3 = "1093"
#
# WBTCPPort3 = "1089"
# WBUDPort3 = "1089"
# WBInstanceGroupID3 = "0"
# WBServiceInstanceID3 = "white_board_instance_3"
# WBServiceInstancePassword3 = "white_board_instance_fsp"
#
# WhiteBoardIP4 = request.GET['whiteboard4']
# WhiteBoardPort4 = "1093"
#
# WBTCPPort4 = "1089"
# WBUDPort4 = "1089"
# WBInstanceGroupID4 = "0"
# WBServiceInstanceID4 = "white_board_instance_4"
# WBServiceInstancePassword4 = "white_board_instance_fsp"
#
# WhiteBoardIP5 = request.GET['whiteboard5']
# WhiteBoardPort5 = "1093"
#
# WBTCPPort5 = "1089"
# WBUDPort5 = "1089"
# WBInstanceGroupID5 = "0"
# WBServiceInstanceID5 = "white_board_instance_5"
# WBServiceInstancePassword5 = "white_board_instance_fsp"



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
        """Install the service

        Download the package and then tar it, and then install on machine

        Args:
            ip_service:this is a dic, key is ip, and value is service and port
            pkgURL: the URL to download the fsp package
            package_path:
            username: the username that login to machine
            password: the password using to login machine
            port: the port that login to machine
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

            :return return the sss-1.2.3.0 package name
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
        b.transferAccessFile(accessIP1, port, username, password, basePath, "Y")



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

