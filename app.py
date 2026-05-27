import streamlit as st

st.set_page_config(page_title="김덕건 자기소개", page_icon="👨‍💻", layout="wide")

# ── 테마 ──
theme = st.sidebar.radio("🎨 테마 선택", ["밝은 테마", "어두운 테마"], index=1)

if theme == "어두운 테마":
    bg       = "#0f0f1a"
    card_bg  = "#1a1a2e"
    text     = "#e0e0f0"
    sub_text = "#8890cc"
    accent   = "#6478ff"
    border   = "rgba(100,120,255,0.25)"
else:
    bg       = "#f5f7ff"
    card_bg  = "#ffffff"
    text     = "#1a1a2e"
    sub_text = "#555577"
    accent   = "#4055dd"
    border   = "rgba(64,85,221,0.2)"

st.markdown(f"""
<style>
    .stApp {{ background-color: {bg}; }}
    h1, h2, h3 {{ color: {accent}; }}
    p, li, label {{ color: {text}; }}
    .info-card {{
        background: {card_bg};
        border: 1px solid {border};
        border-radius: 16px;
        padding: 1.4rem 1.8rem;
    }}
    .info-row {{
        display: flex; gap: 0.6rem;
        margin-bottom: 0.9rem; align-items: flex-start;
    }}
    .info-label {{
        font-size: 0.75rem; color: {accent};
        text-transform: uppercase; letter-spacing: 0.08em;
        min-width: 60px; padding-top: 2px;
    }}
    .info-value {{ font-size: 1rem; font-weight: 600; color: {text}; }}
    .skill-label {{
        display: flex; justify-content: space-between;
        font-size: 0.9rem; color: {text}; margin-bottom: 0.2rem;
    }}
    .section-divider {{
        border: none; border-top: 1px solid {border}; margin: 1.5rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# ── 제목 ──
st.title("👨‍💻 김덕건 · 소프트웨어 개발자")
st.markdown(f"<p style='color:{sub_text}; margin-top:-0.8rem;'>KDN 실습 프로젝트 · 자기소개 페이지</p>", unsafe_allow_html=True)
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# ── 프로필 사진 + 2열 레이아웃 ──
col_img, col_left, col_right = st.columns([1, 2, 2])

with col_img:
    st.image(
        "https://api.dicebear.com/7.x/bottts/svg?seed=dgkim91",
        width=150,
        caption="김덕건"
    )

with col_left:
    st.markdown(f"""
    <div class="info-card">
        <div class="info-row">
            <span class="info-label">이름</span>
            <span class="info-value">김덕건</span>
        </div>
        <div class="info-row">
            <span class="info-label">부서</span>
            <span class="info-value">IT 개발팀</span>
        </div>
        <div class="info-row">
            <span class="info-label">이메일</span>
            <span class="info-value">dgkim91@gmail.com</span>
        </div>
        <div class="info-row">
            <span class="info-label">연락처</span>
            <span class="info-value">010-0000-0000</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown(f"<div class='info-card'>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{accent}; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:1rem;'>🛠 기술 스택</p>", unsafe_allow_html=True)

    skills = [("Python", 80), ("Excel", 90), ("SQL", 70)]
    for skill, pct in skills:
        st.markdown(f"""
        <div class="skill-label">
            <span>{skill}</span><span>{pct}%</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(pct / 100)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# ── 경력 사항 ──
with st.expander("📌 경력 사항 펼치기"):
    st.markdown(f"""
    <div style='color:{text}; line-height:2;'>

    **현재** — 소프트웨어 개발자
    웹/시스템 개발 및 유지보수, 팀 리드 역할 수행

    **2010s** — 시니어 개발자
    대규모 프로젝트 설계 및 개발 주도

    **2000s** — 개발자 경력 시작
    소프트웨어 개발 입문 및 다양한 프로젝트 참여

    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# ── 축하 버튼 ──
st.markdown(f"<p style='color:{sub_text}; text-align:center;'>아래 버튼을 눌러보세요 🎉</p>", unsafe_allow_html=True)
col_btn = st.columns([2, 1, 2])[1]
with col_btn:
    if st.button("🎊 축하!", use_container_width=True):
        st.balloons()
