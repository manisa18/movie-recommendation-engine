import streamlit as st
import bz2
import pickle
import _pickle as cPickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b68dee14d6128412d926397b97a0d971&language=en-US'.format(movie_id))
    data = response.json()
    
    poster_path = data['poster_path']
    poster_url = "http://image.tmdb.org/t/p/w500/" + poster_path
    
    return poster_url

def movie_url(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b68dee14d6128412d926397b97a0d971&language=en-US'.format(movie_id))
    data = response.json()
    
    poster_link = data['homepage']
    return poster_link

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_url = []

    for i in  movies_list:
        movie_id  = movies.iloc[i[0]].movie_id

        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_url.append(movie_url(movie_id))

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,recommended_movies_poster, recommended_movies_url

def decompress_pickle(file):
 similarity = bz2.BZ2File(file, 'rb')
 similarity = cPickle.load(similarity)
 return similarity

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = decompress_pickle('similarity.pbz2') 



st.set_page_config(page_title="Movie Recommendation")
st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'Which movie you want to search?',
    (movies['title'].values))

if st.button('Recommend'):
    name,poster,url = recommend(selected_movie_name)

    css = """

        <style>
        .button {
        display: inline-block;
        padding: 5px 25px;
        background-color: #ffff;
        color: #050505;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        border-radius: 4px;
        border: none;
        cursor: pointer;
        }

        .button:hover {
        text-decoration: none;
        background-color: #dbdbdb;
        }

        .button:active {
        background-color: #dbdbdb;
        }
        </style>
    """
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])
        st.markdown(css, unsafe_allow_html=True)
        button_html = f'<div><a href="{url[0]}" target="_blank" class="button">VISIT</a></div>'
        if not url[0]:
           st.error("Link Not Available") 
        else:
            st.markdown(button_html, unsafe_allow_html=True)
    with col2:
        st.text(name[1])
        st.image(poster[1])
        st.markdown(css, unsafe_allow_html=True)
        button_html = f'<div><a href="{url[1]}" target="_blank" class="button">VISIT</a></div>'
        if not url[1]:
           st.error("Link Not Available") 
        else:
            st.markdown(button_html, unsafe_allow_html=True)

    with col3:
        st.text(name[2])
        st.image(poster[2])
        st.markdown(css, unsafe_allow_html=True)
        button_html = f'<div><a href="{url[2]}" target="_blank" class="button">VISIT</a></div>'
        if not url[2]:
           st.error("Link Not Available") 
        else:
            st.markdown(button_html, unsafe_allow_html=True)

    with col4:
        st.text(name[3])
        st.image(poster[3])
        st.markdown(css, unsafe_allow_html=True)
        button_html = f'<div><a href="{url[3]}" target="_blank" class="button">VISIT</a></div>'
        if not url[3]:
           st.error("Link Not Available") 
        else:
            st.markdown(button_html, unsafe_allow_html=True)

    with col5:
        st.text(name[4])
        st.image(poster[4])
        st.markdown(css, unsafe_allow_html=True)
        button_html = f'<div><a href="{url[4]}" target="_blank" class="button">VISIT</a></div>'
        if not url[4]:
           st.error("Link Not Available.") 
        else:
            st.markdown(button_html, unsafe_allow_html=True)