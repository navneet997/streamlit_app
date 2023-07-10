import streamlit
import pandas
streamlit.title(' New Healthy Diner App')
streamlit.header('🥗 Breakfast Menu')
streamlit.text(' 🥑Pohe')
streamlit.text('🍞Paranthe')
streamlit.text('🥣Magie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
