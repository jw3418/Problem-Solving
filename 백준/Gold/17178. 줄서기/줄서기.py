import sys
from collections import deque

N = int(input())
people = deque([])
for _ in range(N):
	tmp = list(sys.stdin.readline()[:-1].split())
	for t in tmp:
		tmp_element = t.split('-')
		people.append((tmp_element[0], int(tmp_element[1])))

order = sorted(people); order = deque(order) #입장 순서
wait = [] #대기 공간 (stack)
while people:
	person = people.popleft()
	if person == order[0]: #입장할 수 있으면 입장
		order.popleft()
		#print("줄->입장"); print(people); print(wait)
	else: #순서가 맞지 않아서 입장할 수 없는 경우
		if wait:
			wait_person = wait.pop()
			if wait_person == order[0]: #대기 공간에 입장할 수 있는 사람이 있는 경우
				order.popleft()
				people.appendleft(person)
				#print("대기->입장"); print(people); print(wait)
			else: #대기 공간에 입장할 수 있는 사람이 없는 경우
				wait.append(wait_person)
				wait.append(person)
				#print("줄->대기"); print(people); print(wait)
		else: #대기 공간에 입장할 수 있는 사람이 없는 경우
			wait.append(person)
			#print("줄->대기"); print(people); print(wait)
	#print(order)
	#print()

if wait: #종료조건(BAD)
	wait_sorted = sorted(wait, reverse=True)
	if wait_sorted != wait:
		print("BAD")
		exit()
print("GOOD")