# app.py
import time
import streamlit as st

# ----------------------------
# Unicode helper
# ----------------------------
def u_to_s(u_list):
    return "".join(chr(c) for c in u_list)

# ----------------------------
# Your UNICODE messages (unchanged)
# ----------------------------
intro_unicode = [
    72,97,112,112,121,32,86,97,108,101,110,116,105,110,101,8217,115,32,68,97,121,44,32,
    109,121,32,108,111,118,101,32,128149,32,
    71,101,116,32,114,101,97,100,121,32,102,111,114,32,97,32,115,101,99,114,101,116,32,109,101,115,115,97,103,101,33
]

spanish_unicode = [
    79,121,101,32,98,101,98,233,32,128149,32,
    69,114,101,115,32,109,105,32,83,97,110,32,86,97,108,101,110,116,237,110,32,
    112,111,114,32,115,105,101,109,112,114,101,46,32,
    84,101,32,97,109,111,32,109,117,99,104,237,115,105,109,111,32,
    121,32,116,101,32,101,120,116,114,97,241,111,32,117,110,32,109,111,110,116,243,110,32,128557
]

decode_unicode = [
    73,116,8217,115,32,121,111,117,114,32,116,117,114,110,32,116,111,32,100,101,99,111,100,101,32,
    116,104,101,32,109,101,115,115,97,103,101,8230,32,
    84,114,121,32,116,111,32,103,117,101,115,115,32,105,116,33
]

reveal_unicode = [
    79,107,97,121,44,32,108,101,116,8217,115,32,114,101,118,101,97,108,8230
]

final_unicode = [
    72,101,121,32,98,97,98,121,32,128149,32,
    89,111,117,8217,114,101,32,109,121,32,97,108,119,97,121,115,32,97,110,100,32,102,111,114,101,118,101,114,32,118,97,108,101,110,116,105,110,101,46,32,
    73,32,108,111,118,101,32,121,111,117,32,115,111,111,111,32,109,117,99,104,32,97,110,100,32,
    73,32,109,105,115,115,32,121,111,117,32,116,111,110,115,32,128557
]

# ----------------------------
# Page config + Romantic styling
# ----------------------------
st.set_page_config(page_title="Secret Valentine 💌", page_icon="💌", layout="centered")

st.markdown(
    """
    <style>
      /* Background */
      .stApp {
        background: radial-gradient(circle at top, #fff0f6 0%, #ffd6e7 35%, #ffc2d9 70%, #ffb3d1 100%);
      }

      /* Center container max width */
      .block-container {
        max-width: 760px;
        padding-top: 2.0rem;
        padding-bottom: 2.0rem;
      }

      /* Card */
      .val-card {
        background: rgba(255, 255, 255, 0.78);
        border: 1px solid rgba(255, 0, 85, 0.25);
        border-radius: 22px;
        padding: 18px 18px 12px 18px;
        box-shadow: 0 12px 34px rgba(255, 0, 85, 0.15);
        backdrop-filter: blur(7px);
      }
      .val-title {
        font-size: 2.05rem;
        font-weight: 900;
        margin: 0 0 6px 0;
        color: #b3002d;
        text-shadow: 0 0 10px rgba(255, 0, 85, 0.25);
      }
      .val-sub {
        font-size: 1.05rem;
        opacity: 0.9;
        margin: 0 0 12px 0;
      }

      /* Message bubbles */
      .bubble {
        border-radius: 18px;
        padding: 14px 14px;
        margin: 12px 0;
        font-size: 1.15rem;
        line-height: 1.55;
        border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
      }
      .bubble-a { background: rgba(255,255,255,0.95); }
      .bubble-b { background: rgba(255, 240, 246, 0.96); }

      /* Glowing red message text */
      .glowText {
        color:#ff0033;
        font-weight:900;
        text-shadow:
          0 0 4px rgba(255, 0, 51, 0.65),
          0 0 10px rgba(255, 0, 85, 0.70),
          0 0 18px rgba(255, 77, 109, 0.65),
          0 0 34px rgba(255, 0, 85, 0.60);
      }

      /* Hearts animation */
      .hearts {
        position: fixed;
        left: 0; top: 0;
        width: 100vw; height: 100vh;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
      }
      .heart {
        position: absolute;
        font-size: 18px;
        opacity: 0.0;
        animation: floatUp 8s linear infinite;
        filter: drop-shadow(0 0 8px rgba(255,0,85,0.35));
      }
      @keyframes floatUp {
        0%   { transform: translateY(20px) scale(0.9); opacity: 0.0; }
        10%  { opacity: 0.65; }
        50%  { opacity: 0.95; }
        100% { transform: translateY(-110vh) scale(1.35); opacity: 0.0; }
      }

      /* Bouquet animation */
      .bouquet {
        position: fixed;
        bottom: 12px;
        right: 18px;
        font-size: 74px;
        animation: floatBouquet 4s ease-in-out infinite alternate;
        z-index: 1;
        filter: drop-shadow(0 10px 22px rgba(255,0,85,0.20));
      }
      @keyframes floatBouquet {
        0% { transform: translateY(0px) rotate(-6deg); }
        100% { transform: translateY(-22px) rotate(6deg); }
      }

      /* Extra flowers floating near bottom-left */
      .flowers {
        position: fixed;
        bottom: 12px;
        left: 16px;
        font-size: 44px;
        animation: floatFlowers 3.2s ease-in-out infinite alternate;
        z-index: 1;
        filter: drop-shadow(0 10px 20px rgba(255,0,85,0.15));
      }
      @keyframes floatFlowers {
        0% { transform: translateY(0px); opacity: 0.95; }
        100% { transform: translateY(-16px); opacity: 1.0; }
      }

      /* Buttons */
      div.stButton > button {
        border-radius: 14px;
        padding: 0.7rem 1.1rem;
        font-weight: 800;
      }
    </style>

    <div class="hearts">
      <div class="heart" style="left: 10%; animation-delay: 0s;">💗</div>
      <div class="heart" style="left: 25%; animation-delay: 1.2s;">💖</div>
      <div class="heart" style="left: 40%; animation-delay: 0.6s;">💕</div>
      <div class="heart" style="left: 55%; animation-delay: 2.0s;">💗</div>
      <div class="heart" style="left: 70%; animation-delay: 1.6s;">💖</div>
      <div class="heart" style="left: 85%; animation-delay: 2.4s;">💕</div>

      <div class="heart" style="left: 15%; font-size: 22px; animation-delay: 3.1s;">💖</div>
      <div class="heart" style="left: 35%; font-size: 20px; animation-delay: 3.8s;">💕</div>
      <div class="heart" style="left: 65%; font-size: 24px; animation-delay: 4.2s;">💗</div>
      <div class="heart" style="left: 90%; font-size: 20px; animation-delay: 4.8s;">💖</div>
    </div>

    <div class="bouquet">💐</div>
    <div class="flowers">🌹🌸</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="val-card">
      <div class="val-title">💌 Secret Valentine</div>
      <div class="val-sub">Press <b>Start</b> and enjoy the secret message flow.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Controls
# ----------------------------
typing_speed = 0.02
enable_lock = False
wait_seconds = 10

secret_ok = True
if enable_lock:
    SECRET_CODE = "love"
    code = st.text_input("Enter secret code", type="password", placeholder="Type the secret code…")
    secret_ok = (code == SECRET_CODE)
    st.caption("Tip: change SECRET_CODE inside app.py to whatever you want.")

# ----------------------------
# Typing effect (glowing red)
# ----------------------------
def type_bubble(text, kind="a"):
    box = st.empty()
    out = ""
    for ch in text:
        out += ch
        box.markdown(
            f"""
            <div class='bubble bubble-{kind}'>
                <span class="glowText">{out}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(typing_speed)

# ----------------------------
# Run button
# ----------------------------
col1, col2 = st.columns([1, 1])
start = col1.button("▶️ Start 💕", use_container_width=True)
reset = col2.button("🔁 Reset", use_container_width=True)

if reset:
    st.rerun()

if start:
    if enable_lock and not secret_ok:
        st.error("Wrong secret code. Try again 💗")
        st.stop()

    # Step 1
    type_bubble(u_to_s(intro_unicode), kind="a")
    time.sleep(1.0)

    # Step 2 (Spanish)
    type_bubble(u_to_s(spanish_unicode), kind="b")
    time.sleep(1.0)

    # Step 3 (Decode prompt)
    type_bubble(u_to_s(decode_unicode), kind="a")

    # Countdown (single updating box)
    countdown = st.empty()
    for r in range(wait_seconds, 0, -1):
        countdown.info(f"⏳ {r} seconds remaining…")
        time.sleep(1)

    countdown.success("✅ Time’s up!")
    time.sleep(0.6)

    # Step 4 (Reveal)
    type_bubble(u_to_s(reveal_unicode), kind="b")
    time.sleep(1.0)

    # Step 5 (Final English)
    type_bubble(u_to_s(final_unicode), kind="a")
    st.balloons()

