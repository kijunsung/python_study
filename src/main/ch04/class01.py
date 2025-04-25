# python의 class정의
class Student:
    # python은 클래스 메서드와 스태틱 메서드를 구분해둔다
    # 클래스 변수(JAVA의 static 변수)
    name = "김일(클래스변수)"
    age = "25(클래스변수)"
    def __init__(self):
        # 인스턴스 변수
        self.name = "김일1"
        self.age = 25

    def toString(self):
        return f"Student(name: {self.name}, age: {self.age}, clsName: {self,__class__.name}"

    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age: {cls.age}"

    @staticmethod
    def toString3(name, age):
        return f"Student(name: {name}, age: {age})"


print(Student.name)
print(Student.age)
s1 = Student()
print(s1.name)
print(s1.age)
print(s1.toString())

