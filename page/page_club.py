from selenium.webdriver.common.by import By

from base.base import Base
import page


class PageClub(Base):
    # 点击相机
    def page_click_camera(self):
        self.base_click(page.club_camera)

    # 选择图片
    def page_click_img(self):
        self.base_click(page.club_img)

    # 点击完成
    def page_click_done(self):
        self.base_click(page.club_done)

    # 输入心情
    def page_input_mood(self, mood_text):
        self.base_input(page.club_mood, mood_text)

    # 选择标签分类
    def page_click_type(self, target_type):
        # 1. 组装loc
        loc = By.XPATH, "//*[@text='%s']" % target_type
        # 2. 调用点击方法
        self.base_click(loc)

    # 点击发布
    def page_click_publish(self):
        self.base_click(page.club_publish)

    # 判断是否发布成功（指定标签下->心情文章）
    def page_if_success(self, target_type, mood_text):
        # 点击指定标签
        loc = By.XPATH, "//*[@text='%s']" % target_type
        self.base_click(loc)
        # 判断是否存在包含指定文本的元素
        return self.base_if_element_exists(mood_text)

    # 点击返回
    def page_click_back(self):
        self.base_click(page.club_back)

    # 获取提示信息文本
    def page_get_info_text(self):
        return self.base_get_text(page.club_info)

    # 点击确认退出
    def page_click_back_confirm(self):
        self.base_click(page.club_back_confirm)

    # 组合退出提示业务方法
    def page_back(self):
        self.page_click_back()
        self.page_click_back_confirm()

    # 组合选择图片业务方法
    def page_common_img(self):
        self.page_click_camera()
        self.page_click_img()
        self.page_click_done()
