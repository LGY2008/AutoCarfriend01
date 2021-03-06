from appium import webdriver


# 获取driver
def get_driver():
    # 定义空字典
    desired_caps = {}
    # 指定平台名称 必须写对
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 不能为空，可以随便写
    desired_caps['deviceName'] = 'emulator-5554'
    # 包名
    desired_caps['appPackage'] = "com.bjcsxq.chat.carfriend"
    # 启动名
    desired_caps['appActivity'] = ".module_main.activity.MainActivity"
    # toast
    desired_caps['automationName'] = "Uiautomator2"
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 是否重置应用 True:不重置 False:重置
    desired_caps['noReset'] = False

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)