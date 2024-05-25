import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise.dump import dump, load
from collections import defaultdict

# Read the LeetCode dataset


def get_recommendations(username):
    df = pd.read_csv('./Leetcode.csv')

    # Drop unnecessary columns
    df = df.drop(['total', 'easy', 'medium', 'hard', 'rating', 'C++', 'Java', 'Python', 'Python3', 
                'C', 'C#', 'JavaScript', 'TypeScript', 'PHP', 'Swift', 'Kotlin', 'Dart', 'Go', 
                'Ruby', 'Scala', 'Rust', 'Racket', 'Erlang', 'Elixir', 'MySQL', 'MS SQL Server', 
                'Oracle', 'Pandas', 'PostgreSQL', 'ranking', 'contestAttended', 'streak', 
                'totalActiveDays', 'OurRating', 'contest_LastYear', 'contest_6months', 
                'contest_1month', 'last1monthActiveDays', 'last6monthActiveDays'], axis=1)

    # Reshape the data into long format
    df_long = df.melt(id_vars=['username'], var_name='skill', value_name='number_of_questions')

    # Replace 0 values with -1
    df_long['number_of_questions'] = df_long['number_of_questions'].replace(0, -1)

    # Define a reader object
    reader = Reader(rating_scale=(-1, 5))

    # Load dataset from DataFrame
    dataset = Dataset.load_from_df(df_long[['username', 'skill', 'number_of_questions']], reader)

    # Set seed for reproducibility
    seed = 42

    # Split the dataset into train and test sets
    trainset, testset = train_test_split(dataset, test_size=0.2, random_state=seed)

    # Choose a similarity metric and build the model
    sim_options = {'name': 'cosine', 'user_based': True}
    model = KNNBasic(sim_options=sim_options)

    # Train the model
    model.fit(trainset)

    # Save the trained model to disk
    # model_path = 'knn_model.pkl'
    # dump(model_path, algo=model)



    # Load the trained model from disk
    # _, loaded_model = load(model_path)
    
    # Create a dictionary to store recommended items for each user
    recommendations = defaultdict(list)
    
    # Make predictions for the test set
    predictions = model.test(testset)
    
    # Iterate over the predictions
    for prediction in predictions:
        uid = prediction.uid  # Get the user ID
        iid = prediction.iid  # Get the item ID (skill/topic)
        est = prediction.est  # Get the estimated rating
        
        # Store the recommended item for the user with its estimated rating
        recommendations[uid].append((iid, est))
    
    # Sort the recommendations for the provided user based on the estimated rating
    user_recs = recommendations.get(username, [])
    user_recs.sort(key=lambda x: x[1], reverse=True)
    
    return user_recs