import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('데이터 분석 웹앱')

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader('CSV 파일을 업로드하세요', type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('데이터 미리보기')
    st.dataframe(df.head())

    # 2. 전처리: 결측치 처리
    st.subheader('결측치 처리')
    if df.isnull().sum().sum() > 0:
        if st.button('결측치 행 제거'):
            df = df.dropna()
            st.success('결측치가 제거되었습니다.')
            st.dataframe(df.head())
    else:
        st.write('결측치가 없습니다.')

    # 3. 컬럼 선택
    st.subheader('컬럼 선택 및 시각화')
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        col = st.selectbox('시각화할 컬럼을 선택하세요', numeric_cols)
        if st.button('히스토그램 그리기'):
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)
        if st.button('상관관계 히트맵 보기'):
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
    else:
        st.write('수치형 컬럼이 없습니다.')
else:
    st.info('CSV 파일을 먼저 업로드하세요.')