from selenium import webdriver
from cfg import *
import time
from selenium.webdriver.support.ui import Select
class WebFC_lib():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    #打开浏览器
    def SuiteWebsite(self):
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    #关闭浏览器
    def TeardownWebsite(self):
        self.driver.quit()
    #老师登录
    def LoginWebsite(self,username,password):
        self.driver.get(Weburl)
        self.driver.find_element_by_css_selector('.teacher a').click()
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys(username)
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('button[onclick="postLoginRequest()"]').click()
    #学生登录
    def Studentlogin(self,username,password):
        self.driver.get(Weburl)
        self.driver.find_element_by_css_selector('.student a').click()
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys(username)
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('button[onclick="postLoginRequest()"]').click()
    #获取首页信息
    def Gethomeinfo(self):
        self.driver.find_element_by_css_selector('a[href="#/home"]>li').click()
        time.sleep(2)
        eles=self.driver.find_elements_by_css_selector('.opacity-level .ng-binding')
        info=[one.text for one in eles]
        print(info)
        return info

    #获取班级学生信息
    def Getclassinfo(self):
        self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(4)').click()
        self.driver.find_element_by_css_selector('a[href="#/student_group"] li').click()
        time.sleep(2)
        classstudent={}
        classinfo = self.driver.find_elements_by_css_selector('div.panel-green')
        for one in classinfo:
            gradeclassele=one.find_element_by_css_selector('.panel-heading')
            gradeclass=gradeclassele.text.replace(' ','')
            gradeclassele.click()
            time.sleep(2)
            self.driver.implicitly_wait(1)
            student=one.find_elements_by_css_selector('tr>td:nth-child(2)')
            self.driver.implicitly_wait(10)
            students=[ele.text for ele in student]
            classstudent[gradeclass]=students
        print(classstudent)
        return classstudent
    #老师布置作业
    def Teacher_Arrangework(self,homework_name):
        self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(2)').click()
        self.driver.find_element_by_css_selector('a[ng-click="show_page_addexam()"] li').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('button[ng-click="gotoPickQuestion()"]').click()
        time.sleep(3)
        self.driver.switch_to.frame('pick_questions_frame')
        question=self.driver.find_elements_by_css_selector('.div-search-question label:nth-child(2)')
        for one in range(3):
            question[one].click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('.btn-blue').click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('exam_name_text').send_keys(homework_name)
        self.driver.find_element_by_id('btn_submit').click()
        ret=self.driver.find_element_by_css_selector('.bootstrap-dialog-message h3').text
        print(ret)
        #发布给学生
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer button:nth-child(2)').click()
        mainwindow=self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if '下发学习任务' in self.driver.title:
                break

        self.driver.find_element_by_css_selector('label.myCheckbox span').click()
        self.driver.find_element_by_css_selector('.btn-outlined').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.btn-primary').click()
        self.driver.find_element_by_css_selector('.btn-default').click()
        #切回主窗口
        self.driver.switch_to.window(mainwindow)

    #学生完成作业
    def Student_Finshwork(self):
        self.driver.find_element_by_css_selector('a[href="#/task_manage"] li').click()
        self.driver.find_element_by_css_selector('button[ng-click="viewTask(taskTrack)"]').click()
        question=self.driver.find_elements_by_css_selector('.btn-group button:nth-child(1)')
        for one in range(3):
            question[one].click()
        self.driver.find_element_by_css_selector('button[ng-click="saveMyResult(true)"]').click()
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button:nth-child(2)').click()

    #老师检查作业
    def Teacher_Checkwork(self):
        self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(2)').click()
        self.driver.find_element_by_css_selector('a[href="#/task_manage?tt=1"] li').click()
        self.driver.find_element_by_css_selector('a[ng-click="trackTask(task)"] i').click()
        self.driver.find_element_by_css_selector('td[ng-if="taskTrack.finished"] button').click()
        mainwindow=self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if '查看作业' in self.driver.title:
                break
        eles=self.driver.find_elements_by_css_selector('.myCheckbox input:checked')
        answer=[ele.find_element_by_xpath('./..').text.strip() for ele in eles]
        print(answer)
        self.driver.switch_to.window(mainwindow)
        return  answer

if __name__=='__main__':
    a=WebFC_lib()
    a.SuiteWebsite()
    a.LoginWebsite('liumou','888888')
    a.Teacher_Arrangework()
    a.Studentlogin('shishenming','888888')
    a.Student_Finshwork()
    a.LoginWebsite('liumou','888888')
    a.Teacher_Checkwork()