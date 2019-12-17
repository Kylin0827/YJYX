*** Settings ***
Library    pylib.TeacherApi_lib
Library    pylib.WebFC_lib
Suite Setup      SuiteWebsite
Suite Teardown      TeardownWebsite

*** Test Cases ***
老师发布作业1-tc005101
    #登录老师
    LoginWebsite    liumou  888888
    Teacher_Arrangework     皮皮1班作业
    Studentlogin    shisenming     888888
    Student_Finshwork
    LoginWebsite    liumou  888888
    ${answer}   Teacher_Checkwork
    should be true  $answer==['A', 'A', 'A']
