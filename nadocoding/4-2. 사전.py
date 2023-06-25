cabinet={3:"유재석",100:"김태호"} #캐비넷에 두 개의 열쇠, 3번은 유재석꺼 100번은 김태호꺼
print(cabinet[3]) #유재석
print(cabinet[100]) #김태호

print(cabinet.get(3)) #유재석
#print(cabinet[5]) #오류발생, 5가 없기때문, hi도 출력안됨
print(cabinet.get(5)) #None 출력
print(cabinet.get(5,"사용 가능")) #5의 소유주가 없으므로 사용 가능 출력됨
print("hi") #정상출력

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석","B-100":"김태호"} #string 형식도 사용가능
print(cabinet["A-3"])
print(cabinet["B-100"])
#유재석
#김태호

#새 손님
print(cabinet) #{'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet) #{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

#간 손님
del cabinet["A-3"]
print(cabinet)
#{'B-100': '김태호', 'C-20': '조세호'}

#key 들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])

#value(소유주) 들만 출력
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
print(cabinet.items()) #dict_items([('B-100', '김태호'), ('C-20', '조세호')])

#목욕탕 폐점
cabinet.clear() 
print(cabinet) #{}