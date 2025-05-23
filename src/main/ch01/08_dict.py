# 딕셔너리 선언 및 초기화
from re import search

studentDict = dict()
studentDict = {         # dict 만드는 방법
    "name:": "심진우",
    "age" : 25
}
print(studentDict)
# 딕셔너리 값 추가
studentDict["address"] = "부산"
print(studentDict)

# 딕셔너리
anyList = []
anyList.append("test")
print(anyList)

# 딕셔너리 값 조회
name = studentDict.get("name")
print(name)
# print(studentDict["name"])
print(name)
address = studentDict["address"]
print((address))

# 딕셔너리 값 수정
studentDict["address"] = "서울"
print(studentDict)

# 딕셔너리 값 삭제
del studentDict["age"]
print(studentDict)
# studentDict.pop("name")
print(studentDict)

# 딕셔너리의 키, 갑, 한쌍 -> 아이템
print(list(studentDict.items()))       # 1
print(list(studentDict.items())[0])
key, value = list(studentDict.items())[0]
print(f"key:  {key}, value : {value}")

# 직셔너리의 키들만 모두 뽑아 보고 싶을 때
print(studentDict.keys())
print(list(studentDict.keys()))

# 딕셔너리의 값들만 모두 뽑아 보고 싶을 때
print(studentDict.values())
print(list())

searchKey = "name"
students =[
    {"code": 1, "name" : "심민호"
    },
    {"code": 2, "name" : "윤현지"
    },
    {"code": 3, "name" : "이동규"
    }
]
result = []

i = 0
while i < len(students):
    student = students[i]
    result.append(student[searchKey])
    i += 1

print(result)

result = {
    "code": [1,2,3],
    "name": ["심민호", "윤현지", "이동규"]
}

result = {}

i = 0
while i < len(students):
    student = students[i]
    keys = list(student.keys())
    j = 0
    while j < len(keys):
        key = keys[j]
        j += 1
        if key in result:
            result[key].append(student[key])
            continue
        result[key] = [student[key]]
    i += 1

print(result)