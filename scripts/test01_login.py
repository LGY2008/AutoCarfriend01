import pytest

from page.page import Page
from tools.get_driver import get_driver
from tools.read_yaml import read_yaml


class TestLogin:
    # 1. 初始化
    def setup_class(self):
        # 获取driver
        self.driver = get_driver()
        # 获取统一入口类
        self.page = Page(self.driver)
        # 调用page_index中业务方法（关闭更新、点击我的）
        self.page.index_page.page_index_init()
        # 点击登录注册
        self.page.home_page.page_click_login_reg()

    # 2. 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    # 3. 测试方法
    @pytest.mark.parametrize("args", read_yaml("login.yaml", "test_login"))
    def test_login(self, args):
        username = args.get("username")
        pwd = args.get("pwd")
        expect = args.get("expect")
        success = args.get("success")
        # 1. 调用登录业务方法
        self.page.login_page.page_login(username, pwd)
        # 登录成功：
        if success:
            try:
                # 调用点击签到
                self.page.login_page.page_click_sign()
                # 断言昵称
                nickname = self.page.home_page.page_get_nickname()
                print("获取的昵称为：", nickname)
                assert nickname == expect, "断言昵称错误， 登录的昵称为：%s 预期昵称为：%s" % (nickname, expect)
            except:
                # 截图
                self.page.login_page.base_get_img()
                # 抛异常
                raise
            finally:
                # 退出登录
                self.page.home_page.page_logout()
        # 登录失败
        else:
            try:
                # 断言toast
                toast_msg = self.page.login_page.page_get_toast(expect)
                print("toast提示消息为：", toast_msg)
                assert expect in toast_msg, "断言toast错误！预期：%s 不属于 %s" % (expect, toast_msg)
            except:
                # 截图
                self.page.login_page.base_get_img()
                # 抛异常
                raise
