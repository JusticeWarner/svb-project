import json

# Returns dictionary of usernames to amount of repos
# Reads data from users.csv
def get_users():
    users = {}

    with open("users.csv") as f:
        for line in f:
            # Removes new line and gets last item in csv line
            user = line.strip().split(",").pop()

            if user:
                # Add username to dict and set to 0 repos
                users[user] = 0

    return users

# Returns a list of lists containing usernames for each repo
# Reads repos.json
def get_repo_users():
    users = []

    with open("repos.json") as f:
        data = json.load(f)

        # Appends list of users for each repo
        for repo in data:
            users.append(repo["Users"])

    return users

# Calculates the number of repos each user has
def calculate_user_repos(users, repo_users):
    for user in users:
        for repo in repo_users:
            # For each user, loop all the repos

            if user in repo:
                # If the user was included in the repo, increment the user
                users[user] += 1


def main():
    # Dictionary of usernames to the number of repositories
    users = get_users()

    # List of lists containing usernames for each repo
    repo_users = get_repo_users()

    # Count number of assigned repos for each user
    calculate_user_repos(users, repo_users)

    # Sort users based on number of repos in descending order
    for user in sorted(users, key=lambda u: users[u], reverse=True):
        if users[user] > 0:
            # Prints users with repositories
            print(f"{user} - {users[user]} repos")


if __name__ == "__main__":
    main()