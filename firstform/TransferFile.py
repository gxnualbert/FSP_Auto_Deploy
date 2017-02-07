# -*- coding:utf-8 -*-
import paramiko
import os
import shutil
import sys
import datetime

class TransferFSPFile(object):
    def __init__(self):
        pass

    @classmethod
    def sshclient_execmd(self,hostname, port, username, password, execmd):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        print stdout.read()
        # print stderr.read()

        s.close()

    @classmethod
    def mutipCmd(self,hostname, port, username, password, *execmd):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)

        for cmd in range(len(execmd)):
            print "now run cmd:",execmd[cmd]
            stdin, stdout, stderr = s.exec_command(execmd[cmd])
            print stdout.read()
            print stderr.read()

        s.close()

    @classmethod
    def downloadFile(self,host,port,user,password,remotefile_path,local_file_path):
        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remotefile_path,local_file_path )
        sftp.close()

    @classmethod
    def uploadFile(self,host,port,user,password,local_file_path,remotefile_path):
        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_file_path,remotefile_path)
        sftp.close()

        # jdgue whether the folder exit, if not exist, then create it, if exist, then empty the folder

    @classmethod
    def prepareFolder(self):
        if os.path.exists("./TmpFile"):
            shutil.rmtree("./TmpFile")
            os.mkdir("./TmpFile")
        else:
            os.mkdir("./TmpFile")
        accessPath="./TmpFile/access"
        avPath="./TmpFile/av"
        iceMasterPath="./TmpFile/ice_master/"
        iceReplicaPath="./TmpFile/ice_replica"
        managerPath="./TmpFile/manager"
        vncPath="./TmpFile/vnc"
        whiteboardPath="./TmpFile/whiteboard"
        nginxPath="./TmpFile/nginx"
        pathList=[accessPath,avPath,iceMasterPath,iceReplicaPath,managerPath,vncPath,whiteboardPath,nginxPath]
        for folderPath in pathList:
            try:
                if os.path.exists(folderPath):
                    shutil.rmtree(folderPath)
                    os.mkdir(folderPath)
                else:
                    os.mkdir(folderPath)
            except Exception, e:
                print e
                raise e
        # create nginx tmp file
        tmpFileList=['user root;\n', 'worker_processes auto;\n', 'error_log /var/log/nginx/error.log;\n', '#pid /run/nginx.pid;\r\n', 'events {\n', '    worker_connections 1024;\n', '}\n', '\n', 'stream {\n', '    upstream http2_access {\n', '        # default: round-robin\n', '        server XXX.XXX.XXX.XXX:xxxx;\n', '        server YYY.YYY.YYY.YYY:yyyy;\n', '    }\n', '\n', '    server {\n', '        listen AAAAA;\n', '        proxy_pass http2_access;\n', '    }\n', '\n', '}\n']
        tmpFilePath = "./TmpFile/nginx/tmp.nginx.conf"
        # read tmp file
        # create new file and write file
        writeFile = open(tmpFilePath, 'w')
        writeFile.writelines(tmpFileList)
        writeFile.close()
    @classmethod
    def installAccess(self,hostname, port, username, password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh access")

    @classmethod
    def installAv(self,hostname, port, username, password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh av")

    @classmethod
    def installIceMaster(self,hostname,port,username,password,sss):
        self.sshclient_execmd(hostname,port,username,password,"cd /root/"+sss+"\npwd\n./install.sh ice_master")
        self.sshclient_execmd(hostname,port,username,password,"source /etc/profile")

    @classmethod
    def installIceReplica(self,hostname,port,username,password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh ice_replica")
        self.sshclient_execmd(hostname, port, username, password, "source /etc/profile")

    @classmethod
    def installManager(self,hostname, port, username, password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh manager")

    @classmethod
    def installVnc(self,hostname, port, username, password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh vnc")

    @classmethod
    def installWhiteboard(self,hostname, port, username, password,sss):
        self.sshclient_execmd(hostname, port, username, password, "cd /root/" + sss + "\npwd\n./install.sh whiteboard")

    @classmethod
    def installNginx(self,hostname, port, username, password):
        self.sshclient_execmd(hostname, port, username, password,"rm -f /var/lib/rpm/__db*\nrpm –rebuilddb\nyum install nginx\n./install.sh nginx_conf" )

    @classmethod
    def transferAccessFile(self,accessip,port, username, password,basePath,isUpload="N"):
        accessRemoteConfigPath = basePath+"/access/ServiceConfig.xml"
        accessLocalPath = "./TmpFile/access/ServiceConfig.xml"
        if isUpload.lower() == "y":
            self.uploadFile(accessip, port, username, password, accessLocalPath, accessRemoteConfigPath)
        else:
            self.downloadFile(accessip, port, username, password, accessRemoteConfigPath, accessLocalPath)

    @classmethod
    def transferAvFile(self,avip,port, username, password,basePath,isUpload="N"):
        # avip = "192.168.153.128"
        avRemoteConfigPath = basePath+"/av/ServiceConfig.xml"
        avLocalPath = "./TmpFile/av/ServiceConfig.xml"
        if isUpload.lower() == "y":
            self.uploadFile(avip, port, username, password, avLocalPath, avRemoteConfigPath)
        else:
            self.downloadFile(avip, port, username, password, avRemoteConfigPath, avLocalPath)

    @classmethod
    def transferMasterFile(self,iceMasterIp,port, username, password,basePath,isUpload="N"):
        # iceMasterIp = "192.168.153.128"
        iceMasterRemoteConfigPath = basePath+"/ice_master/config.master"
        iceMasterNode1RemoteConfigPath = basePath+"/ice_master/config.node1"
        iceMasterServiceRemoteConfigPath =  basePath+"/ice_master/config.server"
        iceMasterLocalPath = "./TmpFile/ice_master/config.master"
        iceMasterNode1LocalPath = "./TmpFile/ice_master/config.node1"
        iceMasterServerLocalPath = "./TmpFile/ice_master/config.server"
        if isUpload.lower()=="y":
            self.uploadFile(iceMasterIp,port,username,password,iceMasterLocalPath,iceMasterRemoteConfigPath)
            self.uploadFile(iceMasterIp,port,username,password,iceMasterNode1LocalPath,iceMasterNode1RemoteConfigPath)
            self.uploadFile(iceMasterIp,port,username,password,iceMasterServerLocalPath,iceMasterServiceRemoteConfigPath)
        else:
            self.downloadFile(iceMasterIp, port, username, password, iceMasterRemoteConfigPath, iceMasterLocalPath)
            self.downloadFile(iceMasterIp, port, username, password, iceMasterNode1RemoteConfigPath,iceMasterNode1LocalPath)
            self.downloadFile(iceMasterIp, port, username, password, iceMasterServiceRemoteConfigPath,iceMasterServerLocalPath)

    @classmethod
    def transferReplicaFile(self,iceReplicaip,port, username, password,basePath,isUpload="N"):
        # iceReplicaip = "192.168.153.128"
        iceReplicaRemoteConfigPath = basePath+"/ice_replica/config.replica"
        iceReplicaNode2RemoteConfigPath = basePath+"/ice_replica/config.node2"
        iceReplicaServerRemoteConfigPath = basePath+"/ice_replica/config.server"
        iceReplicaLocalPath = "./TmpFile/ice_replica/config.replica"
        iceReplicaNode2LocalPath = "./TmpFile/ice_replica/config.node2"
        iceReplicaServerLocalPath = "./TmpFile/ice_replica/config.server"
        if isUpload.lower()=="y":
            self.uploadFile(iceReplicaip, port, username, password, iceReplicaLocalPath, iceReplicaRemoteConfigPath)
            self.uploadFile(iceReplicaip, port, username, password, iceReplicaNode2LocalPath,
                            iceReplicaNode2RemoteConfigPath)
            self.uploadFile(iceReplicaip, port, username, password, iceReplicaServerLocalPath,
                            iceReplicaServerRemoteConfigPath)


        else:
            self.downloadFile(iceReplicaip, port, username, password, iceReplicaRemoteConfigPath, iceReplicaLocalPath)
            self.downloadFile(iceReplicaip, port, username, password, iceReplicaNode2RemoteConfigPath,
                              iceReplicaNode2LocalPath)
            self.downloadFile(iceReplicaip, port, username, password, iceReplicaServerRemoteConfigPath,
                              iceReplicaServerLocalPath)

    @classmethod
    def transferManagerFile(self,managerIp, port, username, password, basePath,isUpload="N"):
        # managerIp = "192.168.153.128"
        managerRemoteConfigPath = basePath+"/manager/ServiceConfig.xml"
        managerLocalPath = "./TmpFile/manager/ServiceConfig.xml"
        if isUpload.lower()=="y":
            self.uploadFile(managerIp, port, username, password, managerLocalPath, managerRemoteConfigPath)
        else:

            self.downloadFile(managerIp, port, username, password, managerRemoteConfigPath, managerLocalPath)

    @classmethod
    def transferVncFile(self,vncIp, port, username, password,basePath,isUpload="N"):
        # vncIp = "192.168.153.128"
        vncRemoteConfigPath = basePath+"/vnc/ServiceConfig.xml"
        vncLocalPath = "./TmpFile/vnc/ServiceConfig.xml"
        if isUpload.lower()=="y":
            self.uploadFile(vncIp, port, username, password, vncLocalPath, vncRemoteConfigPath)
        else:

            self.downloadFile(vncIp, port, username, password, vncRemoteConfigPath, vncLocalPath)

    @classmethod
    def transferWBFile(self,wbIp, port, username, password,basePath,isUpload="N"):
        # wbIp = "192.168.153.128"
        wbRemoteConfigPath = basePath+"/whiteboard/ServiceConfig.xml"
        wbLocalPath = "./TmpFile/whiteboard/ServiceConfig.xml"
        if isUpload.lower() == "y":
            self.uploadFile(wbIp,port,username,password,wbLocalPath,wbRemoteConfigPath)
        else:
            self.downloadFile(wbIp, port, username, password, wbRemoteConfigPath, wbLocalPath)

    @classmethod
    def transferNginxFile(self,nginxIp, port, username, password,isUpload="N"):
        nginxRemoteConfigPath="/etc/nginx/nginx.conf"
        nginxLocalPath="./TmpFile/nginx/nginx.conf"
        if isUpload.lower() == "y":
            self.uploadFile(nginxIp,port,username,password,nginxLocalPath,nginxRemoteConfigPath)
        else:
            self.downloadFile(nginxIp, port, username, password, nginxRemoteConfigPath, nginxLocalPath)



if __name__ == "__main__":

    global port
    global username
    global password
    global sss
    t1 = datetime.datetime.now()
    print "start time", t1
    b=TransferFSPFile()

    hostname = "192.168.153.128"
    port = 22
    username = 'root'
    password = '123456'
    basePath="/fsmeeting/sss"

    # #download package and install

    # '''download the package from the url'''
    packageURL="http://192.168.5.30:8080/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_sss/lastSuccessfulBuild/artifact/sss-1.2.2.1.tar.gz"
    packageName=packageURL.split("/")[-1]#sss-1.2.2.1.tar.gz
    sss = packageName.split(".tar")[0] #sss-1.2.2.1
    # sss = "sss-1.2.2.1"

    execmd="cd /root\nwget "+packageURL+"\ntar -xzvf "+packageName


    b.prepareFolder()
    sys.exit()
    # b.mutipCmd(hostname,port,username,password)
    # b.sshclient_execmd(hostname, port, username, password, execmd)

    # install service
    b.installAccess(hostname,port,username,password)
    # b.installAv(hostname,port,username,password)
    # b.installIceMaster(hostname,port,username,password)
    # b.installIceReplica(hostname,port,username,password)
    # b.installManager(hostname,port,username,password)
    # b.installVnc(hostname,port,username,password)
    # b.installWhiteboard(hostname,port,username,password)


    # b.transferAccessFile(hostname,port, username, password,basePath)
    # b.transferAvFile(hostname,port, username, password,basePath)
    # b.transferMasterFile(hostname,port, username, password,basePath)
    # b.transferReplicaFile(hostname,port, username, password,basePath)
    # b.transferManagerFile(hostname,port, username, password,basePath)
    # b.transferVncFile(hostname,port, username, password,basePath)
    # b.transferWBFile(hostname,port, username, password,basePath)

    # upload file
    b.transferAccessFile(hostname,port, username, password,basePath,"Y")
    b.transferAvFile(hostname,port, username, password,basePath,"Y")
    b.transferMasterFile(hostname,port, username, password,basePath,"Y")
    b.transferReplicaFile(hostname,port, username, password,basePath,"Y")
    b.transferManagerFile(hostname,port, username, password,basePath,"Y")
    b.transferVncFile(hostname,port, username, password,basePath,"Y")
    b.transferWBFile(hostname,port, username, password,basePath,"Y")

    t2 = datetime.datetime.now()
    print "end time: ", t2

    print t2 - t1






    # modify config file


    #upload config file


    #run the service
    


    # UploadFile(hostname,username,password,local_file_path,remotefile_path)
    # mutipCmd(hostname,port,username,password,**cmds)