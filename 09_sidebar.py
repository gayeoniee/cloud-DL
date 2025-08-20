import streamlit as st
import pandas as pd
from PIL import Image

# sidebar, columns, tabs, expander
st.title('스트림릿 앱 페이지 구성')

st.sidebar.header('welcome menu')
selected_menu = st.sidebar.selectbox(
                    'select menu', ['main', 'analysis', 'setting']
                )

# 분석 페이지의 분석 탭 구성 함수
def make_anal_tab():
    tab1, tab2= st.tabs(['chart', 'data'])
    with tab1:
        st.subheader('chart tab')
        st.bar_chart({'data':[1, 2, 3, 4, 5]})
        
    with tab2:
        st.subheader('data tab')
        st.dataframe({'standard':[1, 2, 3, 4, 5], 'value':['a', 'b', 'c', 'd', 'e']})

# 체크박스(활성화 여부), 슬라이더(업데이트 주기 sec)    
def make_set_tab():
    (tab1,) = st.tabs(['settings'])
    with tab1:
        st.subheader('settings tab')
        st.checkbox('auto update vitalization')
        st.slider('update cycle(sec)', min_value=1, max_value=60, value=1)
    

img = Image.open('img/모래두지.png')
img2 = Image.open('img/리오르.png')

if selected_menu =='main':
    st.subheader('*main page*')
    st.write('welcome!!')
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, width=300, caption='Image from unsplash')
    with col2:
        st.image(img2, width=300, caption='Image from unsplash')

elif selected_menu == 'analysis':
    st.subheader('anal report')
    st.write('you can choose data here!')
    make_anal_tab()
else:
    st.subheader('setting change')
    st.write('you can change settings here!')
    make_set_tab()
    
if st.sidebar.button('select'):
    st.sidebar.write('click select')
    
# 슬라이드바 추가 0~100, 50
st.sidebar.slider('slider', 0, 100, 50)

st.divider()

# 확장영역 추가
st.header('익스팬더 추가')

with st.expander('숨긴 영역'):
    st.write('여기는 클릭해야 보임!')
