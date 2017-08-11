import fresh_tomatoes
import media

captain_america = media.Movie(
                    "Captain America: The First Avenger",
                    "https://www.designerd.com.br/wp-content/uploads/2015/08/releituras-cartazes-filmes-famosos-Marko-Manev-7.jpg",
                    "https://youtu.be/JerVrbLldXw")

les_miserables = media.Movie("Les Miserables",
                    "http://fr.web.img5.acsta.net/medias/nmedia/18/91/00/76/20364091.jpg",
                    "https://youtu.be/YmvHzCLP6ug")

the_avengers = media.Movie(
                    "The Avengers",
                    "https://i.annihil.us/u/prod/marvel/i/mg/6/50/521f70b81f7d3/portrait_incredible.jpg",
                    "https://youtu.be/pPqUuXEzIP4")

the_phantom_menace = media.Movie(
                    "Star Wars Episode I: The Phantom Menace",
                    "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                    "https://youtu.be/bD7bpG-zDJQ")

attack_of_the_clones = media.Movie(
                    "Star Wars Episode II: Attack of the Clones",
                    "https://shotonwhat.com/images/0121765.jpg",
                    "https://youtu.be/gYbW1F_c9eM")

revenge_of_the_sith = media.Movie(
                    "Star Wars Episode III: Revenge of the Sith",
                    "http://br.web.img3.acsta.net/medias/nmedia/18/92/58/33/20207204.jpg",
                    "https://youtu.be/5UnjrG_N8hU")

the_battle_of_the_five_armies = media.Movie(
                    "The Hobbit: The Battle of the Five Armies",
                    "http://br.web.img3.acsta.net/medias/nmedia/18/92/58/33/20207204.jpg",
                    "https://youtu.be/ZSzeFFsKEt4")

my_movies = [captain_america, the_avengers, the_phantom_menace, attack_of_the_clones, les_miserables,
             the_battle_of_the_five_armies]

fresh_tomatoes.open_movies_page(my_movies)