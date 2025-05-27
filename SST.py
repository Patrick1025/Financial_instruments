import streamlit as st
import pandas as pd

def scalping_vs_swing_trading_page():
    translations = {
        "en": {
            "title": "📊 Scalping vs. Swing Trading",
            "concept": "Key Concepts",
            "scalping": "🔍 Scalping",
            "swing_trading": "🔍 Swing Trading",
            "scalping_explanation": "Scalping is a strategy based on making many quick trades to capture small, frequent price changes, usually holding positions from seconds to minutes.",
            "swing_trading_explanation": "Swing trading involves holding positions for several days (sometimes weeks) to capture larger price swings within a trend.",
            "compare_title": "🆚 Key Differences Table",
            "col_strategy": "Strategy",
            "col_time": "Holding Period",
            "col_trade_freq": "Trade Frequency",
            "col_target": "Profit Target",
            "col_risk": "Risk Level",
            "col_typical_asset": "Typical Assets",
            "col_require": "Requirements",
            "scalping_row": ["Scalping", "Seconds to Minutes", "High (10–100/day)", "Small (pips/ticks)", "High (due to leverage, costs)", "FX, Futures, Crypto", "Low latency, discipline, focus"],
            "swing_row": ["Swing Trading", "Days to Weeks", "Low to Medium (1–10/week)", "Large (hundreds of pips/points)", "Moderate", "Stocks, FX, Indices", "Patience, trend analysis"],
            "pros_title": "👍 Advantages",
            "cons_title": "⚠️ Drawbacks",
            "scalping_pros": [
                "Quick realization of gains/losses.",
                "Less overnight risk.",
                "Frequent trading opportunities."
            ],
            "scalping_cons": [
                "High transaction costs (spreads/commission).",
                "Requires constant monitoring.",
                "Can be stressful and mentally demanding."
            ],
            "swing_pros": [
                "Less time at screen, suitable for part-timers.",
                "Fewer trades, lower cost per month.",
                "Potential for larger profits per trade."
            ],
            "swing_cons": [
                "Exposure to overnight/weekend risk.",
                "Requires patience; not always active.",
                "May miss intraday moves."
            ],
            "suitable_title": "👤 Who is it Suitable For?",
            "scalping_people": "Traders with fast reaction, discipline, ability to focus for long sessions, often prefer volatile and liquid markets.",
            "swing_people": "People with a job or school, patience, can withstand overnight risk, and like analyzing trends.",
            "pitfalls_title": "🚨 Common Pitfalls",
            "pitfalls": [
                "**Scalping:** Overtrading, letting losses run, ignoring spreads/slippage, using excessive leverage.",
                "**Swing Trading:** Lacking patience, moving stop too early, ignoring market news or overnight events, overexposing one trend."
            ],
            "which_style": "Which style do you prefer or want to try?",
            "choose_scalping": "Scalping",
            "choose_swing": "Swing Trading",
            "vote": "Submit",
            "your_choice": "You chose: ",
        },
        "zh": {
            "title": "📊 剥头皮 vs. 波段交易",
            "concept": "核心概念",
            "scalping": "🔍 剥头皮交易",
            "swing_trading": "🔍 波段交易",
            "scalping_explanation": "剥头皮交易是一种高频短线策略，通过频繁快进快出，抓取极小幅度波动，持仓时间常为数秒至数分钟。",
            "swing_trading_explanation": "波段交易是一种持仓周期较长的策略，通常持有几天甚至数周，目的是捕捉趋势中的大幅波动。",
            "compare_title": "🆚 主要差异对比表",
            "col_strategy": "策略类型",
            "col_time": "持仓周期",
            "col_trade_freq": "交易频率",
            "col_target": "目标幅度",
            "col_risk": "风险级别",
            "col_typical_asset": "典型品种",
            "col_require": "核心要求",
            "scalping_row": ["剥头皮", "数秒到数分钟", "极高（10-100次/天）", "极小（点/分）", "高（杠杆、滑点）", "外汇、期货、加密", "专注、执行力、极速下单"],
            "swing_row": ["波段", "几天到几周", "较低（1-10次/周）", "大幅波动", "中等", "股票、外汇、指数", "耐心、趋势判断"],
            "pros_title": "👍 优势",
            "cons_title": "⚠️ 劣势",
            "scalping_pros": [
                "盈亏实现快，无隔夜风险。",
                "交易机会多，适合震荡市场。",
                "交易员反馈即时，易于总结经验。"
            ],
            "scalping_cons": [
                "手续费与点差高，长期易被成本侵蚀。",
                "需全天盯盘，精神压力大。",
                "对网络与执行速度要求极高。"
            ],
            "swing_pros": [
                "无需全天盯盘，适合上班族。",
                "月度交易笔数少，成本更低。",
                "单笔获利空间大。"
            ],
            "swing_cons": [
                "面临隔夜/周末跳空风险。",
                "对耐心要求高，等待时间长。",
                "易错过盘中短线机会。"
            ],
            "suitable_title": "👤 适合人群",
            "scalping_people": "反应快、自律、能长时间专注、喜欢高波动流动性强品种的交易员。",
            "swing_people": "有主业或学业、能承受隔夜风险、有耐心、喜欢趋势分析的人。",
            "pitfalls_title": "🚨 常见误区",
            "pitfalls": [
                "**剥头皮**：频繁交易、止损不坚决、忽视点差与滑点、盲目加杠杆。",
                "**波段**：缺乏耐心、过早移动止损、忽略重大消息或隔夜风险、重仓单边。"
            ],
            "which_style": "你更喜欢/更想尝试哪种风格？",
            "choose_scalping": "剥头皮",
            "choose_swing": "波段交易",
            "vote": "提交",
            "your_choice": "你选择了：",
        }
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 900px; padding-top:2rem;}
        .st-emotion-cache-1kyxreq {background: #f7fafc;}
        .pros-card {background:#ebfaf4;border-radius:1.1em;padding:1em 1.2em;}
        .cons-card {background:#fff6f0;border-radius:1.1em;padding:1em 1.2em;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    st.header("🔑 " + t["concept"])
    st.markdown(
        f"<b>{t['scalping']}:</b> {t['scalping_explanation']}<br>"
        f"<b>{t['swing_trading']}:</b> {t['swing_trading_explanation']}",
        unsafe_allow_html=True
    )

    st.divider()

    # 对比表格
    st.subheader(t["compare_title"])
    df = pd.DataFrame(
        [t["scalping_row"], t["swing_row"]],
        columns=[
            t["col_strategy"], t["col_time"], t["col_trade_freq"], t["col_target"],
            t["col_risk"], t["col_typical_asset"], t["col_require"]
        ]
    )
    st.dataframe(df, hide_index=True, use_container_width=True)

    # 优缺点卡片（两栏）
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f"#### {t['scalping']} {t['pros_title']}")
        st.markdown("<div class='pros-card'>" + "<br>".join([f"- {p}" for p in t["scalping_pros"]]) + "</div>", unsafe_allow_html=True)
        st.markdown(f"#### {t['scalping']} {t['cons_title']}")
        st.markdown("<div class='cons-card'>" + "<br>".join([f"- {p}" for p in t["scalping_cons"]]) + "</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"#### {t['swing_trading']} {t['pros_title']}")
        st.markdown("<div class='pros-card'>" + "<br>".join([f"- {p}" for p in t["swing_pros"]]) + "</div>", unsafe_allow_html=True)
        st.markdown(f"#### {t['swing_trading']} {t['cons_title']}")
        st.markdown("<div class='cons-card'>" + "<br>".join([f"- {p}" for p in t["swing_cons"]]) + "</div>", unsafe_allow_html=True)

    st.divider()

    st.subheader(t["suitable_title"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**{t['scalping']}:** {t['scalping_people']}")
    with c2:
        st.markdown(f"**{t['swing_trading']}:** {t['swing_people']}")

    st.subheader(t["pitfalls_title"])
    for p in t["pitfalls"]:
        st.markdown(f"- {p}")

    st.divider()

    st.subheader(t["which_style"])
    if "svst_vote" not in st.session_state:
        st.session_state.svst_vote = ""
    vote = st.radio("", [t["choose_scalping"], t["choose_swing"]], horizontal=True)
    if st.button(t["vote"]):
        st.session_state.svst_vote = vote
    if st.session_state.svst_vote:
        st.success(f"{t['your_choice']} {st.session_state.svst_vote}")

# 用法示例
# scalping_vs_swing_trading_page()
