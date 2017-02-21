from __future__ import unicode_literals
from TransferFile import TransferFSPFile as tf
from ModifyConfigFile import MofidyFSPFile as mfsp
from StartService import StartService as ss
from log import AddLog as log
from django.db import models
import json

# Create your models here.
b = tf()
myMofify = mfsp()

tf.prepareFolder()

logging = log.Log()

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

