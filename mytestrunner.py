import uummtt
import unittest

mysuite =unittest.TestSuite()
mysuite.addTest(uummtt.MyTestCase("test_loginSuccess"))
# mysuite.addTest(uummtt.MyTestCase("test_anything"))
# case = unittest.TestLoader().loadTestsFromTestCase(uummtt.MyTestCase)
# mysuite = unittest.TestSuite([case])
# mysuite.addTest(uummtt.MyTestCase("test_something"))
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)