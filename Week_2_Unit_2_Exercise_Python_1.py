"""Below you find a code snippet to create a Python list containing the titles of all Star Wars movies. The list contains:

A list containing the titles of the prequel trilogy: The Phantom Menace, Attack of the Clones, Revenge of the Sith
A list containing the titles of the original trilogy: A New Hope, The Empire Strikes Back, Return of the Jedi,
A list containing the titles of the sequel trilogy: The Force Awakens, The Last Jedi, The Rise of Skywalker

"""

star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

#Write a program that asks the user for a number of the trilogy (1, 2 or 3) and the number of the film in this trilogy (1, 2 or 3). Print the title of the film corresponding to the user selection.

trilogy = int(input("Write the number of the trilogy:"))
film = int(input("Write the number of the movie:"))
print(star_wars_movies[trilogy - 1][film - 1])