import streamlit as st

st.set_page_config(page_title="자기소개", page_icon="👤", layout="centered")

st.markdown("""
<style>
    .result-card {
        background: linear-gradient(135deg, #1a1a3e, #0d2040);
        border: 1px solid rgba(100,120,255,0.3);
        border-radius: 20px;
        padding: 2rem 2.5rem;
        margin-top: 1.5rem;
    }
    .result-label {
        font-size: 0.8rem;
        color: #6478ff;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.3rem;
    }
    .result-value {
        font-size: 1.3rem;
        font-weight: 700;
        color: #e0e0f0;
        margin-bottom: 1.2rem;
    }
    .title-text {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #6478ff, #00c8b4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
    }
    .subtitle-text {
        text-align: center;
        color: #8890cc;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">👤 자기소개</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">아래 정보를 입력하고 버튼을 눌러주세요</div>', unsafe_allow_html=True)

with st.form("intro_form"):
    name = st.text_input("이름", placeholder="홍길동")
    dept = st.text_input("부서", placeholder="예: IT개발팀")
    interest = st.text_input("관심 분야", placeholder="예: 웹 개발, 인공지능")
    submitted = st.form_submit_button("소개 보기", use_container_width=True)

if submitted:
    if not name or not dept or not interest:
        st.warning("이름, 부서, 관심 분야를 모두 입력해주세요.")
    else:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">이름</div>
            <div class="result-value">👤 {name}</div>
            <div class="result-label">부서</div>
            <div class="result-value">🏢 {dept}</div>
            <div class="result-label">관심 분야</div>
            <div class="result-value">🔍 {interest}</div>
        </div>
        """, unsafe_allow_html=True)
        st.success(f"안녕하세요, {name}님! 반갑습니다 😊")
