from api import request
from input_data import run_time_format
from username_class import UserName
import time


def less_than_180_requests(run_time):
    if run_time is None:
        run_time = "Instantly"
        return run_time
    else:
        run_time = run_time
        new_run_time = run_time_format(run_time)
        return new_run_time


def run_base(usernames_list, v, window):
    new_u_list = []
    requests_limit = 180
    counter = 0
    for name in usernames_list:
        if name == "":
            pass
        else:
            counter += 1
            print(f"Request counter: {counter}")
            v.set(counter)
            window.update()
            can_dm_status = request(name)
            user_object = UserName(name, can_dm_status)
            if user_object.can_dm:
                new_u_list.append(name)
            if counter == requests_limit:
                print("180 requests maded, waiting for 15 minutes")
                requests_limit = requests_limit + 180
                print(f"Second request limit: {requests_limit}")
                time.sleep(900)
    return new_u_list



