import streamlit as st
import pandas as pd

def long_short_page():
    translations = {
        "en": {
            "title": "📊 Long & Short Position Tracker",
            "concept": "Concepts",
            "long": "Long Position",
            "long_text": "A long position means you buy an asset expecting the price to rise. Profit = (Current Price - Entry Price) × Position Size × Contract Size.",
            "short": "Short Position",
            "short_text": "A short position means you sell an asset you do not own, expecting the price to fall. Profit = (Entry Price - Current Price) × Position Size × Contract Size.",
            "add_position": "Add New Position",
            "instrument": "Instrument",
            "position_size": "Position Size",
            "contract_size": "Contract Size (per lot)",
            "direction": "Direction",
            "entry_price": "Entry Price",
            "current_price": "Current Price",
            "long_dir": "Long",
            "short_dir": "Short",
            "add": "Add",
            "positions": "Open Positions",
            "no_positions": "No positions yet.",
            "remove": "Remove",
            "summary": "Position Dashboard",
            "total_long": "Total Long",
            "total_short": "Total Short",
            "net_position": "Net Position",
            "total_pnl": "Total P/L",
            "example": "Examples",
            "ex1": "Long 2 lots of XAUUSD at 2300, current 2310. P/L = (2310-2300)×2×100=2,000 USD.",
            "ex2": "Short 0.5 lots of EUR/USD at 1.1000, current 1.0900. P/L = (1.1000-1.0900)×0.5×100,000=500 USD.",
        },
        "zh": {
            "title": "📊 多头与空头持仓跟踪",
            "concept": "核心概念",
            "long": "多头持仓",
            "long_text": "多头指买入资产，预期价格上涨。盈利=（当前价-开仓价）×持仓手数×合约单位。",
            "short": "空头持仓",
            "short_text": "空头指先卖后买，预期价格下跌。盈利=（开仓价-当前价）×持仓手数×合约单位。",
            "add_position": "添加新持仓",
            "instrument": "品种",
            "position_size": "持仓手数",
            "contract_size": "合约单位（每手）",
            "direction": "方向",
            "entry_price": "开仓价",
            "current_price": "当前价",
            "long_dir": "多头",
            "short_dir": "空头",
            "add": "添加",
            "positions": "当前持仓",
            "no_positions": "暂无持仓",
            "remove": "移除",
            "summary": "持仓看板",
            "total_long": "总多头规模",
            "total_short": "总空头规模",
            "net_position": "净持仓",
            "total_pnl": "总盈亏",
            "example": "示例",
            "ex1": "多头2手黄金（XAUUSD），开2300，现2310，盈亏=(2310-2300)×2×100=2,000美元。",
            "ex2": "空头0.5手欧元兑美元（EUR/USD），开1.1000，现1.0900，盈亏=(1.1000-1.0900)×0.5×100,000=500美元。",
        }
    }

    product_presets = {
        "EUR/USD": 100000,
        "GBP/USD": 100000,
        "USD/JPY": 100000,
        "AUD/USD": 100000,
        "Gold (XAUUSD)": 100,
        "Silver (XAGUSD)": 1000,
        "Oil (WTI)": 1000,
        "BTC/USD": 1,
        "ETH/USD": 1,
        "S&P 500": 50,
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 900px; padding-top:2rem;}
        .metric-value {font-size: 2.2em !important;}
        .st-emotion-cache-1kyxreq {background: #f8fafc;}
        .stForm label {font-weight:600;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    # 概念区
    with st.expander("💡 " + t["concept"], expanded=False):
        st.markdown(f"**🔵 {t['long']}**: {t['long_text']}")
        st.markdown(f"**🟠 {t['short']}**: {t['short_text']}")

    # 新持仓录入
    st.header("➕ " + t["add_position"])
    with st.form("add_pos_form"):
        cols = st.columns([1.5, 2, 1.2, 1.3, 1.3, 1.2])
        with cols[0]:
            instrument = st.selectbox(
                t["instrument"], list(product_presets.keys()), key="ls_instrument"
            )
        with cols[1]:
            contract_size = st.number_input(
                t["contract_size"], min_value=1.0, value=float(product_presets[instrument]), step=1.0, key="ls_contract_size"
            )
        with cols[2]:
            direction = st.selectbox(t["direction"], [t["long_dir"], t["short_dir"]], key="ls_dir")
        with cols[3]:
            position_size = st.number_input(t["position_size"], min_value=0.0, value=1.0, step=0.01)
        with cols[4]:
            entry_price = st.number_input(t["entry_price"], min_value=0.0, value=1.1000)
        with cols[5]:
            current_price = st.number_input(t["current_price"], min_value=0.0, value=1.1200)
        add_btn = st.form_submit_button(t["add"])
        if add_btn:
            if "ls_positions" not in st.session_state:
                st.session_state.ls_positions = []
            st.session_state.ls_positions.append({
                "Instrument": instrument,
                "Contract Size": contract_size,
                "Direction": direction,
                "Position Size": position_size,
                "Entry Price": entry_price,
                "Current Price": current_price,
            })
            st.success("✅ Added!")

    # 展示所有持仓
    st.header("📋 " + t["positions"])
    if "ls_positions" not in st.session_state or not st.session_state.ls_positions:
        st.info(t["no_positions"])
    else:
        df = pd.DataFrame(st.session_state.ls_positions)
        # 展示+移除功能
        for idx, row in df.iterrows():
            pnl = (row["Current Price"] - row["Entry Price"]) * row["Position Size"] * row["Contract Size"] \
                  if row["Direction"] == t["long_dir"] \
                  else (row["Entry Price"] - row["Current Price"]) * row["Position Size"] * row["Contract Size"]
            cols = st.columns([7,1])
            with cols[0]:
                st.write(
                    f"**{row['Instrument']}** | {row['Direction']} | {row['Position Size']} lot × {row['Contract Size']} | {row['Entry Price']} → {row['Current Price']} | "
                    f"<span style='color:{'green' if pnl>=0 else 'red'}'>P/L: {pnl:,.2f}</span>", unsafe_allow_html=True)
            with cols[1]:
                if st.button(f"{t['remove']} {idx+1}", key=f"ls_remove_{idx}"):
                    st.session_state.ls_positions.pop(idx)
                    st.rerun()


        # 计算总多/空、净持仓、总盈亏
        long_sum, short_sum, net_pos, total_pnl = 0.0, 0.0, 0.0, 0.0
        for row in st.session_state.ls_positions:
            pos = row["Position Size"] * row["Contract Size"]
            if row["Direction"] == t["long_dir"]:
                long_sum += pos
                pnl = (row["Current Price"] - row["Entry Price"]) * row["Position Size"] * row["Contract Size"]
            else:
                short_sum += pos
                pnl = (row["Entry Price"] - row["Current Price"]) * row["Position Size"] * row["Contract Size"]
            net_pos += pos if row["Direction"] == t["long_dir"] else -pos
            total_pnl += pnl

        st.divider()
        ca, cb, cc, cd = st.columns(4)
        ca.metric(label=f"🔵 {t['total_long']}", value=f"{long_sum:,.2f}")
        cb.metric(label=f"🟠 {t['total_short']}", value=f"{short_sum:,.2f}")
        cc.metric(label=f"📊 {t['net_position']}", value=f"{net_pos:,.2f}")
        cd.metric(label=f"💰 {t['total_pnl']}", value=f"{total_pnl:,.2f}")

    # 示例与说明
    with st.expander("📖 " + t["example"], expanded=False):
        st.markdown(f"- {t['ex1']}")
        st.markdown(f"- {t['ex2']}")

# 用法示例
# long_short_page()
