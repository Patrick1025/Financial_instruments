import streamlit as st
import pandas as pd

def arbitrage_page():
    # 语言翻译字典
    translations = {
        "en": {
            "title": "📊 Arbitrage",
            "arbitrage": "🔍 Arbitrage Overview",
            "explanation": (
                "Arbitrage is the practice of simultaneously buying and selling the same asset, or equivalent assets, "
                "in different markets to profit from price differences. It exploits temporary inefficiencies between markets."
            ),
            "concept": "What is Arbitrage?",
            "example_title": "💡 Example Scenario",
            "example": (
                "Suppose Bitcoin is trading at $72,500 on Broker A and $72,800 on Broker B. "
                "You could buy Bitcoin on Broker A and sell on Broker B, making a $300 profit (minus fees)."
            ),
            "calc_title": "📈 Try It Yourself: Arbitrage Calculator",
            "buy_price": "Buy Price (Market A)",
            "sell_price": "Sell Price (Market B)",
            "amount": "Amount (BTC)",
            "fees": "Total Fees",
            "calculate": "Calculate Profit",
            "profit": "Estimated Profit",
            "note": "*For simplicity, assume no slippage. Always factor in fees and execution speed in real trading!*",
            "steps": "How Arbitrage Works",
            "step1": "1. Identify price gaps between two markets.",
            "step2": "2. Buy at the lower-priced market, sell at the higher-priced one.",
            "step3": "3. Account for fees, transfer costs, and timing risks.",
            "step4": "4. Execute quickly before the gap closes.",
            "more": "More Resources",
            "learn_more": "Learn more about arbitrage strategies",
        },
        "zh": {
            "title": "📊 套利",
            "arbitrage": "🔍 套利概览",
            "explanation": (
                "套利是指在不同市场同时买入和卖出同一资产或等价资产，从价格差异中获利。"
                "这种方式利用了市场之间的临时价格失衡。"
            ),
            "concept": "什么是套利？",
            "example_title": "💡 示例场景",
            "example": (
                "假设比特币在经纪商A处价格为72,500美元，在经纪商B为72,800美元。"
                "你可以在A买入，在B卖出，获得300美元利润（扣除手续费）。"
            ),
            "calc_title": "📈 自己试一试：套利计算器",
            "buy_price": "买入价（市场A）",
            "sell_price": "卖出价（市场B）",
            "amount": "数量（BTC）",
            "fees": "总手续费",
            "calculate": "计算利润",
            "profit": "预估利润",
            "note": "*为简化计算，假设无滑点。实际操作请考虑手续费与成交速度风险！*",
            "steps": "套利流程",
            "step1": "1. 发现两个市场的价格差。",
            "step2": "2. 在价格低的市场买入，在价格高的市场卖出。",
            "step3": "3. 考虑手续费、转账成本和时间风险。",
            "step4": "4. 尽快执行，否则套利空间可能消失。",
            "more": "扩展阅读",
            "learn_more": "深入了解套利策略",
        }
    }
    lang = st.session_state.get("language", "en")
    t = translations[lang]

    # 页面宽度美化
    st.markdown("""
    <style>
        .block-container {padding-top: 2rem !important; padding-bottom: 2rem !important;}
        .main .block-container {max-width: 900px;}
        h1, h2, h3 {font-weight:700;}
        .st-emotion-cache-1kyxreq {background: #fafbfc;}
    </style>
    """, unsafe_allow_html=True)

    # 页面标题
    st.title(t["title"])

    # 结构化分块
    st.header(t["arbitrage"])
    st.info(t["explanation"], icon="ℹ️")

    st.header(t["concept"])
    st.write(
        "- " + t["step1"] + "\n"
        "- " + t["step2"] + "\n"
        "- " + t["step3"] + "\n"
        "- " + t["step4"]
    )

    st.header(t["example_title"])
    st.success(t["example"])

    # 套利计算器小工具
    with st.expander(t["calc_title"], expanded=True):
        buy = st.number_input(t["buy_price"], min_value=0.0, value=72500.0, format="%.2f")
        sell = st.number_input(t["sell_price"], min_value=0.0, value=72800.0, format="%.2f")
        amount = st.number_input(t["amount"], min_value=0.0, value=1.0, format="%.4f")
        fees = st.number_input(t["fees"], min_value=0.0, value=20.0, format="%.2f")
        if st.button(t["calculate"]):
            profit = (sell - buy) * amount - fees
            st.metric(label=t["profit"], value=f"${profit:,.2f}")
        st.caption(t["note"])

    # 可以加入市场历史价格变化模拟折线图，提升页面体验
    st.header("📉 Price Gap Demo")
    price_df = pd.DataFrame({
        "Broker A": [72500, 72600, 72580, 72550, 72590],
        "Broker B": [72800, 72790, 72650, 72620, 72700]
    }, index=["10:00", "10:01", "10:02", "10:03", "10:04"])
    st.line_chart(price_df)

    # 进一步阅读/外链
    st.header(t["more"])
    st.markdown(f"- [{t['learn_more']}](https://www.investopedia.com/terms/a/arbitrage.asp)")

# 用法示例
# arbitrage_page()
