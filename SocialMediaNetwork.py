########################################################################################################################
#   Computer Project #6
#
#   open_file:
#       Prompt user for file name and open file.
#       If file does not exist then will keep prompting.
#
#   read_file:
#       Will iterate through file and get the number of users in and create a list containing information about each
#       user's friends are.
#
#   num_in_common_between_lists:
#       Will find the number of common friends that users have by comparing 2 lists.
#
#   calc_similarity_scores:
#       Will use the num_in_common_between_lists function to calculate every user's compatibility with every user,
#       and returning one final list with all the results user by user.
#
#   recommend:
#       Will use the calc_similarity_scores funtion to calculate who is the most recommended friend for the user
#       selected in the main funtion.
#
#   main:
#       Will open file, read it, prompt which user recommendation is desired, then give recommendation and ask user if
#       he/she/they want to keep using application.
#
########################################################################################################################

def open_file():
    '''
    Function will keep prompting the user for a valid file name, if a nonexistent file is entered, error message will be
    displayed until necessary, when correct input is received file will be open.
    Returns a file pointer.
    '''
    while True:  # will keep looping until conditions are met
        try:  # try to open an existing file
            file = input("\nEnter a filename: ")
            fp = open(file)
            return fp
        except:  # if file nonexistent prints error message and ask for input again
            print("\nError in filename.")


def read_file(fp):
    '''
    Will use the file pointer from open_file() as the only parameter.
    Will iterate through the first line of the file to get the number of users, then use this variable to create empty
    lists in the final list. Then iterate through the rest of the characters in all the other lines of the file to find
    which user's friends and append it to the list at the user's specific list, for example user 0's list will be in the
    final list 0 index.
    Returns the network
    '''
    first_line = True  # boolean to control which line is being iterated and which action to take.
    network = []
    global num_users  # making num_users global so it can be used in main function without needing to be returned

    for line in fp:
        if first_line == True:  # first line is the one being iterated right now
            num_users = line.replace(" ", "")
            num_users = int(num_users)

            for n in range (num_users):  # creating empty lists in a bigger list, one for each user
                user_list = []
                network.append(user_list)

        if first_line == False:  # after first line the following code will be executed
            nospace = line.split()  # takes all spaces away from line
            num1 = nospace[0]  # num1 is the first number in the list nospace
            num1 = int(num1)
            num2 = nospace[1]  # num2 is the second number in the list nospace
            num2 = int(num2)
            network[num1].append(num2)
            network[num2].append(num1)
        first_line = False  # after reading first line, set variable to false so that if block is executed

    return network


def num_in_common_between_lists(list1, list2):
    '''
    Takes 2 lists as parameters. It will iterate through every number of the list of lists, and will see how many common
    friends both these users have.
    Returns common number
    '''
    common_num = 0
    for item in list1:  # iterate through every item in list
        if item in list2:  # iterate through every number in every item in the list
            common_num += 1
    return common_num


def calc_similarity_scores(network):
    '''
    Will take network as a parameter. First will create a list of lists, with one list for each user. Then it will use
    the function num_in_common_between_lists(list1, list2), to compare every user's friends and create a list of lists
    and each of the lists are for one user and the amount of common friends he/she shares with all the other users.
    Returns the list with the similarity scores
    '''
    list_similarity = []  # initializing empty list for the similarity scores
    for item in network:
        user_list = []
        list_similarity.append(user_list)  # will append n empty lists into similarity list, n is number of users.

    for i in range(len(network)):  # iterate through lists in the similarity list
        for n in range(len(network)):  # iterate through numbers in the lists in the similarity list
            list1 = network[i]  # will set list1 as the first loop counter
            list2 = network[n]  # will set list2 as the second loop counter
            x = num_in_common_between_lists(list1, list2)  # use function to compare both lists and return an integer
            list_similarity[i].append(x)
    return list_similarity


def recommend(user_id, network, similarity_matrix):
    '''
    Will take the user_id, result from read_file function, and the result from calc_similarity_scores function.
    Firstly, will create a list with numbers present in each list in the similarity_matrix for an easier numbers
    management. Then will calculate the maximum number in the list_index, however this max cannot occur in the index
    where this user had been compared to itself nor if it occurs in the index where this user is compared to another
    user whose are already friends.
    Returns a friend suggestion
    '''
    list_index = []  # initialize empty string
    not_found = True  # variable to keep track if friend recommendation has yet been found
    for num in similarity_matrix[user_id]:
        list_index.append(num)
    while not_found:
        max_num = max(list_index)
        friend_recommendation = list_index.index(max(list_index))  # index is equal to where the maximum value occurred

        # if statement will make sure the recommended friend is not the user_id nor already a friend.
        if friend_recommendation not in network[user_id] and friend_recommendation != user_id:
            return friend_recommendation

        list_index[friend_recommendation] = 0
        # if user is already friends with recommended friend or is the recommended friend then set value to 0 and check
        # again for max value


def main():
    print("Facebook friend recommendation.\n")
    option = ""  # initialize option variable to store info weather user wants to keep using application
    fp = open_file()  # open file using function
    network = read_file(fp)  # create a list of which user is friends with.

    while option != "no":  # will keep prompting until user types "no".
        i = 0  # initializes counter
        user_id = input(f"\nEnter an integer in the range 0 to {num_users - 1}:")
        while i != 1:
            try:  # will try to convert input to integer
                user_id = int(user_id)
                if 0 <= user_id < num_users:
                    i += 1  # will break out of loop since we have a valid input

                while user_id < 0 or user_id >= num_users:
                    print(f"\nError: input must be an int between 0 and {num_users - 1}")
                    user_id = int(input(f"\nEnter an integer in the range 0 to {num_users - 1}:"))

            except ValueError:  # if input cannot be converted to a integer
                print(f"\nError: input must be an int between 0 and {num_users - 1}")
                user_id = input(f"\nEnter an integer in the range 0 to {num_users - 1}:")

        similarity_list = calc_similarity_scores(network)
        friend_recommendation = recommend(user_id, network, similarity_list)
        print(f"\nThe suggested friend for {user_id} is {friend_recommendation}")
        option = input("\nDo you want to continue (yes/no)? ").lower()


if __name__ == "__main__":
    main()

