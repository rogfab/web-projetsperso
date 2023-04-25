import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=250)

with col2:
    st.title("Fabrice Roger")
    content1 = """
    Quapropter a natura mihi videtur potius quam ab indigentia orta amicitia, applicatione 
    magis animi cum quodam sensu amandi quam cogitatione quantum illa res utilitatis esset habitura. 
    Quod quidem quale sit, etiam in bestiis quibusdam animadverti potest, quae ex se natos ita amant 
    ad quoddam tempus et ab eis ita amantur ut facile earum sensus appareat.
    """
    st.info(content1)

content2 = """Des projets développés en Python sont donnés ci-dessous. Si vous souhaitez me contacter 
n'hésitez pas à parcourir ma page "A propos" """
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
