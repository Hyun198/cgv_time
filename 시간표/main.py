print("open or close: ")
part = input()

if part == "open":
    # 오픈
    print("시간 분 입력: ")
    hour, minu = input().split(":")
    hour = int(hour)
    minu = int(minu)
    if minu < 30:
        hour = hour-1
        minu -= 30
    else:
        minu -= 30

    if minu < 0:
        minu = abs(minu)

    print("출근시간: "+str(hour)+"시"+str(minu)+"분 AM")
else:
    # 마감
    print("시간 분 입력: ")
    hour, minu = input().split(":")
    hour = int(hour)
    minu = int(minu)
    if minu > 30:
        start_hour = hour-6
        start_minu = minu-30

    else:
        minu = minu+60
        hour = hour-1
        start_hour = hour-6
        start_minu = minu-30

    if start_minu < 0:
        start_minu = abs(start_minu)

    print("출근시간: "+str(start_hour)+"시"+str(start_minu)+"분 PM")
