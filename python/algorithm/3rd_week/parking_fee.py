import math
def solution(fees:list, records:list):
    basic_minutes = fees[0]
    basic_fee = fees[1]
    unit_minutes = fees[2]
    unit_fee = fees[3]
    FINAL_TIME = 1439
    car_num_key = {}
    for record in records:
        car_num = record.split(" ")[1]
        status = record.split(" ")[2]
        car_num_key.setdefault(car_num, {"info": [], "fee": 0, "used_minutes": 0})
        car_num_key[car_num]["info"].append(record)
        if status == "OUT":
            car_num_key[car_num]["used_minutes"] += int(car_num_key[car_num]["info"][len(car_num_key[car_num]["info"])-1].split(" ")[0].split(":")[0])*60+\
            int(car_num_key[car_num]["info"][len(car_num_key[car_num]["info"])-1].split(" ")[0].split(":")[1])-\
            int(car_num_key[car_num]["info"][len(car_num_key[car_num]["info"])-2].split(" ")[0].split(":")[0])*60-\
            int(car_num_key[car_num]["info"][len(car_num_key[car_num]["info"])-2].split(" ")[0].split(":")[1])
    for car_num in car_num_key:
        car_num_key[car_num]["fee"] += basic_fee
        if car_num_key[car_num]["info"][-1].split(" ")[2] == "IN":
            car_num_key[car_num]["used_minutes"] += FINAL_TIME-int(car_num_key[car_num]["info"][-1].split(" ")[0].split(":")[0])*60-int((car_num_key[car_num]["info"][-1].split(" ")[0].split(":")[1]))
        if basic_minutes < car_num_key[car_num]["used_minutes"]:
            car_num_key[car_num]["fee"] += unit_fee*math.ceil((car_num_key[car_num]["used_minutes"]-basic_minutes)/unit_minutes)
    car_num_key = dict(sorted(car_num_key.items()))
    # print(car_num_key)
    answer = [car_num_key[x]["fee"] for x in car_num_key]
    # print(answer)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)