import streamlit as st

def pitfalls_page():
    translations = {
        "en": {
            "title": "📊 Common Pitfalls in Trading",
            "concept_title": "What is a Pitfall?",
            "concept_text": (
                "A trading pitfall is a common trap or mistake that traders—especially beginners—tend to fall into. "
                "They often seem harmless but can lead to significant losses or missed opportunities. "
                "Recognizing these pitfalls is crucial for building a robust trading strategy and risk management system."
            ),
            "scenarios_title": "Common Situations Where Pitfalls Arise",
            "scenarios": [
                "⏳ **Using Pending Orders:** Many traders set pending (limit/stop) orders and then ignore important news or rapid market moves, causing unexpected slippage or missing out.",
                "📈 **Trading with High Leverage:** Leverage amplifies both gains and losses—misjudging risk or not using stop-losses can quickly wipe out an account.",
                "🌙 **Overnight Positions:** Holding trades overnight can expose you to swap costs, gaps, and major news, which are often underestimated.",
                "🔔 **Ignoring Margin Requirements:** Not checking required margin or margin level can result in forced liquidations during volatile moves.",
                "🛑 **Not Adjusting After News Events:** Keeping the same position sizing or stop-loss before/after major economic releases increases risk.",
            ],
            "pitfalls": "🔍 Common Pitfalls",
            "explanation": "Understanding the following pitfalls can help you avoid losses and improve your trading.",
            "pitfall_1_title": "💡 Pitfall 1: Overtrading",
            "pitfall_1_body": "Overtrading happens when traders make too many trades, often impulsively, which leads to unnecessary losses and increased fees.",
            "pitfall_1_advice": "✋ Limit your trades. Stick to your plan, avoid impulsive actions, and set a daily/weekly trade cap.",
            "pitfall_2_title": "💡 Pitfall 2: Lack of Risk Management",
            "pitfall_2_body": "Not using stop-loss orders or failing to calculate risk can lead to significant losses.",
            "pitfall_2_advice": "🔒 Always set a stop-loss and size your positions based on account size and risk tolerance.",
            "pitfall_3_title": "💡 Pitfall 3: Ignoring Market Conditions",
            "pitfall_3_body": "Ignoring broader market trends or economic news can result in missed opportunities or unfavorable trades.",
            "pitfall_3_advice": "📈 Check the economic calendar and major news before trading. Know the market context.",
            "pitfall_4_title": "💡 Pitfall 4: Chasing Losses",
            "pitfall_4_body": "After a loss, traders may try to recoup their money by taking riskier trades. This is known as 'chasing losses,' and it often leads to more losses.",
            "pitfall_4_advice": "🧊 Take a break after a loss. Never revenge trade. Reset your mindset before re-entering the market.",
            "user_pitfall": "Add Your Own Pitfall or Lesson Learned",
            "user_input_placeholder": "E.g. Don't trade when tired or emotional...",
            "submit": "Submit",
            "your_lesson": "Your Shared Lessons",
        },
        "zh": {
            "title": "📊 交易中的常见陷阱",
            "concept_title": "什么是“陷阱”或“误区”？",
            "concept_text": (
                "所谓交易‘陷阱’，就是新手甚至老手经常会踩的坑或容易犯的错。这些问题乍看无害，实则可能导致重大亏损或错失机会。"
                "识别这些陷阱，是完善交易系统和风控的第一步。"
            ),
            "scenarios_title": "常见触发陷阱的场景举例",
            "scenarios": [
                "⏳ **挂单（Pending Order）失控：** 很多人设置挂单（限价单/止损单）后不关注行情，遇到突发新闻导致滑点、挂单误触发，或错失最佳点位。",
                "📈 **高杠杆交易：** 杠杆既能放大利润也会放大亏损，未控制风险或未设置止损时，资金极易爆仓。",
                "🌙 **隔夜持仓风险：** 隔夜持仓常被忽视掉的有隔夜费、跳空、重大新闻，这些经常导致意外损失。",
                "🔔 **忽略保证金要求：** 未实时关注保证金/仓位比，行情波动时容易被强平。",
                "🛑 **大消息前后不调整策略：** 重大数据或政策公布时，若不调整仓位/止损，风险激增。",
            ],
            "pitfalls": "🔍 常见陷阱",
            "explanation": "理解下面这些陷阱，有助于减少损失、提升交易能力。",
            "pitfall_1_title": "💡 陷阱1：过度交易",
            "pitfall_1_body": "过度交易是指交易者频繁下单，容易导致手续费升高和无谓亏损，常因冲动或过度自信。",
            "pitfall_1_advice": "✋ 控制出手频率，严格按计划执行，每天/每周设置交易上限，避免冲动下单。",
            "pitfall_2_title": "💡 陷阱2：缺乏风险管理",
            "pitfall_2_body": "不设止损或未计算风险敞口，极易造成大额亏损。",
            "pitfall_2_advice": "🔒 每单都要设置止损，仓位比例严格与账户规模和风险承受力挂钩。",
            "pitfall_3_title": "💡 陷阱3：忽视市场环境",
            "pitfall_3_body": "忽视市场大势或宏观数据，容易踏错节奏或错过最佳机会。",
            "pitfall_3_advice": "📈 每次下单前，务必浏览重要财经日历与主流走势，搞清楚当前大盘状态。",
            "pitfall_4_title": "💡 陷阱4：追单/追损",
            "pitfall_4_body": "在发生亏损后，为挽回损失而仓促加仓或扩大风险敞口，这种‘追单’常导致更大损失。",
            "pitfall_4_advice": "🧊 亏损后要及时冷静复盘，不要带情绪继续加仓，强行扳回。",
            "user_pitfall": "补充你自己的交易教训或误区",
            "user_input_placeholder": "例如：情绪不稳定时绝不下单...",
            "submit": "提交",
            "your_lesson": "你补充的教训",
        }
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 800px; padding-top:2rem;}
        .st-emotion-cache-1kyxreq {background: #f8fafc;}
        .pitfall-card {background:#f6faff;border-radius:1.1em;padding:1em 1.3em 1em 1.3em;box-shadow:0 2px 8px #eef2f7;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    # 概念区
    st.markdown(f"#### ❓ {t['concept_title']}")
    st.info(t["concept_text"], icon="ℹ️")

    # 触发场景举例
    st.markdown(f"#### ⚠️ {t['scenarios_title']}")
    for scenario in t["scenarios"]:
        st.markdown(f"- {scenario}")

    st.divider()
    st.markdown(f"##### {t['explanation']}")

    # Pitfall 列表
    pitfalls = [
        {"title": t["pitfall_1_title"], "body": t["pitfall_1_body"], "advice": t["pitfall_1_advice"]},
        {"title": t["pitfall_2_title"], "body": t["pitfall_2_body"], "advice": t["pitfall_2_advice"]},
        {"title": t["pitfall_3_title"], "body": t["pitfall_3_body"], "advice": t["pitfall_3_advice"]},
        {"title": t["pitfall_4_title"], "body": t["pitfall_4_body"], "advice": t["pitfall_4_advice"]},
    ]

    for p in pitfalls:
        with st.expander(p["title"], expanded=False):
            st.markdown(f"<div class='pitfall-card'>{p['body']}<br><br><b>{p['advice']}</b></div>", unsafe_allow_html=True)

    st.divider()

    # 用户补充区
    st.subheader("📝 " + t["user_pitfall"])
    if "user_pitfalls" not in st.session_state:
        st.session_state.user_pitfalls = []
    pitfall_input = st.text_input("", placeholder=t["user_input_placeholder"])
    if st.button(t["submit"]):
        if pitfall_input.strip():
            st.session_state.user_pitfalls.append(pitfall_input.strip())
            st.success("✅ Added!")

    if st.session_state.user_pitfalls:
        with st.expander("📒 " + t["your_lesson"], expanded=False):
            for idx, u in enumerate(st.session_state.user_pitfalls, 1):
                st.markdown(f"{idx}. {u}")

# 用法示例
# pitfalls_page()
