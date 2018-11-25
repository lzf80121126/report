import allure
import pytest
class Test01():

    @allure.step("执行登录操作")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_loging(self):
        allure.attach("","")
        allure.attach("描述：", "输入密码")
        allure.attach("描述：", "点击登录")
        print("登录成功")

    @allure.step("执行退出操作")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_logout(self):
        print("退出成功")
        try:
            assert 0
        except:
            with open("./Image/faild.png","rb")as f:
                allure.attach("失败原因请看图：",f.read(),allure.attach_type.PNG)

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_03(self):
        print("test03被执行")
if __name__ == '__main__':
    pytest.main("-s test01.py")