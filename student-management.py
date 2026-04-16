class Student:
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gander = gender
        self.age = age
        self.address = address

#定义学生id并设置id自增
def get_next_id():
    max_id = 0
#捕获异常，可能电脑上没这个文件
    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            student_read = f.readlines()  # 读取文件内容
            for student_data in student_read:  # 遍历，将数据转换成列表封装在student_data中
                if not student_data.strip():
                    continue
                student_id = int(student_data.split(',')[0])  # 对列表进行切分，并通过索引获取id，转换成整数类型
                if student_id > max_id:  # 实现增加一条学生信息，id自增
                    max_id = student_id
        return max_id + 1
    except FileNotFoundError:
        return 1



#定义函数，用来增加学生信息
def add_student():
    next_id = get_next_id()          #调用get_next_id函数，自动为录入的学生信息设置id
    with open("students.txt", "a", encoding="utf-8") as f:
        while True:
            print("请录入学生信息")
            name = input("请输入学生姓名：")
            gender = input("请输入学生性别")
            age = input("请输入学生年龄：")
            address = input("请输入学生家庭地址：")
            student = Student(name, gender, age, address)
            f.write(f"{next_id},{student.name},{student.gander},{student.age},{student.address}\n")
            print(f"学生{name}添加成功，ID={next_id}")
            next_id += 1
            print("当前学生信息录入完毕，是否继续录入？输入1继续录入，否则退出。")
            choose = input("请确认是否继续录入：")
            if choose == "1":
                continue
            else:
                break
        f.close()



def del_student():
    sid = int(input("请输入要删除的学生id："))
    try:
        with open("students.txt", "r", encoding="utf-8") as f:   #捕获找不到文件的异常
            student_read = f.readlines()
    except FileNotFoundError:
        print("文件不存在")
        return
    if not student_read:
        print("暂无数据")
        return
    new_student_read = []
    for student_data in student_read:
        if not student_data.strip():       #设置跳过空行
            continue
        try:
            list_id_data = int((student_data.split(',')[0]))      #捕获输入不是整数时的异常
        except:
            continue
        if list_id_data != sid:
            new_student_read.append(student_data)
    if len(new_student_read) == len(student_read):
        print("未找到该id")
        return
    with open("students.txt", "w", encoding="utf-8") as f:
        for student_data in new_student_read:
            f.write(student_data)
    print("删除成功！")



def find_student_by_id(sid):
    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            student_read = f.readlines()
            for student_data in student_read:
                list_id_data = int((student_data.split(',')[0]))
                if list_id_data != sid:
                    continue
                else:
                    return student_data
    except FileNotFoundError:
        print("文件不存在")
        return None
    return None



def updata_student():
    sid = int(input("请输入要修改的学生id："))
    result = find_student_by_id(sid)
    if result is None:
        print("未找到该学生")
        return
    with open("students.txt", "r", encoding="utf-8") as f:
        student_read = f.readlines()
        idx = -1
        for i,student_data in enumerate(student_read):
            if student_data.strip() == result.strip():
                idx = i
                break
        if idx == -1:
            print("未找到索引")
            return
        update = student_read[idx].strip().split(',')
        print(f"当前信息：姓名：{update[1]},性别：{update[2]},年龄：{update[3]},地址：{update[4]}")
        choose = input("请输入要修改的字段：1姓名 2性别 3年龄 4地址")
        if choose == "1":
            update[1] = input("新姓名：")
        elif choose == "2":
            update[2] = input("新性别：")
        elif choose == "3":
            update[3] = input("新年龄：")
        elif choose == "4":
            update[4] = input("新地址：")
        else:
            print("无效选择")
            return
    new_student_read = ','.join(update) + '\n'
    student_read[idx] = new_student_read
    with open("students.txt", "w", encoding="utf-8") as f:
        f.writelines(student_read)
    print("修改成功")





def main():
    while True:
        print("欢迎进入学生信息管理系统，请选择操作，输入1增加学生信息,输入2删除学生信息，输入3修改学生信息，输入4查询学生信息")
        num = int(input("请输入数字："))
        if num == 1:
            add_student()
        elif num == 2:
            del_student()
        elif num == 3:
            updata_student()
        elif num == 4:
            print("查询功能待实现")
        else:
            break








if __name__ == '__main__':
    main()