*** Settings ***
Library    pylib.SchoolApi_lib

*** Test Cases ***
添加班级1-tc000001
    #添加班级
    ${Addres}   AddClass    1   皮皮1班    30
    #列出班级
    ${Listres}  ListClass
    #检查添加班级返回的retcode
    should be true  $Addres['retcode']==0
    #检查列出班级返回结果包含了刚刚创建的班级信息
    should be true  $Addres['invitecode']==$Listres['retlist'][0]['invitecode']
    should be true  $Addres['id']==$Listres['retlist'][0]['id']
    should be true  $Listres['retlist'][0]['name']=='皮皮1班'
    should be true  $Listres['retlist'][0]['grade__name']=="七年级"
    should be true  $Listres['retlist'][0]['studentlimit']==30
    [Teardown]      DeleteClass     &{Addres}[id]