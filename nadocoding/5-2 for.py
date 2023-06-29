# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

for waiting_no in range(0,5):
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

# 아이언맨, 커피가 준비되었습니다
# 토르, 커피가 준비되었습니다
# 아이엠 그루트, 커피가 준비되었습니다

#while
customer = "토르"
index = 5
while index >= 1:
    print(("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.").format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 토르, 커피가 준비 되었습니다. 5 번 남았어요.
# 토르, 커피가 준비 되었습니다. 4 번 남았어요.
# 토르, 커피가 준비 되었습니다. 3 번 남았어요.
# 토르, 커피가 준비 되었습니다. 2 번 남았어요.
# 토르, 커피가 준비 되었습니다. 1 번 남았어요.
# 커피는 폐기처분되었습니다.

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

    