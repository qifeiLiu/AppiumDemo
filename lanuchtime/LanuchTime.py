# /usr/bin/python
# encoding:utf-8
import csv
import time
import subprocess
import os

class App():
    # start
    def __init__(self):
        self.listcontent = ""  #以列表形式存储内容
        self.StartTime = 0

    def LanuchApp(self):
        cmd = "adb shell am start -W -n com.sec.android.app.camera/com.sec.android.app.camera.Camera"
        subproc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        self.listcontent = subproc.stdout.read().decode().split('\n')
        time.sleep(2)
        # print(self.listcontent)


    def StopApp(self):
        # cmd = "adb shell am force-stop com.sec.android.app.camera/com.sec.android.app.camera.Camera" 冷启动
        cmd = "adb shell input keyevent 3"
        subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        self.listcontent = subproc.stdout.read().decode().split('\n')
        print(self.listcontent)


    def GetLauchedTime(self):
        for line in self.listcontent :
            print(line)
            if "ThisTime" in line:
                self.StartTime = line.split(" ")[1]
                print(self.StartTime)
                break
        return self.StartTime



class Controller():
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp","elapsedtime"),]
    #单次测试过程
    def testprocess(self):
        self.app.LanuchApp()
        elapsedtime = self.app.GetLauchedTime()
        self.app.StopApp()
        currentime = self.getCurrentTime()
        self.alldata.append((currentime,elapsedtime))
    #多次执行测试过程
    def Run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter -1
    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime

    #数据存储
    def SaveDataToCSV(self):
        # self.alldata = [('timestamp', 'elapsedtime'), ('2018-03-09 17:27:05', '712\r'),
        #                 ('2018-03-09 17:27:09', '49\r'), ('2018-03-09 17:27:13', '68\r'),
        #                 ('2018-03-09 17:27:17', '63\r'), ('2018-03-09 17:27:21', '54\r'),
        #                 ('2018-03-09 17:27:25', '58\r'), ('2018-03-09 17:27:29', '60\r'),
        #                 ('2018-03-09 17:27:32', '52\r'), ('2018-03-09 17:27:36', '63\r'),
        #                 ('2018-03-09 17:27:40', '68\r')]
        # # print(self.alldata)

        file_path =(os.path.dirname(__file__))
        # print(file_path)
        file_name = os.path.join(file_path, "startTime.csv")
        print(file_name)
        CsvFile = open(file_name,'w')
        writer = csv.writer(CsvFile)
        writer.writerows(self.alldata)
        CsvFile.close()


if __name__ == '__main__':
    # app = App()
    # app.LanuchApp()
    # app.GetLauchedTime()
    # app.StopApp()

    controller = Controller(10)
    controller.Run()
    controller.SaveDataToCSV()
    # sys.path.append(r'C:\Users\t_qifeil\AppData\Local\Android\sdk\platform-tools')
    # # print(sys.path)
    # cmd = r'adb shell am start -W -n com.sec.android.app.camera/com.sec.android.app.camera.Camera'
    # cmd1 = r"ipconfig"
    # obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    # print(str(obj.stdout.read(),'utf-8'))
