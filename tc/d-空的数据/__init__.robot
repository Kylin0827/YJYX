*** Settings ***
Library  pylib.SchoolApi_lib
Library  pylib.TeacherApi_lib
Library  pylib.StudentApi_lib
Suite Setup  Run Keywords   DeleteAllStudent    AND     DeleteAllTeacher    AND     DeleteAllClass