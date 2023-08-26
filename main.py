from input_data import open_file
from input_data import run_time
from input_data import check_quantity
from brain import less_than_180_requests
from brain import run_base


def main(v, window, file, v_q, save_as_location):
    # Open "usernames list.txt" and store it into list
    inputed_usernames_list = open_file(file)

    # Check usernames list quantity. If usernames list quantity > 180 => Calculate run time
    duration = run_time(inputed_usernames_list)
    new_run_time = less_than_180_requests(duration)
    usernames_list_quantity = check_quantity(inputed_usernames_list)
    print(f"Inputed username list quantity: {usernames_list_quantity}")
    print(f"Run time: {new_run_time}")
    v_q.set(usernames_list_quantity)
    window.update()

    # Main run script
    new_can_dm_true_list = run_base(inputed_usernames_list, v, window)

    # If there is at least one user with has_dm = True, create new .txt file contains it is user name otherwise do
    # nothing.
    if len(new_can_dm_true_list) > 0:
        with open(save_as_location, mode="w") as new_file:
            new_file.write("\n".join(new_can_dm_true_list))
