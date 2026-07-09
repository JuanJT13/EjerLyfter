import csv


def get_games():

    games = []

    number_of_games = int(input("How many games do you want to enter? "))

    for i in range(number_of_games):

        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        esrb = input("ESRB: ")

        games.append([name, genre, developer, esrb])

    return games


def save_games(games):

    with open("games.tsv", "w", newline="") as file:

        writer = csv.writer(file, delimiter="\t")

        writer.writerow(["name", "genre", "developer", "esrb"])

        writer.writerows(games)


def main():

    games = get_games()

    save_games(games)

    print("Games saved successfully")


main()