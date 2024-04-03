from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample DSA topics data
dsa_topics = {
    'topic': ['Arrays', 'Linked Lists', 'Stacks', 'Queues', 'Trees', 'Graphs'],
    'description': [
        'Collection of elements of same data type',
        'Collection of nodes that form a sequence',
        'Last-In-First-Out (LIFO) data structure',
        'First-In-First-Out (FIFO) data structure',
        'Non-linear data structure with parent-child relationships',
        'Non-linear data structure with vertices and edges'
    ]
}

# Convert data into DataFrame
import pandas as pd
topics_df = pd.DataFrame(dsa_topics)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(topics_df['description'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(cosine_sim)

# Function to get content-based recommendations for a DSA topic
def get_dsa_recommendations(topic_name, cosine_sim=cosine_sim, top_n=5):
    idx = topics_df.index[topics_df['topic'] == topic_name].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    topic_indices = [i[0] for i in sim_scores]
    return topics_df['topic'].iloc[topic_indices]

# Example: Get content-based recommendations for 'Arrays'
topic_name = 'Arrays'
recommendations = get_dsa_recommendations(topic_name)
print(f"Content-Based Recommendations for '{topic_name}':")
print(recommendations)
