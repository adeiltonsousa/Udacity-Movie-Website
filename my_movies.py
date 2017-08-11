import fresh_tomatoes
import media

the_phantom_menace = media.Movie(
                    "Star Wars Episode I: The Phantom Menace",
                    "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                    "https://youtu.be/bD7bpG-zDJQ")

attack_of_the_clones = media.Movie(
                    "Star Wars Episode II: Attack of the Clones",
                    "https://shotonwhat.com/images/0121765.jpg",
                    "https://youtu.be/gYbW1F_c9eM")

captain_america = media.Movie(
                    "Captain America: The First Avenger",
                    "https://www.designerd.com.br/wp-content/uploads/2015/08/releituras-cartazes-filmes-famosos-Marko-Manev-7.jpg",
                    "https://youtu.be/JerVrbLldXw")

the_battle_of_the_five_armies = media.Movie(
                    "The Hobbit: The Battle of the Five Armies",
                    "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                    "https://youtu.be/ZSzeFFsKEt4")

les_miserables = media.Movie(
                    "Les Miserables",
                    "http://fr.web.img5.acsta.net/medias/nmedia/18/91/00/76/20364091.jpg",
                    "https://youtu.be/YmvHzCLP6ug")

the_avengers = media.Movie(
                    "The Avengers",
                    "https://i.annihil.us/u/prod/marvel/i/mg/6/50/521f70b81f7d3/portrait_incredible.jpg",
                    "https://youtu.be/pPqUuXEzIP4")

my_movies = [the_phantom_menace, attack_of_the_clones, captain_america, the_battle_of_the_five_armies, les_miserables,
             the_avengers]

# Função "open_movies_pages" presente no arquivo "fresh_tomatoes" resposável por exibir a lista "my_movies" em uma página HTML.
fresh_tomatoes.open_movies_page(my_movies)
