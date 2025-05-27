import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

def swap_page():
    translations = {
        "en": {
            "title": "💱 Swap & Triple Swap Guide",
            "concept_title": "What is Swap (Overnight Interest)?",
            "concept": (
                "Swap, or overnight interest, is the cost or income incurred for holding a position overnight in leveraged products such as Forex, metals, indices, energy, and cryptocurrencies. "
                "It’s calculated based on the interest rate differential of the two currencies or by broker's standard rates for commodities. "
                "Swap can be **positive (you earn)** or **negative (you pay)** depending on position direction and product."
            ),
            "triple_swap_title": "What is Triple Swap (3x Swap)?",
            "triple_swap": (
                "On certain days, usually Wednesdays for FX/Metals, swap is charged **three times** to account for settlement over weekends. "
                "For cryptocurrencies, triple swap is typically applied on Fridays. Always check your broker’s rules!"
            ),
            "common_time_title": "🕑 When is Swap Applied?",
            "common_time": [
                "**FX, Metals, Indices:** Swap is charged at broker's rollover time (often 5am Sydney / 5pm New York).",
                "**Triple Swap:** Applied on Wednesday night (for FX/metals), Friday night (for crypto), or as broker specifies.",
                "**No swap on weekends:** But triple swap covers Sat+Sun.",
                "**Major holidays:** Swap may be adjusted before/after public holidays."
            ],
            "positive_swap": "💡 When Do You Earn or Pay Swap?",
            "earn_swap": [
                "You **earn** swap (get paid) when the interest rate of the bought asset is higher than that of the sold asset, after considering broker commissions.",
                "Example: Buy AUD/USD (if AUD rate > USD rate), you might receive positive swap."
            ],
            "pay_swap": [
                "You **pay** swap (get charged) when the interest rate of the sold asset is higher, or the broker’s swap/commission makes it negative overall.",
                "Example: Sell AUD/USD (if AUD rate < USD rate), you pay swap."
            ],
            "products_title": "Swap Rules by Product",
            "product_table_cols": ["Product", "Triple Swap Day", "Swap Basis", "Common Currencies Involved"],
            "table_fx": ["Forex", "Wednesday", "Interest rate differential", "EUR/USD, AUD/USD, GBP/JPY, etc."],
            "table_metals": ["Metals (Gold/Silver)", "Wednesday", "USD interest rate vs. metal lease rate", "XAUUSD, XAGUSD"],
            "table_energy": ["Energy (Oil)", "Wednesday", "Broker rate / USD Libor", "WTI, Brent"],
            "table_crypto": ["Cryptos", "Friday", "Funding rate, platform policy", "BTC/USD, ETH/USD"],
            "table_indices": ["Indices", "Wednesday", "Index components’ dividend rate", "S&P500, HK50"],
            "calc_title": "Swap & Triple Swap Calculator",
            "direction": "Position Type",
            "long": "Long",
            "short": "Short",
            "volume": "Position Size (lots/contracts)",
            "swap_rate": "Daily Swap Rate (per lot)",
            "days": "Holding Days",
            "calculate": "Calculate",
            "swap_result": "Total Swap (incl. triple swap days)",
            "faq_title": "Frequently Asked Questions",
            "faq": [
                "**Q: Why is swap positive one week and negative the next?**\nA: Central bank rates and broker commissions change; also, dividend/funding/market events may affect swap.",
                "**Q: Why do triple swap days exist?**\nA: Saturday and Sunday don’t charge swap, but positions still cross two days. So, brokers charge 3x swap on a certain day to cover the full period.",
                "**Q: Can swap flip sign (from + to -)?**\nA: Yes! If interest rate policy changes, or your broker adjusts swap rates, positive can become negative and vice versa.",
                "**Q: Is swap the same across all brokers?**\nA: No. Always check your broker’s contract/specification. Some even offer ‘swap free’ accounts for Islamic clients."
            ]
        },
        "zh": {
            "title": "💱 Swap与三倍Swap全解析",
            "concept_title": "什么是Swap（隔夜利息/掉期费）？",
            "concept": (
                "Swap，也叫隔夜利息或掉期费，是指持仓过夜时产生的利息收入或成本。适用于外汇、贵金属、原油、指数、加密货币等杠杆产品。"
                "Swap根据两种货币利差或各平台公布标准费率收取。Swap既可能为正（收钱），也可能为负（扣钱），取决于交易方向和品种。"
            ),
            "triple_swap_title": "什么是三倍Swap（Triple Swap）？",
            "triple_swap": (
                "为覆盖周末无结算的两天，外汇、贵金属等产品一般在周三结算三倍swap；加密货币多为周五结算三倍swap，具体以平台为准。"
            ),
            "common_time_title": "🕑 Swap结算常见时间",
            "common_time": [
                "**外汇、贵金属、指数**：大多在平台结算时间点（常见为悉尼5点/纽约下午5点）计息。",
                "**三倍Swap**：一般周三（外汇/金属），周五（加密），以券商公布为准。",
                "**周末不计息**：但周三或周五的三倍swap自动覆盖周六/日。",
                "**重大节假日**：假期前后swap可能提前或推迟结算。"
            ],
            "positive_swap": "💡 什么时候是收钱/给钱？",
            "earn_swap": [
                "如果买入的货币利率高于卖出货币，并扣除平台手续费后仍为正，则**收利息**（swap为正）。",
                "例如：买入AUD/USD（澳元利率高于美元时），有机会正swap。"
            ],
            "pay_swap": [
                "如果卖出货币利率更高或平台费率因素导致，swap为负则**需要付钱**。",
                "例如：卖出AUD/USD（澳元利率低于美元时），通常会被扣swap。"
            ],
            "products_title": "各品种swap/三倍swap规则",
            "product_table_cols": ["品种", "三倍结算日", "计息依据", "常见合约"],
            "table_fx": ["外汇", "周三", "货币利差", "EUR/USD、AUD/USD、GBP/JPY等"],
            "table_metals": ["贵金属", "周三", "美元利率-金属租借利率", "XAUUSD、XAGUSD"],
            "table_energy": ["能源（原油）", "周三", "平台标准/美元Libor", "WTI、Brent"],
            "table_crypto": ["加密货币", "周五", "Funding费率/平台规则", "BTC/USD、ETH/USD"],
            "table_indices": ["指数", "周三", "指数成分分红率", "标普500、恒指等"],
            "calc_title": "Swap与三倍Swap计算器",
            "direction": "方向",
            "long": "多头",
            "short": "空头",
            "volume": "持仓规模（手/合约）",
            "swap_rate": "每日swap费率（每手）",
            "days": "持仓天数",
            "calculate": "计算",
            "swap_result": "总Swap（含三倍天）",
            "faq_title": "常见问题FAQ",
            "faq": [
                "**问：为什么swap有时正有时负？**\n答：利率政策变动、手续费调整、平台定价变动，都会导致swap方向变化。",
                "**问：三倍swap为什么要存在？**\n答：为覆盖周末两天（无结算），通常在周三（外汇）/周五（加密）一次性计入三天的swap。",
                "**问：swap正负会变化吗？**\n答：当然可能，比如加息、降息、平台策略调整等。",
                "**问：各平台swap一样吗？**\n答：差别很大！一定要查自己券商的合约细则，有的还有伊斯兰“免swap”账户。"
            ]
        }
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 950px; padding-top:2rem;}
        .st-emotion-cache-1kyxreq {background: #f8fafc;}
        .swap-table td, .swap-table th {padding: 0.5em 1em;}
        .swap-card {background:#f6fafd;border-radius:1em;padding:1em 1.3em;box-shadow:0 2px 8px #eef2f7;}
        .pos {color: #0b7c1b;}
        .neg {color: #d1400c;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    # 概念解释
    st.markdown(f"#### ❓ {t['concept_title']}")
    st.info(t["concept"], icon="ℹ️")

    st.markdown(f"#### 🔄 {t['triple_swap_title']}")
    st.success(t["triple_swap"], icon="🔁")

    st.markdown(f"#### {t['common_time_title']}")
    for x in t["common_time"]:
        st.markdown(f"- {x}")

    st.divider()

    # 什么时候收钱/扣钱
    st.markdown(f"#### {t['positive_swap']}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<b class='pos'>📈 可能收钱：</b>", unsafe_allow_html=True)
        for x in t["earn_swap"]:
            st.markdown(f"- {x}")
    with col2:
        st.markdown("<b class='neg'>📉 可能扣钱：</b>", unsafe_allow_html=True)
        for x in t["pay_swap"]:
            st.markdown(f"- {x}")
    # ====== Swap方向测算区 ======
    st.markdown("#### 🧭 Swap Direction Estimator ")

    # 主要品种及示例利率（如实际有最新利率可更新）
    product_rate_dict = {
        "EUR/USD": {"base": "EUR", "quote": "USD", "base_rate": 4.5, "quote_rate": 5.5},
        "AUD/USD": {"base": "AUD", "quote": "USD", "base_rate": 4.35, "quote_rate": 5.5},
        "GBP/USD": {"base": "GBP", "quote": "USD", "base_rate": 5.25, "quote_rate": 5.5},
        "USD/JPY": {"base": "USD", "quote": "JPY", "base_rate": 5.5, "quote_rate": 0.1},
        "Gold (XAUUSD)": {"base": "Gold", "quote": "USD", "base_rate": 0.0, "quote_rate": 5.5},
        "Oil (WTI)": {"base": "Oil", "quote": "USD", "base_rate": 0.0, "quote_rate": 5.5},
        "BTC/USD": {"base": "BTC", "quote": "USD", "base_rate": 0.0, "quote_rate": 5.5},
    }

    product_options = list(product_rate_dict.keys())
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        product = st.selectbox("Product", product_options)
    with col2:
        direction = st.radio("Direction", [t["long"], t["short"]], horizontal=True)
    with col3:
        # 可选显示当前基准利率，用户也可手动调整体验
        base_rate = st.number_input(
            f"{product_rate_dict[product]['base']} rate",
            value=product_rate_dict[product]['base_rate'],
            step=0.01
        )
        quote_rate = st.number_input(
            f"{product_rate_dict[product]['quote']} rate",
            value=product_rate_dict[product]['quote_rate'],
            step=0.01
        )

    if st.button("🔍 Estimate Swap Direction"):
        msg = ""
        color = ""
        # 方向逻辑
        if direction == t["long"]:
            diff = base_rate - quote_rate
            if diff > 0:
                msg = "✅ Likely to **earn** swap (收钱)，但最终以券商为准。"
                color = "green"
            elif diff < 0:
                msg = "❌ Likely to **pay** swap (付钱)，但最终以券商为准。"
                color = "red"
            else:
                msg = "⚠️ Swap direction may be neutral or depends on broker policy."
                color = "orange"
        else:  # 空头
            diff = quote_rate - base_rate
            if diff > 0:
                msg = "✅ Likely to **earn** swap (收钱)，但最终以券商为准。"
                color = "green"
            elif diff < 0:
                msg = "❌ Likely to **pay** swap (付钱)，但最终以券商为准。"
                color = "red"
            else:
                msg = "⚠️ Swap direction may be neutral or depends on broker policy."
                color = "orange"
        st.markdown(f"<div style='font-size:1.2em;color:{color}'>{msg}</div>", unsafe_allow_html=True)
        st.caption("结果仅供参考，实际swap方向及金额以平台/券商报价为准，实际收付还会受手续费、浮动利差影响。")



    st.divider()

    

    # Swap规则表格
    st.markdown(f"#### 📑 {t['products_title']}")
    product_table = [
        t["table_fx"], t["table_metals"], t["table_energy"], t["table_crypto"], t["table_indices"]
    ]
    df = pd.DataFrame(product_table, columns=t["product_table_cols"])
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.divider()

    # Swap计算器
    st.header("🧮 " + t["calc_title"])
    with st.form("swap_calc_form"):
        cols = st.columns(4)
        with cols[0]:
            direction = st.selectbox(t["direction"], [t["long"], t["short"]])
        with cols[1]:
            volume = st.number_input(t["volume"], min_value=0.0, value=1.0, step=0.01)
        with cols[2]:
            swap_rate = st.number_input(
                t["swap_rate"], value=-7.23, step=0.01,
                help=t["swap_rate"]+"（正为收钱，负为扣钱，具体查券商官网）"
            )
        with cols[3]:
            days = st.number_input(t["days"], min_value=1, value=7, step=1,
                                   help="总持仓天数（如遇三倍swap请计入三倍天数）")
        calc = st.form_submit_button(t["calculate"])

        swap_total = None
        if calc:
            # 简化算法：每7天内自动识别“周三/周五为三倍天”
            triple_days = 0
            if days >= 3:
                triple_days = days // 7  # 每周一次三倍swap
            single_days = days - triple_days
            swap_total = swap_rate * single_days + swap_rate * triple_days * 3
            swap_total = swap_total * volume
    if 'swap_total' not in locals():
        swap_total = None
    if swap_total is not None:
        st.metric(label=t["swap_result"], value=f"{swap_total:,.2f}")

    st.divider()

    # FAQ区
    st.subheader("❓ " + t["faq_title"])
    for f in t["faq"]:
        st.markdown(f"- {f}")

# 用法示例
# swap_page()
