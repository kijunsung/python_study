number = 10
name = "기준준준성"
isOpen = True

print(number)
print(name)
# print(name_) # 오류 앞 라인까지는 실행 된다
print(isOpen)

# print(name.index("숭"))  # exception
# print(name.find("숭"))   # return -1  (없으면 -1로 출력인듯?)

print(name.index("준",2))
print(name.find("준"))

print("이름: {name}, 숫자: {number} 열림: {isOpen}".format(name= name, number= number, isOpen= isOpen))
print(f"이름: {name}, 숫자: {number} 열림: {isOpen}")
address = """부
산
동
래
구
중앙대로""" # 여러 줄로 나누어 쓸 수 있음
print(address)
