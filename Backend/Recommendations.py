import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('./Leetcode.csv')

data = data.drop(['total','easy','medium','hard','rating','C++','Java','Python','Python3','C','C#','JavaScript','TypeScript','PHP','Swift','Kotlin','Dart','Go','Ruby','Scala','Rust','Racket','Erlang','Elixir','MySQL','MS SQL Server','Oracle','Pandas','PostgreSQL','ranking','contestAttended','streak','totalActiveDays','OurRating','contest_LastYear','contest_6months','contest_1month','last1monthActiveDays','last6monthActiveDays'],axis=1)

relevant_skill_columns = data.columns[1:]

vectorizer = CountVectorizer()
skill_matrix = vectorizer.fit_transform(data[relevant_skill_columns])

similarity_matrix = cosine_similarity(skill_matrix)


def recommend_skills(username, k=5):
  # Find all rows for the target user
  user_data = data[data["username"] == username]
  # print(len(user_data))

  # Handle cases where a user has only one row
  if len(user_data) == 1:
      user_index = user_data.index.values[0]
      user_skills = user_data[relevant_skill_columns].values.tolist()[0]  # Assuming skills in separate columns
  else:
      # Combine all skills from the user's rows into a set (assuming unique skills)
      user_skills = set(user_data[relevant_skill_columns].values.flatten())

  # Calculate similar users for all cases (single or multiple rows)
 
  user_index = user_data.index.values[0]
  
  similar_users = similarity_matrix[user_index].argsort()[-k:][::-1]
  
  
  # Extract skills from neighbors
  neighbor_skills = data.loc[similar_users, relevant_skill_columns].values.tolist()
  neighbor_skills_flat = [item for sublist in neighbor_skills for item in sublist]  # Flatten nested list
  unique_skills = set(neighbor_skills_flat) - set(user_skills)
  
  # Filter recommended skills based on valid indices
  valid_skill_indices = range(len(vectorizer.get_feature_names_out()))  # Get valid skill indices
  filtered_unique_skills = unique_skills.intersection(valid_skill_indices)
  
  # Map recommended skill indices to skill names using CountVectorizer vocabulary
  recommended_skill_names = [vectorizer.get_feature_names_out()[idx] for idx in filtered_unique_skills]
  return recommended_skill_names
# Example usage
# username = "vivekthedev"
# k = 5  # Number of recommendations

# recommended_skills = recommend_skills(username, k)
# print(f"Recommended skills for {username}: {recommended_skills}")