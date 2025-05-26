import sys

# 단어 입력
word = sys.stdin.readline().rstrip()

# 대문자로 변환
word = word.upper()

# 가장 많이 쓰인 문자 찾기
word_list = list(set(word))
count_list = []

for i in word_list:
    count = word.count(i)
    count_list.append(count)

state = 0 # 가장 많이 사용된 알파벳이 여러 개 인지 확인

for i in range(len(count_list)):
    if count_list[i] == max(count_list):
        max_index = i
        state += 1

if state > 1:
    print("?")
else:
    print(word_list[max_index])