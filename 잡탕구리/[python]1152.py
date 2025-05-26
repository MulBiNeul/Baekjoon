import sys

# 문장 입력
sentence = sys.stdin.readline().strip()

# 공백 기준으로 총 단어의 개수 출력
print(len(sentence.split()))