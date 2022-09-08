# First we ask the user for the name of the restaurant they want to review.
restaurant = input("Please enter the name of the restaurant: ")
# Then we ask the user for the number of critics who have reviewed the restaurant, with a maximum of 10.
num_of_critics = int(input("Please enter the number of critics for " + restaurant + " (maximum 10): "))
# if the number of critics is greater than 10, we ask the user to enter a number less than 10.
while num_of_critics > 10:
    print("Invalid number of critics. Please enter a number between 1 and 10.")
    num_of_critics = int(input("Please enter the number of critics for " + restaurant + " (maximum 10): "))

# We create a list of all the scores.
food_score = []
wine_score = []
atmosphere_score = []

def get_average(score_list):
    # We calculate the average of the scores.
    # Average score should be rounded to 2 decimal places.
    average = round(sum(score_list) / len(score_list), 2)
    return average

# We ask the user to enter the scores for each of the three aspects of the restaurant.
print("Please enter the scores below. If not assessed, please enter NA, otherwise enter a number between 1 and 5.")

for i in range(num_of_critics):
    # We ask the user to enter the food score.
    # If it is NA don't add it to the list.
    # If it is not between 1 and 5, ask the user to enter a number between 1 and 5.
    food_score_input = input("Critic " + str(i + 1) + " Food Score: ")
    if food_score_input == "NA":
        continue
    while int(food_score_input) < 1 or int(food_score_input) > 5:
        print("Invalid score. Please enter a number between 1 and 5.")
        food_score_input = input("Critic " + str(i + 1) + " Food Score: ")
    food_score.append(int(food_score_input))
    # We ask the user to enter the wine score.
    # If it is NA don't add it to the list.
    # If it is not between 1 and 5, ask the user to enter a number between 1 and 5.
    wine_score_input = input("Critic " + str(i + 1) + " Wine Score: ")
    if wine_score_input == "NA":
        continue
    while int(wine_score_input) < 1 or int(wine_score_input) > 5:
        print("Invalid score. Please enter a number between 1 and 5.")
        wine_score_input = input("Critic " + str(i + 1) + " Wine Score: ")
    wine_score.append(int(wine_score_input))
    # We ask the user to enter the atmosphere score.
    # If it is NA don't add it to the list.
    # If it is not between 1 and 5, ask the user to enter a number between 1 and 5.
    atmosphere_score_input = input("Critic " + str(i + 1) + " Atmosphere Score: ")
    if atmosphere_score_input == "NA":
        continue
    while int(atmosphere_score_input) < 1 or int(atmosphere_score_input) > 5:
        print("Invalid score. Please enter a number between 1 and 5.")
        atmosphere_score_input = input("Critic " + str(i + 1) + " Atmosphere Score: ")
    atmosphere_score.append(int(atmosphere_score_input))

print(restaurant + "'s scores\n")

# We print the average scores for each of the aspects.
print("Food Scores\nAverage:" + str(get_average(food_score)) + "\nMaximum:" + str(max(food_score)) + "\nMinimum:" + str(min(food_score)))

# We print the highest score for each of the aspects.
print("\nWine Scores\nAverage:" + str(get_average(wine_score)) + "\nMaximum:" + str(max(wine_score)) + "\nMinimum:" + str(min(wine_score)))

# We print the lowest score for each of the aspects.
print("\nAtmosphere Scores\nAverage:" + str(get_average(atmosphere_score)) + "\nMaximum:" + str(max(atmosphere_score)) + "\nMinimum:" + str(min(atmosphere_score)))