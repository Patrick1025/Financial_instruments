import streamlit as st

def nop_page():
    translations = {
        "en": {
            "title": "📈 Net Open Position (NOP) Tool",
            "concept": "Concept",
            "concept_text": (
                "Net Open Position (NOP) is the sum of all open long positions minus all open short positions for a given instrument. "
                "It reflects your net exposure and is key for risk management and compliance."
            ),
            "formula": "NOP = Σ(Long Positions) - Σ(Short Positions)",
            "calculator": "NOP Calculator",
            "longs": "Total Long Positions (units)",
            "shorts": "Total Short Positions (units)",
            "calculate": "Calculate",
            "result": "Net Open Position",
            "note": "*A positive NOP means net long, negative means net short, zero means fully hedged.*",
            "examples": "Examples",
            "ex1": "Long: 200,000 EUR/USD, Short: 150,000 EUR/USD → NOP = 50,000 EUR/USD (Net Long)",
            "ex2": "Long: 1 BTC, Short: 1.5 BTC → NOP = -0.5 BTC (Net Short)",
        },
        "zh": {
            "title": "📈 净持仓（NOP）工具",
            "concept": "概念",
            "concept_text": (
                "净持仓（NOP）是所有多头持仓总和减去所有空头持仓总和，反映账户整体风险暴露。常用于风控与监管合规。"
            ),
            "formula": "净持仓 = 多头持仓总和 − 空头持仓总和",
            "calculator": "净持仓计算器",
            "longs": "多头持仓总和（单位）",
            "shorts": "空头持仓总和（单位）",
            "calculate": "计算",
            "result": "净持仓",
            "note": "*NOP为正说明净多头，为负说明净空头，等于零表示完全对冲*",
            "examples": "示例",
            "ex1": "多头：20万EUR/USD，空头：15万EUR/USD → 净持仓=5万EUR/USD（净多头）",
            "ex2": "多头：1 BTC，空头：1.5 BTC → 净持仓=-0.5 BTC（净空头）",
        }
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    st.markdown("""
        <style>
        .block-container {max-width: 700px; padding-top: 2rem;}
        .metric-value {font-size: 2em !important;}
        .st-emotion-cache-1kyxreq {background: #f9fafb;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    # 概念与公式
    with st.expander("💡 " + t["concept"], expanded=False):
        st.markdown(f"{t['concept_text']}")
        st.code(t["formula"], language="markdown")

    st.divider()
    st.header("🧮 " + t["calculator"])

    # 输入区（双栏，风格更现代）
    cols = st.columns(2)
    with cols[0]:
        longs = st.number_input(t["longs"], min_value=0.0, value=100000.0, step=100.0)
    with cols[1]:
        shorts = st.number_input(t["shorts"], min_value=0.0, value=50000.0, step=100.0)

    calc = st.button("🟦 " + t["calculate"])
    nop = None
    if calc:
        nop = longs - shorts

    if nop is not None:
        colr, _ = st.columns([1,3])
        # 结果metric卡片，正负一目了然
        nop_str = f"{nop:,.2f}"
        nop_style = "🟢" if nop > 0 else ("🔴" if nop < 0 else "⚪️")
        colr.metric(label=f"{nop_style} {t['result']}", value=nop_str)

    st.caption(t["note"])

    # 示例区
    with st.expander("📖 " + t["examples"], expanded=False):
        st.markdown(f"- {t['ex1']}")
        st.markdown(f"- {t['ex2']}")

# 用法示例
# nop_page()
