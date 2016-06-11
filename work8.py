# coding=utf-8      #输入这个代码就可以让PY源文件里面有中文

db = {}

def newuser():
    prompt = '请输入您的昵称： '
    while True:
        name = input(prompt)
        if name in db:
            prompt = '该昵称已被占用，请重新输入： '
            continue
        else:
            pwd = input("请输入您的密码：")
            db[name] = pwd
            break

def olduser():
    name = input("用户名： ")
    pwd = input("密码： ")
    password = db.get(name)
    if password == pwd:
        print ('欢迎回来：',name)
    else:
        print ('密码有误:')

def showmenu():
    prompt = """
    (1)新用户
    (2)老用户
    (3)退出

    Enter choice:"""
    
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = '3'
            print ('\n您选择了: [%s]' % choice)
            if choice not in '123':
                print ('输入有误，请重新再试：')
            else:
                chosen = True
                done = True
    if choice == '1':
        newuser()
    elif choice == '2':
        olduser()
    elif choice == '3':
        exit()
    showmenu()

showmenu()