# sys 라이브러리의 readline()함수를 사용하면 시간 초과를 피할 수 있다.
import sys

# readline() 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위해 rstrip() 함수를 사용한다.
input_data = sys.stdin.readline().rstrip()

print(input_data)
