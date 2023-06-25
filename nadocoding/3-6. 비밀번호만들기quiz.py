# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 (nav)               (5)             (1)       (!)
# 예) 생성된 비밀번호 : nav51!                                                               

a="http://naver.com"
b=a[7:]
c=b.index(".")

d=b[:c]

print((d[:3])+(str(len(d)))+(str(d.count("e")))+"!") #find 쓰지말고 count 써야됨


#선생님 답안
a1="http://naver.com"
b1=a1.replace("http://","") # 규칙1
b1=b1[:b1.index(".")] # 규칙2
c1=b1[:3]+str(len(b1))+str(b1.count("e"))+"!"

print("{0}의 비밀번호는 {1}입니다.".format(a, c1))