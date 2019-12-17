*** Settings ***
Library  pylib.TeacherApi_lib
Suite Setup  AddTeacher    liumou  刘某  1   ${classid}     13012345678      jcysdf@123.com
...     330302198808081713      teacherid
Suite Teardown  DeleteTeacher     ${teacherid}