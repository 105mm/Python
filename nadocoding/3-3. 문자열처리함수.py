a = "Python is Amazing"
print(a.lower()) #소문자로 출력
print(a.upper()) #대문자로 출력
print(a[0].isupper()) #[]자리 문자가소문자면False 대문자면True
print(len(a)) #문자열 길이출력
print(a.replace("Python", "Java")) #문자열 안의 값 바꾸기

index=a.index("n")
print(index) #n이라는 글자가 몇번째 위치에? 5
index=a.index("n", index+1) #두번째 n찾기 15
print(index)

print(a.find("n")) #5
print(a.find("Java")) #Java는 없으므로 -1 반환
#print(a.index("Java")) #오류발생, index는 -1이 아니라 오류가 발생해버림 프로그램종료
print("hi") #출력안됨 위에 오류발생해서

print(a.count("n")) #n이 몇번 발생하느냐? 2