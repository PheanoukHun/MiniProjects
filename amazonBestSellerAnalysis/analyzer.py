from analyzer_class import Analyzer

if __name__ == "__main__":

    # Initializing the Analyzer Class
    analyze = Analyzer("bestsellers.csv")
    
    # Cleaning up the Data
    analyze.drop_duplicate_data()

    # Renaming the Column
    analyze.rename_columns({"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"})

    # Changing the Datatype of the price to be a Float
    analyze.convertDataType()

    # Gettings the Authors with the Most Best Selling Books
    author_counts = analyze.df["Author"].value_counts()
    print("\n", author_counts, "\n")

    # Getting the Average Rating by Genre
    avg_rating_by_genre = analyze.df.groupby("Genre")["Rating"].mean()
    print("\n", avg_rating_by_genre, "\n")

    # Highest Rated Book
    highest_rated_book = analyze.df.loc[analyze.df["Rating"].idxmax()]
    print("\n", highest_rated_book, "\n")

    # Lowest Price
    cheapest_book = analyze.df.loc[analyze.df["Price"].idxmin()]
    print("\n", cheapest_book, "\n")

    # Sorting the Book Lists by Ratings
    sorted_by_reviews = analyze.df.sort_values("Rating", ascending = False)

    # Exporting the Results
    author_counts.head(10).to_csv("top_author.csv")
    avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
    sorted_by_reviews.to_csv("sorted_by_reviews.csv")

    with open("high_rated_book.txt", "w") as file:
        file.write(highest_rated_book.to_string())

    with open("cheapest_book.txt", "w") as file:
        file.write(cheapest_book.to_string())