*** Settings ***
Library    pylib.SchoolApi_lib

*** Test Cases ***
添加班级2-tc000002
    #添加班级
    ${Addres}   AddClass    1   皮皮2班    30
    #检查添加班级返回的retcode
    should be true  $Addres["retcode"]==0
    #检查列出班级返回结果包含了刚刚创建的班级信息
    ${Listres}  ListClass
    ${reslist}  evaluate  $Listres["retlist"]
    ClassShouldContain  ${reslist}  皮皮2班  七年级   &{Addres}[invitecode]   30   0    &{Addres}[id]
    [Teardown]      DeleteClass     &{Addres}[id]

添加班级3-tc000003
    #列出班级
    ${Listres1}  ListClass
    #添加班级
    ${Addres}   AddClass    1   皮皮1班    30
    #检查添加班级返回的结果
    should be true  $Addres["retcode"]==1
    should be true  $Addres["reason"]=="duplicated class name"
    #列出班级
    ${Listres2}  ListClass
    #比较添加课程前后的班级信息
    should be equal  ${Listres1}    ${Listres2}

修改班级1-tc000051
    #添加班级
    ${Addres}   AddClass    1   皮皮3班    30
    should be true     $Addres['retcode']==0
    #修改班级
    ${Modifyres}    ModifyClass  &{Addres}[id]    皮皮4班   30
    #检查修改班级返回的结果
    should be true  $Modifyres["retcode"]==0
    #列出班级
    ${Listres}  ListClass
    #检查班级名是否改为了新的名字
    ClassShouldContain  &{Listres}[retlist]  皮皮4班  七年级   &{Addres}[invitecode]   30   0    &{Addres}[id]
    [Teardown]      DeleteClass     &{Addres}[id]

修改班级2-tc000052
    #添加班级
    ${Addres}   AddClass    1   皮皮3班    30
    should be true     $Addres['retcode']==0
    #列出班级
    ${Listres1}  ListClass
    #修改班级
    ${Modifyres}    ModifyClass  &{Addres}[id]    皮皮1班   30
    #检查修改班级返回的结果
    should be true  $Modifyres["retcode"]==1
    should be true  $Modifyres["reason"]=="duplicated class name"
    #列出班级
    ${Listres2}  ListClass
    #检查修改前后是否没有任何信息发生改变
    should be equal  ${Listres1}    ${Listres2}
    [Teardown]      DeleteClass     &{Addres}[id]

修改班级3-tc000053
    #修改班级
    ${Modifyres}    ModifyClass  00000000    皮皮4班   30
    #检查修改班级返回的结果
    should be true  $Modifyres["retcode"]==404
    should be true  $Modifyres["reason"]=="id 为`00000000`的班级不存在"

删除班级1-tc000081
    #删除班级
    ${Deleteres}   DeleteClass     000000
    #检查删除返回的结果
    should be true  $Deleteres['retcode']==404
    should be true  $Deleteres['reason']=="id 为`000000`的班级不存在"

删除班级2-tc000082
    #列出班级
    ${Listres1}  ListClass
    #添加班级
    ${Addres}   AddClass    1   皮皮3班    30
    should be true     $Addres['retcode']==0
    #列出班级
    ${Listres2}  ListClass
    #查看班级是否添加成功
    ClassShouldContain  &{Listres2}[retlist]  皮皮3班  七年级   &{Addres}[invitecode]   30   0    &{Addres}[id]
    #删除班级
    ${Deleteres}   DeleteClass  &{Addres}[id]
    #列出班级
    ${Listres3}  ListClass
    #检查删除返回的结果
    should be true  $Deleteres['retcode']==0
    #检查课程是否删除
    should be equal  ${Listres1}    ${Listres3}


