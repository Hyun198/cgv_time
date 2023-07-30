print("open or close or close2: ")
part = input()


if part == "open":
    # 오픈
    print("첫 영화 시간 분 입력: ")
    hour, minu = input().split(":")
    hour = int(hour)
    minu = int(minu)

    start_hour = hour
    start_minu = minu

    if minu < 30:
        start_hour = hour-1
        start_minu = minu+30
    else:
        start_minu = minu - 30

    end_hour = start_hour+7
    end_minu = start_minu+30

    if end_minu > 60:
        end_hour += 1
        end_minu -= 60

    print("출근시간: "+str(start_hour)+"시"+str(abs(start_minu))+"분 ")
    print("퇴근시간: "+str(end_hour)+"시"+str(abs(end_minu))+"분 ")

elif part == "close2":
    # 마감
    print("마지막 영화 시간 분 입력: ")
    hour, minu = input().split(":")
    hour = int(hour)
    minu = int(minu)

    start_hour = hour-7
    start_minu = minu

    end_hour = start_hour+7
    end_minu = start_minu+30

    if end_minu >= 60:
        end_minu -= 60
        end_hour += 1
        if end_minu == 0:
            end_minu == 0

    print("출근시간: "+str(start_hour)+"시"+str(abs(start_minu))+"분 ")
    print("퇴근시간: "+str(end_hour)+"시"+str(abs(end_minu))+"분 ")

elif part == "close":  # close
    # 마지막 본 영화 시작 시간 기준 (마지막 영화시간 +10분) -7시간
    print("마지막 영화 시작 시간 분 입력: ")
    hour, minu = input().split(":")
    hour = int(hour)
    minu = int(minu)

    # 본영화 시작 시간
    if minu > 60:
        hour += 1
        minu -= 60
    else:
        minu = minu+10
        if minu == 60:
            hour += 1
            minu = 0
        elif minu > 60:
            hour += 1
            minu = minu-60
    print("본영화시간: "+str(hour)+":"+str(minu))

    start_hour = hour-7
    start_minu = minu-30

    if minu > 30:
        start_minu = minu-30
    elif minu <= 30:
        start_minu = minu+30
        start_hour -= 1

    end_hour = start_hour+7
    end_minu = start_minu+30
    if end_minu >= 60:
        end_minu = end_minu-60
        end_hour += 1

    print("출근 시간: "+str(start_hour)+":"+str(start_minu))
    print("퇴근시간: "+str(end_hour)+"시"+str(abs(end_minu))+"분 ")

