import pickle
import streamlit as st
import pandas as pd

movies_model_path ='../models/movies.pkl'
similarity_model_path = '../models/similarity.pkl'
def recommend(movie_name, movie_df):

    movie_index=movie_df[movie_df['title']==movie_name].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommendation=[]
    for i in movies_list:
        recommendation.append(movies.iloc[i[0]].title)
    return  recommendation

movie_model=pickle.load(open(movies_model_path, 'rb'))
similarity=pickle.load(open(similarity_model_path, 'rb'))
movies=pd.DataFrame(movie_model)
movies_list=movies['title'].values

st.title('Movies Recommendation System')
selected_movie_name=st.selectbox('Select your movie.',movies_list)
if st.button("Recommend", type="primary"):
    rec=recommend(selected_movie_name,movies)
    for i in rec:
        st.write(i)
