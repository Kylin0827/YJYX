*** Settings ***
Library    pylib.TeacherApi_lib
Library    pylib.SchoolApi_lib

*** Test Cases ***
添加老师1-tc001001
    #添加老师
    ${Addres}    AddTeacher  liumou  刘某  1   ${classid}     13012345678      jcysdf@123.com     3209251983090987899
    #检查添加老师返回的retcode
    should be true  $Addres['retcode']==0
    #列出老师
    ${Listres}  ListTeacher
    TeacherShouldContain    &{Listres}[retlist]   liumou    ${classid}    刘某      &{Addres}[id]     13012345678
    ...     jcysdf@123.com      3209251983090987899
    [Teardown]  DeleteTeacher   &{Addres}[id]