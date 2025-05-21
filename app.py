import streamlit as st

# Set the page title
st.title("📊 Financial Calculation Tool")

# Display calculation formula
st.subheader("📐 Calculation Formula")
st.markdown(r"""
The formula to calculate the spread is:

$$\text{Spread} = \text{Ask Price} - \text{Bid Price}$$
""")

# Show calculation example
st.subheader("💡 Calculation Example")
st.markdown(r"""
For example, if the **Bid Price** for EUR/USD is 1.2000 and the **Ask Price** is 1.2005, then:

$$\text{Spread} = 1.2005 - 1.2000 = 0.0005 \quad \text{(5 pips)}$$
""")

# "Try Calculate" button section
st.subheader("🔍 Calculate Spread Cost")
st.write("Enter the **Bid Price** and **Ask Price** below, then enter **Leverage** and **Trade Size**, and click 'Calculate' to see the result!")

# Product selection dropdown
product = st.selectbox(
    "Select Product",
    [
        "Gold (XAUUSD)", "Silver (XAGUSD)", "Oil", "Index", "Fx Major (G10)", "Crypto"
    ]
)

# Market info placeholder
market_info = ""

# Set unit based on selected product and add technical details
if product == "Gold (XAUUSD)":
    unit = "cents"  # e.g., XAUUSD uses cents
    market_info = "Gold (XAUUSD) is highly sensitive to inflation expectations, geopolitical risks, and interest rate decisions by central banks. Gold is often considered a hedge against inflation and financial instability."
elif product == "Silver (XAGUSD)":
    unit = "cents"  # Silver might use cents
    market_info = "Silver (XAGUSD) is influenced by industrial demand, monetary policies, and geopolitical factors. It tends to follow gold prices but with higher volatility."
elif product == "Oil":
    unit = "dollars"  # Oil might use dollars as unit
    market_info = "Oil prices are impacted by supply/demand dynamics, geopolitical events, and economic indicators like OPEC decisions."
elif product == "Index":
    unit = "points"  # Indices usually use points
    market_info = "Indices reflect the performance of a basket of stocks and are impacted by macroeconomic trends, corporate earnings, and market sentiment."
elif product == "Fx Major (G10)":
    # Select a currency pair after selecting Fx Major
    product_pair = st.selectbox(
        "Select Currency Pair",
        ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "USD/CAD", "NZD/USD", "EUR/JPY", "GBP/JPY", "EUR/GBP"]
    )
    unit = "pips"  # Major currency pairs use pips
    if product_pair == "EUR/USD":
        market_info = "EUR/USD is one of the most traded currency pairs. Its price is influenced by the economic performance of the Eurozone and the US, interest rates, and political developments."
    elif product_pair == "GBP/USD":
        market_info = "GBP/USD, or 'Cable', is affected by the UK's economic performance, inflation reports, and Brexit-related developments."
    elif product_pair == "USD/JPY":
        market_info = "USD/JPY is influenced by the US interest rates, Japanese economic indicators, and risk sentiment in global markets."
    # Add additional market info for other pairs if needed
elif product == "Crypto":
    crypto_pair = st.selectbox(
        "Select Cryptocurrency",
        ["BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "LTC/USD"]  # These are the top 5 cryptos
    )
    unit = "cents"  # Cryptocurrencies might use cents
    market_info = "Cryptocurrencies are volatile and influenced by regulatory news, adoption rates, and technological developments."
else:
    unit = "pips"
    market_info = "No specific market info available."

# Display product and unit
st.write(f"Selected Product: **{product}** (Unit: **{unit}**)")

# Display market info in an expandable section
with st.expander(f"📖 Click to Show Market Info for {product}"):
    st.write(f"### 📈 Market Info: {market_info}")

# User input fields with styling
col1, col2 = st.columns(2)

with col1:
    bid_price = st.number_input("Enter **Bid Price**:", min_value=0.0, format="%.4f", step=0.0001)

with col2:
    ask_price = st.number_input("Enter **Ask Price**:", min_value=0.0, format="%.4f", step=0.0001)

# Input for leverage and trade size
leverage = st.number_input("Enter **Leverage**:", min_value=1.0, step=1.0)
trade_size = st.number_input("Enter **Trade Size** (e.g., in units):", min_value=0.0)

# Calculate button
if st.button("🔄 Calculate"):
    if bid_price > 0 and ask_price > 0 and trade_size > 0:
        spread = ask_price - bid_price
        st.markdown(f"### 📊 The Spread: **{spread:.4f}** (or **{spread * 10000:.0f} {unit}**)")

        # Calculate cost based on leverage and trade size
        cost = spread * trade_size / leverage
        st.markdown(f"### 💰 The cost of the spread is: **{cost:.2f}** (based on leverage and trade size)")
    else:
        st.warning("Please enter valid values for **Bid Price**, **Ask Price**, **Leverage**, and **Trade Size**.")

# Add some space between content
st.markdown("<br>", unsafe_allow_html=True)

# Display some additional notes or information if needed
st.markdown("""
### 📌 Notes:
- **Leverage** affects the spread cost, amplifying both potential profits and risks.
- The **Spread** can vary depending on market conditions and asset volatility.
""")
