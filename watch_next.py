import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_md")

# Define a function to compute similarity scores and return the title of the most similar movie
def recommend_movie(rec_description):
    # Read in the movie descriptions from the file
    with open("movies.txt", "r") as f:
        movie_descriptions = [line.split(" :")[1] for line in f]

    # Compute similarity scores for each movie
    similarities = []
    rec_description_doc = nlp(rec_description)
    for movie_description in movie_descriptions:
        movie_doc = nlp(movie_description)
        similarity = movie_doc.similarity(rec_description_doc)
        similarities.append(similarity)

    # Find the index of the most similar movie
    index = similarities.index(max(similarities))

    # Return the title of the most similar moviels
    with open("movies.txt", "r") as f:
        for i, line in enumerate(f):
            if i == index:
                return line.split(" :")[0]
            

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = recommend_movie(description)
print("You should watch", recommended_movie)