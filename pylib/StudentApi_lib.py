import requests,json
from cfg import student_url,g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

class StudentApi_lib:

    #添加学生
    def AddStudent(self,username,realname,gradeid,classid,phonenumber,addstudentid=None):
        data={
            'vcode':g_vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'gradeid':gradeid,
            'classid':classid,
            'phonenumber':phonenumber,
        }
        res=requests.post(student_url,data=data)
        Add_res = res.json()
        pprint(Add_res)
        if addstudentid:
            # BuiltIn().set_global_variable('${%s}'%Addidname,Add_res['id'])
            BuiltIn().set_global_variable(f'${{{addstudentid}}}', Add_res['id'])
        return Add_res

    #列出学生
    def ListStudent(self):
        params = {
                'vcode': g_vcode,
                'action': 'search_with_pagenation',
        }
        res=requests.get(student_url,params=params)
        List_res = res.json()
        pprint(List_res)
        return List_res

    #删除学生
    def DeleteStudent(self,studentid):
        data={
            'vcode':g_vcode
        }
        res =requests.delete(student_url+f'/{studentid}',data=data)
        Delete_res=res.json()
        pprint(Delete_res)
        return Delete_res

    #删除所有学生
    def DeleteAllStudent(self):
        res = self.ListStudent()
        for one in res['retlist']:
            self.DeleteStudent(one['id'])
        res2 = self.ListStudent()
        assert res2['retlist']==[],'学生没有删除完'

    #是否包含学生
    def StudentShouldContain(self,studentlist,classid,username,realname,phonenumber,studentid):
        list={"classid": classid,
              "username":username,
              "realname":realname,
              "id":int(studentid),
              "phonenumber":phonenumber}
        assert studentlist.count(list)==1,'学生创建出错'

if __name__=='__main__':
    a=StudentApi_lib()
    a.AddStudent()
