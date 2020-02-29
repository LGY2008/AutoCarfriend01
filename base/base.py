import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找方法
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息 格式：元组或列表
        :param timeout: 超时时间
        :param poll: 访问频率
        :return: 元素
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 1. 获取元素
        el = self.base_find(loc)
        # 2. 调用清空
        el.clear()
        # 3. 输入
        el.send_keys(value)

    # 获取toast
    def base_get_toast(self, message):
        # 1. 组装 loc定位信息
        loc = By.XPATH, "//*[contains(@text,'%s')]" % message
        # 2. 调用text 重点：修改访问频率和超时时间
        return self.base_find(loc, timeout=5, poll=0.1).text

    # 获取文本/昵称
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 拖拽方法
    def base_drag_and_drop(self, start_loc, end_loc):
        # 查找起点元素
        start_el = self.base_find(start_loc)
        # 查找结束点元素
        end_el = self.base_find(end_loc)
        # 调用拖拽方法
        self.driver.drag_and_drop(start_el, end_el)

    # 截图
    def base_get_img(self):
        # 1. 调用截图api方法
        self.driver.get_screenshot_as_file("./image/err.png")
        # 2. 调用将图片写入报告方法
        self.__base_write_img()

    # 将图片写入 报告
    def __base_write_img(self):
        with open("./image/err.png", "rb") as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)

    # 判断 页面是否包含指定文本的元素
    def base_if_element_exists(self, text):
        # 1. 组合文本元素定位信息
        loc = By.XPATH, "//*[contains(@text,'%s')]" % text
        try:
            # 查找元素（重点修改 超时时间）
            self.base_find(loc, timeout=3)
            # 返回 True
            return True
        except:
            # 返回False
            return False