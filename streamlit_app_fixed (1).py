
import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="📊 Bitcoin Risk Dashboard", layout="centered")
st.title("📊 Bitcoin Risk Dashboard")
st.caption("Powered by on-chain logic + Binance spot API")

# === HÄMTA BTC SPOTPRIS ===
try:
    spot_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    spot_data = requests.get(spot_url).json()
    spot_price = float(spot_data["price"])
    st.metric("📈 BTC Spotpris", f"${spot_price:,.0f}")
except Exception as e:
    spot_price = 0
    st.warning("⚠️ Kunde inte hämta spotpris. Standardvärde används.")
    st.text(f"Fel: {e}")

# === INPUT FÖR MANUELLA INDIKATORER ===
st.markdown("### 🔧 On-chain & sentiment input")
grs = st.slider("GRS – Global Risk Score (1–5)", 1, 5, 3)
drs = st.slider("DRS – Derivatives Risk Score (1–5)", 1, 5, 3)
nprs = st.slider("NPRS – Network Profitability Risk Score (1–5)", 1, 5, 3)
gli = st.number_input("GLI – Global Liquidity Index (%)", min_value=0, max_value=100, value=50)
mvrv = st.number_input("MVRV Z-Score", min_value=-2.0, max_value=15.0, value=2.5, step=0.1)

# === SCORE & ZON ===
x_score = grs + drs + nprs
st.markdown(f"### 🔢 X-Score: **{x_score} / 15**")

if x_score <= 5:
    st.success("🟢 Accumulation Zone — Low Risk")
elif 6 <= x_score <= 7:
    st.warning("🟡 Neutral Zone — Stay Alert")
else:
    st.error("🔴 High Risk Zone — Take Profits / Hedge")

# === TOLKNING ===
st.markdown("### 🧠 Interpretation")
if x_score <= 5 and gli > 50:
    st.markdown("✅ Low risk with high liquidity — ideal for scaling in.")
if x_score >= 9:
    st.markdown("⚠️ High X-Score — potential for overextension.")
if mvrv > 6:
    st.markdown("🚨 MVRV Z-Score is elevated — unrealized profit is high.")

# === FOOTER ===
st.markdown("---")
st.caption("By you + AI. No financial advice – just quant signals.")
