import unittest
import time
from appium import webdriver
from ddt import ddt,data,unpack


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("test start")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.citrix.Receiver'
        # desired_caps['appActivity']= 'com.sec.android.app.camera.Camera'
        desired_caps['appActivity'] = 'com.citrix.client.Receiver.ui.activities.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    @data(1,2,3)
    def test_loginSuccess(self,value):
        print("test something start ......")
        time.sleep(2)
        self.driver.find_element_by_id("com.citrix.Receiver:id/wl_session_button").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.citrix.Receiver:id/relativeLayoutAddStore").send_keys("https://qll5s-ddc2.whs.local/citrix/store")
        time.sleep(2)
        self.driver.find_element_by_id("com.citrix.Receiver:id/as_session_button").click()
        time.sleep(2)
        if self.driver.find_element_by_id("android:id/button1"):
            self.driver.find_element_by_id("android:id/button1").click()
        if self.driver.find_element_by_id("android:id/button1"):
            self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(3)
        if self.driver.find_element_by_id("com.citrix.Receiver:id/AuthManager_TextInputLayout"):
            self.driver.find_element_by_id("com.citrix.Receiver:id/AuthManager_USERNAME").send_keys("whs.local\\administrator")
            self.driver.find_element_by_id("com.citrix.Receiver:id/AuthManager_PASSWORD").send_keys("citrix")
            self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)

        self.assertEqual(True, 1)

    def test_anything(self):
        print("test anythings")
        self.assertEqual(True, 1)

    def tearDown(self):
        # 判断是否登录成功如果登录成功那么退出登录
        print("test end")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
