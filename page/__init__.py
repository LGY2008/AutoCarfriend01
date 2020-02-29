from selenium.webdriver.common.by import By

"""以下为登录模块元素配置信息"""
# 关闭 更新弹窗
login_close_alert = By.ID, "com.bjcsxq.chat.carfriend:id/bt_no"
# 我的
login_me = By.ID, "com.bjcsxq.chat.carfriend:id/mine_image"
# 登录/注册
login_reg_link = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"
# 账号
login_username = By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et"
# 密码
login_pwd = By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et"
# 登录按钮
login_btn = By.ID, "com.bjcsxq.chat.carfriend:id/login_btn"
# 签到
login_sign = By.ID, "com.bjcsxq.chat.carfriend:id/btn_neg"
# 获取昵称
login_nickname = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"
# 我的订单
login_order = By.XPATH, "//*[@text='我的订单']"
# 新功能介绍
login_new_info = By.XPATH, "//*[@text='新功能介绍']"
# 设置
login_setting = By.ID, "com.bjcsxq.chat.carfriend:id/mine_set_rl"
# 退出当前账号
login_logout = By.ID, "com.bjcsxq.chat.carfriend:id/set_logout_tv"
# 确认退出
login_logout_confirm = By.ID, "com.bjcsxq.chat.carfriend:id/bt_ok"

"""以下为驾考圈元素配置信息"""
# 驾考圈
club_menu = By.ID, "com.bjcsxq.chat.carfriend:id/apply_image"
# 相机
club_camera = By.ID, "com.bjcsxq.chat.carfriend:id/img_put_content"
# 选择照片
club_img = By.ID, "com.bjcsxq.chat.carfriend:id/v_selected"
# 点击完成
club_done = By.ID, "com.bjcsxq.chat.carfriend:id/done"
# 输入心情
club_mood = By.ID, "com.bjcsxq.chat.carfriend:id/edit_publish_conment"
# 发布
club_publish = By.ID, "com.bjcsxq.chat.carfriend:id/title_other"
# 返回
club_back = By.ID, "com.bjcsxq.chat.carfriend:id/title_back"
# 提示信息
club_info = By.ID, "com.bjcsxq.chat.carfriend:id/txt_msg"
# 确定返回
club_back_confirm = By.ID, "com.bjcsxq.chat.carfriend:id/btn_pos"
