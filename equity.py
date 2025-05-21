import streamlit as st
import pandas as pd

def equity_page():
    translations = {
        "en": {
            "title": "📊 Financial Calculation Tool",
            "calculation_formula": "📐 Calculation Formula",
            "spread": "🔍 Calculate Spread Cost",
            "equity": "🔍 Calculate Equity",
            "margin": "🔍 Calculate Margin",
            "concept": "Concept",
            "value": "Value",
            "unit": "Unit",
            "enter_bid_ask": "Enter the **Bid Price** and **Ask Price** below, then enter **Leverage** and **Trade Size**, and click 'Calculate' to see the result!",
            "selected_product": "Selected Product: ",
            "market_info": "📖 Click to Show Market Info for ",
            "notes": "### 📌 Notes:\n- **Leverage** affects the equity, amplifying both potential profits and risks.\n- The **Equity** can vary depending on market conditions and asset volatility.",
            "contract_size": "Contract Size",
            "decimal_places": "Decimal Places",
            "unit_intro": "Unit refers to the standard measurement of each trading contract.",
            "contract_intro": "Contract Size defines the amount of the asset represented by each contract. ",
            "decimal_intro": "Decimal Places refer to the number of decimal points used in pricing. Different products have different decimal places.",
            "select_product": "Please select the product you want to see its unit, contract size, and decimal places:",
        },
        "zh": {
            "title": "📊 财务计算工具",
            "calculation_formula": "📐 计算公式",
            "concept": "概念",
            "value": "值",
            "unit": "单位",
            "spread": "🔍 计算点差成本",
            "equity": "🔍 计算权益",
            "margin": "🔍 计算保证金",
            "enter_bid_ask": "输入 **买入价** 和 **卖出价**，然后输入 **杠杆** 和 **交易规模**，点击“计算”以查看结果！",
            "selected_product": "选择的产品: ",
            "market_info": "📖 点击查看市场信息: ",
            "notes": "### 📌 注意事项:\n- **杠杆** 会影响权益，放大潜在利润和风险。\n- **权益** 会根据市场条件和资产波动性而变化。",
            "contract_size": "合约大小",
            "decimal_places": "小数点位数",
            "unit_intro": "单位（Unit）指每个交易合约的标准计量单位。例如，在外汇交易中，1手通常等于100,000单位的基础货币。",
            "contract_intro": "合约大小（Contract Size）定义每个合约代表的资产数量。例如，XAU/USD（黄金）的合约大小通常是100盎司。",
            "decimal_intro": "小数点位数（DP）指价格中保留的小数位数。不同的产品有不同的小数点位数。",
            "select_product": "请选择你想查看其单位、合约大小和小数点位数的产品：",
        }
    }

    # Set the page title based on selected language
    st.title(translations[st.session_state.language]["title"])

    # Products data dictionary with the full list of 19 products
    products = {
        "Gold (XAUUSD)": {"unit": "Ounces", "contract_size": "100 Ounces", "decimal_places": 2},
        "Silver (XAGUSD)": {"unit": "Ounces", "contract_size": "100 Ounces", "decimal_places": 2},
        "Oil (WTI)": {"unit": "Barrels", "contract_size": "1000 Barrels", "decimal_places": 2},
        "Index (S&P 500)": {"unit": "Points", "contract_size": "$50 per point", "decimal_places": 2},
        "EUR/USD": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "GBP/USD": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "USD/JPY": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 2},
        "AUD/USD": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "USD/CHF": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "USD/CAD": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "NZD/USD": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 4},
        "EUR/JPY": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 2},
        "GBP/JPY": {"unit": "Units of Base Currency", "contract_size": "100,000 Units", "decimal_places": 2},
        "BTC/USD": {"unit": "Coins", "contract_size": "1 Coin", "decimal_places": 8},
        "ETH/USD": {"unit": "Coins", "contract_size": "1 Coin", "decimal_places": 8},
        "BNB/USD": {"unit": "Coins", "contract_size": "1 Coin", "decimal_places": 8},
        "XRP/USD": {"unit": "Coins", "contract_size": "1 Coin", "decimal_places": 8},
        "LTC/USD": {"unit": "Coins", "contract_size": "1 Coin", "decimal_places": 8}
    }

    # Product selection
    product_selection = st.selectbox(
        translations[st.session_state.language]["select_product"],
        list(products.keys())
    )

    # Update dropdown values when product changes
    selected_product = products[product_selection]
    st.session_state.selected_unit = selected_product["unit"]
    st.session_state.selected_contract_size = selected_product["contract_size"]
    st.session_state.selected_decimal_places = selected_product["decimal_places"]

    # Helper function to display static rows
    def display_static_row(label, value, intro_text):
        col1, col2, col3 = st.columns([2, 6, 2])
        with col1:
            st.write(f"**{label}**")
        with col2:
            st.write(f"{intro_text}")
        with col3:
            st.write(f"**{value}**")

    # Display static rows
    display_static_row(
        translations[st.session_state.language]["unit"],
        st.session_state.selected_unit,
        translations[st.session_state.language]["unit_intro"]
    )
    display_static_row(
        translations[st.session_state.language]["contract_size"],
        st.session_state.selected_contract_size,
        translations[st.session_state.language]["contract_intro"]
    )
    display_static_row(
        translations[st.session_state.language]["decimal_places"],
        st.session_state.selected_decimal_places,
        translations[st.session_state.language]["decimal_intro"]
    )

    # Equity calculation logic
    bid_price = st.number_input(f"Enter **Bid Price** for {product_selection}:", min_value=0.0)
    ask_price = st.number_input(f"Enter **Ask Price** for {product_selection}:", min_value=0.0)
    leverage = st.number_input("Enter **Leverage**:", min_value=1.0, step=1.0)
    trade_size = st.number_input(f"Enter **Trade Size** (in {st.session_state.selected_unit}):", min_value=0.0)

    if st.button("🔄 Calculate Equity"):
        if bid_price > 0 and ask_price > 0 and trade_size > 0:
            equity = (ask_price * trade_size) / leverage
            st.markdown(f"### 📊 The Equity: **{equity:.4f}**")

            cost = equity * leverage
            st.markdown(f"### 💰 The total cost of the equity is: **{cost:.4f}**")
        else:
            st.warning("Please enter valid values for **Bid Price**, **Ask Price**, **Leverage**, and **Trade Size**.")

    st.markdown(translations[st.session_state.language]["notes"])

    if st.button("Export Results to CSV"):
        result = {
            "Product": product_selection,
            "Bid Price": bid_price,
            "Ask Price": ask_price,
            "Leverage": leverage,
            "Trade Size": trade_size,
            "Equity": equity if 'equity' in locals() else None,
            "Cost": cost if 'cost' in locals() else None
        }

        df = pd.DataFrame([result])
        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="calculation_results.csv",
            mime="text/csv"
        )
