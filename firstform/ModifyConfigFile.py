# -*- coding: UTF-8 -*-

import time
import datetime
import lxml.etree
import os

class MofidyFSPFile(object):

    def __init__(self):
        pass
    @classmethod
    def xmlObj(self):
        xmlPath = {}
        # ICE Server
        MasterDBServer = "//ICEServer[1]/DBServer"
        MasterDBPort = "//ICEServer[1]/DBPort"
        BackupDBServer = "//ICEServer[2]/DBServer"
        BackupDBPort = "//ICEServer[2]/DBPort"

        # ListenList
        TCPPort = "//Listen[1]/Port"
        UDPPort = "//Listen[2]/Port"

        # Config
        InstanceGroupID = "//Config/InstanceGroupID"
        ManagerServiceIPv4Addr = "//Config/ManagerServiceIPv4Addr"
        ServiceAddress = "//Service[1]/Config/ServiceAddress"
        AdaptorAddress = "//Config/AdaptorAddress"
        ServiceInstanceID = "//Config/ServiceInstanceID"
        ServiceInstancePassword = "//Config/ServiceInstancePassword"
        AdapterService = "//Service[2]/Config/ServiceAddress"

        #Access http2 listen port
        AccessHTTPServiceListenPort="//Service[2]/Config/ListenPort"
        ICEInfo = {"MasterDBServer": MasterDBServer, "MasterDBPort": MasterDBPort, "BackupDBServer": BackupDBServer,
                   "BackupDBPort": BackupDBPort}
        ListenList = {"TCPPort": TCPPort, "UDPPort": UDPPort}
        Config = {"InstanceGroupID": InstanceGroupID, "ManagerServiceIPv4Addr": ManagerServiceIPv4Addr,
                  "ServiceAddress": ServiceAddress, "AdaptorAddress": AdaptorAddress,
                  "ServiceInstanceID": ServiceInstanceID, "ServiceInstancePassword": ServiceInstancePassword,
                  "AdapterService": AdapterService}

        AccessInfo={"AccessHTTPServiceListenPort":AccessHTTPServiceListenPort}

        xmlPath.update(ICEInfo)
        xmlPath.update(ListenList)
        xmlPath.update(Config)
        xmlPath.update(AccessInfo)
        return xmlPath

    @classmethod
    def modifyFile(self,fileName, srcStr, oldStr, newStr):
        try:
            readFile = open(fileName, 'rb')
            lines = readFile.readlines()
            readFile.close()
            fileLen = len(lines)
            writeFile = open(fileName, 'w')
            for i in range(fileLen):
                lines[i] = lines[i].replace("\r", "")
                if srcStr in lines[i]:
                    lines[i] = lines[i].replace(oldStr, newStr)
            writeFile.writelines(lines)
            writeFile.close()

        except Exception, e:
            print e
            raise e

    @classmethod
    def modifyXmlNodeValue(self,docObj, nodePath, nodeValue):
        docObj.xpath(nodePath)[0].text = nodeValue

    @classmethod
    def modifyXMLFile(self,xmlPath, docObj, **xmlInstance):
        try:
            # because manager only has 4 value need to config
            if "managerNode" in xmlInstance.keys():

                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBServer"], xmlInstance["MasterDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBPort"], xmlInstance["MasterDBPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBServer"], xmlInstance["BackupDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBPort"], xmlInstance["BackupDBPortV"])

            elif "AccessNode" in xmlInstance.keys():
                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBServer"], xmlInstance["MasterDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBPort"], xmlInstance["MasterDBPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBServer"], xmlInstance["BackupDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBPort"], xmlInstance["BackupDBPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["TCPPort"], xmlInstance["TCPPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["UDPPort"], xmlInstance["UDPPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ManagerServiceIPv4Addr"], xmlInstance["ManagerServiceIPv4AddrV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ServiceInstanceID"], xmlInstance["ServiceInstanceIDV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ServiceInstancePassword"], xmlInstance["ServiceInstancePasswordV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["AccessHTTPServiceListenPort"],xmlInstance["AccessHTTPServiceListenPortV"])
            else:
                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBServer"], xmlInstance["MasterDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["MasterDBPort"], xmlInstance["MasterDBPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBServer"], xmlInstance["BackupDBServerV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["BackupDBPort"], xmlInstance["BackupDBPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["TCPPort"], xmlInstance["TCPPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["UDPPort"], xmlInstance["UDPPortV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["InstanceGroupID"], xmlInstance["InstanceGroupIDV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ManagerServiceIPv4Addr"], xmlInstance["ManagerServiceIPv4AddrV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ServiceAddress"], xmlInstance["ServiceAddressV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["AdaptorAddress"], xmlInstance["AdaptorAddressV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ServiceInstanceID"], xmlInstance["ServiceInstanceIDV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["ServiceInstancePassword"], xmlInstance["ServiceInstancePasswordV"])
                self.modifyXmlNodeValue(docObj, xmlInstance["AdapterService"], xmlInstance["AdapterServiceV"])

            docObj.write(xmlPath, encoding="UTF-8")
        except Exception, e:
            print e
            raise e
    @classmethod
    def modifyAccessConfigFile(self,ACTCPPort,ACUDPPort,ACServiceInstanceID,ACServiceInstancePassword,HTTPServiceListenPort,ManagerServiceIPv4Addr,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort):
        xmlInstance = self.xmlObj()
        ACValue = {"MasterDBServerV": ICEMasterIP, "MasterDBPortV": ICEMasterPort, "BackupDBServerV": ICEReplicaIP,
                   "BackupDBPortV": ICEReplicaPort, "TCPPortV": ACTCPPort, "UDPPortV": ACUDPPort,
                   "ManagerServiceIPv4AddrV": ManagerServiceIPv4Addr, "ServiceInstanceIDV": ACServiceInstanceID, \
                   "ServiceInstancePasswordV": ACServiceInstancePassword,
                   "AccessHTTPServiceListenPortV": HTTPServiceListenPort, "AccessNode": "AccessNode"}
        xmlInstance.update(ACValue)
        newFilePath = "./TmpFile/access/NewServiceConfig.xml"
        oldFilePath = "./TmpFile/access/ServiceConfig.xml"
        ACObj = lxml.etree.parse(oldFilePath)
        self.modifyXMLFile(newFilePath, ACObj, **xmlInstance)
        xmlInstance.clear()
        os.remove(oldFilePath)
        os.rename(newFilePath, oldFilePath)

    @classmethod
    def modifyNgixConfigFile(self,accessIP1,accessPort1,accessIP2,accessPort2,http2ListenPort):
        #if file exist, delete it
        tmpFile="./TmpFile/nginx/tmp.nginx.conf"
        nginxFilePath = "./TmpFile/nginx/nginx.conf"
        if os.path.exists(nginxFilePath):
            os.remove(nginxFilePath)

        #read tmp.ngixn.conf
        readTmpConf=open(tmpFile,'rb')
        lines = readTmpConf.readlines()
        readTmpConf.close()
        # os.mknod(nginxFilePath)
        nginxFile=open(nginxFilePath,'w')
        for i in lines:
            i=i.replace("\r","")
            nginxFile.writelines(i)

        nginxFile.close()

        self.modifyFile("./TmpFile/nginx/nginx.conf","server","XXX.XXX.XXX.XXX",accessIP1)
        print "modify ngix file",accessIP1
        self.modifyFile("./TmpFile/nginx/nginx.conf","server","xxxx",accessPort1)
        self.modifyFile("./TmpFile/nginx/nginx.conf","server","YYY.YYY.YYY.YYY",accessIP2)
        self.modifyFile("./TmpFile/nginx/nginx.conf","server","yyyy",accessPort2)
        self.modifyFile("./TmpFile/nginx/nginx.conf","listen","AAAAA",http2ListenPort)

        # nginxConfigFile = open("../nginx/tmp.nginx.conf", 'w')
        # for i in range(fileLen):
        #     lines[i] = lines[i].replace("\r", "")
        #     if srcStr in lines[i]:
        #         lines[i] = lines[i].replace(oldStr, newStr)
        # writeFile.writelines(lines)
        # writeFile.close()
    @classmethod
    def modifyIceMasterConfigFile(self,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,dbHost,dbPort,dbName,dbUser,dbPwd):
        # config.master
        filePath = ("./TmpFile/ice_master/config.master", "./TmpFile/ice_master/config.node1", "./TmpFile/ice_master/config.server")
        configInfo = {"ICEMasterIP": ICEMasterIP, "ICEMasterPort": ICEMasterPort, "ICEReplicaIP": ICEReplicaIP,
                          "ICEReplicaPort": ICEReplicaPort, "dbHost": dbHost, "dbPort": dbPort, "dbName": dbName,
                          "dbUser": dbUser, "dbPwd": dbPwd}
        try:
            self.modifyFile(filePath[0], "IceGrid.Registry.Client.Endpoints", "xxxx", configInfo["ICEMasterPort"])
            print "Update config.master successfully!"
        except Exception, e:
            print "Error occur in modify file: IceGrid Master config.master.xml!"
            raise e
        # config.node1
        try:
            self.modifyFile(filePath[1], "Ice.Default.Locator", "XXX.XXX.XXX.XXX", configInfo["ICEMasterIP"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "xxxx", configInfo["ICEMasterPort"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "YYY.YYY.YYY.YYY", configInfo["ICEReplicaIP"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "yyyy", configInfo["ICEReplicaPort"])
            print "Update config.node1 successfully!"
        except Exception, e:
            print "Error occur in modify file:IceGrid Master config.node1!"
            raise e
        # config.server
        try:
            self.modifyFile(filePath[2], "ip=", "XXX.XXX.XXX.XXX", configInfo["ICEMasterIP"])
            self.modifyFile(filePath[2], "port=", "xxxx", configInfo["ICEMasterPort"])
            self.modifyFile(filePath[2], "db=", "数据库实例名", configInfo["dbName"])
            self.modifyFile(filePath[2], "user=", "用户名", configInfo["dbUser"])
            self.modifyFile(filePath[2], "password=", "用户密码", configInfo["dbPwd"])
            self.modifyFile(filePath[2], "AdapterEndpoints", "YYY.YYY.YYY.YYY", configInfo["ICEReplicaIP"])
            self.modifyFile(filePath[2], "AdapterEndpoints", "yyyy", configInfo["ICEReplicaPort"])
            print "Update config.server successfully!"
        except Exception, e:
            print "Error occur in modify file: IceGrid Master config.server!"
            raise e

    @classmethod
    def modifyIceReplicaConfigFile(self,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,dbHost,dbPort,dbName,dbUser,dbPwd):
        # config.replica
        filePath = ("./TmpFile/ice_replica/config.replica", "./TmpFile/ice_replica/config.node2", "./TmpFile/ice_replica/config.server")
        configInfo = {"ICEMasterIP": ICEMasterIP, "ICEMasterPort": ICEMasterPort, "ICEReplicaIP": ICEReplicaIP,
                      "ICEReplicaPort": ICEReplicaPort, "dbHost": dbHost, "dbPort": dbPort, "dbName": dbName,
                      "dbUser": dbUser, "dbPwd": dbPwd}
        try:
            self.modifyFile(filePath[0], "Ice.Default.Locator", "XXX.XXX.XXX.XXX", configInfo["ICEMasterIP"])
            self.modifyFile(filePath[0], "Ice.Default.Locator", "xxxx", configInfo["ICEMasterPort"])
            self.modifyFile(filePath[0], "IceGrid.Registry.Client.Endpoints", "yyyy", configInfo["ICEReplicaPort"])
            print "Update config.replica successfully"
        except Exception, e:
            print "Error occur in modify file: IceGrid Replica config.replica!"
            raise e
        # config.node2
        try:
            self.modifyFile(filePath[1], "Ice.Default.Locator", "XXX.XXX.XXX.XXX", configInfo["ICEMasterIP"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "xxxx", configInfo["ICEMasterPort"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "YYY.YYY.YYY.YYY", configInfo["ICEReplicaIP"])
            self.modifyFile(filePath[1], "Ice.Default.Locator", "yyyy", configInfo["ICEReplicaPort"])
            print "Update config.node2 successfully"
        except Exception, e:
            print "Error occur in modify file: IceGrid Replica config.node2!"
            raise e
        # config.server
        try:
            self.modifyFile(filePath[2], "ip=", "XXX.XXX.XXX.XXX", configInfo["dbHost"])
            self.modifyFile(filePath[2], "port=", "xxxx", configInfo["dbPort"])
            self.modifyFile(filePath[2], "db=", "数据库实例名", configInfo["dbName"])
            self.modifyFile(filePath[2], "user=", "用户名", configInfo["dbUser"])
            self.modifyFile(filePath[2], "password=", "用户密码", configInfo["dbPwd"])
            self.modifyFile(filePath[2], "AdapterEndpoints", "YYY.YYY.YYY.YYY", configInfo["ICEReplicaIP"])
            self.modifyFile(filePath[2], "AdapterEndpoints", "yyyy", configInfo["ICEReplicaPort"])
            print "Update config.server successfully!"
        except Exception, e:
            print "Error occur in modify file: IceGrid Replica config.server!"
            raise e

    # def commonConfigFIle(newfilePath,oldFilePath,**newValue):
    #
    #     xmlInstance = xmlObj()
    #
    #     # VNCTCPPort = "1090"
    #     # VNCUDPPort = "1090"
    #     # VNCInstanceGroupID = "0"
    #     # VNCServiceInstanceID = "av_instance_3"
    #     # VNCServiceInstancePassword = "av_instance_fsp"
    #     # VNCServiceAddress = "TCP:" + ICEReplicaIP + ":" + ICEReplicaPort + ";" + "UDP:" + ICEReplicaIP + ":" + ICEReplicaPort
    #     # VNCAdaptorAddress = VNCServiceAddress
    #     # VNCAdaptorService = VNCServiceAddress
    #
    #     VNCValue = {"TCPPortV": newValue["TCPPortV"], "UDPPortV": newValue["UDPPortV"], "InstanceGroupIDV": newValue["InstanceGroupIDV"],
    #                 "ServiceInstanceIDV": newValue["ServiceInstanceIDV"], "ServiceInstancePasswordV": newValue["ServiceInstancePasswordV"],
    #                 "ServiceAddressV": newValue["ServiceAddressV"], "AdaptorAddressV": newValue["AdaptorAddressV"],
    #                 "AdapterServiceV": newValue["AdapterServiceV"], "MasterDBServerV": newValue["MasterDBServerV"], "MasterDBPortV": newValue["MasterDBPortV"],
    #                 "BackupDBServerV": newValue["BackupDBServerV"], "BackupDBPortV": newValue["BackupDBPortV"],
    #                 "ManagerServiceIPv4AddrV": newValue["ManagerServiceIPv4AddrV"]}
    #     xmlInstance.update(VNCValue)
    #     filePath = newfilePath
    #     # VNCObj = lxml.etree.parse("./vnc/ServiceConfig.xml")
    #     VNCObj = lxml.etree.parse(oldFilePath)
    #
    #     modifyXMLFile(filePath, VNCObj, **xmlInstance)
    #     # after finished used the dic, clear it so that next time the vnc value not in the dic
    #     xmlInstance.clear()
    @classmethod
    def modifyManagerConfigFile(self,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,):
        xmlInstance = self.xmlObj()
        ManagerValue = {"MasterDBServerV": ICEMasterIP, "MasterDBPortV": ICEMasterPort, "BackupDBServerV": ICEReplicaIP,
                        "BackupDBPortV": ICEReplicaPort, "managerNode": "managernode"}
        xmlInstance.update(ManagerValue)
        newFilePath = "./TmpFile/manager/NewServiceConfig.xml"
        oldFilePath = "./TmpFile/manager/ServiceConfig.xml"
        AVObj = lxml.etree.parse(oldFilePath)
        try:
            self.modifyXMLFile(newFilePath, AVObj, **xmlInstance)
            print "Update manager ServiceConfig.xml successfully"
        except Exception,e:
            print "Error occur in modify file: manager ServiceConfig.xml!"
            raise e
        xmlInstance.clear()
        # Remove file and Rename file
        os.remove(oldFilePath)
        os.rename(newFilePath, oldFilePath)

    def modifyVncConfigFile(self,VNCIP,VNCPort,VNCTCPPort,VNCUDPPort,VNCInstanceGroupID,VNCServiceInstanceID,VNCServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr):
        xmlInstance = self.xmlObj()
        VNCServiceAddress = "TCP:" + VNCIP + ":" + VNCPort + ";" + "UDP:" + VNCIP + ":" + VNCPort
        VNCAdaptorAddress = VNCServiceAddress
        VNCAdaptorService = VNCServiceAddress
        VNCValue = {"TCPPortV": VNCTCPPort, "UDPPortV": VNCUDPPort, "InstanceGroupIDV": VNCInstanceGroupID,
                    "ServiceInstanceIDV": VNCServiceInstanceID, "ServiceInstancePasswordV": VNCServiceInstancePassword,
                    "ServiceAddressV": VNCServiceAddress, "AdaptorAddressV": VNCAdaptorAddress,
                    "AdapterServiceV": VNCAdaptorService, "MasterDBServerV": ICEMasterIP,
                    "MasterDBPortV": ICEMasterPort,
                    "BackupDBServerV": ICEReplicaIP, "BackupDBPortV": ICEReplicaPort,
                    "ManagerServiceIPv4AddrV": ManagerServiceIPv4Addr}
        xmlInstance.update(VNCValue)
        newFilePath = "./TmpFile/vnc/NewServiceConfig.xml"
        oldFilePath = "./TmpFile/vnc/ServiceConfig.xml"
        VNCObj = lxml.etree.parse(oldFilePath)
        self.modifyXMLFile(newFilePath, VNCObj, **xmlInstance)
        # after finished used the dic, clear it so that next time the vnc value not in the dic
        xmlInstance.clear()
        # Remove file and Rename file
        os.remove(oldFilePath)
        os.rename(newFilePath, oldFilePath)
    def modifyWhiteBoardConfigFile(self,WhiteBoardIP,WhiteBoardPort,WBTCPPort,WBUDPort,WBInstanceGroupID,WBServiceInstanceID,WBServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr):
        xmlInstance = self.xmlObj()
        WBServiceAddress = "TCP:" + WhiteBoardIP + ":" + WhiteBoardPort
        WBAdaptorAddress = WBServiceAddress
        WBAdaptorService = WBServiceAddress

        WBValue = {"TCPPortV": WBTCPPort, "UDPPortV": WBUDPort, "InstanceGroupIDV": WBInstanceGroupID,
                   "ServiceInstanceIDV": WBServiceInstanceID, "ServiceInstancePasswordV": WBServiceInstancePassword,
                   "ServiceAddressV": WBServiceAddress, "AdaptorAddressV": WBAdaptorAddress,
                   "AdapterServiceV": WBAdaptorService, "MasterDBServerV": ICEMasterIP, "MasterDBPortV": ICEMasterPort,
                   "BackupDBServerV": ICEReplicaIP, "BackupDBPortV": ICEReplicaPort,
                   "ManagerServiceIPv4AddrV": ManagerServiceIPv4Addr}
        xmlInstance.update(WBValue)
        newFilePath = "./TmpFile/whiteboard/NewServiceConfig.xml"
        oldFilePath = "./TmpFile/whiteboard/ServiceConfig.xml"
        WBObj = lxml.etree.parse(oldFilePath)
        self.modifyXMLFile(newFilePath, WBObj, **xmlInstance)
        xmlInstance.clear()
        # Remove file and Rename file
        os.remove(oldFilePath)
        os.rename(newFilePath, oldFilePath)

    def modifyAvConfigFile(self,AVIP,AVTCPPort,AVUDPort,AVInstanceGroupID,AVServiceInstanceID,AVServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr):
        xmlInstance = self.xmlObj()
        AVServiceAddress = "TCP:" + AVIP + ":" + AVTCPPort + ";" + "UDP:" + AVIP + ":" + AVTCPPort
        AVAdaptorAddress = "TCP:" + AVIP + ":" + AVTCPPort + ";" + "UDP:" + AVIP + ":" + AVTCPPort
        AVAdaptorService = "TCP:" + AVIP + ":" + AVTCPPort + ";" + "UDP:" + AVIP + ":" + AVTCPPort

        AVValue = {"TCPPortV": AVTCPPort, "UDPPortV": AVUDPort, "InstanceGroupIDV": AVInstanceGroupID,
                   "ServiceInstanceIDV": AVServiceInstanceID,
                   "ServiceInstancePasswordV": AVServiceInstancePassword, "ServiceAddressV": AVServiceAddress,
                   "AdaptorAddressV": AVAdaptorAddress,
                   "AdapterServiceV": AVAdaptorService, "MasterDBServerV": ICEMasterIP, "MasterDBPortV": ICEMasterPort,
                   "BackupDBServerV": ICEReplicaIP,
                   "BackupDBPortV": ICEReplicaPort, "ManagerServiceIPv4AddrV": ManagerServiceIPv4Addr}
        xmlInstance.update(AVValue)
        newFilePath = "./TmpFile/av/NewServiceConfig.xml"
        oldFilePath = "./TmpFile/av/ServiceConfig.xml"
        AVObj = lxml.etree.parse(oldFilePath)
        self.modifyXMLFile(newFilePath, AVObj, **xmlInstance)
        xmlInstance.clear()
        # Remove file and Rename file
        os.remove(oldFilePath)
        os.rename(newFilePath, oldFilePath)



if __name__ == "__main__":
    a=MofidyFSPFile()
    # print "start time",time.ctime()
    t1=datetime.datetime.now()
    print "start time",t1
    # DB info
    dbHost = "192.168.7.105"
    dbPort = "3306"
    dbName = "fsp_sss_db"
    dbUser = "root"
    dbPwd = "Pass@1234"

    # Access config info
    ACTCPPort="1089"
    ACUDPPort="1089"
    ACServiceInstanceID="access_instance_1"
    ACServiceInstancePassword="access_instance_fsp"
    HTTPServiceListenPort="3000"
    AccessMasterIP="192.168.7.106"
    AccessMasterPort="1089"
    HTTP2ServicePort="3000"

    # ICEMaster config Info
    ICEMasterIP = "192.168.7.105"
    ICEMasterPort = "10000"

    # ICEReplicaInfo
    ICEReplicaIP = "192.168.7.106"
    ICEReplicaPort = "10001"

    ManagerIP="192.168.7.105"
    ManagerPort="1089"
    ManagerServiceIPv4Addr = "TCP:" + ManagerIP + ":" + ManagerPort

    # av config info
    AVIP="192.168.7.108"
    AVTCPPort="1089"
    AVUDPort="1089"
    AVInstanceGroupID="1"
    AVServiceInstanceID="av_instance_1"
    AVServiceInstancePassword="av_instance_fsp"

    # vnc config info
    VNCIP="192.168.7.108"
    VNCPort="1091"
    VNCTCPPort="1089"
    VNCUDPPort="1089"
    VNCInstanceGroupID="0"
    VNCServiceInstanceID="vnc_instance_1"
    VNCServiceInstancePassword="vnc_instance_fsp"


    WhiteBoardIP="192.169.7.108"
    WhiteBoardPort="1093"

    WBTCPPort="1089"
    WBUDPort="1089"
    WBInstanceGroupID="1"
    WBServiceInstanceID="white_board_instance_1"
    WBServiceInstancePassword="white_board_instance_fsp"


    accessIP1="sss.168.7.106"
    accessPort1="10000"
    accessIP2="ggg.168.7.106"
    accessPort2="10001"
    ListenPort="22222"

    # # Access config file
    # a.modifyAccessConfigFile(ACTCPPort,ACUDPPort,ACServiceInstanceID,ACServiceInstancePassword,HTTPServiceListenPort,ManagerServiceIPv4Addr,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort)
    #
    # # AV config file
    # a.modifyAvConfigFile(AVTCPPort,AVUDPort,AVInstanceGroupID,AVServiceInstanceID,AVServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr)
    #
    # # ICE master config
    # a.ICEMasterConfigFile(ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,dbHost,dbPort,dbName,dbUser,dbPwd)
    #
    # # ICE Replica config
    # a.ICEReplicaConfigFile(ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,dbHost,dbPort,dbName,dbUser,dbPwd)
    #
    # # Manager config file
    # a.mofidfyManagerConfigFile(ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort)
    #
    # # VNC config info:
    # a.modifyVncConfigFile(VNCTCPPort,VNCUDPPort,VNCInstanceGroupID,VNCServiceInstanceID,VNCServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr)
    #
    # # Whiteboard config info
    # a.modifyWhiteBoardConfigFile(WBTCPPort,WBUDPort,WBInstanceGroupID,WBServiceInstanceID,WBServiceInstancePassword,ICEMasterIP,ICEMasterPort,ICEReplicaIP,ICEReplicaPort,ManagerServiceIPv4Addr)
    a.modifyNgixConfigFile(accessIP1,accessPort1,accessIP2,accessPort2,ListenPort)




    # print "end time: ",time.ctime()
    t2=datetime.datetime.now()
    print "end time: ", t2

    print t2-t1