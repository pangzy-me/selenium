print('------css选择器 选择元素------')
'''
CSS选择器常见语法
find_elements_by_css_selector("xxx")
.class      .intro          class选择器，选择class="intro"的所有元素
#id         #firstname      id选择器，选择id="firstname"的所有元素
*           *               选择所有元素
element     p               选择所有<p>元素
ele>ele     div>input       选择父元素为<div>的所有<input>元素 ## 父子关系定位方法一
ele ele     div input       选择父元素为<div>的所有<input>元素 ## 父子关系定位方法二
ele+ele     div+input       选择同一级中紧接<div>元素后的所有<input>元素
ele~ele     food~div        选择在另一个元素后的元素，二者有相同的父元素

[attribute=value]   [target=_blank] 选择target="_blan"的所有元素
1.组(group)选择用, 逗号隔开 p,button
2.组合使用：选择id是food下面的span，和所有的p     ## 逗号的优先级最低
    #food > span , p
3.选择所有的元素，使用通配符 *   ## 选择id是food的下的直接所有子节点
    #food > * 
4.属性选择器
    可以根据元素的属性及属性值来选择元素
    *[style]
    p[spec=len2]
    p[spec='len2 len3']
    p[spec*='len2']         #包含
    p[spec^='len2']         #开头    
    p[spec$='len2']         #结尾
    p[class=special][name=p1]   #多个属性联合
5.验证CSS选择器
    1.element标签内查找 就是使用ctrl+f
    2.
'''
from selenium import  webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get('http://music.baidu.com/top/new')
## 设置浏览器窗口大小
driver.maximize_window()    ## 设置浏览器为全屏显示
# driver.set_window_size(1024,800)    ## 设置浏览器的宽、高
## 方法一：逐级使用 父元素>子元素 来定位找到元素
songList = driver.find_elements_by_css_selector("#songListWrapper>div>ul>li")  ## elements
## 方法二：父元素 子元素，使用空格隔开这种方式，只要子元素在父元素里即可，不关心层级
# songList = driver.find_elements_by_css_selector("#songListWrapper li")

for slist in songList[1:11]:
    upTags = slist.find_elements_by_class_name("up")
    if upTags:
        ## 取歌曲名字
        ## 第一种写法
        # title = slist.find_element_by_class_name("song-title")
        # titleStr = title.find_element_by_tag_name("a").text
        ## 第二种写法 使用css选择器
        titleSTR = slist.find_element_by_css_selector(".song-title>a").text
        ## 取歌曲作者
        author = slist.find_element_by_class_name("author_list").text
        print(u'{:20s}:{}'.format(titleSTR,author))
driver.quit()

'''
编辑框的常见操作用法：
1.input.clear()     ## 先清除掉页面加载的默认的值
2.input.get_attribute('value')      ## 获取input元素里输入的文本内容

单选框的常见操作用法：<input>...</input>
1.单选框，使用click()
2.勾选框，
    a.先使用is_selected()方法确认是否已经选中。
    b.若已选中返回true，若没选中返回false，在使用click()勾选
    
3.多值复选框
    如：
        选择你喜欢的车
            比亚迪
            华为
            奥迪
        选择你的性别
            男
            女
    <select>...</select>这种的html元素可以使用，其他的不行
    使用select类：
    
print('练习使用多值复选框--3')
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id("multi"))
select.deselect_all()
select.select_by_visible_text("华为")
select.select_by_visible_text("奥迪")

selectSex = Select(driver.find_element_by_id("single"))
selectSex.select_by_visible_text("男")

'''


