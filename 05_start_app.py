import streamlit as st

st.title('스트림릿 !')
st.write('Hi~ streamlit')

st.divider()  # 구분선

name = st.text_input('이름: ')
if name:    
    st.write(f'안녕하세요 {name} 님')


st.divider()

import pandas as pd

df_abnb = pd.read_csv('data/ABNB_stock.csv')
print(df_abnb)
df_abnb