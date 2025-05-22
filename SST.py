import streamlit as st

def scalping_vs_swing_trading_page():
    # 语言翻译字典
    translations = {
        "en": {
            "title": "📊 Scalping vs. Swing Trading",
            "scalping": "🔍 Scalping",
            "swing_trading": "🔍 Swing Trading",
            "scalping_explanation": "Scalping is a trading strategy that involves making numerous small trades to capture minor price changes over short periods. The goal is to take advantage of small market movements and accumulate profits quickly.",
            "swing_trading_explanation": "Swing trading is a longer-term trading strategy where traders hold positions for several days to capitalize on expected upward or downward market trends.",
            "scalping_vs_swing_trading": "### 💡 Key Differences\n- **Scalping**: Quick trades with small profits.\n- **Swing Trading**: Holds positions for days or weeks to capture larger price movements.",
            "example": "### 💡 Example\n\nFor example, a scalper might trade EUR/USD several times in a day, aiming for small profit targets, while a swing trader may hold EUR/USD for several days, waiting for the price to move significantly in one direction."
        },
        "zh": {
            "title": "📊 剥头皮交易与波段交易",
            "scalping": "🔍 剥头皮交易",
            "swing_trading": "🔍 波段交易",
            "scalping_explanation": "剥头皮交易是一种交易策略，涉及在短时间内进行大量小额交易，以捕捉小幅价格波动。目标是通过快速获取小幅市场波动来积累利润。",
            "swing_trading_explanation": "波段交易是一种较长期的交易策略，交易者通常持有仓位几天，以抓住预期的市场上涨或下跌趋势。",
            "scalping_vs_swing_trading": "### 💡 主要区别\n- **剥头皮交易**: 快速交易，获取小额利润。\n- **波段交易**: 持仓数天或数周，抓住较大的价格波动。",
            "example": "### 💡 示例\n\n例如，剥头皮交易者可能在一天内多次交易EUR/USD，目标是小幅盈利，而波段交易者可能会持有EUR/USD几天，等待价格朝某个方向大幅波动。"
        }
    }

    # 设置页面标题
    st.title(translations[st.session_state.language]["title"])

    # Scalping 说明
    st.subheader(translations[st.session_state.language]["scalping"])
    st.write(translations[st.session_state.language]["scalping_explanation"])

    # Swing Trading 说明
    st.subheader(translations[st.session_state.language]["swing_trading"])
    st.write(translations[st.session_state.language]["swing_trading_explanation"])

    # 比较两者
    st.subheader(translations[st.session_state.language]["scalping_vs_swing_trading"])
    st.write(translations[st.session_state.language]["scalping_vs_swing_trading"])

    # 示例
    st.markdown(translations[st.session_state.language]["example"])

    # 页面结束
    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
