import streamlit as st

def pitfalls_page():
    # 语言翻译字典
    translations = {
        "en": {
            "title": "📊 Common Pitfalls in Trading",
            "pitfalls": "🔍 Common Pitfalls",
            "explanation": "Trading comes with risks and common mistakes. Understanding these pitfalls can help you avoid losses and improve your trading strategy.",
            "pitfall_1": "### 💡 Pitfall 1: Overtrading\nOvertrading occurs when traders make too many trades, often out of impulse, which leads to unnecessary losses.",
            "pitfall_2": "### 💡 Pitfall 2: Lack of Risk Management\nNot using stop-loss orders or failing to calculate risk can lead to significant losses. Always manage risk by setting stop-loss levels and understanding position sizing.",
            "pitfall_3": "### 💡 Pitfall 3: Ignoring Market Conditions\nIgnoring broader market trends or economic news can result in missed opportunities or unfavorable trades.",
            "pitfall_4": "### 💡 Pitfall 4: Chasing Losses\nAfter a loss, traders may try to recoup their money by taking riskier trades. This is known as 'chasing losses,' and it often leads to more losses."
        },
        "zh": {
            "title": "📊 交易中的常见陷阱",
            "pitfalls": "🔍 常见陷阱",
            "explanation": "交易伴随着风险和常见错误。了解这些陷阱可以帮助你避免损失并改善你的交易策略。",
            "pitfall_1": "### 💡 陷阱 1: 过度交易\n过度交易是指交易者做出过多的交易，通常是出于冲动，导致不必要的损失。",
            "pitfall_2": "### 💡 陷阱 2: 缺乏风险管理\n不使用止损单或未能计算风险可能导致重大损失。始终通过设置止损位和了解仓位大小来管理风险。",
            "pitfall_3": "### 💡 陷阱 3: 忽视市场情况\n忽视更广泛的市场趋势或经济新闻可能导致错失机会或做出不利交易。",
            "pitfall_4": "### 💡 陷阱 4: 追逐损失\n在遭遇损失后，交易者可能会试图通过进行更高风险的交易来弥补损失。这种行为被称为'追逐损失'，往往导致更多损失。"
        }
    }

    # 设置页面标题
    st.title(translations[st.session_state.language]["title"])

    # 陷阱说明
    st.write(translations[st.session_state.language]["explanation"])

    # 陷阱 1
    st.subheader(translations[st.session_state.language]["pitfall_1"])

    # 陷阱 2
    st.subheader(translations[st.session_state.language]["pitfall_2"])

    # 陷阱 3
    st.subheader(translations[st.session_state.language]["pitfall_3"])

    # 陷阱 4
    st.subheader(translations[st.session_state.language]["pitfall_4"])

    # 页面结束
    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
