from data import randomuser_data
from randomusers import (get_full_names , get_users_by_country , count_users_by_gender , get_emails_of_older_than,sort_users_by_age, get_usernames_starting_with, get_average_age,group_users_by_nationality ,get_all_coordinates ,get_oldest_user,find_users_in_timezone,get_registered_before_year)


def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    print("Full Names:", get_full_names(randomuser_data))
    print("Names and Emails:", get_users_by_country(randomuser_data, 'India'))
    print("Gender counts:", count_users_by_gender(randomuser_data))
    print("Older people's emails:", get_emails_of_older_than(randomuser_data, 60))
    print("Users sorted by age (ascending):", sort_users_by_age(randomuser_data))
    print("Users sorted by age (descending):", sort_users_by_age(randomuser_data, descending=True))
    print("Username by first letter:", get_usernames_starting_with(randomuser_data, "a"))
    print("Average age: ", get_average_age(randomuser_data))
    print("Group by nationality", group_users_by_nationality(randomuser_data))
    print("All user coordinates:", get_all_coordinates(randomuser_data))
    print("Oldest user info:", get_oldest_user(randomuser_data))
    print("Users in timezone +5:30:", find_users_in_timezone(randomuser_data, "+5:30"))
    print("Users registered before 2010:", get_registered_before_year(randomuser_data, 2010))
    





run_functions()