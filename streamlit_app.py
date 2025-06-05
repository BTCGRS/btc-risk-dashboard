
import streamlit as st

st.set_page_config(page_title="BTC Risk Dashboard", layout="centered")

st.title("📊 Bitcoin Risk Dashboard")
st.markdown("Använd GLI, GRS, DRS, NPRS, MVRV för att mäta positioneringsläge.")

# === INPUT SECTION ===
grs = st.slider("GRS (1-5)", 1, 5, 3)
drs = st.slider("DRS (1-5)", 1, 5, 3)
nprs = st.slider("NPRS (1-5)", 1, 5, 3)
gli = st.number_input("GLI (0–100, eller %)", value=50)
mvrv = st.number_input("MVRV Z-Score", value=2.5)
funding_rate = st.number_input("Funding Rate (%)", value=0.05)
open_interest = st.number_input("Open Interest (Bn USD)", value=10.0)

# === SCORE + RISK ZONE ===
x_score = grs + drs + nprs
st.markdown(f"### 🔢 X-Score: {x_score} / 15")

if x_score <= 5:
    st.success("🟢 Accumulation Zone — Low Risk")
elif 6 <= x_score <= 7:
    st.warning("🟡 Neutral Zone — Stay Alert")
else:
    st.error("🔴 High Risk Zone — Take Profits / Hedge")

# === Interpretation block ===
st.markdown("#### Interpretation")
if x_score <= 5 and gli > 50:
    st.markdown("✅ Low risk, liquidity supportive — ideal for scaling in.")
elif x_score >= 8 and mvrv > 6:
    st.markdown("⚠️ Market is overheated and speculative — reduce exposure.")

# === Footer ===
st.markdown("---")
st.caption("Built by you. Powered by on-chain + macro signal logic 💡")
