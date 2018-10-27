print('------selenium实用技能汇总------')
'''
1.获取浏览器的标题栏title
2.获取浏览器当前窗口地址栏的地址
3.截屏保存当前窗口图片
4.切换窗口操作，target="_blank" 会在新窗口中打开页面
    <a href="https://www.sogou.com/" target="_blank"></a>
5.弹出对话框
    alert   消息提示框，只有一个按钮
    confirm 消息提示框，包含确认、取消两个按钮
    prompt  消息提示看，包含输入框、确认、取消三个控件
        ## 点击确认按钮
        driver.switch_to.alert.accept()
        ## 得到对话框的内容
        driver.switch_to.alert.text
        ## 点击取消按钮
        driver.switch_to.alert.dismiss()
        ## 输入文本框内容
        driver.switch_to.alert.send_keys('输入内容...')
    注意：非原生态浏览器消息提示框，即包含html元素，可以用F12查看的，还是使用之前的方法定位操作元素
6.上传文件测试方法：
    使用直接发送键盘消息给应用程序，前提是浏览器必须是当前应用
    ##  pip install pypiwin32
    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(r"d:\上传图片.jpg" + '\n')
7.刷新、前进、后退
    driver.refresh()、driver.forward()、driver.back()
8.12306网站出发地、目的地选择方法：
    先定位，在输入，在回车确定，否则定位不到
    fromEle = driver.find_element_by_id('fromStationText')
    fromEle.click()                  ## 先click定位到
    fromEle.send_keys('上海\n')       ## 在输入完之后 \n 回车确定
9.12306选择有票的二等座的车次
    //*[@id='queryLeftTable']/tr/td[4][@class]/../td[1]//a      ## 使用xpath选择器选择
10.对于鼠标放置后悬停的页面，定位时可使用在console中输入语句：
    setTimeout(function(){debugger},2000)

'''
from selenium import webdriver
import time
import traceback    ## 捕获程序异常时需要导入的包

driver = webdriver.Chrome()
# driver.get('https://www.sohu.com')
driver.get('http://intranet.hd123.com/bin/hdnet.dll/login')
driver.maximize_window()
title = driver.title
print('浏览器的title是：' + title)    ## title是根据每次页面变化而变化的，实时的

# current_url = driver.current_url
# print('获取当前窗口地址栏的地址：' + current_url)

## 实用技能3，截屏保存图片文件
# screenShot1 = driver.get_screenshot_as_file('shotfile1.png')
# screenShot2 = driver.get_screenshot_as_file('d:\python_pro\selenium_pro\shotfile2.png')
# screenShot3 = driver.get_screenshot_as_png('shotfile3.png')   ##截屏保存为二进制数据，暂不用此方法

# '''
# 以下为练习实用技能4，多个窗口切换操作
# '''
# driver.find_element_by_css_selector(".product-list [href='https://www.sogou.com/']").click()
# print('title 是 ：' + driver.title)
#
# mainHandle = driver.current_window_handle
# print('主窗口的handle为：%s' % mainHandle)
# print('打印出当前所有窗口的句柄(handles)：')
# print(driver.window_handles)
# ## 切换到新窗口
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if u'搜狗搜索引擎' in driver.title:
#         break
# print('新窗口的title为：' + driver.title)
# driver.find_element_by_css_selector('#query').send_keys('用搜狗搜百度')
# driver.find_element_by_css_selector('#stb').click()
# time.sleep(5)
# ## 关闭窗口
# driver.close()
# ## 切换到主窗口
# driver.switch_to.window(mainHandle)
# print(driver.title + ',handle 是：' + mainHandle)
# '''
# 以上为练习实用技能4，多个窗口切换操作
# '''
'''此部分为实用技能5，弹出对话框'''
# ## 得到对话框的内容(即默认提示信息内容)
# driver.switch_to.alert.text
# ## 点击确认按钮
# driver.switch_to.alert.accept()
# ## 点击取消按钮
# driver.switch_to.alert.dismiss()
# ## 输入文本框内容
# driver.switch_to.alert.send_keys('输入内容...')
'''此部分为实用技能5，弹出对话框'''
driver.find_element_by_css_selector("[onclick='CheckSubmit();']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
username = driver.find_element_by_css_selector("[name='txtUsrCode']")
username.send_keys('pangzhenying')
password = driver.find_element_by_css_selector("[name='psdUsrPassword']")
password.send_keys('1313133540wode')
driver.find_element_by_css_selector("[onclick='CheckSubmit();']").click()
try:
    driver.switch_to.alert.dismiss()
except:
    print('------程序异常错误信息捕获------')
    print(traceback.format_exc())
finally:
    driver.quit()





