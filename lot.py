import streamlit as st

def lot_page():
    translations = {
        "en": {
            "title": "🔢 Lot Size Calculator",
            "concept": "Concept",
            "concept_text": "A 'Lot' is the standardized quantity of a financial instrument being traded. For example, 1 standard Forex lot = 100,000 units of the base currency. Different assets have different lot sizes.",
            "formula": "Lot Size = Position Size (units) ÷ Contract Size (per lot)",
            "calculator": "Lot Size Calculator",
            "position_size": "Position Size (units)",
            "contract_size": "Contract Size (per lot)",
            "calculate": "Calculate",
            "result": "Required Lots",
            "note": "*Always refer to your broker's specification for each instrument.*",
            "examples": "Common Standard Lots",
            "forex": "Forex: 1 lot = 100,000 units (standard)",
            "gold": "Gold: 1 lot = 100 ounces (standard)",
            "btc": "BTC: 1 lot = 1 coin (standard)",
            "quick_select": "Quick Select Instrument",
        },
        "zh": {
            "title": "🔢 手数（Lot）计算器",
            "concept": "概念",
            "concept_text": "“手数”是金融市场的标准交易单位。例如，外汇1标准手=10万基础货币。不同品种手数定义不同。",
            "formula": "手数 = 持仓规模（单位） ÷ 合约单位（每手）",
            "calculator": "手数计算器",
            "position_size": "持仓规模（单位）",
            "contract_size": "合约单位（每手）",
            "calculate": "计算",
            "result": "所需手数",
            "note": "*具体请以交易商品参数为准*",
            "examples": "常用标准手数",
            "forex": "外汇：1标准手=100,000单位",
            "gold": "黄金：1标准手=100盎司",
            "btc": "比特币：1标准手=1枚",
            "quick_select": "一键选择品种",
        }
    }

    product_presets = {
        "Forex (EUR/USD, USD/JPY, etc)": 100000,
        "Gold (XAUUSD)": 100,
        "Silver (XAGUSD)": 1000,
        "Oil (WTI)": 1000,
        "Index (S&P 500)": 50,
        "BTC/USD": 1,
        "ETH/USD": 1,
        "XRP/USD": 1,
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 750px; padding-top:2rem;}
        .metric-value {font-size: 2em !important;}
        .st-emotion-cache-1kyxreq {background: #f8fafc;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    # 概念区
    with st.expander("💡 " + t["concept"], expanded=False):
        st.markdown(f"**{t['concept_text']}**")
        st.code(t["formula"], language="markdown")

    # 计算区块
    st.divider()
    st.header("🧮 " + t["calculator"])

    # 一键选择常用品种
    col1, col2 = st.columns([2, 3])
    with col1:
        quick_choice = st.selectbox(
            t["quick_select"],
            [""] + list(product_presets.keys()),
            index=0,
            help="Choose an instrument to autofill contract size"
        )
    with col2:
        st.caption("")

    # 参数录入
    cols = st.columns(2)
    with cols[0]:
        position_size = st.number_input(
            t["position_size"], min_value=0.0, value=100000.0, step=100.0
        )
    with cols[1]:
        if quick_choice:
            contract_size = st.number_input(
                t["contract_size"], min_value=1.0, value=float(product_presets[quick_choice]), step=1.0, key="lot_contract_size"
            )
        else:
            contract_size = st.number_input(
                t["contract_size"], min_value=1.0, value=100000.0, step=1.0, key="lot_contract_size"
            )

    # 计算按钮
    calc = st.button("🟩 " + t["calculate"])
    lots = None
    if calc:
        lots = position_size / contract_size if contract_size else 0.0

    # 结果展示区卡片
    if lots is not None:
        colr, _ = st.columns([1,3])
        colr.metric(label="🔢 " + t["result"], value=f"{lots:,.2f}")

    st.caption(t["note"])

    # 常见品种标准
    with st.expander("📖 " + t["examples"], expanded=False):
        st.markdown(f"- {t['forex']}")
        st.markdown(f"- {t['gold']}")
        st.markdown(f"- {t['btc']}")

# 用法示例
# lot_page()
