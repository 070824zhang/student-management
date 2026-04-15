class Student:
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gander = gender
        self.age = age
        self.address = address
def add_student():
    f = open("students.txt", "a", encoding="utf-8")
    while True:
        print("请录入学生信息")
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别")
        age = input("请输入学生年龄：")
        address = input("请输入学生家庭地址：")
        student = Student(name,gender,age,address)
        f.write(f"学生姓名：{student.name},性别：{student.gander},年龄：{student.age},家庭住址:{student.address}\n")
        print("当前学生信息录入完毕，是否继续录入？继续录入请输入1，退出录入请输入0")
        choose = input("请确认是否继续录入：")
        if choose == "1":
            continue
        else:
            break
        f.close()

def main():
    while True:
        print("欢迎进入学生信息管理系统，请选择操作，输入1增加学生信息,输入2删除删除学生信息，输入3修改学生信息，输入4查询学生信息")
        num = int(input("请输入数字："))
        if num == 1:
            add_student()
        elif num == 2:
            print("删除功能待实现")



if __name__ == '__main__':
    main()