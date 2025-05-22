import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def spread_page():
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
        "notes": "### 📌 Notes:\n- **Leverage** affects the spread cost, amplifying both potential profits and risks.\n- The **Spread** can vary depending on market conditions and asset volatility.",
        "contract_size": "Contract Size",
        "decimal_places": "Decimal Places",
        "unit_intro": "Unit refers to the standard measurement of each trading contract.",
        "contract_intro": "Contract Size defines the amount of the asset represented by each contract.",
        "decimal_intro": "Decimal Places refer to the number of decimal points used in pricing. Different products have different decimal places.",
        "select_product": "Please select the product you want to see its unit, contract size, and decimal places:",
        "pips_vs_points": "### 📌 Pips vs Points\n\n- **Pips** (Percentage in Points) is the smallest price movement in most **forex currency pairs**, typically **0.0001**.\n- In **JPY pairs**, a pip is defined as **0.01** (two decimal places).\n- **Points** refer to price changes in **stocks**, **commodities**, and **futures** markets, usually representing a **whole unit** price change.",
        "spread_calculation": "### 📌 Spread Calculation Formula\n\nThe formula to calculate the spread is:\n\n$$\text{Spread} = \text{Ask Price in pips} - \text{Bid Price in pips}$$",
        "calculation_example": "### 💡 Calculation Example\n\nFor example, if the **Bid Price** for EUR/USD is 1.2000 and the **Ask Price** is 1.2005, then:"
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
        "notes": "### 📌 注意事项:\n- **杠杆** 会影响点差成本，放大潜在利润和风险。\n- **点差** 会根据市场条件和资产波动性而变化。",
        "contract_size": "合约大小",
        "decimal_places": "小数点位数",
        "unit_intro": "单位（Unit）指每个交易合约的标准计量单位。例如，在外汇交易中，1手通常等于100,000单位的基础货币。",
        "contract_intro": "合约大小（Contract Size）定义每个合约代表的资产数量。例如，XAU/USD（黄金）的合约大小通常是100盎司。",
        "decimal_intro": "小数点位数（DP）指价格中保留的小数位数。不同的产品有不同的小数点位数。",
        "select_product": "请选择你想查看其单位、合约大小和小数点位数的产品：",
        "pips_vs_points": "### 📌 Pips 与 Points\n\n- **Pips**（Percentage in Points）是大多数 **外汇货币对** 的最小价格变动，通常为 **0.0001**。\n- 在 **JPY 货币对** 中，1个 pip 定义为 **0.01**（两位小数）。\n- **Points** 用于 **股票**、**商品** 和 **期货** 市场，通常表示 **一个整体单位** 的价格变动。",
        "spread_calculation": "### 📌 点差计算公式\n\n计算点差的公式是：\n\n$$\text{Spread} = \text{买入价（Bid Price）以pips为单位} - \text{卖出价（Ask Price）以pips为单位}$$",
        "calculation_example": "### 💡 计算示例\n\n例如，如果 **EUR/USD** 的 **买入价** 为 1.2000，**卖出价** 为 1.2005，则："
    }
}

    # Set the page title based on selected language
    st.title(translations[st.session_state.language]["title"])

    # Products data dictionary with the full list of 19 products
    products = {
        "Gold (XAUUSD)": {"unit": "Ounces", "contract_size": "100 Ounces", "decimal_places": 2},
        "Silver (XAGUSD)": {"unit": "Ounces", "contract_size": "1000 Ounces", "decimal_places": 3},
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



    # Initialize session state variables for dropdown selections if they don't exist
    st.session_state.selected_unit = "Units"
    st.session_state.selected_contract_size = "Contract size"
    st.session_state.selected_decimal_places = "Decimal places"

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



    # Helper function to display static rows with values
    def display_static_row(label, value, intro_text):
        col1, col2, col3 = st.columns([2, 6, 2])
        with col1:
            st.write(f"**{label}**")
        with col2:
            st.write(f"{intro_text}")
        with col3:
            st.write(f"**{value}**")

    # Create a container for the table
    table_container = st.container()

    # Use columns to create the table structure
    with table_container:
        # Table header
        col1, col2, col3 = st.columns([2, 6, 2])
        with col1:
            st.write("##")  # Empty header for first column
        with col2:
            st.write(f"### {translations[st.session_state.language]['concept']}")
        with col3:
            st.write(f"### {translations[st.session_state.language]['value']}")
        
        # Unit row
        display_static_row(
            translations[st.session_state.language]["unit"],
            st.session_state.selected_unit,
            translations[st.session_state.language]["unit_intro"]
        )

        # Contract Size row
        display_static_row(
            translations[st.session_state.language]["contract_size"],
            st.session_state.selected_contract_size,
            translations[st.session_state.language]["contract_intro"]
        )

        # Decimal Places row
        display_static_row(
            translations[st.session_state.language]["decimal_places"],
            st.session_state.selected_decimal_places,
            translations[st.session_state.language]["decimal_intro"]
        )

    # Apply some CSS to style the table
    st.markdown("""
    <style>
        div.row-widget.stSelectbox {
            margin-bottom: 0px;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        div[data-testid="stVerticalBlock"] > div:has(div.row-widget.stSelectbox) {
            background-color: #f9f9f9;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    market_info = ""

    # Set unit based on selected product and add technical details
    if product_selection == "Gold (XAUUSD)":
        unit = "cents"
        market_info = "Gold (XAUUSD) is highly sensitive to inflation expectations, geopolitical risks, and interest rate decisions by central banks. Gold is often considered a hedge against inflation and financial instability." if st.session_state.language == 'en' else "黄金 (XAUUSD) 对通胀预期、地缘政治风险和中央银行的利率决策高度敏感。黄金通常被视为对抗通胀和金融不稳定的对冲工具。"
    elif product_selection == "Silver (XAGUSD)":
        unit = "cents"
        market_info = "Silver (XAGUSD) is influenced by industrial demand, monetary policies, and geopolitical factors. It tends to follow gold prices but with higher volatility." if st.session_state.language == 'en' else "白银 (XAGUSD) 受工业需求、货币政策和地缘政治因素的影响。它通常跟随黄金价格波动，但波动性更大。"
    elif product_selection == "Oil":
        unit = "dollars"
        market_info = "Oil prices are impacted by supply/demand dynamics, geopolitical events, and economic indicators like OPEC decisions." if st.session_state.language == 'en' else "石油价格受供需动态、地缘政治事件和经济指标（如欧佩克决策）影响。"
    elif product_selection == "Index":
        unit = "points"
        market_info = "Indices reflect the performance of a basket of stocks and are impacted by macroeconomic trends, corporate earnings, and market sentiment." if st.session_state.language == 'en' else "指数反映了一篮子股票的表现，受宏观经济趋势、公司盈利和市场情绪的影响。"
    elif product_selection == "EUR/USD":
        unit = "Units of Base Currency"
        market_info = "EUR/USD is heavily influenced by monetary policy and interest rate decisions from the European Central Bank and the Federal Reserve. It's a major currency pair in the Forex market." if st.session_state.language == 'en' else "EUR/USD 主要受到欧洲中央银行和美联储的货币政策和利率决策的影响。它是外汇市场中的主要货币对。"

    elif product_selection == "GBP/USD":
        unit = "Units of Base Currency"
        market_info = "GBP/USD is a highly traded currency pair, with movements often linked to UK economic data and global risk sentiment." if st.session_state.language == 'en' else "GBP/USD 是一个高度交易的货币对，其波动通常与英国经济数据和全球风险情绪相关。"

    elif product_selection == "USD/JPY":
        unit = "Units of Base Currency"
        market_info = "USD/JPY is driven by global risk sentiment and is often used as a safe haven currency during periods of market instability." if st.session_state.language == 'en' else "USD/JPY 受全球风险情绪的驱动，通常在市场不稳定时期作为避险货币。"

    elif product_selection == "AUD/USD":
        unit = "Units of Base Currency"
        market_info = "AUD/USD is influenced by commodity prices, particularly iron ore and gold, and is often considered a proxy for global economic growth." if st.session_state.language == 'en' else "AUD/USD 受大宗商品价格的影响，特别是铁矿石和黄金，并常被视为全球经济增长的代理指标。"

    elif product_selection == "USD/CHF":
        unit = "Units of Base Currency"
        market_info = "USD/CHF is often used as a safe haven currency in times of geopolitical and financial uncertainty." if st.session_state.language == 'en' else "USD/CHF 常在地缘政治和金融不确定时期作为避险货币。"

    elif product_selection == "USD/CAD":
        unit = "Units of Base Currency"
        market_info = "USD/CAD is influenced by oil prices, with movements often following trends in the crude oil market." if st.session_state.language == 'en' else "USD/CAD 受油价影响，波动通常跟随原油市场的趋势。"

    elif product_selection == "NZD/USD":
        unit = "Units of Base Currency"
        market_info = "NZD/USD is sensitive to agricultural commodity prices, and it tends to follow global risk sentiment and commodity price trends." if st.session_state.language == 'en' else "NZD/USD 对农业商品价格敏感，通常跟随全球风险情绪和商品价格趋势。"

    elif product_selection == "EUR/JPY":
        unit = "Units of Base Currency"
        market_info = "EUR/JPY is highly sensitive to the economic performance of the Eurozone and Japan, as well as global economic risk factors." if st.session_state.language == 'en' else "EUR/JPY 对欧元区和日本的经济表现以及全球经济风险因素高度敏感。"

    elif product_selection == "GBP/JPY":
        unit = "Units of Base Currency"
        market_info = "GBP/JPY is often influenced by political events and economic data from the UK and Japan." if st.session_state.language == 'en' else "GBP/JPY 常受到来自英国和日本的政治事件和经济数据的影响。"

    elif product_selection == "BTC/USD":
        unit = "Coins"
        market_info = "BTC/USD is highly volatile and influenced by investor sentiment, news related to cryptocurrencies, and regulatory changes." if st.session_state.language == 'en' else "BTC/USD 波动性大，受投资者情绪、与加密货币相关的新闻和监管变化的影响。"

    elif product_selection == "ETH/USD":
        unit = "Coins"
        market_info = "ETH/USD is often driven by developments in the Ethereum network, as well as broader trends in the cryptocurrency market." if st.session_state.language == 'en' else "ETH/USD 通常受以太坊网络的动态以及加密货币市场的广泛趋势的驱动。"

    elif product_selection == "BNB/USD":
        unit = "Coins"
        market_info = "BNB/USD is influenced by changes in the Binance exchange ecosystem and overall market sentiment towards cryptocurrencies." if st.session_state.language == 'en' else "BNB/USD 受币安交易所生态系统的变化以及市场对加密货币的整体情绪的影响。"

    elif product_selection == "XRP/USD":
        unit = "Coins"
        market_info = "XRP/USD is influenced by developments in the Ripple network, legal actions, and cryptocurrency market sentiment." if st.session_state.language == 'en' else "XRP/USD 受瑞波网络的发展、法律行动和加密货币市场情绪的影响。"

    elif product_selection == "LTC/USD":
        unit = "Coins"
        market_info = "LTC/USD is driven by changes in the Litecoin network and market sentiment towards cryptocurrencies." if st.session_state.language == 'en' else "LTC/USD 受莱特币网络的变化和市场对加密货币的情绪的影响。"    

    else:
        unit = "pips"
        market_info = "No specific market info available." if st.session_state.language == 'en' else "没有具体的市场信息。"

    # Display product and unit
    st.write(f"{translations[st.session_state.language]['selected_product']} **{product_selection}** (Unit: **{unit}**)")

    # Display market info in an expandable section
    with st.expander(f"{translations[st.session_state.language]['market_info']} {product_selection}"):
        st.write(f"### 📈 {market_info}")
    st.subheader(translations[st.session_state.language]["calculation_formula"])
 
  
    st.markdown(translations[st.session_state.language]["pips_vs_points"])

    # Use st.latex for rendering the formula properly
    st.latex(r"Spread = \text{Ask Price in pips} - \text{Bid Price in pips}")

    st.markdown(translations[st.session_state.language]["calculation_example"])
    st.latex(r"Spread = 1.2005 - 1.2000 = 0.0005 \quad \text{(5 pips)}")


        

    # "Try Calculate" button section
    st.subheader(translations[st.session_state.language]["spread"])
    selected_products = st.multiselect(
    "🔍 Select multiple products to compare:",
    list(products.keys())

    
) 
    if len(selected_products) >= 2:

        with st.expander("⚙️ Click here to input parameters for selected products", expanded=True):
            product_inputs = {}

            for product in selected_products:
                st.markdown(f"### 🎯 **{product}**")
                decimal_places = products[product]["decimal_places"]
                unit = products[product]["unit"]

                # 调整后的更佳列宽比例
                cols = st.columns([1, 1, 1, 1])
                def check_decimal_places(value, decimal_places):
                    # 如果输入的价格的实际小数位数不符合要求，返回 False
                    if len(str(value).split('.')[-1]) > decimal_places:
                        return False
                    return True

                with cols[0]:
                    bid_price = st.number_input(
                        f"{product} - Bid Price",
                        min_value=0.0,
                        format=f"%.{decimal_places}f",
                        step=10 ** (-decimal_places),
                        key=f"bid_{product}"
                    )
                    if not check_decimal_places(bid_price, decimal_places):
                        show_warning_bid = True
                    else:
                        show_warning_bid = False

                    if show_warning_bid:
                        st.warning(f"**Warning:** Bid Price for {product_selection} should have {decimal_places} decimal places.")  # 显示警告消息
                with cols[1]:
                    ask_price = st.number_input(
                        f"{product} - Ask Price",
                        min_value=0.0,
                        format=f"%.{decimal_places}f",
                        step=10 ** (-decimal_places),
                        key=f"ask_{product}"
                    )
                with cols[2]:
                    leverage = st.number_input(
                        f" Leverage",
                        min_value=1.0,
                        step=1.0,
                        value=1.0,
                        key=f"leverage_{product}"
                    )
                with cols[3]:
                    trade_size = st.number_input(
                        f"Trade Size ({unit})",
                        min_value=0.0,
                        step=10 ** (-decimal_places),
                        format=f"%.{decimal_places}f",
                        key=f"size_{product}"
                    )

                product_inputs[product] = {
                    "Bid Price": bid_price,
                    "Ask Price": ask_price,
                    "Leverage": leverage,
                    "Trade Size": trade_size,
                    "Decimal Places": decimal_places,
                    "Unit": unit
                }

            if st.button("🔄 Calculate & Compare"):
                results = []
                for product, params in product_inputs.items():
                    bid = params["Bid Price"]
                    ask = params["Ask Price"]
                    lev = params["Leverage"]
                    size = params["Trade Size"]
                    spread = ask - bid
                    cost = spread * size / lev

                    results.append({
                        "Product": product,
                        "Bid Price": bid,
                        "Ask Price": ask,
                        "Spread": spread,
                        "Leverage": lev,
                        "Trade Size": size,
                        "Spread Cost": cost,
                        "Decimal Places": params["Decimal Places"]  # 新增用于动态格式化
                    })

                df_results = pd.DataFrame(results)

                # 动态格式化展示表格
                styled_df = df_results.style.format({
                    "Bid Price": lambda x, dp=df_results: f"{x:.{dp.loc[dp['Bid Price']==x, 'Decimal Places'].iloc[0]}f}",
                    "Ask Price": lambda x, dp=df_results: f"{x:.{dp.loc[dp['Ask Price']==x, 'Decimal Places'].iloc[0]}f}",
                    "Spread": lambda x, dp=df_results: f"{x:.{dp.loc[dp['Spread']==x, 'Decimal Places'].iloc[0]}f}",
                    "Spread Cost": "{:.4f}",
                    "Trade Size": lambda x, dp=df_results: f"{x:.{dp.loc[dp['Trade Size']==x, 'Decimal Places'].iloc[0]}f}",
                    "Leverage": "{:.2f}"
                })

                st.markdown("### 📋 Comparison Results")
                st.dataframe(styled_df)

                # Fancy可视化展示Spread Cost对比
                fig, ax = plt.subplots(figsize=(10, 5))
                bars = ax.bar(df_results["Product"], df_results["Spread Cost"], color='skyblue')

                ax.set_xlabel("Product")
                ax.set_ylabel("Spread Cost")
                ax.set_title("📊 Spread Cost Comparison")
                ax.grid(axis='y', linestyle='--', alpha=0.7)

                for bar in bars:
                    yval = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.4f}', va='bottom', ha='center', fontsize=10, fontweight='bold')

                st.pyplot(fig)

                # CSV导出功能（去掉Decimal Places列）
                csv = df_results.drop(columns=["Decimal Places"]).to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Results CSV",
                    data=csv,
                    file_name="multi_products_results.csv",
                    mime="text/csv"
                )

    else:
        # st.info("ℹ️ Select at least **2 products** to trigger the comparison form.")
        st.write(translations[st.session_state.language]["enter_bid_ask"])

        






        # User input fields with styling
        col1, col2 = st.columns(2)

        unit = products[product_selection]["unit"]
        contract_size = products[product_selection]["contract_size"]
        decimal_places = products[product_selection]["decimal_places"]


        # 检查用户输入的价格是否符合 decimal_places
        def check_decimal_places(value, decimal_places):
            # 如果输入的价格的实际小数位数不符合要求，返回 False
            if len(str(value).split('.')[-1]) > decimal_places:
                return False
            return True

        # 用于存储是否需要显示警告的状态
        show_warning_bid = False
        show_warning_ask = False

        with col1:
            bid_price = st.number_input(
                f"Enter **Bid Price** for {product_selection}:" if st.session_state.language == 'en' else f"输入 **买入价** ({product_selection}):",
                min_value=0.0,
                format=f"%.{decimal_places}f",
                step=10**(-decimal_places),  # 动态步长
                key=f"bid_price_{product_selection}"  # 确保唯一的 key
            )
            # 检查输入的小数位数是否符合要求
            if not check_decimal_places(bid_price, decimal_places):
                show_warning_bid = True
            else:
                show_warning_bid = False

            if show_warning_bid:
                st.warning(f"**Warning:** Bid Price for {product_selection} should have {decimal_places} decimal places.")  # 显示警告消息

        with col2:
            ask_price = st.number_input(
                f"Enter **Ask Price** for {product_selection}:" if st.session_state.language == 'en' else f"输入 **卖出价** ({product_selection}):",
                min_value=0.0,
                format=f"%.{decimal_places}f",
                step=10**(-decimal_places),  # 动态步长
                key=f"ask_price_{product_selection}"  # 确保唯一的 key
            )
            # 检查输入的小数位数是否符合要求
            if not check_decimal_places(ask_price, decimal_places):
                show_warning_ask = True
            else:
                show_warning_ask = False

            if show_warning_ask:
                st.warning(f"**Warning:** Ask Price for {product_selection} should have {decimal_places} decimal places.")  # 显示警告消息


        # Input for leverage and trade size
        leverage = st.number_input("Enter **Leverage**:" if st.session_state.language == 'en' else "输入 **杠杆**:", min_value=1.0, step=1.0)
        unit = products[product_selection]["unit"]
        contract_size = products[product_selection]["contract_size"]
        decimal_places = products[product_selection]["decimal_places"]

        # 根据产品动态设置 Trade Size 输入框
        trade_size_label = f"Enter **Trade Size** (e.g., in {unit}):" if st.session_state.language == 'en' else f"输入 **交易规模** (例如，{unit}):"

        # 在col1中创建交易规模的输入框
        trade_size = st.number_input(
            trade_size_label,
            min_value=0.0,
            step=10**(-decimal_places),  # 动态调整步长，基于产品的小数位数
            format=f"%.{decimal_places}f",  # 动态调整显示格式
            key=f"trade_size_{product_selection}"  # 确保唯一的key
        )

        # Calculate based on selected calculation type


        st.subheader("📊 Spread Calculation")
        # 点差计算逻辑
        if st.button("🔄 Calculate Spread" if st.session_state.language == 'en' else "🔄 计算点差"):
            if bid_price > 0 and ask_price > 0 and trade_size > 0:
                spread = ask_price - bid_price
                st.markdown(f"### 📊 The Spread: **{spread:.4f}** (or **{spread * 10000:.0f} {unit}**)" if st.session_state.language == 'en' else f"### 📊 点差: **{spread:.4f}** (或 **{spread * 10000:.0f} {unit}**)")

                cost = spread * trade_size / leverage
                st.markdown(f"### 💰 The cost of the spread is: **{cost:.4f}** (based on leverage and trade size)" if st.session_state.language == 'en' else f"### 💰 点差成本为: **{cost:.4f}** (根据杠杆和交易规模计算)")
            else:
                st.warning("Please enter valid values for **Bid Price**, **Ask Price**, **Leverage**, and **Trade Size**." if st.session_state.language == 'en' else "请输入有效的 **买入价**、**卖出价**、**杠杆** 和 **交易规模**。")


    

        # Display additional notes
        st.markdown(translations[st.session_state.language]["notes"])

        if st.button("Export Results to CSV" if st.session_state.language == 'en' else "导出结果为CSV"):
        
            result = {
                "Product": product_selection,
                "Bid Price": bid_price,
                "Ask Price": ask_price,
                "Leverage": leverage,
                "Trade Size": trade_size,
                "Spread": spread if 'spread' in locals() else None,
                "Cost": cost if 'cost' in locals() else None
            }
            
            df = pd.DataFrame([result])
            

            st.download_button(
                label="Download CSV" if st.session_state.language == 'en' else "下载CSV",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name="calculation_results.csv",
                mime="text/csv"
            )