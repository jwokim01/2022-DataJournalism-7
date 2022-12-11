import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import plotly.graph_objects as go

st.title("제21대 국회의원 발의 법률안 키워드 분석")
st.write("최종 편집일: 2022.12.15.")
st.write("데이터저널리즘 7조: 김정우, 신유진, 안범영, 유창민")

# 국회 이미지
url = 'https://www.assembly.go.kr/cmmn/file/imageSrc.do?fileStreCours=829f7616fd59d611d6ee0bd750a47a6a&streFileNm=c4898d8acfe52e943d8691202e8e2fd5db110d2cdf90c86ad45263107332adc5'
st.image(url)

st.info(
"""
21대 국회에서 의원들은 어떤 발의안을 내놓았을까요? 

정당, 연령, 트렌드를 중심으로 법률안 키워드를 분석해보았습니다.
""")
st.markdown(
"""
* 목차
	* Ⅰ. (서론 제목)
	* Ⅱ. 국회와 사회의 트랜드 비교
	* Ⅲ. 국회의원 소속 정당 및 연령별 분석
	* Ⅳ. 결론
""")

st.header("Ⅰ. (서론 제목)")



st.header("Ⅱ. 국회와 사회의 트랜드 비교")



st.header("Ⅲ. 국회의원 소속 정당 및 연령별 분석")
st.subheader("1) 제21대 국회의원 인적 구성")

# '이름','나이','성별','소속 정당','소속 위원회'
df = pd.read_csv('members.csv')
members = df.values.tolist()

democrtic = []
peoplepower = []
justice = []

for i in members:
	if (i[3] == "더불어민주당"):
		democrtic.append(i[1])
	elif (i[3] == "국민의힘"):
		peoplepower.append(i[1])
	elif (i[3] == "정의당"):
		justice.append(i[1])

fig = go.Figure()
fig.add_trace(go.Histogram(x=democrtic, name='더불어민주당', marker_color='#004EA1', xbins=dict(size=1)))
fig.add_trace(go.Histogram(x=peoplepower, name='국민의힘', marker_color='#E61E2B', xbins=dict(size=1)))
fig.add_trace(go.Histogram(x=justice, name='정의당', marker_color='#ffed00', xbins=dict(size=1)))

fig.update_layout(barmode='overlay', title_text='정당별 연령 분포', xaxis_title_text='나이',  yaxis_title_text='인원수')
fig.update_traces(opacity=0.75)

st.plotly_chart(fig, use_container_width=True)

demo_mean = round(np.mean(democrtic),1)
peo_mean = round(np.mean(peoplepower),1)
justice_mean = round(np.mean(justice),1)

st.write('더불어민주당 국회의원의 평균 연령 : {}세'.format(demo_mean))
st.write('국민의힘 국회의원의 평균 연령 : {}세'.format(peo_mean))
st.write('정의당 국회의원의 평균 연령 : {}세'.format(justice_mean))

st.subheader("2) 정당별 법률안 발의 키워드")

st.subheader("3) 위원회별 정당, 연령 기준 워드클라우드")
option = st.selectbox('결과를 확인하고 싶은 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

committee = {
    '국회운영위원회' : '분석 내용 : ', 
    '법제사법위원회' : '분석 내용 : ', 
    '정무위원회' : '분석 내용 : ', 
    '기획재정위원회' : '분석 내용 : 중앙값 아래는 경제에, 중앙값 위는 과세 문제에, 다만 정의당의 경우 중앙값 위에서 가사 및 서비스에 대해 관심', 
    '교육위원회' : '분석 내용 : ', 
    '과학기술정보방송통신위원회' : '분석 내용 : ', 
    '외교통일위원회' : '분석 내용 : ', 
    '국방위원회' : '분석 내용 : ', 
    '행정안전위원회' : '분석 내용 : ', 
    '문화체육관광위원회' : '분석 내용 : ', 
    '농림축산식품해양수산위원회' : '분석 내용 : ', 
    '산업통상자원중소벤처기업위원회' : '분석 내용 : 산업통상자원중소벤처기업위원회: 중앙값 아래는 에너지와 발전에, 중앙값 위는 중소기업에 대한 발의안 많음(다만 국민의힘의 경우 기술에 대한 발의안이 많음)', 
    '보건복지위원회' : '분석 내용 : ',
    '환경노동위원회' : '분석 내용 : ', 
    '국토교통위원회' : '분석 내용 : ', 
    '정보위원회' : '분석 내용 : 중앙값 아래는 직원에, 중앙값 위는 기관에 대한 발의안(다만 정보위원회의 경우 발의안 수가 20개로 다른 위원회에 비해 매우 적음. 정의당의 경우 아예 발의안이 없음)', 
    '여성가족위원회' : '분석 내용 : '}

img = Image.open('committee_wordcloud/{}.png'.format(option))
st.image(img)
st.write(committee[option])

st.header("Ⅳ. 결론")



st.markdown("***")
if st.button("참고문헌 및 외부자료 출처"):
	st.markdown(
	"""
    ##### 이미지
    * 국회 이미지자료실 : https://www.assembly.go.kr/cmmn/file/imageSrc.do?fileStreCours=829f7616fd59d611d6ee0bd750a47a6a&streFileNm=c4898d8acfe52e943d8691202e8e2fd5db110d2cdf90c86ad45263107332adc5
	""")
