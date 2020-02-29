from page.page import Page
from tools.get_driver import get_driver
from tools.read_yaml import read_yaml

"""构造发布心情数据"""
data = read_yaml("club.yaml", "test_club")[0]
mood_text = data.get("mood_text")
target_type = data.get("target_type")
expect_msg = data.get("expect_msg")
toast_msg_text = data.get("toast_msg_text")
toast_msg_type = data.get("toast_msg_type")


class TestClub:

    # 1. 初始化
    def setup_class(self):
        # 获取driver
        self.driver = get_driver()
        # 获取Page对象
        self.page = Page(self.driver)
        # 调用PageIndex中 业务方法（关闭弹窗、点击我的）
        self.page.index_page.page_index_init()
        # 点击登录/注册
        self.page.home_page.page_click_login_reg()
        # 调用成功登录依赖方法
        self.page.login_page.page_login_success()
        # 点击签到
        self.page.login_page.page_click_sign()
        # 点击 驾考圈
        self.page.index_page.page_click_club()
        # 调用 选择图片业务方法
        self.page.club_page.page_common_img()

    # 2. 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    # 3. 发布心情成功测试方法
    def test01_publish_success(self, mood_text=mood_text, target_type=target_type):
        try:
            # 输入心情
            self.page.club_page.page_input_mood(mood_text)
            # 选择分类
            self.page.club_page.page_click_type(target_type)
            # 点击发布
            self.page.club_page.page_click_publish()
            # 断言是否发布成功
            result = self.page.club_page.page_if_success(target_type, mood_text)
            print("发布文章是否成功：", result)
            assert result, "发布文章失败！没有找到指定的心情文章"
        except:
            # 截图
            self.page.club_page.base_get_img()
            # 抛异常
            raise
        finally:
            # 调用 选择图片业务方法
            self.page.club_page.page_common_img()

    # 4. 发布心情失败 -> 返回提示信息
    def test02_publish_back(self, expect=expect_msg):
        try:
            # 返回
            self.page.club_page.page_click_back()
            # 断言
            result = self.page.club_page.page_get_info_text()
            print("提示信息为：", result)
            assert expect in result, "断言失败！"
            # 确认返回
            self.page.club_page.page_click_back_confirm()
        except:
            # 截图
            self.page.club_page.base_get_img()
            # 抛异常
            raise
        finally:
            # 调用 选择图片业务方法
            self.page.club_page.page_common_img()

    # 5. 发布心情失败 ->请填写帖子内容
    def test03_publish_text(self, toast_msg=toast_msg_text):
        try:
            # 点击发布
            self.page.club_page.page_click_publish()
            # 断言toast
            result = self.page.club_page.base_get_toast(toast_msg)
            print("获取的toast消息为：", result)
            assert toast_msg in result, "断言失败！"
        except:
            # 截图
            self.page.club_page.base_get_img()
            # 抛异常
            raise

    # 6. 发布心情失败 ->请选择帖子标签
    def test04_publish_type(self, expect=toast_msg_type, mood_text=mood_text):
        try:
            # 输入心情
            self.page.club_page.page_input_mood(mood_text)
            # 点击发布
            self.page.club_page.page_click_publish()
            # 断言toast
            result = self.page.club_page.base_get_toast(expect)
            print("获取的toast提示信息为：", result)
            assert expect in result
        except:
            # 截图
            self.page.club_page.base_get_img()
            # 抛异常
            raise
