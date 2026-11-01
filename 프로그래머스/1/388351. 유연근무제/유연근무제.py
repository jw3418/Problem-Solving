def solution(schedules, timelogs, startday):
    N = len(schedules)

    cnt = 0

    for n in range(N):
        schedule = (schedules[n] // 100) * 60 + (schedules[n] % 100)

        flag = True

        for i in range(7):
            day = (startday + i - 1) % 7 + 1

            if day >= 6: continue

            time_ = (timelogs[n][i] // 100) * 60 + (timelogs[n][i] % 100)

            if time_ > schedule + 10:
                flag = False
                break

        if flag:
            cnt += 1

    return cnt