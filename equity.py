import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

def equity_page():
    products = {
        "Gold (XAUUSD)": {"unit": "Ounces", "contract_size": 100, "decimal_places": 2},
        "Silver (XAGUSD)": {"unit": "Ounces", "contract_size": 1000, "decimal_places": 3},
        "Oil (WTI)": {"unit": "Barrels", "contract_size": 1000, "decimal_places": 2},
        "Index (S&P 500)": {"unit": "Points", "contract_size": 50, "decimal_places": 2},
        "EUR/USD": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "GBP/USD": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "USD/JPY": {"unit": "Units", "contract_size": 100000, "decimal_places": 3},
        "AUD/USD": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "USD/CHF": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "USD/CAD": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "NZD/USD": {"unit": "Units", "contract_size": 100000, "decimal_places": 5},
        "EUR/JPY": {"unit": "Units", "contract_size": 100000, "decimal_places": 3},
        "GBP/JPY": {"unit": "Units", "contract_size": 100000, "decimal_places": 3},
        "BTC/USD": {"unit": "Coins", "contract_size": 1, "decimal_places": 8},
        "ETH/USD": {"unit": "Coins", "contract_size": 1, "decimal_places": 8},
        "BNB/USD": {"unit": "Coins", "contract_size": 1, "decimal_places": 8},
        "XRP/USD": {"unit": "Coins", "contract_size": 1, "decimal_places": 8},
        "LTC/USD": {"unit": "Coins", "contract_size": 1, "decimal_places": 8},
    }

    translations = {
        "en": {
            "title": "📊 Balance, Equity, Margin & Margin Level Tool",
            "balance": "Balance (Closed P/L)",
            "balance_concept": "Balance is the historical net worth in your account, excluding any open trades. It reflects deposits, withdrawals, and closed position P/L.",
            "equity": "Equity (Real-Time Value)",
            "equity_concept": "Equity = Balance + floating P/L from open positions. Reflects the real-time account value.",
            "floating_pl": "Floating Profit/Loss",
            "floating_pl_concept": "Sum of all open positions' unrealized profits and losses, based on real-time prices.",
            "used_margin": "Used Margin",
            "used_margin_concept": "Total margin currently locked for open trades. Varies by position size, instrument, and real-time price.",
            "free_margin": "Free Margin",
            "free_margin_concept": "Equity minus Used Margin. It’s the margin left for new trades or to absorb losses.",
            "margin_level": "Margin Level",
            "margin_level_formula": "Margin Level = (Equity ÷ Used Margin) × 100%",
            "margin_level_concept": "Shows how much your equity covers your used margin. <100% = margin call risk.",
            "margin_requirement": "Margin Requirement",
            "margin_requirement_formula": "Margin Requirement = Position Size × Price × Margin Rate",
            "order_entry": "Enter Your Open Positions",
            "instrument": "Instrument",
            "position_size": "Position Size",
            "entry_price": "Entry Price",
            "current_price": "Current Price",
            "direction": "Direction",
            "long": "Long",
            "short": "Short",
            "margin_rate": "Margin Rate (%)",
            "add_order": "Add Position",
            "delete_order": "Delete Selected",
            "calc_all": "🔄 Calculate Account Status",
            "summary": "Account Summary",
            "no_orders": "No open positions yet. Add one below.",
            "remove_order": "Remove",
            "concepts": "🧮 Concepts Explained",
            "formulas": "🔗 Key Formulas",
            "delete_confirm": "Are you sure to delete this order?",
        },
        "zh": {
            "title": "📊 余额、权益、保证金与比率工具",
            "balance": "余额（已平仓盈亏）",
            "balance_concept": "余额是账户历史净值，不包含未平仓订单。反映入金、出金和已平仓盈亏。",
            "equity": "权益（实时）",
            "equity_concept": "权益 = 余额 + 未平仓单浮动盈亏。反映账户实时价值。",
            "floating_pl": "浮动盈亏",
            "floating_pl_concept": "所有未平仓单的浮动盈亏总和，根据实时行情计算。",
            "used_margin": "已用保证金",
            "used_margin_concept": "当前未平仓订单占用的保证金总额。与持仓、品种、实时价格等相关。",
            "free_margin": "可用保证金",
            "free_margin_concept": "权益减去已用保证金，可用来开新仓或抵御亏损。",
            "margin_level": "保证金比率",
            "margin_level_formula": "保证金比率 = (权益 ÷ 已用保证金) × 100%",
            "margin_level_concept": "反映权益对已用保证金的覆盖。低于100%面临强平风险。",
            "margin_requirement": "保证金要求",
            "margin_requirement_formula": "保证金要求 = 持仓规模 × 当前价格 × 保证金率",
            "order_entry": "请录入你的未平仓订单",
            "instrument": "品种",
            "position_size": "持仓规模",
            "entry_price": "开仓价",
            "current_price": "当前价",
            "direction": "方向",
            "long": "买入",
            "short": "卖出",
            "margin_rate": "保证金率（%）",
            "add_order": "添加订单",
            "delete_order": "删除选中订单",
            "calc_all": "🔄 计算账户状态",
            "summary": "账户汇总",
            "no_orders": "暂无未平仓单，请下方添加。",
            "remove_order": "移除",
            "concepts": "🧮 核心概念说明",
            "formulas": "🔗 主要公式",
            "delete_confirm": "确认要删除该订单？",
        }
    }

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    # 统一页面样式
    st.markdown("""
        <style>
        .block-container {padding-top: 2rem !important; max-width: 1100px;}
        .metric-value {font-size: 2.2em !important; font-weight: 600;}
        .stDataFrame thead tr th {background-color: #f7f8fa !important;}
        .st-emotion-cache-1kyxreq {background: #f9f9fa;}
        .stForm label {font-weight:600;}
        </style>
    """, unsafe_allow_html=True)

    st.title(t["title"])

    with st.expander(t["concepts"], expanded=False):
        st.markdown(f"- **{t['balance']}**: {t['balance_concept']}")
        st.markdown(f"- **{t['equity']}**: {t['equity_concept']}")
        st.markdown(f"- **{t['floating_pl']}**: {t['floating_pl_concept']}")
        st.markdown(f"- **{t['used_margin']}**: {t['used_margin_concept']}")
        st.markdown(f"- **{t['free_margin']}**: {t['free_margin_concept']}")
        st.markdown(f"- **{t['margin_level']}**: {t['margin_level_concept']}")

    with st.expander(t["formulas"], expanded=False):
        st.code(f"{t['margin_level_formula']}", language="markdown")
        st.code(f"{t['margin_requirement_formula']}", language="markdown")

    st.divider()

    # 账户初始余额输入 + 汇总卡片区
    balance = st.number_input(f"💰 {t['balance']}", min_value=0.0, value=10000.0, step=100.0, key="balance_input")
    if "orders" not in st.session_state:
        st.session_state.orders = []

    # 新订单录入
    with st.form("order_form"):
        cols = st.columns([2, 1, 1, 1.5, 1.5, 1])
        with cols[0]:
            instrument = st.selectbox(t["instrument"], list(products.keys()), key="order_instrument")
        product_params = products[instrument]
        contract_size = product_params["contract_size"]
        decimals = product_params["decimal_places"]
        unit = product_params["unit"]

        with cols[1]:
            direction = st.selectbox(t["direction"], [t["long"], t["short"]])
        with cols[2]:
            size = st.number_input(t["position_size"], min_value=0.0, value=1.0)
        with cols[3]:
            entry_price = st.number_input(t["entry_price"], min_value=0.0, value=1.1000)
        with cols[4]:
            current_price = st.number_input(t["current_price"], min_value=0.0, value=1.1100)
        with cols[5]:
            margin_rate = st.number_input(t["margin_rate"], min_value=0.1, max_value=100.0, value=2.0)
        submitted = st.form_submit_button(t["add_order"])
        if submitted:
            st.session_state.orders.append({
                "Instrument": instrument,
                "Direction": direction,
                "Position Size": size,
                "Entry Price": entry_price,
                "Current Price": current_price,
                "Margin Rate": margin_rate,
                "Contract Size": contract_size,
                "Unit": unit,
                "Decimals": decimals
            })
            st.success("✅ Added!")

    # 展示已输入订单 + 单个移除按钮
    if st.session_state.orders:
        orders_df = pd.DataFrame(st.session_state.orders)
        # 添加删除功能
        for idx, row in orders_df.iterrows():
            cols = st.columns([8,1])
            with cols[0]:
                st.write(f"{row['Instrument']} | {row['Direction']} | {row['Position Size']} @ {row['Entry Price']}→{row['Current Price']} | {row['Margin Rate']}%")
            with cols[1]:
                if st.button(f"{t['remove_order']} {idx+1}", key=f"delete_{idx}"):
                    st.session_state.orders.pop(idx)
                    st.experimental_rerun()
        st.divider()
    else:
        st.info(t["no_orders"])

    # 计算所有账户关键指标
    if st.button(t["calc_all"]):
        total_floating = 0.0
        total_used_margin = 0.0
        for order in st.session_state.orders:
            cs = order.get("Contract Size", 100000)
            pnl_per_unit = (order["Current Price"] - order["Entry Price"]) if order["Direction"] == t["long"] else (order["Entry Price"] - order["Current Price"])
            floating = pnl_per_unit * order["Position Size"] * cs
            total_floating += floating
            margin_req = order["Position Size"] * cs * order["Current Price"] * (order["Margin Rate"] / 100)
            total_used_margin += margin_req

        equity = balance + total_floating
        free_margin = equity - total_used_margin
        margin_level = (equity / total_used_margin * 100) if total_used_margin > 0 else float('inf')

        # 卡片区 summary
        colA, colB, colC, colD, colE, colF = st.columns(6)
        colA.metric(label=t["balance"], value=f"{balance:,.2f}")
        colB.metric(label=t["floating_pl"], value=f"{total_floating:,.2f}")
        colC.metric(label=t["equity"], value=f"{equity:,.2f}")
        colD.metric(label=t["used_margin"], value=f"{total_used_margin:,.2f}")
        colE.metric(label=t["free_margin"], value=f"{free_margin:,.2f}")
        colF.metric(label=t["margin_level"], value=f"{margin_level:.2f} %")
        st.caption(t["margin_level_concept"])
        st.divider()

        # 详细说明
        with st.expander(t["summary"], expanded=True):
            st.markdown(f"- **{t['balance']}:** {balance:.2f}")
            st.markdown(f"- **{t['floating_pl']}:** {total_floating:.2f} ({t['floating_pl_concept']})")
            st.markdown(f"- **{t['equity']}:** {equity:.2f} ({t['equity_concept']})")
            st.markdown(f"- **{t['used_margin']}:** {total_used_margin:.2f} ({t['used_margin_concept']})")
            st.markdown(f"- **{t['free_margin']}:** {free_margin:.2f} ({t['free_margin_concept']})")
            st.markdown(f"- **{t['margin_level']}:** {margin_level:.2f}% ({t['margin_level_concept']})")

# 调用页面函数
# equity_page()
