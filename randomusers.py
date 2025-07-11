


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    results =data  ['results']

    names = []
    for user in results:
        name = user['name']
        first_name = name['first']
        last_name = name['last']

        full_name = first_name + ' '+ last_name
        names.append(full_name)

    return names



def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    users = data['results']
    list_of_dict = list()
    
    for user in users:
        if user['location']['country'] == country:

            name_email= dict()

            name = user['name']
            first_name = name['first']
            last_name = name['last']

            email = user['email']  

            full_name = f"{first_name} {last_name}"
            name_email['name'] = full_name
            name_email['email'] = email

            list_of_dict.append(name_email)

    return list_of_dict

def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
        
    """
    users = data['results']
    male_count = 0
    female_count = 0

    for user in users:
        if user['gender'] == 'male':
            male_count += 1
        elif user['gender'] == 'female':
            female_count += 1

    return {"male": male_count, "female": female_count}
    


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    users = data['results']
    older_ages = []

    for user in users:
        if user["dob"]["age"] > age:
            older_ages.append(user["email"])

    return older_ages


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    users = data["results"]

    sorted_users = sorted(users, key=lambda user: user["dob"]["age"], reverse=descending)

    result = []
    for user in sorted_users:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        age = user["dob"]["age"]
        result.append({"name": full_name, "age": age})

    return result


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    usernames = []

    for user in data["results"]:
        username = user["login"]["username"]
        if username.startswith(letter):
            usernames.append(username)

    return usernames



def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    total_age = 0
    users = data['results']

    for user in users:
        total_age += user['dob']['age']

    average = total_age / len(users)
    return average


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    users = data["results"]
    nationalities = {}

    for user in users:
     nat = user["nat"]
     if nat in nationalities:
        nationalities[nat] += 1
     else:
        nationalities[nat] = 1
    return nationalities


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    return [
        (user["location"]["coordinates"]["latitude"], user["location"]["coordinates"]["longitude"])
        for user in data["results"]
    ]


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    oldest = max(data["results"], key=lambda u: u["dob"]["age"])
    full_name = f"{oldest['name']['first']} {oldest['name']['last']}"
    return {
        "name": full_name,
        "age": oldest["dob"]["age"],
        "email": oldest["email"]
    }



def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    users = []
    for user in data["results"]:
        if user["location"]["timezone"]["offset"] == offset:
            full_name = f"{user['name']['first']} {user['name']['last']}"
            city = user["location"]["city"]
            users.append({"name": full_name, "city": city})
    return users


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    users = []
    for user in data["results"]:
        reg_date = user["registered"]["date"]  # Example: '2004-06-29T12:00:00Z'
        reg_year = int(reg_date[:4])
        if reg_year < year:
            full_name = f"{user['name']['first']} {user['name']['last']}"
            users.append({"name": full_name, "registered": reg_date[:10]})
    return users


