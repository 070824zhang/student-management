class Student:
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gander = gender
        self.age = age
        self.address = address

def get_next_id():
    max_id = 0
    try:
       f = open("students.txt", "r", encoding="utf-8")
       student_read = f.readlines()
       f.close()
       for student_data in student_read:
           student_id = int(student_data.split(',')[0])
           if student_data.strip() == "":
               continue
           if student_id > max_id:
                max_id = student_id
       return max_id + 1
    except FileNotFoundError:
        return 1


def add_student():
    next_id = get_next_id()
    with open("students.txt", "a", encoding="utf-8") as f:
        while True:
            print("请录入学生信息")
            name = input("请输入学生姓名：")
            gender = input("请输入学生性别")
            age = input("请输入学生年龄：")
            address = input("请输入学生家庭地址：")
            student = Student(name, gender, age, address)
            f.write(f"{next_id}{student.name},{student.gander},{student.age},{student.address}\n")
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
        with open("students.txt", "r", encoding="utf-8") as f:
            student_read = f.readlines()
    except FileNotFoundError:
        print("文件不存在")
        return
    if not student_read:
        print("暂无数据")
        return
    new_student_read = []
    for student_data in student_read:
        if not student_data.strip():
            continue
        try:
            list_id_data = int((student_data.split(',')[0]))
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





def main():
    while True:
        print("欢迎进入学生信息管理系统，请选择操作，输入1增加学生信息,输入2删除删除学生信息，输入3修改学生信息，输入4查询学生信息")
        num = int(input("请输入数字："))
        if num == 1:
            add_student()
        elif num == 2:
            del_student()
        elif num == 3:
            print("修改功能待实现")
        elif num == 4:
            print("查询功能待实现")
        else:
            break








if __name__ == '__main__':
    main()