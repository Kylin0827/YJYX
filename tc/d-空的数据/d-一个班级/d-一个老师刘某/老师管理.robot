*** Settings ***
Library    pylib.TeacherApi_lib
Library    pylib.SchoolApi_lib

*** Test Cases ***
添加老师2-tc001002
    #添加老师
    ${Addres}    AddTeacher  lubenwei  卢本伟  5   ${classid}     13012345670     lubenwei@123.com     3309251983090987899
    #检查添加老师返回的retcode
    should be true  $Addres['retcode']==0
    #列出老师
    ${Listres}  ListTeacher
    TeacherShouldContain    &{Listres}[retlist]   lubenwei    ${classid}    卢本伟      &{Addres}[id]     13012345670
    ...     lubenwei@123.com      3309251983090987899
    [Teardown]  DeleteTeacher   &{Addres}[id]

添加老师3-tc001003
    #列出老师
    ${Listres1}  ListTeacher
    #添加老师
    ${Addres}    AddTeacher  liumou  刘某  1   ${classid}     13012345678      jcysdf@123.com     330302198808081713
    #检查添加老师返回的retcode
    should be true  $Addres['retcode']==1
    should be true  $Addres['reason']=='登录名 liumou 已经存在'
    #列出老师
    ${Listres2}  ListTeacher
    should be true  $Listres1==$Listres2