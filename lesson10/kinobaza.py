import sqlite3
import datetime

def movie_age(release_year):
    """Calculates the number of years from the release of a movie to the current year."""
    if release_year is None:
        return 0
    current_year = datetime.datetime.now().year
    return current_year - int(release_year)


def init_db():
    """Creating a database"""
    try:
        sqlite_connection = sqlite3.connect("./lesson10/kinobaza.db")
        sqlite_connection.create_function("movie_age", 1, movie_age)
        sqlite_connection.execute("PRAGMA foreign_keys = ON;")
        cursor = sqlite_connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
                       id INTEGER PRIMARY KEY,
                       title TEXT NOT NULL,
                       release_year INTEGER,
                       genre TEXT
                       )"""
                       )


        cursor.execute("""CREATE TABLE IF NOT EXISTS actors(
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       birth_year INTEGER
                       )"""
                       )
        

        cursor.execute("""CREATE TABLE IF NOT EXISTS movie_cast(
                    movie_id INTEGER,
                    actor_id INTEGER,
                    PRIMARY KEY(movie_id, actor_id),
                    FOREIGN KEY(movie_id) REFERENCES movies(id),
                    FOREIGN KEY(actor_id) REFERENCES actors(id)
                    )"""
                    )
        sqlite_connection.commit()

    except sqlite3.Error as error:
        print(f"Error: {error}")

    return sqlite_connection, cursor


def add_movie(sqlite_connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """Functiom for add movies to database"""
    title = input("Enter the title of movie: ")
    try:
        release_year = int(input("Enter the year of release: "))
    except ValueError:
        print("Error: Year must be a number.")
        return
    genre = input("Enter the genre: ")

    cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES(?, ?, ?)",
                   (title, release_year, genre))
    movie_id = cursor.lastrowid
    sqlite_connection.commit()

    print(f"Good. Movie {title} successffuly added! Now let's add a actors.")
    cursor.execute("SELECT id, name FROM actors")
    actors = cursor.fetchall()

    if actors:
        print("Available actors: ")
        for act in actors:
            print(f"{act[0]}. {act[1]}")

        actor_ids = input("Enter actor IDs separated by commas (or leave blank to skip): ")
        if actor_ids.strip():
            ids = [i.strip() for i in actor_ids.split(",")]
            
            for one_id in ids:
                try:
                    cursor.execute("INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)", (movie_id, int(one_id)))
                except sqlite3.Error as error:
                    print(f"Error: {error}")
                except ValueError:
                    print(f"{one_id} not correct ID.")

            sqlite_connection.commit()
            print("The actors have been successfully attached to the movie!")
    else:
        print("There are no actors in the database yet. First, add them via the menu.")


def add_actor(sqlite_connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """Function for add a actors to database"""
    name = input("Enter the name of actor: ")
    try:
        birth_year = int(input("Ether his birth of year: "))
    except ValueError:
        print("Error: Year must be a number.")
        return
    
    cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)", (name, birth_year))
    sqlite_connection.commit()
    print(f"Actor {name} successfully added!")


def show_movies_with_actors(cursor: sqlite3.Cursor) -> str:
    """Function displays a list of movies along with the names of all the actors who starred in each movie"""
    query = """
        SELECT movies.title, GROUP_CONCAT(actors.name, ', ')
        FROM movies
        INNER JOIN movie_cast ON movies.id = movie_cast.movie_id
        INNER JOIN actors ON movie_cast.actor_id = actors.id
        GROUP BY movies.id
        """
    
    cursor.execute(query)
    results = cursor.fetchall()

    print("\nMovies and actors:")

    if not results:
        print("The list is empty (add a movie and associate actors with it).")
        return
    
    for i, row in enumerate(results, 1):
        print(f"{i}. Movie: {row[0]}, Actors: {row[1]}")


def show_unique_genres(cursor: sqlite3.Cursor) -> str:
    """Function displays a unique list of movie genres"""
    cursor.execute("SELECT DISTINCT genre FROM movies WHERE genre IS NOT NULL AND genre != ''")
    results = cursor.fetchall()

    print("\nUnique genres:")

    for i, row in enumerate(results, 1):
        print(f"{i}. {row[0]}")

def count_movies_by_genre(cursor: sqlite3.Cursor) -> str:
    """Function to count the number of films made in each genre"""
    cursor.execute("SELECT genre, COUNT(*) FROM movies GROUP BY genre")
    results = cursor.fetchall()

    print("\nGenres and number of films:")
    
    for i, row in enumerate(results, 1):
        genre = row[0] if row[0] else "Without genre"
        print(f"{i}. Movie: {genre}: {row[1]}")


def avg_year_of_bitrh_by_genre(cursor: sqlite3.Cursor) -> str:
    """Function that finds the average year of birth of actors who appeared in films of a certain genre"""
    genre = input("Select a genre for counting: ")
    query = """
        SELECT AVG(actors.birth_year) 
        FROM actors
        INNER JOIN movie_cast ON actors.id = movie_cast.actor_id
        INNER JOIN movies ON movie_cast.movie_id = movies.id
        WHERE movies.genre = ?"""

    cursor.execute(query, (genre,))
    average_year = cursor.fetchone()[0]

    if average_year:
        print(f"\nAverage year of birth of actors in the genre '{genre}: {int(average_year)}'")
    else:
        print(f"\nNo actors found for genre '{genre}'.")


def search_movies_by_title(cursor: sqlite3.Cursor) -> str:
    """Function for search for movies by keyword in the title."""
    keyword = input("Enter the keyword for searching: ")
    cursor.execute("SELECT title, release_year FROM movies WHERE title LIKE ?", (f"%{keyword}%",))
    
    results = cursor.fetchall()
    
    if results:
        print("n\Found movies:")
        for i, row in enumerate(results, 1):
            print(f"{i}. {row[0]} ({row[1]})")
    else:
        print("No movies found.")


def show_moives_pagination(cursor: sqlite3.Cursor) -> str:
    """Function for watching movies with pagination."""
    try:
        limit = int(input("How many movies to show on a page? (LIMIT): "))
        page = int(input("Which page to show? (starting from 1): "))
    except ValueError:
        print("Please, enter the number!")
        return
    
    offset = (page - 1) * limit
    cursor.execute("SELECT title, release_year FROM movies LIMIT ? OFFSET ?", (limit, offset))
    results = cursor.fetchall()

    print(f"\nPage {page}:")
    if results:
        for i, row in enumerate(results, 1):
            print(f"{i}. {row[0]} ({row[1]})")
    else:
        print("There are no movies on this page.")


def show_union_names_and_titles(cursor: sqlite3.Cursor) -> str:
    """Function displays the names of all actors and the titles of all movies in one result"""
    query = """
        SELECT name AS entity_name, 'Actor' AS type FROM actors
        UNION
        SELECT title AS entity_name, 'Movie' AS type FROM movies"""
    
    cursor.execute(query)
    results = cursor.fetchall()

    print("\nNames of all actors and titles of all movies:")
    for i, row in enumerate(results, 1):
        print(f"{i}. {row[0]} ({row[1]})")


def show_moives_ages(cursor: sqlite3.Cursor) -> str:
    """Using our own movie_age() function"""
    cursor.execute("SELECT title, movie_age(release_year) FROM movies")
    results = cursor.fetchall()
    print("\nMovies and their age:")
    for i, row in enumerate(results, 1):
        age = row[1]
        word = "years"
        if age % 10 == 1 and age % 100 != 11:
            word = "year"
        elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
            word = "years"
            
        print(f"{i}. Movie: \"{row[0]}\" — {age} {word}")

def main():
    sqlite_connection, cursor = init_db()

    while True:
        print("\n--- Main menu ---")
        print("1. Add a movie.")
        print("2. Add a actor.")
        print("3. Show all movies with actors.")
        print("4. Show unique genres.")
        print("5. Show number of movies by genre.")
        print("6. Show the average year of birth of actors in films of a specific genre.")
        print("7. Search for a movie by title.")
        print("8. Show movies.")
        print("9. Show all actors names and all movie titles")
        print("10. Show movie age.")
        print("0. Exit.")

        choice = input("\nChoise the action: ")

        match choice:
            case "1":
                add_movie(sqlite_connection, cursor)
            case "2":
                add_actor(sqlite_connection, cursor)
            case "3":
                show_movies_with_actors(cursor)
            case "4":
                show_unique_genres(cursor)
            case "5":
                count_movies_by_genre(cursor)
            case "6":
                avg_year_of_bitrh_by_genre(cursor)
            case "7":
                search_movies_by_title(cursor)
            case "8":
                show_moives_pagination(cursor)
            case "9":
                show_union_names_and_titles(cursor)
            case "10":
                show_moives_ages(cursor)
            case "0":
                break
            case _:
                print("Unknown command. Try one more time.")

    sqlite_connection.close()

if __name__ == "__main__":
    main()
