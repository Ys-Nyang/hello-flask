import nvapi

keyword = input("맛집 검색: ") #입력창에 입력 받기
nvapi.blog(keyword)

# 아래는 연습
def hello(msg):
    #print(f"hello {msg}")
    #return "출력" #결과값
    return f"hello {msg}"

#keyword = input("맛집 검색: ") #입력창에 입력 받기
# 입력 받은 값을 keyword에 저장
# 입력 받은 데이터를 hello 함수에 입력값으로 넣기
result = hello(keyword) #위 함수에서 전달된 값을 result에 전달
print(result) #전달된 값을 화면에 출력