
from TransferFile import TransferFSPFile as tf

class StartService(object):
    def __init__(self):
        pass

    @classmethod
    def startAv(self,hostname, port, username, password,basePath):
        # for single one
        # execmd="cd "+basePath+"/av\n./service"
        execmd="systemctl start av"
        tf.sshclient_execmd(hostname, port, username, password, execmd)

    @classmethod
    def startAccess(self,hostname, port, username, password):
        # execmd = "cd "+basePath+"/access\n./service"
        execmd = "systemctl start access"
        # execmd="cd /root\n screen -R myav"
        tf.sshclient_execmd(hostname, port, username, password, execmd)

    @classmethod
    def startIceMaster(self,hostname, port, username, password,basePath):
        execmd = "cd " + basePath + "/ice_master\nicegridregistry --Ice.Config=config.master --daemon --nochdir"
        tf.sshclient_execmd(hostname, port, username, password, execmd)
        execmd2="cd " + basePath + "/ice_master\nicegridnode --Ice.Config=config.node1 --daemon --nochdir"
        tf.sshclient_execmd(hostname, port, username, password, execmd2)

    @classmethod
    def startIceReplica(self,hostname, port, username, password,basePath):
        execmd = "cd " + basePath + "/access\n./service"
        tf.sshclient_execmd(hostname, port, username, password, execmd)
        execmd2 = "cd " + basePath + "/ice_replica\nicegridnode --Ice.Config=config.node2 --daemon --nochdir"
        tf.sshclient_execmd(hostname, port, username, password, execmd2)
        execmd3="icegridadmin --Ice.Config=config.client -e \"application add 'application.xml'\""
        tf.sshclient_execmd(hostname, port, username, password, execmd3)

    @classmethod
    def startManager(self,hostname, port, username, password):
        # execmd = "cd " + basePath + "/manager\n./service"
        execmd = "systemctl start manager"

        tf.sshclient_execmd(hostname, port, username, password, execmd)

    @classmethod
    def startVnc(self,hostname, port, username, password,basePath):
        # execmd = "cd " + basePath + "/vnc\n./service"
        execmd = "systemctl start vnc"
        tf.sshclient_execmd(hostname, port, username, password, execmd)

    @classmethod
    def startWhiteBoard(self,hostname, port, username, password,basePath):
        # execmd = "cd " + basePath + "/whiteboard\n./service"
        execmd = "systemctl start whiteboard"
        tf.sshclient_execmd(hostname, port, username, password, execmd)

    @classmethod
    def startNginx(self,hostname, port, username, password):
        execmd="systemctl start nginx"
        tf.sshclient_execmd(hostname, port, username, password, execmd)


if __name__ == "__main__":
    hostname="192.168.153.128"
    port=22
    username="root"
    password="123456"
    basePath="/fsmeeting/sss"
    ss=StartService()
    ss.startAccess(hostname, port, username, password,basePath)
