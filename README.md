
# 📊 Bitcoin Risk Dashboard

Ett realtidsdashboard för att mäta marknadsrisk för Bitcoin (BTC) baserat på både on-chain indikatorer och derivatdata från Binance.

## ✅ Funktioner

- Live Funding Rate och Open Interest (Binance API, ingen nyckel krävs)
- Manuella on-chain riskindikatorer:
  - GRS – Global Risk Score
  - DRS – Derivatives Risk Score
  - NPRS – Network Profitability Risk Score
  - GLI – Global Liquidity Index
  - MVRV Z-Score
- Automatisk X-Score-beräkning (1–15)
- Visuell riskzon: 🟢🟡🔴
- Tolkningar baserat på kombinationer av datapunkter

## 🚀 Starta appen lokalt

```bash
pip install streamlit
streamlit run streamlit_app.py
```

## 🌐 Deployment
Deploya till [Streamlit Cloud](https://streamlit.io/cloud) eller hosta själv via server/Heroku/Docker.

## 🛡️ Ansvarsfriskrivning

Detta är **inte finansiell rådgivning**. Dashboarden bygger på kvantitativa signaler och historiska samband. Gör alltid egen analys.

---

Byggt av dig. Assisterat av AI. 🔮
