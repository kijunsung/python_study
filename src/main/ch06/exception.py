if __name__ == '__main__':
    print("예외처리")

    numvers =[1,2,3,4,5]
    try:
        print(numvers[5])
    except IndexError as e:
        print(e)
        print("범위 초과임")

    try:
        print("예외처리 강제 발생")
        raise TypeError("자료형좀 맞춰써라~")
    except TypeError as e:
        print(e)
