n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # input_data = ['John', '80', 'Alice', '90', 'Mike', '70'] 저장
    array.append((input_data[0], int(input_data[1])))
    # array = [('Mike', 70), ('John', 80), ('Alice', 90)] 3개의 튜플로 저장

array = sorted(array, key=lambda student: student[1])
# array = [('Mike', 70), ('John', 80), ('Alice', 90)] 저장

for student in array:
    print(student[0], end=' ')
