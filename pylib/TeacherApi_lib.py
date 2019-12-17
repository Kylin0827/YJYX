import requests,json
from cfg import teacher_url,g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

class TeacherApi_lib:

    #添加老师
    def AddTeacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber,addteacherid=None):
        classinfo = [{'id':one}for one in str(classlist).split(',') if one!='']
        data={
            'vcode':g_vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':int(subjectid),
            'classlist':json.dumps(classinfo),
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }
        res=requests.post(teacher_url,data=data)
        Add_res = res.json()
        pprint(Add_res)
        if addteacherid:
            # BuiltIn().set_global_variable('${%s}'%Addidname,Add_res['id'])
            BuiltIn().set_global_variable(f'${{{addteacherid}}}', Add_res['id'])
        return Add_res

    #列出老师
    def ListTeacher(self,subjectid=None):
        if  subjectid != None:
            params={
                'vcode':g_vcode,
                'action':'search_with_pagenation',
                'subjectid':subjectid
            }
        else:
            params = {
                'vcode': g_vcode,
                'action': 'search_with_pagenation',
            }
        res=requests.get(teacher_url,params=params)
        List_res = res.json()
        pprint(List_res)
        return List_res

    #删除老师
    def DeleteTeacher(self,teacherid):
        data={
            'vcode':g_vcode
        }
        res =requests.delete(teacher_url+f'/{teacherid}',data=data)
        Delete_res=res.json()
        pprint(Delete_res)
        return Delete_res

    #删除所有老师
    def DeleteAllTeacher(self):
        res = self.ListTeacher()
        for one in res['retlist']:
            self.DeleteTeacher(one['id'])
        res2 = self.ListTeacher()
        assert res2['retlist']==[],'老师没有删除完'

    #修改老师
    def ModifyTeacher(self,teacherid,realname=None,subjectid=None,classlist=None,phonenumber=None,email=None,idcardnumber=None):
        data = {
            'vcode': g_vcode,
            'action': 'modify',
        }
        if realname:
            data['realname']=realname
        if subjectid:
            data['subjectid']=subjectid
        if classlist:
            classinfo = [{'id': one} for one in str(classlist).split(',') if one != '']
            data['classlist']=json.dumps(classinfo)
        if phonenumber:
            data['phonenumber']=phonenumber
        if realname:
            data['email']=email
        if realname:
            data['idcardnumber']=idcardnumber
        res = requests.put(teacher_url+"/"+str(teacherid), data=data)
        Put_res = res.json()
        pprint(Put_res)
        return Put_res

    #是否包含老师
    def TeacherShouldContain(self,teacherlist,username,classlist,realname,teacherid,phonenumber,email,idcardnumber):
        teachclasslist = [int(one) for one in str(classlist).split(',') if one != '']
        list={"username": username,
              "teachclasslist":teachclasslist,
              "realname":realname,
              "id":int(teacherid),
              "phonenumber":phonenumber,
              "email":email,
              "idcardnumber":idcardnumber}
        assert teacherlist.count(list)==1,'老师创建出错'

if __name__=='__main__':
    a=TeacherApi_lib()