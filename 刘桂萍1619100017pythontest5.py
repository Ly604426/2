num=[1,2,3,4,5,6,7,8,9]
name=["Jerry","Ben","Merry","Mike","Nacy","Fancy","Kangkang","Lucky","Yeacy"]
tel=[13553273035,10086,18344069718,6966637,13698768908,18718337412,17528903671,15778971207,6723088]
Tellbook={}                                     #创建一个空字典
for i in range(len(name)):
    d0="{}".format(num[i])                      #从num中取一个数字
    d1="{}".format(name[i])                     #从name中取一个名字
    d2="{}".format(tel[i])                      #从tel中取一个电话
    Tellbook[d0]=d1,d2                          #再把d1,d2赋值给字典Tellbook的d0键
dic={}
while True:
    print("="*7,"通讯录管理系统","="*7)
    print("1.新增联系人")
    print("2.删除联系人")
    print("3.退出")
    print("4.显示所有联系人")
    print("5.查找联系人")
    a=input("请选择要执行的项目：")
    if a=="1":
        name=input("请输入联系人姓名：")
        tel=input("请输入手机号：")
        # if tel.isdigit() and len(tel)==11:
        if name in dic:
            print("联系人已存在")
        else:
            d1="{}".format(name)                     #从name中取一个名字
            d2="{}".format(tel)                      #从tel中取一个电话
            Tellbook[d1]=d2  
       
    elif a=="2":
        name=input("请输入要删除的姓名：")
        if name in Tellbook:
            del Tellbook[name]
            print("已删除：")
        else:
            print("该联系人不存在")
        
    elif a=="3":
        print("已退出")
        break
    elif a=="4":
        print("当前手机内联系人：",Tellbook)

    elif a=="5":
        name=input("请输入要查询的联系人姓名：")
 
 
        if name in Tellbook:
            print(Tellbook[name])
        else:
            print("联系人不存在")
    
    else:
        print("输入有误")