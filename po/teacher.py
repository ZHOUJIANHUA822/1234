from selenium.webdriver.common.by import By
class Add_Teacher(object):
    #对象层
    zhanghao=(By.ID,'username')
    mima=(By.ID,'password')
    denglubt=(By.XPATH,'//*[@id="loginFrm"]/input')
    vip_centers=(By.XPATH,'//*[@id="header"]/ul/li[3]/a')
    teacher_list=(By.LINK_TEXT,'教师列表')
    add_teacher_info=(By.LINK_TEXT,'添加教师')
    teacher_iframe=(By.XPATH,'//*[@id="mainframe"]')
    ve_text=(By.XPATH,'//*[@id="form"]/div/div[1]/label')
    #操作层
    def open(self):
        from selenium import webdriver
        driver=webdriver.Chrome()
        return driver
    def open_url(self,driver):
        driver.get('http://localhost/admin.php')
        driver.maximize_window()
        driver.implicitly_wait(10)
    def login(self,driver):
        driver.find_element(*self.zhanghao).send_keys('admin')
        driver.find_element(*self.mima).send_keys('admin')
        driver.find_element(*self.denglubt).click()
    def click_vipcenter(self,driver):
        driver.find_element(*self.vip_centers).click()
    def click_teacherlist(self,driver):
        driver.find_element(*self.teacher_list).click()
    def add_techerinfo(self,driver):
        ele=driver.find_element(*self.teacher_iframe)
        driver.switch_to.frame(ele)
        driver.find_element(*self.add_teacher_info).click()
    def verify(self,driver):

        r=driver.find_element(*self.ve_text).text
        return r
    #业务层
    def teacher_op(self,driver):
        # self.open()
        driver=self.open()
        self.open_url(driver)
        self.login(driver)
        self.click_vipcenter(driver)
        self.click_teacherlist(driver)
        self.add_techerinfo(driver)
        result=self.verify(driver)
        return result


# if __name__ == '__main__':
#     from selenium import webdriver
#     driver=webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get('http://localhost/admin.php')
#     a=Teacher()
#
#     a.teacher_op(driver)