from base.base import Base
import page


class PageHome(Base):
    # 1. 点击登录/注册 连接
    def page_click_login_reg(self):
        self.base_click(page.login_reg_link)

    # 2. 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 向上拖拽 新功能介绍->我的订单
    def page_drag_and_drop_up(self):
        self.base_drag_and_drop(page.login_new_info, page.login_order)

    # 向下拖拽 我的订单->新功能介绍
    def page_drag_and_drop_down(self):
        self.base_drag_and_drop(page.login_order, page.login_new_info)

    # 点击 设置
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 点击 退出当前账号
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 点击 确认退出
    def page_click_logout_confirm(self):
        self.base_click(page.login_logout_confirm)

    # 组合退出登录 业务方法
    def page_logout(self):
        self.page_drag_and_drop_up()
        self.page_click_setting()
        self.page_click_logout()
        self.page_click_logout_confirm()
        self.page_drag_and_drop_down()
        self.page_click_login_reg()
