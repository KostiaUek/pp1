movie_titles = ["Inception", "The Shawshank Redemption", "Blade Runner 2049", "La La Land", "The Dark Knight"]


file = open("movies.txt", "w")
for title in movie_titles:
    file.write(title+"\n")
file.close()
