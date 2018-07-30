# /usr/bin/python
# encoding:utf-8
import csv
import time
import subprocess
import os

class Controller(object):
    def __init__(self,count):
        self.counter = count
        self.alldata = [("timestamp","cpustatus"),]

    #单次测试过程
    def testprocess(self):
        cmd = 'adb shell dumpsys cpuinfo|find \"com.citrix.Receiver\"'
        subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        result = subproc.stdout.readlines()[0].decode().split("%")
        print(result)
        cpuvalue = result[0]
        # print(cpuvalue)
        currentime = self.getCurrentTime()
        self.alldata.append((currentime,cpuvalue))
        time.sleep(2)
    #多次执行测试过程
    def Run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter -1
    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime

    # #数据存储
    def SaveDataToCSV(self):
        file_path =(os.path.dirname(__file__))
        # print(file_path)
        file_name = os.path.join(file_path, "Cpustatus.csv")
        print(file_name)
        CsvFile = open(file_name,'w')
        writer = csv.writer(CsvFile)
        writer.writerows(self.alldata)
        CsvFile.close()
if __name__ == '__main__':
    controller = Controller(10)
    # controller.testprocess()
    controller.Run()
    controller.SaveDataToCSV()

