import matplotlib.pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West side story']
num_oscar = [5,11,3,8,10]

plt.bar(range(len(movies)), num_oscar)
plt.title("Meus filmes favoritos")
plt.ylabel("Da academia awards")
plt.xticks(range(len(movies)), movies)
plt.show()