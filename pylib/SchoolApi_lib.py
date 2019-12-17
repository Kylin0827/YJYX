import requests
from cfg import class_url,g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

class SchoolApi_lib:

    #删除所有课程
    def DeleteAllClass(self):
        res = self.ListClass()
        for one in res['retlist']:
            self.DeleteClass(one['id'])
        List_res=self.ListClass()
        assert List_res['retlist']==[],  '课程没有删完'

    #查看课程
    def ListClass(self,gradeid=None):
        if  gradeid != None:
            params={
                'vcode':g_vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':gradeid
            }
        else:
            params = {
                'vcode': g_vcode,
                'action': 'list_classes_by_schoolgrade',
            }
        res=requests.get(class_url,params=params)
        List_res = res.json()
        pprint(List_res)
        return List_res

    #添加课程
    def AddClass(self,grade,name,studentlimit,Addidname=None):
        data={
            'vcode':g_vcode,
            'action':'add',
            'grade':int(grade),
            'name':name,
            'studentlimit':int(studentlimit)
        }
        res=requests.post(class_url,data=data)
        Add_res = res.json()
        pprint(Add_res)
        if Addidname:
            # BuiltIn().set_global_variable('${%s}'%Addidname,Add_res['id'])
            BuiltIn().set_global_variable(f'${{{Addidname}}}', Add_res['id'])
        return Add_res

    #删除课程
    def DeleteClass(self,classid):
        data={
            'vcode':g_vcode
        }
        res =requests.delete(class_url+f'/{classid}',data=data)
        Delete_res=res.json()
        pprint(Delete_res)
        return Delete_res

    #是否包含课程
    def ClassShouldContain(self,classlist,classname,gradename,invitecode,studentlimit,studentnumber,id):
        list={"name":classname,
              "grade__name":gradename,
              "invitecode":invitecode,
              "studentlimit":int(studentlimit),
              "studentnumber":int(studentnumber),
              "id":id,
              "teacherlist":[]}
        assert classlist.count(list)==1,'课程创建出错'

    #修改课程
    def ModifyClass(self,classid,classname,studentlimit):
        data = {
            'vcode': g_vcode,
            'action': 'modify',
            'name': classname,
            'studentlimit': int(studentlimit)
        }
        res = requests.put(class_url+"/"+str(classid), data=data)
        Put_res = res.json()
        pprint(Put_res)
        return Put_res


if __name__=='__main__':
    a=SchoolApi_lib()
    # a.ListClass()
    # a.AddClass(2,'皮皮2班',30)
    # a.DeleteClass(204144)
    # a.AddClass(1,'皮皮一班',30,'id')
    a.DeleteAllClass()