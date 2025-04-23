result = 10 + 20

def get10():
    return 10       # 모든 언어는 스텍형으로 대입한다 근데 함수는 먼저한다 이걸 호스팅

result = get10() + 20

if get10() < 20:
    pass

def isEmpty(value):
    return str(value).strip()==""

for text in ["", "a", "   ", "b"]:
    if isEmpty(text):
        print("비었음")
        continue
    print(text)


def aaaa():
    pass

class Student:
    pass
