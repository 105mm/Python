#리스트보다 빠름

menu=("돈까스","치즈까스")
print(menu[0]) #돈까스
print(menu[1]) #치즈까스

#menu.add("생선까스") #에러발생, 튜플은 값 변경 불가

name="김종국"
age=20
hobby="코딩"
print(name,age,hobby)
#김종국 20 코딩

name,age,hobby=("김종국",20,"코딩") #한 번에 넣기
print(name,age,hobby)
#김종국 20 코딩