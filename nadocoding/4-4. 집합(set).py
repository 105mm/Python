#집합(set)
#중복 안됨, 순서 없음

my_set={1,2,3,3,3}
print(my_set) #{1, 2, 3} 중복 허용하지 않음

java={"유재석","김태호","양세형"}
python=set(["유재석","박명수"]) #리스트를 먼저 만들고 set으로 감싸서 집합을 만든다

#교집합 (java와 python 모두 가능한 개발자)
print(java&python)#{'유재석'}
print(java.intersection(python))#{'유재석'}

#합집합(둘 중 하나라도 할 수 있는 개발자)
print(java|python)
print(java.union(python))
#{'유재석', '김태호', '박명수', '양세형'}
#{'유재석', '김태호', '박명수', '양세형'}
#순서는 보장되지 않는다


#차집합(java 할 줄 알지만 python 할 줄 모르는 개발자
print(java-python)
print(java.difference(python))
#{'김태호', '양세형'}
#{'김태호', '양세형'}

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) #{'유재석', '김태호', '박명수'}

#java 할 줄 아는 사람이 줄어듬
java.remove("김태호")
print(java) #{'양세형', '유재석'}