import random
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
print("-------您正在使用rubisco的腾讯文档自动填写脚本------")
print("-version1.1-")
url = input("请输入问卷地址：")
f = open('path.txt', "r")
driver = Chrome(f.read())
driver.get(url)
driver.minimize_window()


def auto():
    driver.maximize_window()
    try:
        driver.find_element_by_css_selector("button.white.loginBt").click()
    except:
        print("好像什么地方出错了！请手动登陆")
        by_hand()
        pass


# ByHand
def by_hand():
    driver.minimize_window()
    print("******重要提示******")
    print("在您执行之前请确认已经完成手工登录")
    print("*********************************")
    input("知道了，现在去登陆")
    driver.maximize_window()
    input("如果您登陆好了，请按【ENTER】继续")


############
# 自动填写部分#
############

def randomtemp(low,high):
    temp = random.uniform(low, high)
    lstemp = str(temp)
    endtemp = lstemp[0:4]
    return endtemp


def persion():
    # 自动体温
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp(36.0, 36.5))
    ActionChains(driver).key_down(Keys.TAB).perform()
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp(36.4, 36.9))
    ActionChains(driver).key_down(Keys.TAB).perform()
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp(36.1, 36.6))
    # 正常
    ActionChains(driver).key_down(Keys.TAB).perform()
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys("正常")
    ActionChains(driver).key_down(Keys.TAB).perform()
    # 是否在宿舍
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys("是")
    pass



def changerow():
    ActionChains(driver).key_down(Keys.ENTER).perform()
    for time in range(0, 4):
        ActionChains(driver).key_down(Keys.LEFT).perform()


# 开始定位
def inItDefaultKey():  # 这两个操作是为了保证每次从表格开头进行
    for time in range(0, 299):
        ActionChains(driver).key_down(Keys.UP).perform()

    for time in range(0, 35):
        ActionChains(driver).key_down(Keys.LEFT).perform()


def pointIt():
    driver.minimize_window()
    num = int(input("请输入宿舍第一个人所在的行号："))
    driver.maximize_window()
    for i in range(0, num - 3):  # 这里的循环的次数，修改为自己的信息所在的行号。
        ActionChains(driver).key_down(Keys.ENTER).perform()
    day = int(datetime.datetime.now().weekday() + 1)
    for j in range(0, day):
        for i in range(0, 5):
            ActionChains(driver).key_down(Keys.TAB).perform()
    ActionChains(driver).key_down(Keys.LEFT).perform()
    ActionChains(driver).key_down(Keys.LEFT).perform()


# 序号=i++
def getNumber():  # 个性化宿舍人数
    driver.minimize_window()
    people = int(input("请输入宿舍人数："))
    driver.maximize_window()
    for i in range(0, people):
        persion()
        changerow()


mod = int(input("请选择登陆模式，手动登录输入0，自动登陆（需要挂起qq）输入1\n注意，其他输入默认需要手动登陆,自动登陆可能会存在bug\n"))
if mod == 1:
    auto()
else:
    by_hand()
inItDefaultKey()
pointIt()
getNumber()