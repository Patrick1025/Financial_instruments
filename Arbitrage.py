import streamlit as st

def arbitrage_page():
    # 语言翻译字典
    translations = {
        "en": {
            "title": "📊 Arbitrage",
            "concept": "Concept",
            "description": "Description",
            "arbitrage": "🔍 Arbitrage",
            "explanation": "Arbitrage refers to the practice of simultaneously buying and selling the same asset or equivalent assets in different markets to profit from price differences. It exploits temporary price inefficiencies between markets.",
            "example": "### 💡 Example\n\nFor example, if Bitcoin is trading at $72500 on Broker A and $72800 on Broker B, you could buy Bitcoin on Broker A and sell it on Broker B, making a $300 profit (minus transaction fees).",
        },
        "zh": {
            "title": "📊 套利",
            "concept": "概念",
            "description": "描述",
            "arbitrage": "🔍 套利",
            "explanation": "套利指的是在不同市场同时买入和卖出相同或等价资产，以从价格差异中获利。这种做法利用了市场之间的暂时价格失衡。",
            "example": "### 💡 示例\n\n例如，如果比特币在经纪商A处的价格为72500美元，而在经纪商B处的价格为72800美元，你可以在经纪商A买入比特币，同时在经纪商B卖出，获得300美元的利润（扣除交易费用）。",
        }
    }

    # 设置页面标题
    st.title(translations[st.session_state.language]["title"])

    # 页面内容
    st.subheader(translations[st.session_state.language]["arbitrage"])
    st.write(translations[st.session_state.language]["explanation"])

    st.markdown(translations[st.session_state.language]["example"])

    # 其他说明
    st.subheader(translations[st.session_state.language]["concept"])
    st.write(translations[st.session_state.language]["description"])

    # 页面结束
    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
