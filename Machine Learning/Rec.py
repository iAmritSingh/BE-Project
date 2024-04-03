import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Load your DataFrame
# Example DataFrame:
# df_long = pd.DataFrame({
#     'username': ['user1', 'user1', 'user2', 'user2', 'user3'],
#     'skill': ['skill1', 'skill2', 'skill1', 'skill3', 'skill2'],
#     'number_of_questions': [10, 5, 8, 3, 6]
# })

df = pd.read_csv('Leetcode.csv')

df = df.drop(['total','easy','medium','hard','rating','C++','Java','Python','Python3','C','C#','JavaScript','TypeScript','PHP','Swift','Kotlin','Dart','Go','Ruby','Scala','Rust','Racket','Erlang','Elixir','MySQL','MS SQL Server','Oracle','Pandas','PostgreSQL','ranking','contestAttended','streak','totalActiveDays','OurRating'],axis=1)

df_long = df.melt(id_vars=['username'], var_name='skill', value_name='number_of_questions')


# Step 1: Preprocess the data
def preprocess_data(df):
    # Encode categorical variables
    # print(df)
    for i in df['number_of_questions']:
       
           
        if i>15:
            i = 1
        else:
            i = 0
            
    label_encoder = LabelEncoder()
    df['username'] = label_encoder.fit_transform(df['username'])
    df['skill'] = label_encoder.fit_transform(df['skill'])
    return df

# Step 2: Calculate user-skill similarity matrix
def calculate_similarity_matrix(df):
    pivot_table = df.pivot_table(index='username', columns='skill', values='number_of_questions', fill_value=0)
    similarity_matrix = cosine_similarity(pivot_table)
    return similarity_matrix

# Step 3: Identify similar users for a specific skill
def identify_similar_users(skill_index, similarity_matrix, df):
    pivot_table = df.pivot_table(index='username', columns='skill', values='number_of_questions', fill_value=0)
    
    # Sort users by similarity score for the given skill
    similar_users_indices = sorted(range(len(similarity_matrix)),
                                   key=lambda i: similarity_matrix[i][skill_index],
                                   reverse=True)
    
    return similar_users_indices

# Step 4: Generate recommendations for users to do questions on a specific skill
def generate_skill_recommendations(skill, similarity_matrix, df, n=5):
    # Find the index of the skill
    label_encoder = LabelEncoder()
    skill_index = label_encoder.fit_transform([skill])[0]
    
    # Identify similar users for the given skill
    similar_users_indices = identify_similar_users(skill_index, similarity_matrix, df)
    
    # Get users who haven't done questions on the skill
    users_with_skill = df[df['skill'] == skill_index]['username']
    users_without_skill = set(df['username']) - set(users_with_skill)
    
    # Generate recommendations for users without the skill
    recommendations = []
    for user_index in users_without_skill:
        similar_user_index = next((i for i in similar_users_indices if pivot_table.iloc[i][user_index] > 0), None)
        if similar_user_index is not None:
            recommendations.append((user_index, similarity_matrix[similar_user_index][user_index]))
    
    # Sort recommendations by similarity score
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:n]

# Example usage
if __name__ == "__main__":

    df = pd.read_csv('Leetcode.csv')

    df = df.drop(['total','easy','medium','hard','rating','C++','Java','Python','Python3','C','C#','JavaScript','TypeScript','PHP','Swift','Kotlin','Dart','Go','Ruby','Scala','Rust','Racket','Erlang','Elixir','MySQL','MS SQL Server','Oracle','Pandas','PostgreSQL','ranking','contestAttended','streak','totalActiveDays','OurRating'],axis=1)

    df_long = df.melt(id_vars=['username'], var_name='skill', value_name='number_of_questions')
    # Preprocess the data
    df_long = preprocess_data(df_long)

    print(df)

    
    # Calculate user-skill similarity matrix
    similarity_matrix = calculate_similarity_matrix(df_long)
    
    # Specify the skill for which recommendations will be generated
    target_skill = 'Backtracking'  # Replace with the target skill
    
    # Generate recommendations for users to do questions on the specified skill
    recommendations = generate_skill_recommendations(target_skill, similarity_matrix, df_long)
    
    print("Recommendations for users to try questions on {}: \n{}".format(target_skill, recommendations))
