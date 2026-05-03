import streamlit as st
import numpy as np
import re

st.set_page_config(
    page_title="Buhoor",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

import json, os

CLASSES = {
    0: "البسيط", 1: "الخفيف", 2: "الرجز",  3: "الرمل",    4: "السريع",
    5: "الطويل", 6: "الكامل", 7: "المتقارب", 8: "المجتث", 9: "المنسرح", 10: "الوافر",
}

_MAPPING_PATH = r"C:\Users\NSHAT\school\Arabic Poetry Project\models\id_to_meter.json" # doesnt exist any way
if os.path.exists(_MAPPING_PATH):
    with open(_MAPPING_PATH, encoding="utf-8") as _f:
        CLASSES = {int(k): v for k, v in json.load(_f).items()}

METER_DESCRIPTIONS = {
    "البسيط":   "مستفعلن فاعلن مستفعلن فاعلن",
    "الخفيف":   "فاعلاتن مستفعلن فاعلاتن",
    "الرجز":    "مستفعلن مستفعلن مستفعلن",
    "الرمل":    "فاعلاتن فاعلاتن فاعلاتن",
    "السريع":   "مستفعلن مستفعلن فاعلن",
    "الطويل":   "فعولن مفاعيلن فعولن مفاعيلن",
    "الكامل":   "متفاعلن متفاعلن متفاعلن",
    "المتقارب": "فعولن فعولن فعولن فعولن",
    "المجتث":   "مستفعلن فاعلاتن",
    "المنسرح":  "مستفعلن مفعولات مستفعلن",
    "الوافر":   "مفاعلتن مفاعلتن فعولن",
}

EXAMPLES = [
    "— اختر مثالاً —",
    "إني لَعَمركَ مَا أخشَى إِذَا ذُكِرَت # مِنِّي الخَلاَئِقُ في مُستَكرِهِ الزَّمَنِ",
    "قِفا نَبكِ مِن ذِكرى حَبيبٍ وَمَنزِلِ # بِسِقطِ اللِوى بَينَ الدَخولِ فَحَومَلِ",
    "أَلا لَيتَ الشَبابَ يَعودُ يَوماً # فَأُخبِرَهُ بِما فَعَلَ المَشيبُ",
    "قف شامخا مثل المآذن طولا # و إبعث رصاصك وابلا سجّيلا",
]

@st.cache_resource(show_spinner=False)
def load_model():
    try:
        import tensorflow as tf
        model_path = "models/best_model_meter_95acc.h5"
        return tf.keras.models.load_model(model_path), None
    except Exception as e:
        return None, str(e)

def preprocess_verse(verse: str) -> str:
    verse = verse.strip()
    verse = re.sub(r'[أإآ]', 'ا', verse)
    verse = re.sub(r'ة', 'ه', verse)
    verse = re.sub(r'ى', 'ي', verse)
    return verse

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Scheherazade+New:wght@400;700&display=swap');

:root {
    --gold:       #C9A84C;
    --gold-light: #E8C97A;
    --gold-dark:  #8B6914;
    --deep:       #0D0A06;
    --teal:       #1A5C5A;
    --parchment:  #F5EDD8;
    --muted:      #6B5533;
}

html, body, [class*="css"] {
    font-family: 'Amiri', serif;
    background-color: var(--deep);
    color: var(--parchment);
    direction: rtl;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 20%, rgba(201,168,76,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 80%, rgba(26,92,90,0.09) 0%, transparent 50%),
        linear-gradient(160deg, #0D0A06 0%, #12100A 60%, #0A0D10 100%);
    min-height: 100vh;
    overflow: hidden;
}

#MainMenu, footer, header { visibility: hidden; }

/* Wide layout: no padding waste */
.block-container {
    padding: 1rem 2.5rem 1rem 2.5rem !important;
    max-width: 100% !important;
}

/* ── Header ── */
.header-wrap { text-align: center; padding: 0.6rem 1rem 0.5rem; }
.header-wrap::before {
    content: '';
    display: block;
    width: 180px; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 0 auto 0.6rem;
}
.main-title {
    font-family: 'Scheherazade New', serif;
    font-size: 2.4rem; font-weight: 700;
    color: var(--gold-light);
    text-shadow: 0 0 40px rgba(201,168,76,0.3);
    margin: 0;
}
.sub-title { font-size: 0.82rem; color: var(--muted); margin-top: 0.25rem; letter-spacing: 0.06em; }
.header-wrap::after {
    content: '✦  ❖  ✦';
    display: block; color: var(--gold-dark);
    font-size: 0.85rem; margin-top: 0.5rem; letter-spacing: 0.5em;
}

/* ── Cards ── */
.card {
    background: linear-gradient(145deg, #1C1508, #14110A);
    border: 1px solid rgba(201,168,76,0.22);
    border-radius: 4px;
    padding: 1.2rem 1.5rem;
    margin: 0.7rem 0;
    position: relative;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5), inset 0 1px 0 rgba(201,168,76,0.08);
}
.card::before {
    content: '';
    position: absolute; top: 5px; left: 5px; right: 5px; bottom: 5px;
    border: 1px solid rgba(201,168,76,0.07);
    border-radius: 2px; pointer-events: none;
}
.corner { position: absolute; width: 14px; height: 14px; border-color: var(--gold); border-style: solid; opacity: 0.65; }
.corner-tl { top:-1px; left:-1px;    border-width: 2px 0 0 2px; border-radius: 2px 0 0 0; }
.corner-tr { top:-1px; right:-1px;   border-width: 2px 2px 0 0; border-radius: 0 2px 0 0; }
.corner-bl { bottom:-1px; left:-1px; border-width: 0 0 2px 2px; border-radius: 0 0 0 2px; }
.corner-br { bottom:-1px; right:-1px; border-width: 0 2px 2px 0; border-radius: 0 0 2px 0; }
.card-label { font-size: 0.68rem; letter-spacing: 0.18em; color: var(--gold-dark); text-transform: uppercase; margin-bottom: 0.6rem; }

/* ── Column divider ── */
.col-divider {
    width: 1px;
    background: linear-gradient(180deg, transparent, rgba(201,168,76,0.3), transparent);
    align-self: stretch;
    margin: 0 0.5rem;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    font-family: 'Scheherazade New', serif !important;
    font-size: 1rem !important;
    direction: rtl !important;
    background: rgba(5,4,2,0.7) !important;
    border: 1px solid rgba(201,168,76,0.28) !important;
    border-radius: 3px !important;
    color: var(--parchment) !important;
}
.stSelectbox label { color: var(--muted) !important; font-size: 0.75rem !important; margin-bottom: 0.3rem !important; }

/* ── Textarea ── */
.stTextArea textarea {
    font-family: 'Scheherazade New', serif !important;
    font-size: 1.4rem !important;
    direction: rtl !important;
    text-align: right !important;
    background: rgba(5,4,2,0.6) !important;
    border: 1px solid rgba(201,168,76,0.28) !important;
    border-radius: 3px !important;
    color: var(--parchment) !important;
    line-height: 1.9 !important;
    padding: 0.8rem 1rem !important;
    caret-color: var(--gold) !important;
    resize: none !important;
}
.stTextArea textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.1) !important;
    outline: none !important;
}
.stTextArea label { display: none !important; }

/* ── Button ── */
.stButton > button {
    font-family: 'Scheherazade New', serif !important;
    font-size: 1.15rem !important; font-weight: 700 !important;
    width: 100% !important; padding: 0.6rem 2rem !important;
    background: linear-gradient(135deg, #8B6914, #C9A84C, #8B6914) !important;
    background-size: 200% 100% !important;
    color: var(--deep) !important;
    border: none !important; border-radius: 3px !important;
    letter-spacing: 0.1em !important;
    box-shadow: 0 4px 16px rgba(201,168,76,0.2) !important;
    transition: box-shadow 0.2s, transform 0.15s !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 24px rgba(201,168,76,0.32) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Result ── */
.result-wrap { text-align: center; padding: 0.4rem 0.2rem; }
.result-verse {
    font-family: 'Scheherazade New', serif;
    font-size: 1rem; color: var(--muted);
    margin-bottom: 0.7rem; line-height: 1.8;
    border-bottom: 1px solid rgba(201,168,76,0.12);
    padding-bottom: 0.7rem;
}
.result-meter {
    font-family: 'Scheherazade New', serif;
    font-size: 2.4rem; font-weight: 700;
    color: var(--gold-light);
    text-shadow: 0 0 30px rgba(201,168,76,0.45);
    margin: 0.15rem 0;
}
.result-taf3ila { font-size: 0.88rem; color: var(--muted); margin-top: 0.25rem; }
.result-conf { font-size: 0.78rem; color: var(--gold-dark); margin-top: 0.7rem; letter-spacing: 0.1em; }
.conf-bar-wrap { width: 55%; height: 4px; background: rgba(255,255,255,0.07); border-radius: 2px; margin: 0.35rem auto 0; overflow: hidden; }
.conf-bar-fill { height: 100%; background: linear-gradient(90deg, var(--gold-dark), var(--gold-light)); border-radius: 2px; }

.prob-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
.prob-table th { font-size: 0.68rem; letter-spacing: 0.12em; color: var(--gold-dark); text-transform: uppercase; padding: 0.3rem 0.5rem; border-bottom: 1px solid rgba(201,168,76,0.18); text-align: right; }
.prob-table td { padding: 0.32rem 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.04); color: var(--parchment); vertical-align: middle; }
.prob-bar { height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden; min-width: 60px; }
.prob-bar-fill { height: 100%; background: linear-gradient(90deg, var(--teal), var(--gold)); border-radius: 3px; }
.top-row td { color: var(--gold-light) !important; font-weight: 700; }

.banner-err { background: rgba(139,46,10,0.18); border: 1px solid rgba(139,46,10,0.5); border-radius: 3px; padding: 0.6rem 1rem; color: #E8927A; font-size: 0.88rem; text-align: right; }
.banner-info { background: rgba(26,92,90,0.13); border: 1px solid rgba(26,92,90,0.35); border-radius: 3px; padding: 0.5rem 1rem; color: #7ABFBD; font-size: 0.78rem; text-align: right; margin-top: 0.4rem; }

.divider { text-align: center; margin: 0.5rem 0; color: var(--gold-dark); font-size: 0.9rem; letter-spacing: 0.6em; }
.stSpinner > div { border-top-color: var(--gold) !important; }

/* placeholder column */
.placeholder-wrap {
    text-align: center;
    padding: 3rem 1rem;
    opacity: 0.25;
}
.placeholder-icon { font-size: 3rem; margin-bottom: 0.5rem; }
.placeholder-text { font-family: 'Scheherazade New', serif; font-size: 1rem; color: var(--gold); letter-spacing: 0.1em; }

/* tighten streamlit column gaps */
[data-testid="column"] { padding: 0 0.6rem !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
    <div class="main-title">ميزان الشعر العربي (بحور)</div>
    <div class="sub-title">Arabic Poetry Meter Classifier  .علم العروض - بحور الشعر</div>
</div>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────────────────────
if "verse" not in st.session_state:
    st.session_state.verse = ""
if "result_html" not in st.session_state:
    st.session_state.result_html = None
if "error_html" not in st.session_state:
    st.session_state.error_html = None

# ── Two-column layout ────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="medium")

# ════════════════════════════════════════════════════════════════════════════
# LEFT COLUMN — Input
# ════════════════════════════════════════════════════════════════════════════
with left_col:
    st.markdown('<div class="card-label" style="margin-bottom:0.5rem;">أدخل البيت الشعري</div>', unsafe_allow_html=True)

    verse_input = st.text_area(
        label="verse",
        value=st.session_state.verse,
        height=110,
        placeholder="الصدر  #  العجز",
    )

    st.markdown('<div class="banner-info">افصل بين الصدر والعجز بعلامة &nbsp;<strong>#</strong></div>', unsafe_allow_html=True)

    selected = st.selectbox("اختر مثالاً من التراث", EXAMPLES, index=0)
    if selected != EXAMPLES[0]:
        st.session_state.verse = selected

    classify_clicked = st.button("تحليل الوزن الشعري  ✦")

    if classify_clicked:
        verse = verse_input.strip()
        if not verse:
            st.session_state.error_html = '<div class="banner-err">⚠ الرجاء إدخال بيت شعري.</div>'
            st.session_state.result_html = None
        elif "#" not in verse:
            st.session_state.error_html = '<div class="banner-err">⚠ يرجى الفصل بين الصدر والعجز بعلامة #</div>'
            st.session_state.result_html = None
        else:
            with st.spinner("جارٍ التحليل …"):
                model, err = load_model()

            if err or model is None:
                st.session_state.error_html = f'<div class="banner-err">⚠ تعذّر تحميل النموذج — {err}</div>'
                st.session_state.result_html = None
            else:
                try:
                    clean = preprocess_verse(verse)

                    MAX_LEN = 128
                    CHAR2IDX_PATH = "models\char2idx.json"
                    #CHAR2IDX_PATH = r"C:\Users\NSHAT\school\Arabic Poetry Project\models\char2idx.json"

                    if os.path.exists(CHAR2IDX_PATH):
                        with open(CHAR2IDX_PATH, encoding="utf-8") as _f:
                            char2idx = json.load(_f)
                    else:
                        _chars = sorted(list(set(
                            " #آأإابةتثجحخدذرزسشصضطظعغـفقكلمنهوىيءٌٍَُِّْٰٱ"
                        )))
                        char2idx = {c: i+1 for i, c in enumerate(_chars)}

                    seq = [char2idx.get(ch, 0) for ch in clean]
                    seq = seq[:MAX_LEN] + [0] * max(0, MAX_LEN - len(seq))
                    x = np.array([seq], dtype=np.int32)

                    preds = model.predict(x, verbose=0)[0]
                    top_idx = int(np.argmax(preds))
                    confidence = float(preds[top_idx])
                    meter_name = CLASSES.get(top_idx, "غير معروف")
                    taf3ila = METER_DESCRIPTIONS.get(meter_name, "")
                    conf_pct = int(confidence * 100)

                    parts = verse.split("#")
                    verse_display = f"{parts[0].strip()} &nbsp;❙&nbsp; {parts[1].strip()}" if len(parts) == 2 else verse

                    sorted_indices = np.argsort(preds)[::-1]
                    rows_html = ""
                    for rank, idx in enumerate(sorted_indices):
                        name = CLASSES[idx]
                        prob = preds[idx]
                        bar_w = int(prob * 100)
                        row_class = "top-row" if rank == 0 else ""
                        rows_html += f"""
                        <tr class="{row_class}">
                            <td>{name}</td>
                            <td>{prob:.1%}</td>
                            <td><div class="prob-bar"><div class="prob-bar-fill" style="width:{bar_w}%"></div></div></td>
                        </tr>"""

                    st.session_state.result_html = (meter_name, taf3ila, conf_pct, verse_display, rows_html)
                    st.session_state.error_html = None

                except Exception as ex:
                    st.session_state.error_html = f'<div class="banner-err">⚠ حدث خطأ: {ex}</div>'
                    st.session_state.result_html = None

    if st.session_state.error_html:
        st.markdown(st.session_state.error_html, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# RIGHT COLUMN — Results
# ════════════════════════════════════════════════════════════════════════════
with right_col:
    if st.session_state.result_html:
        meter_name, taf3ila, conf_pct, verse_display, rows_html = st.session_state.result_html

        st.markdown(f"""
        <div class="card">
            <span class="corner corner-tl"></span><span class="corner corner-tr"></span>
            <span class="corner corner-bl"></span><span class="corner corner-br"></span>
            <div class="result-wrap">
                <div class="result-verse">{verse_display}</div>
                <div class="card-label">البحر المُشخَّص</div>
                <div class="result-meter">{meter_name}</div>
                <div class="result-taf3ila">{taf3ila}</div>
                <div class="result-conf">نسبة الثقة: {conf_pct}%</div>
                <div class="conf-bar-wrap">
                    <div class="conf-bar-fill" style="width:{conf_pct}%"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="divider">❖</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
            <span class="corner corner-tl"></span><span class="corner corner-tr"></span>
            <span class="corner corner-bl"></span><span class="corner corner-br"></span>
            <div class="card-label">توزيع الاحتماليات</div>
            <table class="prob-table">
                <thead><tr><th>البحر</th><th>الاحتمالية</th><th></th></tr></thead>
                <tbody>{rows_html}</tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="placeholder-wrap">
            <div class="placeholder-icon">✦</div>
            <div class="placeholder-text">ستظهر نتائج التحليل هنا</div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:1.5rem;color:rgba(201,168,76,0.18);font-size:0.68rem;letter-spacing:0.18em;">
    ✦ &nbsp;Nasha't - ميزان الشعر العربي &nbsp; ✦
</div>
""", unsafe_allow_html=True)