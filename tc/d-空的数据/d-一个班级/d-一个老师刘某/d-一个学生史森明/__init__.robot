*** Settings ***
Library    pylib.StudentApi_lib
Suite Setup  AddStudent   shisenming  史森明  1   ${classid}  13612345678     studentid
Suite Teardown  DeleteStudent   ${studentid}