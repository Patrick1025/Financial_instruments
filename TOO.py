import streamlit as st
import pandas as pd

def order_types_page():
    translations = {
        "en": {
            "title": "📑 Types of Orders",
            "switch_lang": "切换到中文",
            "select_type": "Order Type Selector",
            "main_types": "Order Types Overview",
            "market": "Market Order",
            "pending": "Pending Order",
            "tif": "Time-in-Force",
            "conditional": "Conditional Order",
            "desc_market": "Market Order: Execute buy/sell instantly at current best price. Used for quick entry/exit. No price guarantee during volatility.",
            "desc_pending": "Pending Orders: Activate only when price meets your specified level (includes Limit and Stop orders). Used for strategic entries/exits.",
            "desc_tif": "Time-in-Force (TIF): Special instructions specifying order validity (e.g. GTC, FOK, IOC, GTD).",
            "desc_conditional": "Conditional Orders: Linked logic like OCO (One Cancels Other), OTO (One Triggers Other). Often used for complex exit/entry logic.",
            "table_cols": ["Order Type", "Sub-Type", "Trigger", "Example Use"],
            "table_data": [
                ["Market", "Buy/Sell", "Now", "Immediate trade at market price"],
                ["Limit", "Buy Limit", "Price ≤ set value", "Buy pullback at good price"],
                ["Limit", "Sell Limit", "Price ≥ set value", "Sell rally at good price"],
                ["Stop", "Buy Stop", "Price ≥ set value", "Buy breakout"],
                ["Stop", "Sell Stop", "Price ≤ set value", "Sell breakdown"],
                ["Stop Loss", "Linked to trade", "Price hits stop", "Limit max loss"],
                ["Trailing Stop", "Dynamic", "Trail price", "Lock in profit on trends"],
            ],
            "types_list": [
                "Market Order",
                "Buy Limit",
                "Sell Limit",
                "Buy Stop",
                "Sell Stop",
                "Stop Loss",
                "Trailing Stop",
                "OCO / OTO",
                "Time-in-Force"
            ],
            "explain": {
                "Market Order": {
                    "title": "Market Order",
                    "brief": "Immediate execution at current best price (no price guarantee).",
                    "example": "E.g. Buy EUR/USD at 1.2142 right now; filled instantly.",
                    "risk": "⚠️ May cause slippage in fast markets."
                },
                "Buy Limit": {
                    "title": "Buy Limit Order",
                    "brief": "Buy when price drops to (or below) a level you set, usually to enter at a lower price.",
                    "example": "E.g. Set Buy Limit at 1.2050 when current price is 1.2080.",
                    "risk": "⏳ May not fill if price doesn't fall enough."
                },
                "Sell Limit": {
                    "title": "Sell Limit Order",
                    "brief": "Sell when price rises to (or above) a level you set, usually to sell at a higher price.",
                    "example": "E.g. Set Sell Limit at 1.2100 when current price is 1.2080.",
                    "risk": "⏳ May not fill if price doesn't rise enough."
                },
                "Buy Stop": {
                    "title": "Buy Stop Order",
                    "brief": "Buy only if price rises to (or above) your stop level; used for breakouts.",
                    "example": "E.g. Set Buy Stop at 1.2100; triggers only if price hits or exceeds.",
                    "risk": "⚡️ May fill at worse price if spike is fast."
                },
                "Sell Stop": {
                    "title": "Sell Stop Order",
                    "brief": "Sell only if price drops to (or below) your stop level; used for breakdowns.",
                    "example": "E.g. Set Sell Stop at 1.2050; triggers only if price falls to or below.",
                    "risk": "⚡️ May fill at worse price in flash crash."
                },
                "Stop Loss": {
                    "title": "Stop Loss",
                    "brief": "Linked to an open trade; auto close at set price to limit loss.",
                    "example": "E.g. Long EUR/USD at 1.2100, stop loss at 1.2060.",
                    "risk": "⚠️ Not always filled at exact price if market gaps."
                },
                "Trailing Stop": {
                    "title": "Trailing Stop",
                    "brief": "Stop price moves in your favor automatically, locks profit while allowing further gains.",
                    "example": "E.g. Short USD/JPY with 20-pip trailing stop: stop moves lower as price drops.",
                    "risk": "⚡️ Trailing stop can be triggered by short-term spikes."
                },
                "OCO / OTO": {
                    "title": "OCO & OTO (Conditional)",
                    "brief": "OCO: If one order fills, the other is canceled. OTO: Placing an order triggers another.",
                    "example": "E.g. OCO: set both take profit and stop loss; one triggers, the other cancels. OTO: entry triggers target & stop.",
                    "risk": "🧩 Not all brokers/platforms support these advanced types."
                },
                "Time-in-Force": {
                    "title": "Time-in-Force (TIF)",
                    "brief": "Set how long your order remains valid (GTC, FOK, IOC, GTD).",
                    "example": "E.g. GTC: Good till cancelled. FOK: Fill all now or none.",
                    "risk": "⏱️ Make sure to use TIF matching your trading plan."
                }
            }
        },
        "zh": {
            "title": "📑 常见订单类型",
            "switch_lang": "Switch to English",
            "select_type": "订单类型选择",
            "main_types": "订单类型一览",
            "market": "市价单",
            "pending": "挂单",
            "tif": "时效类型",
            "conditional": "条件单",
            "desc_market": "市价单：以当前市场最优价立即成交。用于快速进出场。行情剧烈波动时可能滑点。",
            "desc_pending": "挂单：仅当市价到达你指定价位时自动激活（含限价/止损单）。适合策略性入场/止盈/止损。",
            "desc_tif": "时效（TIF）：设定订单有效期，如GTC、FOK、IOC、GTD等。",
            "desc_conditional": "条件单：如OCO（一个成交另一个撤销）、OTO（一个触发另一个），多用于复杂策略。",
            "table_cols": ["订单类型", "细分", "触发方式", "常见用途"],
            "table_data": [
                ["市价单", "买入/卖出", "立即", "按市价成交"],
                ["限价单", "买入限价", "价格≤指定价", "低吸买入"],
                ["限价单", "卖出限价", "价格≥指定价", "高位卖出"],
                ["止损单", "买入止损", "价格≥指定价", "突破追多"],
                ["止损单", "卖出止损", "价格≤指定价", "跌破追空"],
                ["止损单", "关联交易", "价格触发", "控制亏损"],
                ["跟踪止损", "动态", "浮盈跟随", "浮盈锁定"],
            ],
            "types_list": [
                "市价单",
                "买入限价单",
                "卖出限价单",
                "买入止损单",
                "卖出止损单",
                "止损单",
                "跟踪止损",
                "OCO / OTO",
                "时效类型"
            ],
            "explain": {
                "市价单": {
                    "title": "市价单",
                    "brief": "以当前市场最优价立即成交（不能保证价格）。",
                    "example": "如：买入EUR/USD于1.2142，立即成交。",
                    "risk": "⚠️ 行情波动快时可能滑点。"
                },
                "买入限价单": {
                    "title": "买入限价单",
                    "brief": "当市价跌至或低于你设定价位时买入。常用于回调低吸。",
                    "example": "如：现价1.2080，挂买入限价1.2050。",
                    "risk": "⏳ 如价格未跌到则无法成交。"
                },
                "卖出限价单": {
                    "title": "卖出限价单",
                    "brief": "当市价涨至或高于你设定价位时卖出。常用于高位卖出。",
                    "example": "如：现价1.2080，挂卖出限价1.2100。",
                    "risk": "⏳ 如价格未涨到则无法成交。"
                },
                "买入止损单": {
                    "title": "买入止损单",
                    "brief": "当市价涨至你设定止损价位时买入，常用于突破追多。",
                    "example": "如：挂买入止损1.2100，只有价格涨到才触发。",
                    "risk": "⚡️ 快速突破时可能高于止损价成交。"
                },
                "卖出止损单": {
                    "title": "卖出止损单",
                    "brief": "当市价跌至你设定止损价位时卖出，常用于跌破追空。",
                    "example": "如：挂卖出止损1.2050，只有价格跌到才触发。",
                    "risk": "⚡️ 急跌时可能低于止损价成交。"
                },
                "止损单": {
                    "title": "止损单",
                    "brief": "挂在持仓方向反向价位自动止损，限制亏损。",
                    "example": "如：多头EUR/USD于1.2100，止损1.2060。",
                    "risk": "⚠️ 跳空/剧烈波动时止损不一定精确成交。"
                },
                "跟踪止损": {
                    "title": "跟踪止损",
                    "brief": "止损价随浮盈自动上移，趋势行情中可锁定利润。",
                    "example": "如：做空USD/JPY，20点跟踪止损，价格下跌止损同步下移。",
                    "risk": "⚡️ 短期波动也可能触发止盈。"
                },
                "OCO / OTO": {
                    "title": "OCO & OTO（条件单）",
                    "brief": "OCO：一个成交另一个自动撤销；OTO：一个成交后自动挂出另一个。",
                    "example": "OCO：止盈止损挂一起，任何一单成交另一个自动撤销。OTO：入场后自动挂止盈/止损。",
                    "risk": "🧩 并非所有券商/平台都支持高级条件单。"
                },
                "时效类型": {
                    "title": "时效类型（TIF）",
                    "brief": "设定订单有效期，如GTC、FOK、IOC、GTD。",
                    "example": "GTC：撤单前一直有效。FOK：必须全部成交否则全撤。",
                    "risk": "⏱️ 请根据策略合理选择时效。"
                }
            }
        }
    }

    # if "order_type_lang" not in st.session_state:
    #     st.session_state["order_type_lang"] = "en"
    # lang = st.session_state["order_type_lang"]
    # t = translations[lang]

    lang = st.session_state.get("language", "en")
    t = translations[lang]

    # # 右上角语言切换按钮
    # cols = st.columns([10,2])
    # with cols[-1]:
    #     if st.button(t["switch_lang"]):
    #         st.session_state["order_type_lang"] = "zh" if lang == "en" else "en"
    #         st.rerun()

    st.title(t["title"])
    st.divider()

    grid = st.columns(4)
    grid[0].markdown(f"""<div style="background:#e6f3ff;padding:1em;border-radius:1em"><b>{t["market"]}</b><br>{t["desc_market"]}</div>""", unsafe_allow_html=True)
    grid[1].markdown(f"""<div style="background:#f7f7e3;padding:1em;border-radius:1em"><b>{t["pending"]}</b><br>{t["desc_pending"]}</div>""", unsafe_allow_html=True)
    grid[2].markdown(f"""<div style="background:#f2ecef;padding:1em;border-radius:1em"><b>{t["tif"]}</b><br>{t["desc_tif"]}</div>""", unsafe_allow_html=True)
    grid[3].markdown(f"""<div style="background:#e8f7ec;padding:1em;border-radius:1em"><b>{t["conditional"]}</b><br>{t["desc_conditional"]}</div>""", unsafe_allow_html=True)

    st.markdown("### 🗺️ " + t["main_types"])
    st.dataframe(pd.DataFrame(t["table_data"], columns=t["table_cols"]), hide_index=True, use_container_width=True)

    # 交互式订单类型说明
    st.markdown(f"#### 🎯 {t['select_type']}")
    selected_type = st.radio(
        label="",
        options=t["types_list"],
        horizontal=True
    )

    detail = t["explain"][selected_type]
    card_color = "#f9fafd" if lang=="en" else "#f7fbe7"
    st.markdown(f"""
    <div style="background:{card_color};border-radius:1em;padding:1.5em 2em;box-shadow:0 2px 12px #f4f6fb;">
        <h4 style="margin-bottom:0.2em">{detail['title']}</h4>
        <b>{detail['brief']}</b>
        <ul>
            <li><b>Example:</b> {detail['example']}</li>
            <li><b>Risk Tip:</b> {detail['risk']}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 可选：增加流程图/可视化辅助理解（如配合draw.io图片或外链）

    st.info("💡 Always check with your broker which order types, TIF, and advanced conditional orders are available on your platform.")

# 用法：order_types_page()
