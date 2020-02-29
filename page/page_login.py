from base.base import Base
import page


class PageLogin(Base):
    # 1. 输入账号
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 2. 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 3. 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 4. 获取toast提示信息
    def page_get_toast(self, message):
        return self.base_get_toast(message)

    # 5. 点击签到
    def page_click_sign(self):
        self.base_click(page.login_sign)

    # 6. 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 7. 组合业务方法
    def page_login_success(self, username="18610453007", pwd="qq123456"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()