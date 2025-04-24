# 람다 함수
"""
JAVA
@FunctionalInterface
public interface addition{
    int add(int a, int b);
    }
    public statix void main (String[] args) {
        Addition a = (n, n2) -> n + n2;
        int result = a.add(10, 20);
        system.out.println(result);
    }
}
"""

# python에서 람다 함수
# students = [("김준일", 90),("김준이", 85), ("김준삼", 95)]
# sorted(
# )

numbers3 = list(filter(lambda num:  num % 2 == 0, numbers))
print(numbers3)
numbers4 = list(map(lambda num: f"<h1>{num}</h1>", numbers3))
print(numbers4)

