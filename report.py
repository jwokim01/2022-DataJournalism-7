import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import plotly.graph_objects as go

st.title("제21대 국회의원 발의 법률안 키워드 분석")
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
	* Ⅰ. 기획 의도
	* Ⅱ. 법률안 분석과 사회 트렌드 비교
	* Ⅲ. 국회의원 소속 정당 및 연령별 분석
	* Ⅳ. 결론
""")

st.header("Ⅰ. 기획 의도")
st.write("**날이 갈수록 늘어가는 국회의원 발의 법률안, 도대체 무슨 내용이지?**")

chart_data = pd.DataFrame({'임기':['14대','15대','16대','17대','18대','19대','20대','21대 전반기'],
                          '의원발의':[321,1144,1912,6387,12220,16729,23047,14831],
                          '정부제출':[581,807,595,1102,1693,1093,1094,491]})

st.bar_chart(chart_data, x='임기')

st.markdown(
"""
투표는 주권자인 국민의 가장 중요한 권리 중 하나로, 우리를 대신하여 일할 국회의원을 선출하는 국회의원 선거는 늘 관심의 대상이 되어 왔다. 그렇지만 이들이 실제로 선출된 후에 무엇에 대해, 얼마나 활동하고 있는지 제대로 알고 있는 학생들은 많지 않을 것이다. 21대 국회 전반기 동안 국회의원에 의해 발의된 법률안은 16,781건에 달하는데, 하루에 약 21건 꼴로 발의된 법안을 우리가 매번 찾아보기는 어려운 일이다.

이번 프로젝트는 크게 두 부분으로 구성된다. 21대 국회 총 16,781건의 국회의원 발의안을 분석하여 첫째, ‘어떤 내용’과 '어떤 특성'의 법률안이 발의되었는지를 살펴본다. 이에 더해, 84,257건 의 뉴스 데이터를 분석한 결과를 토대로 이러한 법률안을 21대 회기 동안의 사회 트렌 드와 비교해본다. 둘째, ‘누가’ 이러한 법률안을 발의하였는지를 살펴본다. 이 부분에서는 발의자인 국회의원의 소속 정당과 연령을 기준으로 어떤 법률안이 발의되는지를 살펴본다.
"""
)


st.header("Ⅱ. 법률안 분석과 사회 트렌드 비교")
st.subheader("1) 법률안 트렌드")
st.markdown(
"""
제21대 국회의원들은 어떤 법률과 단어에 관심을 가졌을까? 이 부분에서는 상기된 질문에 대한 명쾌한 해답을 얻기 위해 워드클라우드와 네트워크 연결망 등을 활용하였다. 먼저 각 위원회별로 소관 법률안의 제목과 내용을 분석하였다. 그리고 국회의원들이 가장 많이 다루었던 법률 3개와 단어 5개를 많이 도출된 순으로 나열하였으며, 법률안의 내용에서 명사를 선별하여 워드클라우드를 그렸다. 그다음으로 제21대 국회의원 발의 법률안 전체 내용을 분석하여 단어 네트워크 연결망을 그렸다.
"""
)

option3 = st.selectbox('워드클라우드를 확인할 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

committee2 = {
    '국회운영위원회' : '분석 내용 : 국회운영위원회 소관 법률안과 관련하여, 국회의원들이 가장 많은 관심을 보인 법률에는 ‘국회법’, ‘인사청문회법’ , ‘국회에서의 증언·감정 등에 관한 법률’ 등이 있었다. 이중 국회의원들은 ‘국회법’에 압도적으로 큰 관심을 보여주었다. 이와 함께 국회의원들이 관련 법률안에 가장 많이 담았던 단어는 ‘국회’, ‘심사’, ‘국회의원’, ‘의결’, ‘제출’ 등이었던 것으로 드러났다.', 
    '법제사법위원회' : '분석 내용 : 법제사법위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 법률에는 ‘형사소송법’, ‘형법’, ‘아동학대범죄의 처벌 등에 관한 특례법’ 등이 있었다. 아울러 법률안 내용을 분석하였을 때, 국회의원들은 ‘범죄’, ‘보호’, ‘사건’, ‘피해자’, ‘수사’와 같은 단어들을 가장 많이 담은 것으로 드러났다.', 
    '정무위원회' : '분석 내용 : 정무위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 법률은 ‘독점규제 및 공정거래에 관한 법률’, ‘자본시장과 금융투자업에 관한 법률’, ‘하도급거래 공정화에 관한 법률’ 등이었다. 더불어 국회의원들이 관련 법률안에 가장 많이 사용하였던 단어들에는 ‘금융’, ‘거래’, ‘사업자’, ‘행위’, ‘국가’ 등이 있었다.', 
    '기획재정위원회' : '분석 내용 : 기획재정위원회 소관 법률안과 관련하여, 국회의원들이 가장 많은 관심을 보였던 법률에는 ‘조세특례제한법’, ‘국가재정법’, ‘소득세법’ 등이 있었다. 이중에서도 국회의원들은 ‘조세특례제한법’에 대단히 큰 관심을 보여주었다. 관련 법률안들에서, 국회의원들은 ‘과세’, ‘공제’, ‘지원’, ‘사업’, ‘경제’ 등의 단어들을 가장 많이 사용하였다.', 
    '교육위원회' : '분석 내용 : 교육위원회 소관 법률안과 관련하여, 국회의원들이 가장 많은 관심을 보였던 법률은 ‘초·중등교육법’, ‘사립학교법’, ‘고등교육법’ 등이었다. 국회의원들이 관련 법률안들에서 가장 많이 사용했던 단어들은 ‘교육’, ‘학교’, ‘학생’, ‘대학’, ‘운영’ 등이었다.', 
    '과학기술정보방송통신위원회' : '분석 내용 : 과학기술정보방송통신위원회 소관 법률안과 관련하여, 국회의원들이 가장 많은 관심을 보였던 법률은 ‘전기통신사업법’, ‘정보통신망 이용촉진 및 정보보호 등에 관한 법률’, ‘방송법’ 등이었다. 관련 법률안에서, 국회의원들이 가장 많이 사용하였던 단어에는 ‘정보’, ‘통신’, ‘방송’, ‘사업자’, ‘서비스’ 등이 있었다.', 
    '외교통일위원회' : '분석 내용 : 외교통일위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 법률에는 ‘북한이탈주민의 보호 및 정착지원에 관한 법률’, ‘남북교류협력에 관한 법률’, ‘남북협력기금법’ 등이 있었다. 국회의원들이 관련 법률안에 가장 많이 담았던 단어들은 ‘협력’, ‘남북’, ‘북한’, ‘지원’, ‘보호’와 같은 단어들이었다.', 
    '국방위원회' : '분석 내용 : 국방위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 법률에는 ‘병역법’, ‘군인사법’, ‘군인의 지위 및 복무에 관한 기본법’ 등이 있었다. 관련 법률안에 국회의원들이 가장 많이 담아내었던 단어들은 ‘군인’, ‘군’, ‘복무’, ‘국가’, ‘사업’ 등이었다.', 
    '행정안전위원회' : '분석 내용 : 행정안전위원회 소관 법률안과 관련하여, 국회의원들은 ‘공직선거법’, ‘지방세특례제한법’, ‘도로교통법’ 등에 가장 많은 관심을 가졌다. 나아가 국회의원들은 ‘지방’, ‘선거’, ‘자치’, ‘단체’, ‘지역’ 등의 단어들을 관련 법률안에 가장 많이 사용하였다.', 
    '문화체육관광위원회' : '분석 내용 : 문화체육관광위원회 소관 법률안과 관련하여, 국회의원들은 ‘국민체육진흥법’, ‘문화재보호법’, ‘저작권법’ 등에 가장 큰 관심을 가졌다. 아울러 ‘문화’, ‘체육’, ‘문화재’, ‘산업’, ‘진흥’ 등은 국회의원들이 관련 법률안에 가장 많이 담아내었던 단어들이었다.', 
    '농림축산식품해양수산위원회' : '분석 내용 : 농림축산식품해양수산위원회 관련 법률과 관련하여, 국회의원들이 가장 많은 관심을 가졌던 법률에는 ‘동물보호법’, ‘농지법’, ‘농업협동조합법’ 등이 있었다. 또한 ‘동물’, ‘사업’, ‘관리’, ‘농업’, ‘지원’ 등의 단어들을 국회의원들은 관련 법률안에 가장 많이 사용하였다.', 
    '산업통상자원중소벤처기업위원회' : '분석 내용 : 산업통상자원중소벤처기업위원회 소관 법률과 관련하여, ‘전기사업법’, ‘소상공인 보호 및 지원에 관한 법률’, ‘국가균형발전 특별법’에 국회의원들이 가장 큰 관심을 가진 것으로 드러났다. 아울러 관련 법률안에는 ‘산업’, ‘지원’, ‘사업’, ‘기업’, ‘지역’ 등의 단어가 가장 많이 사용된 것으로 드러났다.', 
    '보건복지위원회' : '분석 내용 : 보건복지위원회 소관 법률안과 관련하여, 국회의원들이 가장 중요하게 생각했던 법안에는 ‘감염병의 예방 및 관리에 관한 법률’, ‘아동복지법’, ‘의료법’ 등이 있었다. 아울러 ‘의료’, ‘지원’, ‘아동’, ‘기관’, ‘장애인’ 등의 단어들이 관련 법률안에서 가장 많이 사용된 것으로 드러났다. ',
    '환경노동위원회' : '분석 내용 : 환경노동위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 것들에는 ‘근로기준법’, ‘남녀고용평등과 일·가정 양립 지원에 관한 법률’, ‘산업안전보건법’ 등이 있었다. 또한 국회의원들이 관련 법률안에 가장 많이 사용했던 단어는 ‘근로자’, ‘고용’, ‘근로’, ‘관리’, ‘지원’ 등이었다.', 
    '국토교통위원회' : '분석 내용 : 국토교통위원회 소관 법률안과 관련하여, 국회의원들이 가장 많이 관심을 가졌던 법률은 ‘자동차관리법’, ‘공동주택관리법’, ‘주택법’ 등이었다. 국회의원들은 ‘사업’, ‘주택’, ‘관리’, ‘지역’, ‘자동차’와 같은 단어들을 관련 법률안에 가장 많이 사용하였다.', 
    '정보위원회' : '분석 내용 : 정보위원회 소관 법률안은 국가정보원과 밀접하게 연관된다. 국회의원들이 가장 많은 관심을 가졌던 법률은 ‘국가정보원직원법’, ‘국가정보원법’, ‘국민보호와 공공안전을 위한 테러방지법’ 등이었으며, 법률안에 가장 많이 사용하였던 단어는 ‘국가’, ‘정보’, ‘정보원’, ‘안보’, ‘사이버’ 등이었다.', 
    '여성가족위원회' : '분석 내용 : 여성가족위원회 소관 법률안과 관련하여, 국회의원들은 ‘아동·청소년의 성보호에 관한 법률’, ‘청소년복지 지원법’, ‘성폭력방지 및  피해자보호 등에 관한 법률’ 등에 가장 큰 관심을 보였다. 더불어 관련 법률안에는 ‘청소년’, ‘지원’, ‘아동’, ‘가족’, ‘피해자’와 같은 단어들이 가장 많이 사용되었다.'}

img = Image.open('committee_wordcloud2/{}.png'.format(option3))
st.image(img, width=400)
st.info(committee2[option3])

img = Image.open("image/법률단어_네트워크.png")
st.image(img, caption='국회의원 발의 법률안 전체 단어 네트워크 그래프')

st.markdown(
"""
이 그래프는 법률안 전체의 내용 속에 들어있는 단어들을 기반으로 그려진 단어 네트워크 연결망이다. 서로 다른 색은 서로 다른 집단을 의미하며, 여기에는 총 4개의 집단이 존재하고 있다. 또한 단어 노드의 크기 비교를 통해 각 단어들이 가지는 비중을 알 수 있으며, 단어들 간의 연결 링크(link)의 두께를 통해 단어들이 서로 얼마나 관계가 있는지 확인해볼 수도 있다. 
이 연결망에서 특기할 만한 점은 다음과 같다. 먼저 옥색 집단을 살펴보았을 때, ‘개정’, ‘수정’, ‘조정’과 같은 단어들이 긴밀히 연결되어 있는 모습을 볼 수 있다. 이를 통해 국회의원 발의 법률안에는 이미 존재하고 있는 법률들을 개정, 수정하고자 하는 성격이 강하게 존재하고 있다는 사실을 알 수 있다. 나아가 녹색 집단과 붉은 색 집단을 살펴보면, 녹색 집단은 ‘국가’, ‘자치’, ‘지방’, ‘단체’ 등의 단어들이 서로 긴밀히 연관되어 있으며, 또 빨간색 집단의 단어인 ‘지원’은 녹색 집단과 연결되어 있다. 이를 통해 미루어 보았을 때 지방자치단체를 국가가 지원하는 것이 제21대 국회의원들의 주요 화두 중 하나이며, 현재 지속되고 있는 지방 소멸 문제 등을 국회의원들이 유심히 주시하고 있다는 사실을 알 수 있다.

이상의 데이터와 그에 따른 설명을 통해 국회의원들이 각 위원회별로 다양한 법률에 관심을 가지고 또 다양한 단어들을 법률안에 사용한다는 사실을 알 수 있다. 국회의원들은 우리 사회 내 다양한 이슈에 관심을 가지고 그에 따른 법률안을 발의하고 있다. 나아가 법률안 전체 내용을 분석한 단어 네트워크 연결망을 살펴보았을 때, 국회의원들이 발의한 법률안에는 이미 존재하는 법률안들을 개정하고자 하는 성격이 강하게 존재하고 있으며, 또 지방자치단체를 지원하는 문제에 국회의원들이 큰 관심을 가지고 있다는 사실을 확인해볼 수 있다.
"""
)

st.subheader("2) 보수/진보 언론 매체 트렌드")

st.markdown(
"""
##### 2-1) 위원회별 보수/진보 언론 매체 키워드 분석

각 위원회의 아젠다에 대해서 언론에서는 어떤 이야기를 했을까? 이 분석에서는 앞서 도출된 위원회별 핵심 키워드를 중심으로 조선일보와 중앙일보, 그리고 한겨레와 경향신문에서 총 84, 257건의 뉴스(기간: 2020.07~2022.06)를 크롤링하여 가중치순 상위 50개 키워드를 분석하였다.
"""
)

option2 = st.selectbox('언론별 결과를 확인할 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

press = {
    '국회운영위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('민주당', 5846), ('윤석열', 4876), ('국민', 4571), ('더불어민주당', 4423), ('이재명', 4382), 진보 언론에서 상위 키워드는 5개는 ('민주당', 682), ('더불어민주당', 604), ('국민', 499), ('법', 469), ('서울', 429)이었다. 정당 ‘국민의 힘’이 키워드 ‘국민’으로 분류되었다는 점을 고려했을 때, 국회운영과 관련해서는 전반적으로 양 매체 모두 정당에 초점을 맞추어 논의를 전개하고 있음을 확인할 수 있다. 반면, 보수 언론이 상대적으로 진보 언론에 비해 ‘윤석열’, ‘이재명’, ‘문재인’ 등 특정 인물에 대한 언급 빈도가 높다.", 
    '법제사법위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('민주당', 682), ('더불어민주당', 604), ('국민', 499), ('법', 469), ('서울', 429), 진보 언론에서 상위 키워드 5개는 ('서울', 798), ('피해자', 502), ('수사', 475), ('법', 360), ('지검', 276)이었다. ‘서울’이라는 키워드의 언급 빈도가 양 매체 모두 가장 많이 나타났는데, 이는 전반적인 논의가 서울 지역에 치중되어 있음을 보여준다. 또한, 사법 영역에서는 양 매체가 모두 ‘수사’, 법무부‘, ’지검‘, ’경찰청‘ 등 유사한 주제에 대해 보도하였음을 알 수 있다.", 
    '정무위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 176), ('한국', 176), ('투자', 139), ('미국', 129), ('관계자', 127), 진보 언론에서 상위 키워드 5개는 ('코로나', 145), ('19', 110), ('한국', 99), ('소비자', 91), ('서울', 90)이었다.", 
    '기획재정위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 360), ('서울', 326), ('부동산', 292), ('지원금', 253), ('이재명', 198), 진보 언론에서 상위 키워드 5개는 ('코로나', 378), ('19', 301), ('지원금', 251), ('서울', 240), ('기본소득', 225)이었다. 전반적으로 진보 매체에서 보수 매체에 비해 기본소득에 많은 관심을 보였음을 알 수 있다.", 
    '교육위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 828), ('서울', 648), ('온라인', 500), ('교육부', 499), ('19', 476), 진보 언론에서 상위 키워드 5개는 ('교육청', 740), ('코로나', 700), ('19', 595), ('서울', 480), ('교육부', 429)이었다. 교육위원회에 관해서도 타 위원회에 비해 양 매체 모두 코로나 언급 수준이 유의미하게 높았으며, 온라인 수업의 증대에서 알 수 있듯 ‘온라인’ 키워드가 자주 언급된다다. 두 매체 간 차이에 있어 보수 매체가 진보 매체에 비해 ‘교육청’을 다루는 경우가 훨씬 많은 것으로 확인된다.", 
    '과학기술정보방송통신위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('서울', 370), ('수사', 247), ('코로나', 240), ('처', 237), ('관계자', 221), 진보 언론에서 상위 키워드 5개는 ('서울', 211), ('수사', 149), ('코로나', 139), ('개인정보', 131), ('한국', 123)이었다. 해당 위원회에 대해서는 두 매체 간의 차이가 두드러지지 않는다.", 
    '외교통일위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('미국', 323), ('한국', 315), ('중국', 231), ('외교부', 144), ('일본', 134), 진보 언론에서 상위 키워드 5개는 ('미국', 233), ('한국', 184), ('중국', 144), ('코로나', 84), ('일본', 83)이었다. 전반으로 외교통일위원회 관련 주제에서 언론은 남북관계나 통일보다는 외교관계에 집중하였는데, 그럼에도 보수 언론은 상위 30개 키워드 중 통일 관련 키워드가 ‘통일부’ 하나에 그친 반면, 진보 언론은 ‘통일부’, ‘남북’, ‘평화’ 등 비교적 다양하게 통일 관련 주제를 다루었다.", 
    '국방위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('국방부', 169), ('코로나', 149), ('관계자', 115), ('서울', 110), ('미국', 91), 진보 언론에서 상위 키워드 5개는 ('국방부', 312), ('코로나', 163), ('19', 142), ('서울', 102), ('관계자', 97)이었다. 특히, 진보 언론에서 국방부에 대해 피해자, 성추행, 가해자 등의 키워드를 자주 사용하였으며, 이는 진보 언론이 보수 언론에 비해 군 내 인권 문제에 대한 관심이 높았음을 시사한다.", 
    '행정안전위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('서울', 716), ('민주당', 589), ('더불어민주당', 383), ('국민', 311), ('위원장', 305), 진보 언론에서 상위 키워드 5개는 ('서울', 502), ('민주당', 496), ('더불어민주당', 317), ('국민', 237), ('위원장', 231)이었다. 두 매체 간의 차이가 적게 나타나며, 두 매체 모두 서울을 제외하면 부산 지역에 대한 언급 빈도가 높다.", 
    '문화체육관광위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 429), ('한국', 341), ('19', 232), ('서울', 229), ('장', 177), 진보 언론에서 상위 키워드 5개는 ('코로나', 241), ('19', 197), ('한국', 165), ('서울', 154), ('시설', 143)이었다. 두 매체 간의 차이가 적게 나타나며, 두 매체 모두 관광, 관광지, 관광객 등 관광 산업에 대한 관심도가 높았음음을 확인할 수 있다.", 
    '농림축산식품해양수산위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 108), ('서울', 105), ('관계자', 93), ('반려', 88), ('마리', 87), 진보 언론에서 상위 키워드 5개는 ('반려', 141), ('서울', 138), ('코로나', 108), ('마리', 100), ('한국', 91). 흥미롭게도, 해당 위원회와 관련하여 두 매체 모두 ‘반려동물’에 대한 사회의 관심도를 반영하고 있다. 이외에도 ‘동물학대’, ‘동물권’ 등을 단어를 확인할 수 있다.", 
    '산업통상자원중소벤처기업위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 1140), ('한국', 1044), ('미국', 768), ('서울', 655), ('19', 621), 진보 언론에서 상위 키워드 5개는 ('코로나', 569), ('한국', 466), ('19', 457), ('서울', 413), ('미국', 346)이었다. 해당 데이터에서 주요하게 다루어지는 산업 분야는 반도체, 자동차, 금융이다.", 
    '보건복지위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 221), ('19', 119), ('사회', 88), ('의료', 81), ('서울', 78), 진보 언론에서 상위 키워드 5개는 ('코로나', 194), ('19', 162), ('서울', 115), ('센터', 98), ('사회', 95)이었다. 두 매체 간의 차이가 적게 나타났으며, 전반적으로 의료와 안전에 대한 키워드가 두드러진다",
    '환경노동위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 426), ('노동자', 298), ('19', 231), ('일자리', 221), ('한국', 204), 진보 언론에서 상위 키워드 5개는 ('노동자', 2307), ('코로나', 633), ('19', 522), ('서울', 464), ('노동부', 421)이었다. 두 매체 모두 환경보다는 노동 분야에 대한 보도가 두드러지며, 특히 ‘노동자’ 키워드가 자주 언급된다.", 
    '국토교통위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('서울', 631), ('부동산', 605), ('주택자', 348), ('다', 247), ('임대', 164), 진보 언론에서 상위 키워드 5개는 ('서울', 434), ('부동산', 361), ('임대', 250), ('공공', 239), ('사업', 177)이었다. 공통적으로 교통 관련 사업보다는 ‘서울’과 ‘부동산’, ‘임대’, ‘공공’ 등 문재인 정부의 부동산 정책과 관련된 키워드가 많이 나타난다.", 
    '정보위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('코로나', 438), ('한국', 368), ('서울', 346), ('미국', 306), ('19', 220), 진보 언론에서 상위 키워드 5개는 ('서울', 301), ('코로나', 292), ('한국', 272), ('19', 220), ('미국', 179)이었다. 크게 두 매체 간의 두드러지지는 않았으나 보수 언론에서는 부동산이 상위 언급 11위 키워드, 진보 언론에서는 30위권밖이었다는 점에서 부동산에 대한 보수 언론의 전반적으로 높은 관심도가 해당 위원회 관련 뉴스 데이터에서 확인된다.", 
    '여성가족위원회' : "분석 내용 : 보수 언론에서 상위 키워드 5개는 ('서울', 974), ('코로나', 927), ('피해자', 622), ('미국', 596), ('경찰', 527), 진보 언론에서 상위 키워드 5개는 ('서울', 639), ('코로나', 637), ('19', 536), ('한국', 418), ('피해자', 312)이었다. 보수 매체에서 ‘경찰’ 키워드의 언급 빈도가 유의미하게 높게 나왔으며, 전반적으로 폭력 범죄와 피해자, 코로나에 대해 많이 다루고 있다"}

img = Image.open('press_wordcloud/{}_c.png'.format(option2))
st.image(img, caption='보수 언론 키워드', width=400)
img = Image.open('press_wordcloud/{}_p.png'.format(option2))
st.image(img, caption='진보 언론 키워드', width=400)
st.info(press[option2])

st.markdown(
"""
전반적으로, 어느 분야건 간에 코로나가 핵심 키워드로 등장하였고, 지역적으로는 서울 지역에 논의가 편중된 경향을 보이고 있다.
"""
)

st.markdown(
"""
##### 2-2) 전반적인 보수/진보 언론 매체 트렌드 분석

* 보수 매체에서 2년간 가장 많이 제시된 키워드 TOP5 (빈도수)
    * 기업(3899), 여성(3464), 가족(2917), 이재명(2709), 사업(2401)
* 진보 매체에서 2년간 가장 많이 제시된 키워드 TOP5 
    * 여성(2480), 기업(1821), 노동자(1730), 정보(1630), 선거(1558)

위와 같이 도출된 보수 언론과 진보 언론 각각의 TOP5 키워드를 중심으로, 각 언론들의 연관 단어 산점도 네트워크를 그렸다. 분석에는 워드투벡(word2vec) 모델이 사용됐으며, 가까이 있을수록 연관성이 높다는 의미이다. 각 매체의 자세한 키워드 네트워크는 맨 아래 첨부해놓았다.
""")

img = Image.open('image/보수_산점도.png')
st.image(img, caption='보수 매체 키워드의 네트워크 산점도')
img = Image.open('image/진보_산점도.png')
st.image(img, caption='진보 매체 키워드의 네트워크 산점도')
st.markdown(
"""
**‘여성’** 키워드에 대해 진보 매체는 보수 매체에 비해 ‘페미니스트’, ‘유리천장’ 등 사회적 장벽 관련 용어와의 상관관계가 높다면, 보수 매체는 ‘구타’, ‘주먹질’, ‘남성’ 등 폭력 범죄 관련 용어와의 상관관계가 높다.

**‘기업’** 키워드에 대해 보수 매체는 ‘금융’, ‘투자’ 등 해당 업계 내 용어와의 상관관계가 높은 반면, 진보 매체는 ‘소비자보호’, ‘신재생에너지’, ‘곡물’ 등 상대적으로 다양한 영역의 키워드와 연결되어 있다. 

위원회별 뉴스 분석 결과를 살펴봤을 때, 해당 위원회별 뉴스 데이터는 위원회 상위 빈도수 키워드를 중심으로 수집하였음에도, 법률발의안과 달리 ‘민주당’, ‘이재명’ 등 주요 인물이나 정당에 대한 키워드, ‘서울’, ‘수도권’과 같이 특정 지역 중심의 키워드가 높은 빈도로 도출되었으며, ‘코로나’, ‘확진’, ‘부동산’, ‘온라인’ 등 보다 시의성 있는 키워드들이 이용되었다. 예컨대, 교육위원회 법률발의안은 ‘교육’, ‘대학’, ‘교원’이 주요 키워드였다면, 언론 매체에서는 공통적으로 ‘코로나’, ‘온라인’, ‘방역’ 등의 언급 빈도가 유의미하게 높았다. 코로나 19 대응을 위한 ‘디지털 기반의 원격교육 활성화 기본법’ 등의 법률에도 불구하고 관련 키워드인 ‘보건’, ‘안전’, ‘코로나’의 비율이 전체 교육위원회 발의법률안 가운데 높지 않았음을 알 수 있다. 이외에도 여성가족위원회의 법률발의안은 ‘청소년’, ‘아동’에 대한 발의법률안 비율이 매우 높았던 반면, 언론에서는 상대적으로 아동이나 청소년보다는 ‘범죄’, ‘경찰’, ‘피해자’ 등 전반적인 범죄 행태에 대한 주목도가 높았다. 법제사법위원회 역시 상대적으로 ‘아동’에 관한 제안 내용을 언론에서 주목된 정도보다 높은 수준으로 법률안에 반영하였다. 

그러나 동시에, 여러 핵심적인 언론 의제가 적절히 법률안에 반영된 위원회 역시 확인되었다. 대표적으로 국토교통위원회는 주택법, 공동주택관리법, 그리고 ‘건설’, ‘도시’, ‘관리’ 등에 대한 키워드가 많이 활용되었는데, 관련 뉴스 데이터를 살펴보면, 유사하게 ‘주택’, ‘공공’, ‘가수, 부동산’ 등 전반적인 주거 관련 키워드가 다수 이용되었다. 또한, 환경노동위원회는 상대적으로 환경에 비해 ‘고용’, ‘근로자’, ‘근로’ 등 노동에 관련된 법률안이 적극적으로 발의되었는데, 이는 언론에서 ‘노동자’, ‘사업장’, ‘노동부’, ‘일자리’에 주로 주목한 것과 유사한 양상이었다. 결과적으로, 이렇게 법률안 아젠다와 언론 아젠다가 유사한 것은 법률안이 국민의 관심사 및 주요한 의제를 적절히 반영하고 있다는 해석이 가능하다. 그러나, 그 중요성에도 불구하고 국회와 언론 모두에서 적게 다루어지는 ‘환경’ 관련 의제처럼 국민적 관심도가 낮을 경우 그 필요성에도 입법이 제대로 행해지는 않는 문제점을 생각해볼 수 있다. 
"""
)

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

st.markdown(
"""
그 다음으로 국회의원 법률안을 소속 정당과 연령별로 비교분석을 진행할 것이다. 그에 앞서, 현재 국회의원의 인적 구성을 간단하게 살펴보자.

작성일 기준(2022.12.15.) 국회의원은 총 299명이며, 그중 더불어민주당이 169석, 국민의힘이 115석, 정의당이 6석, 기본소득당과 시대전환이 각각 1석, 무소속이 7석을 차지하고 있다. 남성은 242명(80.9%), 여성은 57명(19.1%)로 남성의 비율이 압도적으로 높게 나타났다. 연령별로는 30대 9명(3.0%), 40대 25명(8.7%), 50대 139명(46.5%), 60대 118명(39.5%), 70대 이상 8명(2.7%)으로 현재 국회가 50, 60대를 중심으로 구성되어 있음을 보여준다.

위의 히스토그램은 정당별 연령 분포를 보여준다. 거대 양당인 더불어민주당이 국민의힘은 종형 분포를 보여주며, 더불어민주당의 최빈값, 평균값이 국민의힘보다 낮게 형성되어 있다. 더불어민주당 국회의원의 평균 연령은 {}세이고, 국민의힘은 {}세, 정의당은 {}세이다.
""".format(demo_mean, peo_mean, justice_mean)
)

st.subheader("2) 정당별 법률안 발의 키워드")
st.markdown(
"""
국회의 작동에 핵심적인 역할을 하는 더불어민주당, 국민의힘, 정의당을 중심으로 국회의원들의 발의 키워드를 살펴보자. 법안 심의를 위해 국회의 17개 상임위원회에 올라온 안건에서 명사 키워드를 추출해 정당별 워드클라우드로 만들었다. 워드클라우드는 정당 간의 차이를 조명하기 위해 국회 입법과정에서 사용되는 용어(ex. 현행법, 규정, 경우), 소관 위원회의 성격에 따라 공통적으로 많이 등장한 단어(ex. 국회, 정보, 주택)는 제외한 뒤에 제작되었다. 해당 '제외 용어(stopwords)'는 글 마지막에 첨부했다.

분석 결과 더불어민주당에서는 ‘사회’, ‘국민’, 국민의힘에서는 ‘자치’, ‘시설’, 정의당에서는 ‘장애인’, ‘사회’와 같은 키워드가 주로 등장하였다. 이를 통해, 더불어민주당과 국민의힘이 거대 양당으로서 국가 전체의 제도나 국민 전반에 영향을 끼치는 기반 시설과 관련한 법안을 많이 발의하였다면, 정의당은 사회 내부의 소수자를 조망하고 이들의 인권이나 안전 등을 보장하고자 하는 법안을 많이 발의하였다고 볼 수 있다.
"""
)
img = Image.open('image/3당.png')
st.image(img, caption='더불어민주당/국민의힘/정의당 국회 전체 키워드')

st.markdown(
"""
자카드 유사도 분석을 통해 정당 워드클라우드 간의 유사성을 분석해보자. 자카드 유사도란 두 집합 사이의 유사도를 측정하는 방법들 중 하나로서, 0부터 1까지의 수로 표현할 수 있다. 자카드 유사도가 높을 수록 두 집합 사이의 공통된 원소(교집합의 원소)가 많다는 것을 의미한다. 예를 들어,  두 집합의 원소가 완전히 동일하다면 1의 값을 갖고 교집합의 원소가 없다면 0의 값을 갖는다. 집합의 원소 크기를 통하여 이를 공식화하면 아래와 같다.

$J(A,B) = n(A \cap B)/n(A \cup B)$

이러한 유사도를 적용하여 세 정당 간의 유사설을 판단하기 위해, 두 정당씩 짝을 지어 유사도를 측정하였다. 분석결과는 다음과 같이 나타났다.

* 더불어민주당-국민의힘 유사도: 0.754
* 더불어민주당-정의당 유사도: 0.709
* 국민의힘-정의당 유사도: 0.653

분석 결과, 앞서 ‘제21대 국회의원 인적 구성’을 통해 살펴보았듯이 거대 양당인 더불어민주당과 국민의힘 사이의 유사도가 가장 높게 나타났고, 더불어민주당-정의당, 국민의힘-정의당 순으로 유사도가 나타났다. 이는 ‘정당별 법률안 발의 키워드’에서 살펴본 바와 같이 거대 양당으로서 국가 전체의 제도나 국민 전반에 영향을 끼치는 기반 시설과 관련한 법안을 많이 발의하였다는 점을 수치로서 나타낸다. 특히 정의당의 경우 국민의힘보다는 더불어민주당과 유사도가 높게 나타났다는 점 또한 부가적으로 확인할 수 있다.

"""
)

st.subheader("3) 위원회별 정당, 연령 기준 워드클라우드")
option2 = st.selectbox('정당/연령별 워드클라우드를 확인할 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

committee = {
    '국회운영위원회' : "분석 내용 : 국회운영위원회에서는 더불어민주당과 정의당이 ‘보호’, ‘청원', ‘군인' 등의 키워드를 공유하며 비슷한 양상을 보이나, 국민의힘의 경우 ‘국회의원', ‘위원'과 같은 키워드를 주로 가지고 있음을 알 수 있다.", 
    '법제사법위원회' : "분석 내용 : 법제사법위원회에서는 정의당에서도 ‘피해자’라는 키워드가 많이 등장하였다. 결과적으로, 모든 구간에서 ‘아동' 혹은 ‘피해자'라는 키워드가 많이 등장하였음을 확인할 수 있다.", 
    '정무위원회' : "분석 내용 : 정무위원회에서는 ‘거래'나 ‘국가'와 같은 키워드를 워드클라우드에서 찾아볼 수 있다.", 
    '기획재정위원회' : "분석 내용 : 중간값 미만은 ‘경제’ 및 ‘사회'에, 중앙값 위는 ‘과세’에 주요한 관심을 보이고 있다. 다만 정의당의 경우 중간값 이상의 구간에서 가사 및 서비스에 대해 관심을 가지고 있음을 확인할 수 있다. 비교적 젊은층에서 경제 문제를 주요한 안건으로 인식하는 것에 대한 이유는 이들이 경제활동을 하여 소득을 얻는 생애구간에 있다는 것으로부터 찾을 수 있어 보인다. 반면 중간값 이상에서 과세 문제를 주요한 안건으로 인식하는 것에 대한 이유는 기존에 얻은 소득을 바탕으로 형성한 자본에 부과되는 세금에 관심을 가지고 있다는 것을 드러내는 듯해 보인다.", 
    '교육위원회' : "분석 내용 : 모든 구간에서 ‘대학'이라는 키워드가 많이 등장하였다. 다만 국민의힘의 중간값 미만에서 ‘특수교육'과 ‘장애인'에 대한 키워드가 많이 나온 데 비해, 중간값 이상에서는 ‘의료'와 ‘법'에 대한 키워드가 많이 나온 점을 발견할 수 있다.", 
    '과학기술정보방송통신위원회' : "분석 내용 : 더불어민주당과 국민의힘 사이에서는 정당 혹은 연령이라는 지표에 따라 큰 차이가 나타나지 않았지만, 정의당의 경우 ‘우주', ‘통신망'이라는 키워드가 타 정당들에 비해 두드러졌다.", 
    '외교통일위원회' : "분석 내용 : 외교통일위원회는 정당과 연령 두 기준에서 차이를 보였다. 먼저 정당별로 보면 더불어민주당은 ‘남북’과 ‘협력’, ‘보호’라는 키워드에 초점을 맞추고 있었으나, 국민의힘은 ‘남북’보다는 ‘북한'이라는 키워드가 더욱 많이 등장하고 ‘인권' 및 ‘재단'과 같은 키워드를 포함하고 있는 발의안이 많았다. 반면 정의당에서는 ‘중남미'와 ‘아랍'과 같이 남북관계 외의 다른 지역과의 관계를 고려하는 키워드를 발견할 수 있었다. 연령별로 보면 중간값 미만에서는 ‘협력'과 ‘인권', ‘교류'와 같은 키워드가 주로 등장한 반면, 중간값 이상에서는 ‘보호'와 ‘동포', ‘과학기술'과 같은 키워드가 주로 등장하였음을 확인할 수 있다. 이를 통해 두 집단에서 외교 방식을 바라보는 시선에 다소간 차이가 있음을 확인할 수 있다.", 
    '국방위원회' : "분석 내용 : 국방위원회의 경우, 중간값 이상에서는 ‘방위’나 ‘국가'와 같은 키워드가 많이 등장하였고, 중간값 이하에서는 ‘지급'과 같은 키워드가 많이 등장하였다.", 
    '행정안전위원회' : "분석 내용 : 행정안전위원회는 정당이나 연령을 기준으로 보았을 때 대부분의 영역에서 ‘자치', ‘단체', ‘국가'와 같은 키워드를 강조하며 차이가 두드러지지 않았다.", 
    '문화체육관광위원회' : "분석 내용 : 문화체육관광위원회같은 경우 연령에 따른 차이가 나타날 것이라 예상하였는데, 실제로는 두 범주에서 모두 ‘문화재’나 ‘진흥’ 등의 키워드를 많이 쓰며 이러한 차이가 나타나지 않았다. 다만 정의당의 경우 중간값 미만의 구간에서 ‘게임’과 같은 키워드가 들어간 발의안이 많다는 것을 볼 수 있다.", 
    '농림축산식품해양수산위원회' : "분석 내용 : 농림축산식품해양수산위원회에서는 ‘농업', ‘해양', ‘지원' 등의 키워드가 공통적으로 많이 등장하였다. 세 정당 모두 중간값 미만의 구간에서는 ‘농업' 키워드를 많이 발견할 수 있었으나, 중간값 이상에서는 그 양상이 조금 달라져 ‘어업', ‘해양' 등의 키워드가 많이 나타났다. 정의당의 경우 연령대에 따라 ‘안전', ‘시장’이나 ‘도매'와 같은 키워드 또한 발견할 수 있었다.", 
    '산업통상자원중소벤처기업위원회' : "분석 내용 : 산업통상자원중소벤처기업위원회의 경우, 중간값 미만에서는 ‘에너지’와 ‘발전’에, 중간값 이상에서는 ‘중소기업’에 대한 발의안이 많음을 확인할 수 있다. (다만 국민의힘의 경우 ‘기술’에 대한 발의안이 많음을 볼 수 있다.)", 
    '보건복지위원회' : "분석 내용 : 정의당의 중간값 이상을 제외한 5가지 부분 모두에서 ‘의료'라는 키워드가 주요하게 나타났다. 반대로, 정의당의 해당 영역에서는 ‘체납'이라는 용어가 유의미하게 많이 등장하였음을 발견할 수 있다.",
    '환경노동위원회' : "분석 내용 : 중간값 미만에서는 ‘지원’과 ‘사업’, ‘노동'에 대한 키워드가 두드러지게 나타났다면, 중간값 이상에서는 ‘관리', ‘시설' 등의 키워드가 많이 나타났다.", 
    '국토교통위원회' : "분석 내용 : 국토교통위원회에서는 중간값 미만에서 ‘공공', ‘지원'이라는 키워드가 많이 등장하였다. 더불어민주당의 중간값 이상 부분에서 많이 등장한 키워드인 ‘자동차', ‘도시', ‘계획'과 같은 키워드가 국민의힘의 중간값 미만 부분에서도 비슷하게 나타났다는 점에서, 연령과 정당을 가로질러 공통된 키워드를 찾을 수 있었다.", 
    '정보위원회' : "분석 내용 : 중앙값 미만에서는 ‘직원’에, 중앙값 이상에서는 ‘사이버', ‘기관’에 대한 발의안이 많았다. 정의당의 경우 정보위원회의 발의안에 참여한 의원이 없어 워드클라우드가 그려지지 않았다.", 
    '여성가족위원회' : "분석 내용 : 모든 구간에서 ‘아동’ 혹은 ‘가족'이라는 키워드가 주요하게 등장함을 확인할 수 있다. 더불어민주당과 국민의힘에선 ‘피해자’라는 키워드가 많이 나타났다면, 정의당에서는 '외국인', '(다)문화', '(다)자녀'라는 키워드가 많이 나타났음을 볼 수 있다."}

img = Image.open('committee_wordcloud/{}.png'.format(option2))
st.image(img)
st.info(committee[option2])
st.markdown(
"""
전체 분석 결과, 정당과 연령별로 차이를 확인할 수 있었던 위원회는 크게 외교통일위원회와 기획재정위원회였다.

**외교통일위원회**의 경우, 먼저 정당별로 보면 더불어민주당은 ‘남북’과 ‘협력’, ‘보호’라는 키워드에 초점을 맞추고 있었으나, 국민의힘은 ‘남북’보다는 ‘북한'이라는 키워드가 더욱 많이 등장하고 ‘인권' 및 ‘재단'과 같은 키워드를 포함하고 있는 발의안이 많았다. 반면 정의당에서는 ‘중남미'와 ‘아랍'과 같이 남북관계 외의 다른 지역과의 관계를 고려하는 키워드를 발견할 수 있었다. 연령별로 보면 중간값 미만에서는 ‘협력'과 ‘인권', ‘교류'와 같은 키워드가 주로 등장한 반면, 중간값 이상에서는 ‘보호'와 ‘동포', ‘과학기술'과 같은 키워드가 주로 등장하였음을 확인할 수 있다. 이를 통해 두 집단에서 외교 방식을 바라보는 시선에 다소간 차이가 있음을 확인할 수 있다.

**기획재정위원회**의 경우, 중간값 미만은 ‘경제’ 및 ‘사회'에, 중앙값 위는 ‘과세’에 주요한 관심을 보이고 있다. 다만 정의당의 경우 중간값 이상의 구간에서 가사 및 서비스에 대해 관심을 가지고 있음을 확인할 수 있다. 비교적 젊은층에서 경제 문제를 주요한 안건으로 인식하는 것에 대한 이유는 이들이 경제활동을 하여 소득을 얻는 생애구간에 있다는 것으로부터 찾을 수 있어 보인다. 반면 중간값 이상에서 과세 문제를 주요한 안건으로 인식하는 것에 대한 이유는 기존에 얻은 소득을 바탕으로 형성한 자본에 부과되는 세금에 관심을 가지고 있다는 것을 드러내는 듯해 보인다.

반대로 두 조건에 따른 차이가 크게 나타나지 않은 위원회는 행정안전위원회와 법제사법위원회였다.

행정안전위원회의 경우, 대부분의 영역에서 ‘자치', ‘단체', ‘국가'와 같은 키워드를 많이 사용하였다. 법제사법위원회의 경우, ‘아동' 혹은 ‘피해자'라는 키워드가 많이 등장하였다. 마지막으로 문화체육관광위원회같은 경우 연령에 따른 차이가 나타날 것이라 예상하였는데, 실제로는 두 범주에서 모두 ‘문화재’나 ‘진흥’ 등의 키워드를 많이 쓰며 이러한 차이가 나타나지 않았다. 다만 정의당의 경우 중앙값 이하에서 ‘게임’과 같은 키워드가 들어간 발의안이 많았다.

"""
)

if st.button("참고) 국회의원 네트워크 그래프"):
    img = Image.open('image/국회의원_네트워크.png')
    st.image(img)
    st.markdown(
"""
이 그래프는 대표발의자인 국회의원들을 대상으로 유의미한 네트워크 연결망을 그린 결과이다. 이때 동명이인은 고려되지 않았으므로 연결망에 포함된 국회의원의 수는 34명 이상이며, 실제로 김병욱 의원과 이수진 의원이 제 21대 국회 내에 각각 2명씩 존재하므로 연결망 속의 국회의원 수는 총 36명이다. 네트워크에서 서로 다른 색은 서로 다른 집단을 나타내는데, 이 연결망에서는 총 네 집단을 찾을 수 있다. 아울러 국회의원 노드의 크기 비교를 통해 각 국회의원이 가지는 비중을, 그리고 국회의원 간의 연결 링크(link)의 두께를 통해 각 국회의원 간의 연결이 얼마나 두터운지도 알 수 있다.

이 연결망에서는 다음과 같은 점들을 살펴볼 수 있다. 먼저 빨간 색, 녹색, 옥색 집단의 경우 소수의 국민의 힘 국회의원과 정의당 국회의원을 제외한 나머지는 모두 더불어민주당 국회의원들이다. 남색 집단의 경우 집단에 속한 모든 국회의원들이 더불어민주당에 소속되어 있다. 이를 통해 집단을 넘어, 더불어민주당 국회의원들이 서로 유의미한 네트워크를 형성하고 있다는 사실을 알 수 있다. 또한 각 집단 속에서 확인되는 국민의 힘, 정의당 국회의원들의 존재를 통해 법률안 발의의 측면에서 국회의원들의 성향이 정당을 따라 언제나 극명하게 대비되지 않고, 때에 따라 서로 연결되는 측면이 존재한다는 사실을 알 수 있다. 또 한 가지 특기할 만한 사실은 남색 집단에서 찾아볼 수 있다. 남색 집단에서는 4명의 국회의원들이 서로 긴밀히 연결되어 있는데, 이들은 상기하였듯이 모두 더불어민주당 국회의원들이며, 이들의 지역구는 모두 해안 지방이거나 해안 지방을 포함하고 있다. 나아가 이들은 해양, 어촌, 수산업 등과 관련된 법률안을 대표발의하였다는 공통점을 가지고 있는데, 남색 집단에서의 연결 양상은 이러한 현실을 잘 반영하고 있다고 볼 수 있다.   
"""
)

st.header("Ⅳ. 결론")
img = Image.open('image/국회.jpg')
st.image(img)
st.markdown(
"""
본 프로젝트는 제21대 국회의원들이 발의한 법률안을 중심으로, 현재 국회가 실제로 어떤 키워드에 관심을 갖고 일을 하는지 살펴보고자 했다. 먼저, '어떤 내용'과 '어떤 특성'의 법률안이 발의됐는지를 살펴보기 위해 위원회별 워드클라우드를 분석하고 모든 법률안의 내용을 기반으로 한 단어 네트워크 연결망을 그렸다. 이를 바탕으로 보수/진보 언론별 키워드를 분석해 국회와 사회의 연결성을 살펴보았다. 그 결과 국회의원들은 우리 사회 내 다양한 이슈에 관심을 가지고 그에 따른 법률안을 발의하고 있음을 알 수 있었다. 언론은 특정 인물, 지역 등과 관련되거나 시의성이 있는 키워드가 많이 나타났으며, 사안별로 국회 법률안에 비슷하게 나타나는 것(부동산, 노동 등)과 그렇지 않은 것(디지털 교육, 범죄 등)을 확인할 수 있었다. 그 다음으로, '누가' 어떤 법률안을 발의하는지를 정당과 연령을 기준으로 분석했다. 정당의 전체 발의 내역을 워드클라우드로 분석한 결과 더불어민주당과 국민의힘이 거대 양당으로서 국가 전체의 제도나 국민 전반에 영향을 끼치는 기반 시설과 관련한 법안을 많이 발의하였다면, 정의당은 사회 내부의 소수자를 조망하고 이들의 인권이나 안전 등을 보장하고자 하는 법안을 많이 발의하였다. 연령별 효과는 위원회별로 차이가 있었으나 외교통일위원회와 기획재정위원회에서 의미있는 차이를 확인할 수 있다. 

민주시민으로서 국회와 정치를 이해하는 것은 중요하지만, 국회 안팎에서 쏟아지는 많은 양의 데이터와 이를 포장하는 자극적인 언어들은 국회의 모습을 있는 그대로 바라보기 어렵게 만든다. 본 프로젝트의 결과물이 국회를 보다 객관적으로 비추어, 정치에 대한 이해를 높이는 기회가 되기를 기대한다.
"""
)


st.markdown("***")
if st.button("OPEN API 및 외부자료 출처"):
	st.markdown(
	"""
    ##### OPEN API 자료
    * 열린국회정보, <국회의원 인적사항>
    * 열린국회정보, <국회의원 발의법률안>
    
    ##### 이미지
    * 국회 이미지자료실 : https://www.assembly.go.kr/cmmn/file/imageSrc.do?fileStreCours=829f7616fd59d611d6ee0bd750a47a6a&streFileNm=c4898d8acfe52e943d8691202e8e2fd5db110d2cdf90c86ad45263107332adc5
	""")

if st.button("참고) 보수/진보 매체 주요 단어 네트워크"):
    img = Image.open('image/보수_네트워크.png')
    st.image(img, caption='보수 매체 주요 단어 네트워크')
    st.write("보수 매체에서는 기업에서 집중적으로 뻗어나가는 단어 연결망이 눈에 띈다. 기업과 국가가 밀접하게 관련되어 있는 키워드이며, 이외에도 선거, 가족, 교육에 대한 관심도가 높다.")
    img = Image.open('image/진보_네트워크.png')
    st.image(img, caption='진보 매체 주요 단어 네트워크')
    st.write("진보 매체에서는 비교적 다양한 단어 연결망이 형성되어 있는데, 노동자가 중심적으로 위치해 있으며, 노동자, 코로나, 기업이라는 세 키워드 간의 연결성을 확인할 수 있다. ")


if st.button("참고) 제외 용어(stopwords) 목록"):
    st.code(
"""
stop_words = ["제안", "이유", "주요", "내용", "현행법", "규정", 
  "위원회", "경우", "안", "제", "조", "항", "조제", 
  "조의", "신설", "임", "법률", '등', '수', '것', '년', 
  '법', '호', '자', '해당', '제도', '중', '명', '시', '명', 
  '바', '때', '기관', '관련', '발생', '단체']

if (committee =='국회운영위원회'):
    stop_words += ['국회', '심사', '의원']
elif (committee =='법제사법위원회'):
    stop_words += ['보호', '범죄', '사건']
elif (committee =='정무위원회'):
    stop_words += ['금융','행위']
elif (committee =='기획재정위원회'):
    pass
elif (committee =='교육위원회'):
    stop_words += ['교육', '학교', '학생', '운영','지원','국가']
elif (committee =='과학기술정보방송통신위원회'):
    stop_words += ['정보', '방송', '통신','사업자', '제공']
elif (committee =='외교통일위원회'):
    pass
elif (committee =='국방위원회'):
    stop_words += ['군인', '군']
elif (committee =='행정안전위원회'):
    stop_words += ['지방','선거']
elif (committee =='문화체육관광위원회'):
    stop_words += ['문화','체육','산업','지원']
elif (committee =='농림축산식품해양수산위원회'):
    stop_words += ['동물','관리','사업','농']
elif (committee =='산업통상자원중소벤처기업위원회'):
    stop_words += ['산업', '지원','사업','기업']
elif (committee =='보건복지위원회'):
    stop_words += ['지원']
elif (committee =='환경노동위원회'):
    stop_words += ['근로', '근로자', '고용']
elif (committee =='국토교통위원회'):
    stop_words += ['사업','주택','관리','지역']
elif (committee =='정보위원회'):
    stop_words += ['국가','정보원']
elif (committee =='여성가족위원회'):
    stop_words += ['청소년','지원']
""", language="python")
