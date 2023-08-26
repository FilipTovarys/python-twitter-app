import math
from datetime import timedelta


def open_file(file):
    data_list = []
    with open(file) as my_file:
        my_file = my_file.readlines()
    for names in my_file:
        names = names.strip()
        data_list.append(names)
    return data_list


def check_quantity(u_n_list):
    quantity = 0
    for item in u_n_list:
        if item == "":
            pass
        else:
            quantity += 1
    return quantity


def run_time(input_file):
    usernames_quantity = len(input_file)
    api_rate = 180
    if usernames_quantity < 180:
        pass
    else:
        ratio = math.ceil(usernames_quantity/api_rate)
        run_time_in_minutes = 15 * ratio
        return run_time_in_minutes


def run_time_format(run_time_in_minutes):
    if run_time_in_minutes > 60:
        run_time_in_hours = str(timedelta(minutes=run_time_in_minutes))[:-3]
        return run_time_in_hours
    else:
        time = run_time_in_minutes
        return time
