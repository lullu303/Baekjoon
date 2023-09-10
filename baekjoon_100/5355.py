# 테스트 케이스 개수를 입력받기
t = int(input())

# t에 저장된 테스트 케이스 수만큼 반복
for _ in range(t) :
    # line에 문자열을 입력받아 분할하기
    line = list(map(str, input().split()))

    # 리스트의 첫번째 문자열을 result에 저장
    ans = line[0]

    # line의 길이만큼 반복 (연산자의 수만큼 연산자 계산)
    for i in range(len(line)) :
        if i == 0:
            ans = float(line[i])
        if line[i] =='@':
            ans *=3 
        elif line[i] =='%' :
            ans +=5
        elif line[i] =='#' :
            ans -=7

    print("{:.2f}".format(ans))



# # a에 테스트 케이스 개수를 입력 받기
# a = int(input()) 

# # a에 저장된 테스트 케이스 수만큼 반복
# for i in  range(a): 
#     # l에 문자열을 입력받아 분할하기
#     l = list(map(str, input().split())) 
    
#     #리스트의 첫 번째 문자열을 result에 저장
#     result = eval(l[0])
    
#     # l의 길이만큼 반복 (연산자의 수만큼 연산자 계산)
#     for j in range(len(l)):
#         if l[j] == "@":
#           result = result * 3
#         elif l[j] == "%":
#           result = result + 5
#         elif l[j] == "#":
#           result = result -7
#     print("%0.2f" %result)
