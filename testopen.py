# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/31 10:02
@Auth ： Mr. love nza
@Company ：Even in darkness, it is possible to create light
@Function ：请输入模块功能描述
"""
from selenium import webdriver

import  time
from selenium.webdriver.common.by import  By


def run_webdriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  #不自动关闭浏览器
    options.add_argument('--start-maximized')#浏览器窗口最大化
    driver = webdriver.Chrome(options=options)
    driver.get('https://open.163.com')


    driver.implicitly_wait(5)  # 隐式等待
    # ele = driver.find_element('id', 'urs_login_btn')
    ele = driver.find_element('xpath','//*[@id="urs_login_btn"]').click()
    # driver.implicitly_wait(5)  # 隐式等待

    # 点击登录后 点击登录窗口右上角的切换登录方式
    # # 切换到 iframe
    iframes = driver.find_elements('calss name',"page")
    for iframe in iframes:
        try:
            # 将上下文切换到当前的 iframe 中
            driver.switch_to.frame(iframe)

            # 在当前 iframe 中尝试定位元素
            element = driver.find_element('class name',"normal-login-btn")

            # 如果找到要定位的元素，退出循环
            break

        except:
            # 如果在当前 iframe 中定位元素失败，则切换到下一个 iframe
            driver.switch_to.default_content()
            continue


if __name__ == '__main__':
    run_webdriver()
    print()


