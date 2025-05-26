import heapq
import sys

def min_time_to_defeat(N, HP, skills):
    pq = [(0, 0, HP)]  # (현재 시간, 다음 사용 가능 시간, 남은 체력)
    visited = {}  # {남은 체력: 최소 도달 시간}

    while pq:
        time, cooldown, hp = heapq.heappop(pq)

        # 몬스터 체력이 0 이하라면 최소 시간 반환
        if hp <= 0:
            return time
        
        # 이미 더 빠르게 방문한 적이 있다면 스킵
        if hp in visited and visited[hp] <= time:
            continue
        visited[hp] = time  # 최소 시간 갱신

        # 가능한 모든 스킬 사용하여 새로운 상태 탐색
        for skill_cooldown, damage in skills:
            new_time = time + 1  # 스킬 사용 1초 추가
            new_hp = hp - damage  # 새 체력

            # 다음 스킬 사용 가능 시간 계산
            next_cooldown = new_time + skill_cooldown  

            # 우선순위 큐에 삽입 (쿨다운 시간 관리)
            heapq.heappush(pq, (next_cooldown, next_cooldown, new_hp))

    return -1  # 도달할 수 없는 경우 (문제 조건상 발생하지 않음)

# 입력 처리
N, HP = map(int, sys.stdin.readline().split())
skills = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과 출력
print(min_time_to_defeat(N, HP, skills))
