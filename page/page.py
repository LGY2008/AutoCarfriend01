from page.page_club import PageClub
from page.page_home import PageHome
from page.page_index import PageIndex
from page.page_login import PageLogin


class Page:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获取首页对象
    @property
    def index_page(self):
        return PageIndex(self.driver)

    # 获取主页对象
    @property
    def home_page(self):
        return PageHome(self.driver)

    # 获取登录页面对象
    @property
    def login_page(self):
        return PageLogin(self.driver)

    # 获取驾考圈页面对象
    @property
    def club_page(self):
        return PageClub(self.driver)