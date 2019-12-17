*** Settings ***
Library    pylib.TeacherApi_lib
Library    pylib.WebFC_lib
Suite Setup      SuiteWebsite
Suite Teardown      TeardownWebsite

*** Test Cases ***
老师登录1-tc005001
    #添加老师
    ${Addres}    AddTeacher  liumou  刘某  1   ${classid}     13012345678      jcysdf@123.com     3209251983090987899
    #检查添加老师返回的retcode
    should be true  $Addres['retcode']==0
    #登录老师
    LoginWebsite    liumou  888888
    #获取首页信息
    ${Homeinfo}  Gethomeinfo
    #检查首页信息
    should be true  $Homeinfo==['松勤学院00675','刘某','初中数学','0','0','0']
    #获取班级信息
    ${Classinfo}    Getclassinfo
    should be true  $Classinfo=={'七年级皮皮1班': []}
    [Teardown]  DeleteTeacher   &{Addres}[id]
