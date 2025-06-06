import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="📊 Bitcoin Risk Dashboard", layout="centered")
st.title("📊 Bitcoin Risk Dashboard")
st.caption("Powered by on-chain logic + Binance public API")

# === HÄMTA LIVE DATA ===
try:
    # Funding Rate
    funding_url = "https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1"
    funding_data = requests.get(funding_url).json()
    funding_rate = float(funding_data[0]["fundingRate"]) * 100
    funding_time = datetime.fromtimestamp(funding_data[0]["fundingTime"] / 1000)

    # Open Interest
    oi_url = "https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT"
    oi_data = requests.get(oi_url).json()
    open_interest = float(oi_data["openInterest"]) / 1_000_000

    st.metric("Funding Rate (%)", f"{funding_rate:.4f}")
    st.metric("Open Interest (M USD)", f"{open_interest:.2f}")
    st.caption(f"Senaste funding: {funding_time.strftime('%Y-%m-%d %H:%M UTC')}")
except Exception as e:
    funding_rate = 0.05
    open_interest = 10
    st.warning("⚠️ Kunde inte hämta live-data. Standardvärden används.")

# === INPUTS FÖR ÖVRIGA INDIKATORER ===
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
if x_score >= 9 and funding_rate > 0.1:
    st.markdown("⚠️ High funding + risk = possible blow-off top. Market overheated.")
if mvrv > 6:
    st.markdown("🚨 MVRV Z-Score is elevated — unrealized profit is high.")
if open_interest > 12:
    st.markdown("🧨 Open Interest unusually high — expect volatility.")

# === FOOTER ===
st.markdown("---")
st.caption("By you + AI. No financial advice – just quant signals.")

