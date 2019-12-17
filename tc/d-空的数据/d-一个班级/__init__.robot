*** Settings ***
Library  pylib.SchoolApi_lib
Suite Setup  AddClass    1   皮皮1班    30     classid
Suite Teardown  DeleteClass     ${classid}