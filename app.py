import streamlit as st
from domain_clean_streamlit import read_xl
import zipfile

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.download_button('Process CSV', read_xl(uploaded_file), f'{uploaded_file.name}'.split('.')[0]+'.csv', 'text/csv')
    #st.success('Thanks for downloading!', icon="✅")

st.write("Powered by [dJolt](https://djolt.co/)")

# #draft decorator
# def out_fn(in_fn):
#     archive = zipfile.ZipFile('filename.zip', 'r')
#     xlfile = archive.open('filename.xlsx')
#     if uploaded_file is not None:
#         st.download_button('Process CSV', read_xl(uploaded_file), f'{uploaded_file.name}'.split('.')[0]+'.csv', 'text/csv')

# #draft - zip_file opener and read excel
# def archive(uploaded_file):
#     archive = zipfile.ZipFile('filename.zip', 'r')
#     xlfile = archive.open('filename.xlsx')