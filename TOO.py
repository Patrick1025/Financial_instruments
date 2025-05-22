import streamlit as st

def pending_order_page():
    # 语言翻译字典
    translations = {
        "en": {
            "title": "📊 Pending Order",
            "limit_order": "🔍 Limit Order",
            "stop_entry_order": "🔍 Stop Entry Order",
            "stop_loss_order": "🔍 Stop Loss Order",
            "trailing_stop": "🔍 Trailing Stop",
            "time_in_force": "🔍 Time-in-Force Orders",
            "conditional_orders": "🔍 Conditional Orders",
            "limit_order_explanation": "A limit order is an order placed to either buy below the market or sell above the market at a certain price. It is executed once the market reaches the specified price.",
            "stop_entry_order_explanation": "A stop entry order is used to buy above the market or sell below the market once a specific price is reached.",
            "stop_loss_order_explanation": "A stop loss order is used to limit potential losses by automatically closing a position when a specified price is reached.",
            "trailing_stop_explanation": "A trailing stop is a stop loss order that moves as the price fluctuates, locking in profits while protecting against a reversal.",
            "time_in_force_explanation": "Time-in-force (TIF) orders specify how long an order remains active before being canceled if not executed.",
            "conditional_orders_explanation": "Conditional orders, such as OCO (One-Cancels-the-Other) and OTO (One-Triggers-the-Other), are linked orders that become active based on specific conditions being met.",
            "example": "### 💡 Example\n\nFor example, placing a **Buy Limit** order allows you to buy at or below a specified price. If the price falls to your limit price, your order will be executed."
        },
        "zh": {
            "title": "📊 待处理订单",
            "limit_order": "🔍 限价单",
            "stop_entry_order": "🔍 停止入场单",
            "stop_loss_order": "🔍 止损单",
            "trailing_stop": "🔍 移动止损",
            "time_in_force": "🔍 有效时间订单",
            "conditional_orders": "🔍 条件订单",
            "limit_order_explanation": "限价单是一种买入低于市场价格或卖出高于市场价格的订单。一旦市场达到指定价格，该订单将被执行。",
            "stop_entry_order_explanation": "停止入场单是在市场达到某一价格时买入或卖出，用于在特定价格触及时进入市场。",
            "stop_loss_order_explanation": "止损单是一种用于限制潜在损失的订单，当市场价格达到指定价格时，自动平仓。",
            "trailing_stop_explanation": "移动止损是止损单的一种，它随着价格波动而移动，锁定利润同时防止价格回撤。",
            "time_in_force_explanation": "有效时间订单（TIF）指定订单在未执行时保持有效的时间，直到被取消。",
            "conditional_orders_explanation": "条件订单，如 OCO（一个取消另一个）和 OTO（一个触发另一个），是根据特定条件触发的链接订单。",
            "example": "### 💡 示例\n\n例如，设置一个 **买入限价单** 允许你以指定价格或更低价格买入。当价格达到限价时，订单将被执行。"
        }
    }

    # 设置页面标题
    st.title(translations[st.session_state.language]["title"])

    # Limit Order 说明
    st.subheader(translations[st.session_state.language]["limit_order"])
    st.write(translations[st.session_state.language]["limit_order_explanation"])

    st.markdown(translations[st.session_state.language]["example"])

    # Stop Entry Order 说明
    st.subheader(translations[st.session_state.language]["stop_entry_order"])
    st.write(translations[st.session_state.language]["stop_entry_order_explanation"])

    # Stop Loss Order 说明
    st.subheader(translations[st.session_state.language]["stop_loss_order"])
    st.write(translations[st.session_state.language]["stop_loss_order_explanation"])

    # Trailing Stop 说明
    st.subheader(translations[st.session_state.language]["trailing_stop"])
    st.write(translations[st.session_state.language]["trailing_stop_explanation"])

    # Time-in-Force Orders 说明
    st.subheader(translations[st.session_state.language]["time_in_force"])
    st.write(translations[st.session_state.language]["time_in_force_explanation"])

    # Conditional Orders 说明
    st.subheader(translations[st.session_state.language]["conditional_orders"])
    st.write(translations[st.session_state.language]["conditional_orders_explanation"])

    # 页面结束
    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
