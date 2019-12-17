*** Settings ***
Library    pylib.StudentApi_lib

*** Test Cases ***
添加学生1-tc002001
    #添加学生
    ${Addres}    AddStudent   shishenming  史森明  1   ${classid}  13612345678
    #检查添加学生返回的retcode
    should be true  $Addres['retcode']==0
    #列出学生
    ${Listres}  ListStudent
    StudentShouldContain    &{Listres}[retlist]   ${classid}    shishenming  史森明    13612345678     &{Addres}[id]
    [Teardown]  DeleteStudent   &{Addres}[id]