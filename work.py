#初始账户
users=['admin']
pwds=['admin']
tea_users=['teacher']
tea_pwds=['teacher']
stu_users=['student']
stu_pwds=['student']

student_list=[]
student_dict={}
teacher_list=[]
teacher_dict={}
chengji_list=[]
chengji_dict={}


#添加学生
def stu_tianjia():
    name=input("请输入学生姓名:")
    age=input("请输入学生年龄:")
    cls=input("请输入学生班级:")
    major=input("请输入学生专业")
    phone=input("请输入学生手机号:")
    num=input("请输入学生学号:")
    student_dict={"name":name,"age":age,"class":cls,"major":major,"phone":phone,"num":num}
    student_list.append(student_dict)
    print("录入成功!")

#查找学生
def stu_chaxun():
    find_name=input("请输入需要查找的学生姓名:")
    for student_dict_1 in student_list:
        if find_name == student_dict_1["name"]:
            print()
            print("-------查询结果-------")
            print("姓名\t\t", "年龄\t\t", "班级\t\t","专业\t\t", "电话\t\t", "学号\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" 
                  %(student_dict_1["name"],
                    student_dict_1["age"], 
                    student_dict_1["class"],
                    student_dict_1["major"],
                    student_dict_1["phone"],
                    student_dict_1["num"]))
        else:
            print("无此学生信息")

#修改学生
def stu_xiugai():
    name_xiugai=input("请输入想要修改的学生姓名:")
    for student_dict_1 in student_list:
        if name_xiugai == student_dict_1["name"]:
            print("-----修改界面-----")
            print("姓名\t\t", "年龄\t\t", "班级\t\t", "专业\t\t", "电话\t\t", "学号\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" 
                  %(student_dict_1["name"],
                    student_dict_1["age"],
                    student_dict_1["class"],
                    student_dict_1["major"],
                    student_dict_1["phone"],
                    student_dict_1["num"]))

            student_dict_1["name"]=new_input(student_dict_1["name"],"请输入修改后的学生姓名[回车不修改]:")
            student_dict_1["age"]=new_input(student_dict_1["age"],"请输入修改后的学生年龄[回车不修改]:")
            student_dict_1["class"]=new_input(student_dict_1["class"],"请输入修改后的学生班级[回车不修改]:")
            student_dict_1["major"]=new_input(student_dict_1["major"],"请输入修改后的学生专业[回车不修改]:")
            student_dict_1["phone"]=new_input(student_dict_1["phone"],"请输入修改后的学生电话[回车不修改]:")
            student_dict_1["num"]=new_input(student_dict_1["num"],"请输入修改后的学生学号[回车不修改]:")
            print("修改成功!")
            break
    else:
        print("您输入的学生姓名错误，请重新输入")

#删除学生
def stu_shanchu():
    name_del=input("请输入想要删除的学生姓名:")
    for student_dict_1 in student_list:
        if name_del in student_dict_1["name"]:
            student_list.remove(student_dict_1)
            print("删除%s信息成功!" % name_del)
            break
    else:
        print("您输入的学生姓名错误，请重新输入")

#显示所有学生信息
def showall():
    print("-----显示所有学生信息-----")
    print("姓名\t\t", "班级\t\t", "年龄\t\t", "电话号\t\t", "家庭住址\t\t")
    for student_dict_1 in student_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (student_dict_1["name"],
                                              student_dict_1["class"],
                                              student_dict_1["age"],
                                              student_dict_1["phone"],
                                              student_dict_1["address"]))

#添加教师
def tea_tianjia():
    name=input("请输入教师姓名:")
    age=input("请输入教师年龄:")
    phone=input("请输入教师电话:")
    sex=input("请输入教师性别")
    address=input("请输入教师住址:")
    teacher_dict={"name":name,"age":age,"phone":phone,"sex":sex,"address":address}
    teacher_list.append(teacher_dict)
    print("录入成功!")

#查找教师
def tea_chaxun():
    find_name=input("请输入需要查找的教师姓名:")
    for teacher_dict_1 in teacher_list:
        if find_name == teacher_dict_1["name"]:
            print()
            print("-------查询结果-------")
            print("姓名\t\t", "年龄\t\t", "电话\t\t","性别\t\t", "地址\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s" 
                  %(teacher_dict_1["name"],
                    teacher_dict_1["age"], 
                    teacher_dict_1["phone"],
                    teacher_dict_1["sex"],
                    teacher_dict_1["address"]))
        else:
            print("无此教师信息")

#修改教师
def tea_xiugai():
    name_xiugai=input("请输入想要修改的教师姓名:")
    for teacher_dict_1 in teacher_list:
        if name_xiugai == teacher_dict_1["name"]:
            print("-----修改界面-----")
            print("姓名\t\t", "年龄\t\t", "电话\t\t", "性别\t\t", "地址\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s" 
                  %(teacher_dict_1["name"],
                    teacher_dict_1["age"],
                    teacher_dict_1["phone"],
                    teacher_dict_1["sex"],
                    teacher_dict_1["address"]))

            teacher_dict_1["name"]=new_input(teacher_dict_1["name"],"请输入修改后的教师姓名[回车不修改]:")
            teacher_dict_1["age"]=new_input(teacher_dict_1["age"],"请输入修改后的教师年龄[回车不修改]:")
            teacher_dict_1["phone"]=new_input(teacher_dict_1["phone"],"请输入修改后的教师电话[回车不修改]:")
            teacher_dict_1["sex"]=new_input(teacher_dict_1["sex"],"请输入修改后的教师性别[回车不修改]:")
            teacher_dict_1["address"]=new_input(teacher_dict_1["address"],"请输入修改后的教师住址[回车不修改]:")
            print("修改成功!")
            break
    else:
        print("您输入的教师姓名错误，请重新输入")

#删除教师
def tea_shanchu():
    name_del=input("请输入想要删除的教师姓名:")
    for teacher_dict_1 in teacher_list:
        if name_del in teacher_dict_1["name"]:
            student_list.remove(teacher_dict_1)
            print("删除%s信息成功!" % name_del)
            break
    else:
        print("您输入的教师姓名错误，请重新输入")    

#课程查询
def kecheng():
    pass

#成绩录入
def cj_luru():
    name=input("请输入学生姓名:")
    cj_1=input("请输入语文成绩:")
    cj_2=input("请输入数学成绩:")
    cj_3=input("请输入外语成绩")
    cj_4=input("请输入物理成绩:")
    cj_5=input("请输入历史成绩:")
    chengji_dict={"name":name,"语文":cj_1,"数学":cj_2,"外语":cj_3,"物理":cj_4,"历史":cj_5}
    chengji_list.append(chengji_dict)
    print("录入成功!")

#成绩查询
def cj_chaxun():
    pass

#成绩修改
def cj_xiugai():
    pass

#成绩删除
def cj_shanchu():
    pass

#设置用户不输入内容返回原值，输入内容返回新内容
def new_input(yuanzhi,message):
    input_str=input(message)

    if len(input_str)>0:
        return input_str
    else:
        return yuanzhi

#登录
def denglu():
    shenfen = input("请选择登录身份（1.学生 2.教师 3.管理员）：")
    user = input("请输入您的用户名:")
    pwd = input("请输入您的密码:")
    if shenfen=='1':
        if user in stu_users and pwd in stu_pwds:
            print("登录成功！")
            student()
        else:
            print("账号或密码不正确")
    elif shenfen=='2':
        if user in tea_users and pwd in tea_pwds:
            print("登录成功！")
            teacher()
        else:
            print("账号或密码不正确")
    elif shenfen=='3':
        if user in users and pwd in pwds:
            print("登录成功！")
            admin()
        else:
            print("账号或密码不正确")
    else:
        print("身份错误，请重新输入")

#注册
def zhuce():
    shenfen = input("请选择要注册的用户（1.学生 2.教师）")
    user=input("请输入您要注册的用户名:")
    pwd=input("请输入您要注册的密码:")
    if shenfen==1:
        stu_users.append(user)
        stu_pwds.append(pwd)
    elif shenfen==2:
        tea_users.append(user)
        tea_pwds.append(pwd)
    else:
        print("身份错误，请重新输入")
    print("注册成功!")

#登录界面
def main():

    while True:
        print("---------------------------")
        print("       管理系统登陆界面     ")
        print("                           ")
        print("        1:登   录           ")
        print("        2:注   册           ")
        print("        3:退   出           ")
        print("                           ")
        print("---------------------------")
        xx = input("请输入您的选择:")
        #1.登录
        if xx=='1':
            denglu()
        elif xx=='2':
        #3.注册
            zhuce()
        elif xx=='3':
        #3.退出
            print()
            print("成功退出!")
            print()
            break
        else:
            print("输入错误，请重新输入")

#学生管理系统
def student():
    while True:
        #学生管理系统界面
        print("---------------------------")
        print("      管理系统-学生端        ")
        print("      1:课程查找            ")
        print("      2:修改个人信息        ")
        print("      3:成绩查询            ")
        print("      0:退出系统"            )
        print("---------------------------")
        x=input("请输入功能对应序号:")
    
        #添加学生
        if x=='1':
            kecheng()
        #修改学生信息
        elif x=='2':
            stu_xiugai()
        #成绩查询
        elif x=='3':
            cj_chaxun()
        #退出学生管理系统,返回上一层登录界面系统
        elif x=='0':
            print("成功退出管理系统!")
            break
        else:
            print("输入错误，请重新输入")

#教师管理系统
def  teacher():
    while True:
        print("----------------------------")
        print("       管理系统-教师端       ")
        print("       1.查询教师信息        ")
        print("       2.查询学生信息        ")
        print("       3.录入学生成绩        ")
        print("       4.修改学生成绩        ")
        print("       5.删除学生成绩        ")
        print("       0.退出系统            ")
        print("----------------------------")
        x = input("请输入功能对应的序号:")
        if x=='1':
            tea_chaxun()
        elif x=='2':
            stu_chaxun()
        elif x=='3':
            cj_luru()
        elif x=='4':
            cj_xiugai()
        elif x=='5':
            cj_shanchu()
        elif x=='0':
            print("成功退出管理系统!")
            break
        else:
            print("输入错误，请重新输入")

#管理员系统
def admin():
    while True:
        print("----------------------------")
        print("        管理系统后台        ")
        print("       1.添加教师信息        ")
        print("       2.查询教师信息        ")
        print("       3.修改教师信息        ")
        print("       4.删除教师信息        ")
        print("       5.添加学生信息        ")
        print("       6.查询学生信息        ")
        print("       7.修改学生信息        ")
        print("       8.删除学生信息        ")
        print("       9.sudo rm -rf /*     ")
        print("       0.退出系统            ")
        print("----------------------------")
        x = input("请输入功能对应的序号:")
        if x=='1':
            tea_tianjia()
        elif x=='2':
            tea_chaxun()
        elif x=='3':
            tea_xiugai()
        elif x=='4':
            tea_shanchu()
        elif x=='5':
            stu_tianjia()
        elif x=='6':
            stu_chaxun()
        elif x=='7':
            stu_xiugai()
        elif x=='8':
            stu_shanchu()
        elif x=='9':
            exit
        elif x=='0':
            print("成功退出管理系统!")
            break
        else:
            print("输入错误，请重新输入")

#主函数
main()
