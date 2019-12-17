*** Settings ***
Library    pylib.StudentApi_lib

*** Test Cases ***
添加学生2-tc002002
    #添加学生
    ${Addres}    AddStudent   mafeifei  马飞飞  1   ${classid}  13612345679
    #检查添加学生返回的retcode
    should be true  $Addres['retcode']==0
    #列出学生
    ${Listres}  ListStudent
    StudentShouldContain    &{Listres}[retlist]   ${classid}    mafeifei  马飞飞    13612345679     &{Addres}[id]
    [Teardown]  DeleteStudent   &{Addres}[id]

删除学生1-tc002081
    #列出学生
    ${Listres1}  ListStudent
    #添加学生
    ${Addres}    AddStudent   mafeifei  马飞飞  1   ${classid}  13612345679
    #检查添加学生返回的retcode
    should be true  $Addres['retcode']==0
    #删除学生
    ${Deleteres}    DeleteStudent   &{Addres}[id]
    #检查删除学生返回的retcode
    should be true  $Deleteres['retcode']==0
    #列出学生
    ${Listres2}  ListStudent
    should be equal  ${Listres1}    ${Listres2}