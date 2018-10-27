print('------selenium实用技能之鼠标键盘------')
'''
鼠标事件:
1.单击
2.双击
3.右击
4.悬停
5.拖放

键盘事件：
1.输入空格
2.全选
3.剪切
4.复制
5.粘贴
6.回车

'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    ## 引入鼠标ActionChains类
from selenium.webdriver.common.keys import Keys     ## 引入键盘Keys类
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# driver.maximize_window()
print(driver.get_window_size())     ## 获取窗口大小
driver.set_window_size(1366,768)    ## 设置浏览器窗口大小
inputText = driver.find_element_by_id('kw')
enterBtn = driver.find_element_by_id('su')
morePro = driver.find_element_by_name('tj_briicon')

# ## 鼠标右击操作
# ActionChains(driver).context_click(inputText).perform()

# ## 鼠标双击操作
# inputText.send_keys('中秋节')
# ActionChains(driver).double_click(inputText).perform()

# ## 鼠标悬停操作
# ActionChains(driver).move_to_element(morePro).perform()
# driver.find_element_by_name('tj_mp3').click()
# driver.back()

# ## 鼠标拖放
# fromEle = driver.find_element_by_name('sourceEle')
# toEle = driver.find_element_by_name('targetEle')
# ActionChains(driver).drag_and_drop(fromEle,toEle).perform()

inputText.send_keys('键盘使用练习...')
## 删除一个多输入的文字
inputText.send_keys(Keys.BACK_SPACE)

## 输入空格
inputText.send_keys(Keys.SPACE)

## 全选输入框里的内容
inputText.send_keys(Keys.CONTROL,'a')   ## 注意区分大小写a(not A)
time.sleep(2)
## 剪切输入框里的内容
inputText.send_keys(Keys.CONTROL,'x')
time.sleep(2)
## 粘贴输入框里的内容
inputText.send_keys(Keys.CONTROL,'v')
time.sleep(2)
## 回车代替单击'百度一下'
enterBtn.send_keys(Keys.ENTER)

# ## 执行JavaScript脚本
# driver.excute_script('window.scrollBy(200,300)')

driver.quit()

'''
------实现删除表格数据------
对于表格中的数据，删除后会动态更新，需要重新获取表格数据
1.因为每次都会刷新表格数据，所以只需取第一条删除即可
2.删除之后，由于表格要刷新，所以需等待1秒钟时间
3.如果表格已经删除完毕，是个空列表，则跳出循环

while True:
    delButton = driver.find_elements_by_id('delDataBtn')
    if delButton == []:
        break
    delButton[0].click()
    driver.find_element_by_id('delForSure').click()
    time.sleep(1)
'''

'''
另附：
调用系统声音进行提示，如果需要人工输入验证码的话可以这样操作
import winsound
winsound.Beep(1500,3000)
'''