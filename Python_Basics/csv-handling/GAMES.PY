number_of_games = int(input("How many games do you want to enter? "))

with open("games.csv", "w") as file:

    file.write("name,genre,developer,esrb\n")

    for i in range(number_of_games):

        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        esrb = input("ESRB: ")

        file.write(f"{name},{genre},{developer},{esrb}\n")

print("Games saved successfully")