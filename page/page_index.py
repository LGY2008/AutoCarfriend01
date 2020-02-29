from base.base import Base
import page


class PageIndex(Base):
    # 1. 关闭更新弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 2. 点击我的
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击驾考圈
    def page_click_club(self):
        self.base_click(page.club_menu)

    # 3. 组合业务
    def page_index_init(self):
        self.page_close_alert()
        self.page_click_me()