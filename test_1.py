import unittest

from class_function_6 import User, TestFunc  # 引入 User 和 TestFunc

class MyTestCase(unittest.TestCase):
    def test_user_weight(self):
        user = User("Alice", 70)  # 创建 User 实例
        self.assertEqual(user.getWeight(), 70)  # 测试 getWeight 方法

    def test_testfunc(self):
        self.assertEqual(TestFunc(), 1)  # 测试 TestFunc 函数

if __name__ == '__main__':
    unittest.main()
