#coding:utf-8
import logging
import logging.handlers
import time,os
# if not os.path.exists("log"):
#     os.mkdir("log")
# fileName = "./log/" + time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time())) + ".log"
# myLog=open("./log/"+fileName, 'w')
# myLog.close()
# logging.basicConfig(filename=fileName, filemode="w", level=logging.INFO)
# logger = logging.getLogger('main')
# logger.setLevel(logging.DEBUG)
# zlg_log = logging.FileHandler("zlg.log")
# formatter = logging.Formatter('%(asctime)s %(message)s')
# zlg_log.setFormatter(formatter)
#
# def log(info):
#     logger.info(info)
#
#
# log("test")



# LOG_FILE = 'tst.log'
class AddLog(object):
    def __init__(self):
        pass

    @classmethod
    def Log(self):
        if not os.path.exists("log"):
            os.mkdir("log")
        LOG_FILE =  "./log/" + time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time())) + ".log"
        Logger=time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
        print "The logger is ",Logger
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        fmt = '%(asctime)s - %(filename)s:- %(message)s'
        # fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)  # 实例化formatter
        handler.setFormatter(formatter)  # 为handler添加formatter

        logger = logging.getLogger(Logger)  # 获取名为tst的logger
        logger.addHandler(handler)  # 为logger添加handler
        logger.setLevel(logging.DEBUG)

        return logger