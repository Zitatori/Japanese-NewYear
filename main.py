import streamlit as st
import json
import random
import os

st.set_page_config(page_title="Japanese New Year", layout="wide")

st.markdown("""
    <style>
    
    body {
        background-color: #fff0f5;
        background-size: cover;
        background-position: center;
        background-repeat: repeat;
        font-family: "Noto Sans JP", sans-serif;
    .item {
        display: inline-block;
        margin: 40px;
        text-align: center;
    }
    .item img {
        width: 160px;
        height: auto;
        border-radius: 12px;
        cursor: pointer;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    .item img:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    }
    .desc-box {
        background-color: #fff5e1;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #222;
        margin-top: 20px;
    }
    h1 {
        text-align: center;
        color: #b33;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ===== データ読み込み =====
with open("items.json", "r", encoding="utf-8") as f:
    items = json.load(f)

if "selected" not in st.session_state:
    st.session_state["selected"] = None

# ===== タイトル =====
st.markdown("<h1>🎍 Japanese New Year🎍</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Click on a decoration to learn its meaning.</p>", unsafe_allow_html=True)



# ===== 飾りの配置 =====
cols = st.columns(5)
keys = list(items.keys())

for i, key in enumerate(keys):
    item = items[key]
    img_path = os.path.join("images", item["file"])

    with cols[i]:
        st.markdown(f"<div class='item'>", unsafe_allow_html=True)
        if os.path.exists(img_path):
            if st.button("", key=key):
                st.session_state["selected"] = key
            st.image(img_path, use_container_width=True, caption=key)
        else:
            if st.button(f"🏮 {key}", key=key):
                st.session_state["selected"] = key
        st.markdown("</div>", unsafe_allow_html=True)
# ===== 説明表示 =====
if st.session_state["selected"]:
    sel = st.session_state["selected"]
    desc = items[sel]["english"]
    st.markdown(f"""
        <div class="desc-box">
            <h2 style="color:#b33;">{sel}</h2>
            <p style="font-size:18px;">{desc}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; color:#666;'>👆 Tap an image to see its meaning!</p>", unsafe_allow_html=True)


