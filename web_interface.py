import streamlit as st
import pandas as pd
import pickle
import requests  #to get the api

#creating the moive_poster path through api
def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    complete_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return complete_path


#this function returns the top five similar movies name (code is similar to jupyter)
def recommend(movie): 
    movie_indx = df[df['title'] == movie].index[0]
    distance = similarity[movie_indx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    movie_posters=[]
    for i in movie_list:
        movie_id=df.iloc[i[0]].movie_id
        movie_posters.append(fetch_poster(movie_id))   #it is the moive_id 
        recommend_movies.append(df.iloc[i[0]].title)

    return recommend_movies, movie_posters


#loading the files that are created in ipython
df_dict=pickle.load(open('df_dict.pkl','rb'))   #getting the df but in dict format using pickle
df=pd.DataFrame(df_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_moive_name=st.selectbox("Type or select a movie from the dropdown",options=df['title'].values)

# displaying moive name and its image or poster
if st.button('Show Recommendations'):
    name,poster=recommend(selected_moive_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
 