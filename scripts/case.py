import unittest
from po.teacher import *
class Test_Teacher(unittest.TestCase):
    def setUp(self):

        self.a = Add_Teacher()
        self.driver=self.a.open()
    def zhixing(self,driver):
        resulte=self.a.teacher_op(driver)
        return resulte
    def test_001(self):
        r=self.zhixing(self.driver)
        self.assertEqual(r,'会员管理')
if __name__ == '__main__':
    unittest.main()