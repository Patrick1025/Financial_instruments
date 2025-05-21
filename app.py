import streamlit as st

# Language switcher
if 'language' not in st.session_state:
    st.session_state.language = 'en'  # Default language is English

# Function to toggle language
def toggle_language():
    if st.session_state.language == 'en':
        st.session_state.language = 'zh'
    else:
        st.session_state.language = 'en'

# Add a language toggle button
st.button("Switch to 中文" if st.session_state.language == 'en' else "Switch to English", on_click=toggle_language)

# Language translations
translations = {
    "en": {
        "title": "📊 Financial Calculation Tool",
        "calculation_formula": "📐 Calculation Formula",
        "calculation_example": "💡 Calculation Example",
        "try_calculate": "🔍 Calculate Spread Cost",
        "enter_bid_ask": "Enter the **Bid Price** and **Ask Price** below, then enter **Leverage** and **Trade Size**, and click 'Calculate' to see the result!",
        "selected_product": "Selected Product: ",
        "market_info": "📖 Click to Show Market Info for ",
        "notes": "### 📌 Notes:\n- **Leverage** affects the spread cost, amplifying both potential profits and risks.\n- The **Spread** can vary depending on market conditions and asset volatility."
    },
    "zh": {
        "title": "📊 财务计算工具",
        "calculation_formula": "📐 计算公式",
        "calculation_example": "💡 计算示例",
        "try_calculate": "🔍 计算点差成本",
        "enter_bid_ask": "输入 **买入价** 和 **卖出价**，然后输入 **杠杆** 和 **交易规模**，点击“计算”以查看结果！",
        "selected_product": "选择的产品: ",
        "market_info": "📖 点击查看市场信息: ",
        "notes": "### 📌 注意事项:\n- **杠杆** 会影响点差成本，放大潜在利润和风险。\n- **点差** 会根据市场条件和资产波动性而变化。"
    }
}

# Set the page title based on selected language
st.title(translations[st.session_state.language]["title"])

# Display calculation formula
st.subheader(translations[st.session_state.language]["calculation_formula"])
st.markdown(r"""
The formula to calculate the spread is:

$$\text{Spread} = \text{Ask Price} - \text{Bid Price}$$
""")

# Show calculation example
st.subheader(translations[st.session_state.language]["calculation_example"])
st.markdown(r"""
For example, if the **Bid Price** for EUR/USD is 1.2000 and the **Ask Price** is 1.2005, then:

$$\text{Spread} = 1.2005 - 1.2000 = 0.0005 \quad \text{(5 pips)}$$
""")

# "Try Calculate" button section
st.subheader(translations[st.session_state.language]["try_calculate"])
st.write(translations[st.session_state.language]["enter_bid_ask"])

# Product selection dropdown
product = st.selectbox(
    "Select Product" if st.session_state.language == 'en' else "选择产品",
    [
        "Gold (XAUUSD)", "Silver (XAGUSD)", "Oil", "Index", "Fx Major (G10)", "Crypto"
    ]
)

# Market info placeholder
market_info = ""

# Set unit based on selected product and add technical details
if product == "Gold (XAUUSD)":
    unit = "cents"  # e.g., XAUUSD uses cents
    market_info = "Gold (XAUUSD) is highly sensitive to inflation expectations, geopolitical risks, and interest rate decisions by central banks. Gold is often considered a hedge against inflation and financial instability." if st.session_state.language == 'en' else "黄金 (XAUUSD) 对通胀预期、地缘政治风险和中央银行的利率决策高度敏感。黄金通常被视为对抗通胀和金融不稳定的对冲工具。"
elif product == "Silver (XAGUSD)":
    unit = "cents"  # Silver might use cents
    market_info = "Silver (XAGUSD) is influenced by industrial demand, monetary policies, and geopolitical factors. It tends to follow gold prices but with higher volatility." if st.session_state.language == 'en' else "白银 (XAGUSD) 受工业需求、货币政策和地缘政治因素的影响。它通常跟随黄金价格波动，但波动性更大。"
elif product == "Oil":
    unit = "dollars"  # Oil might use dollars as unit
    market_info = "Oil prices are impacted by supply/demand dynamics, geopolitical events, and economic indicators like OPEC decisions." if st.session_state.language == 'en' else "石油价格受供需动态、地缘政治事件和经济指标（如欧佩克决策）影响。"
elif product == "Index":
    unit = "points"  # Indices usually use points
    market_info = "Indices reflect the performance of a basket of stocks and are impacted by macroeconomic trends, corporate earnings, and market sentiment." if st.session_state.language == 'en' else "指数反映了一篮子股票的表现，受宏观经济趋势、公司盈利和市场情绪的影响。"
elif product == "Fx Major (G10)":
    # Select a currency pair after selecting Fx Major
    product_pair = st.selectbox(
        "Select Currency Pair" if st.session_state.language == 'en' else "选择货币对",
        ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "USD/CAD", "NZD/USD", "EUR/JPY", "GBP/JPY", "EUR/GBP"]
    )
    unit = "pips"  # Major currency pairs use pips
    if product_pair == "EUR/USD":
        market_info = "EUR/USD is one of the most traded currency pairs. Its price is influenced by the economic performance of the Eurozone and the US, interest rates, and political developments." if st.session_state.language == 'en' else "EUR/USD 是最常交易的货币对之一，其价格受欧元区和美国的经济表现、利率和政治发展的影响。"
    elif product_pair == "GBP/USD":
        market_info = "GBP/USD, or 'Cable', is affected by the UK's economic performance, inflation reports, and Brexit-related developments." if st.session_state.language == 'en' else "GBP/USD，或称“Cable”，受英国经济表现、通胀报告和与英国脱欧相关的因素影响。"
    elif product_pair == "USD/JPY":
        market_info = "USD/JPY is influenced by the US interest rates, Japanese economic indicators, and risk sentiment in global markets." if st.session_state.language == 'en' else "USD/JPY 受美国利率、日本经济指标和全球市场风险情绪的影响。"
    # Add additional market info for other pairs if needed
elif product == "Crypto":
    crypto_pair = st.selectbox(
        "Select Cryptocurrency" if st.session_state.language == 'en' else "选择加密货币",
        ["BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "LTC/USD"]  # These are the top 5 cryptos
    )
    unit = "cents"  # Cryptocurrencies might use cents
    market_info = "Cryptocurrencies are volatile and influenced by regulatory news, adoption rates, and technological developments." if st.session_state.language == 'en' else "加密货币波动性大，受监管新闻、采纳率和技术发展等因素影响。"
else:
    unit = "pips"
    market_info = "No specific market info available." if st.session_state.language == 'en' else "没有具体的市场信息。"

# Display product and unit
st.write(f"{translations[st.session_state.language]['selected_product']} **{product}** (Unit: **{unit}**)")

# Display market info in an expandable section
with st.expander(f"{translations[st.session_state.language]['market_info']} {product}"):
    st.write(f"### 📈 {market_info}")

# User input fields with styling
col1, col2 = st.columns(2)

with col1:
    bid_price = st.number_input("Enter **Bid Price**:" if st.session_state.language == 'en' else "输入 **买入价**:", min_value=0.0, format="%.4f", step=0.0001)

with col2:
    ask_price = st.number_input("Enter **Ask Price**:" if st.session_state.language == 'en' else "输入 **卖出价**:", min_value=0.0, format="%.4f", step=0.0001)

# Input for leverage and trade size
leverage = st.number_input("Enter **Leverage**:" if st.session_state.language == 'en' else "输入 **杠杆**:", min_value=1.0, step=1.0)
trade_size = st.number_input("Enter **Trade Size** (e.g., in units):" if st.session_state.language == 'en' else "输入 **交易规模** (例如，单位):", min_value=0.0)

# Calculate button
if st.button("🔄 Calculate" if st.session_state.language == 'en' else "🔄 计算"):
    if bid_price > 0 and ask_price > 0 and trade_size > 0:
        spread = ask_price - bid_price
        st.markdown(f"### 📊 The Spread: **{spread:.4f}** (or **{spread * 10000:.0f} {unit}**)" if st.session_state.language == 'en' else f"### 📊 点差: **{spread:.4f}** (或 **{spread * 10000:.0f} {unit}**)")

        # Calculate cost based on leverage and trade size
        cost = spread * trade_size / leverage
        st.markdown(f"### 💰 The cost of the spread is: **{cost:.2f}** (based on leverage and trade size)" if st.session_state.language == 'en' else f"### 💰 点差成本为: **{cost:.2f}** (根据杠杆和交易规模计算)")
    else:
        st.warning("Please enter valid values for **Bid Price**, **Ask Price**, **Leverage**, and **Trade Size**." if st.session_state.language == 'en' else "请输入有效的 **买入价**、**卖出价**、**杠杆** 和 **交易规模**。")

# Display additional notes
st.markdown(translations[st.session_state.language]["notes"])
