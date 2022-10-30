from collections import defaultdict


def cal_time(intime, outtime):
    hour = int(outtime[:2]) - int(intime[:2])
    minute = int(outtime[3:]) - int(intime[3:])

    return hour * 60 + minute


def solution(fees, records):
    fee_dict = defaultdict(int)
    time_dict = {}
    answer = []

    for record in records:
        time, number, info = record.split()
        if info == 'IN':
            time_dict[number] = time
        else:
            fee_dict[number] += cal_time(time_dict[number], time)
            time_dict[number] = False

    for number, value in time_dict.items():
        if value is not False:
            fee_dict[number] += cal_time(value, "23:59")
            time_dict[number] = False

    fee_list = sorted(fee_dict.items(), key = lambda x: x[0])


    for _, value in fee_list:
        addition_time = value - fees[0]
        add_fee, is_clean = 0, 0
        if addition_time > 0:
            add_fee, is_clean = addition_time // fees[2], addition_time % fees[2]

        answer.append(fees[1] + add_fee * fees[3] if is_clean == 0 else fees[1] + (add_fee + 1) * fees[3])

    return answer