import streamlit as st
from spread import spread_page
from equity import equity_page
from margin import margin_page
from Arbitrage import arbitrage_page
from TOO import order_types_page
from SST import scalping_vs_swing_trading_page
from Pitfalls import pitfalls_page
from lot import lot_page
from NOP import nop_page
from SL import long_short_page
from swap import swap_page

# 统一的英文页面 key
PAGE_KEYS = [
    "Spread", "Balance & Equity", "Swap", "Types of Orders", "Scalping vs. Swing Trading",
    "Pitfalls", "NOP", "Short & Long position", "Arbitrage", "Lot"
]
PAGE_NAMES = {
    "en": [
        "Spread", "Balance & Equity", "Swap", "Types of Orders", "Scalping vs. Swing Trading",
        "Pitfalls", "NOP", "Short & Long position", "Arbitrage", "Lot"
    ],
    "zh": [
        "点差", "账户余额与净值", "隔夜利息", "订单类型", "剥头皮与波段交易",
        "注意事项", "净头寸(NOP)", "多空头", "套利", "手数"
    ]
}

if 'language' not in st.session_state:
    st.session_state.language = 'en'

if 'page_selection' not in st.session_state:
    st.session_state.page_selection = "Spread"  # 默认首页

def toggle_language():
    if st.session_state.language == 'en':
        st.session_state.language = 'zh'
    else:
        st.session_state.language = 'en'

with st.sidebar:
    st.image('https://www.sequoiacap.com/wp-content/uploads/sites/6/2021/12/Upway_Logo_RGB_Electric_Blue.png', use_container_width=True)
    st.write("### Welcome to Upway Global!")
    st.write("Upway Global is a leading company in financial technologies. We provide cutting-edge solutions for trading and market analysis.")
    st.markdown("[Visit our website](https://www.upwaygroup.com)")
    st.markdown("[Follow us on LinkedIn](https://www.linkedin.com/company/upwayglobal)")
    st.markdown("[Follow us on Twitter](https://twitter.com/upwayglobal)")

    st.button("Switch to 中文" if st.session_state.language == 'en' else "Switch to English", on_click=toggle_language)

    # 关键: 只用 key="page_selection"，不自己赋值
    st.selectbox(
        "Select Page" if st.session_state.language == 'en' else "选择页面",
        PAGE_KEYS,
        format_func=lambda x: PAGE_NAMES[st.session_state.language][PAGE_KEYS.index(x)],
        key="page_selection"
    )

# 这里直接用 session_state.page_selection 判断即可
if st.session_state.page_selection == "Spread":
    spread_page()
elif st.session_state.page_selection == "Balance & Equity":
    equity_page()
elif st.session_state.page_selection == "Margin":
    margin_page()
elif st.session_state.page_selection == "Arbitrage":
    arbitrage_page()
elif st.session_state.page_selection == "Types of Orders":
    order_types_page()
elif st.session_state.page_selection == "Scalping vs. Swing Trading":
    scalping_vs_swing_trading_page()
elif st.session_state.page_selection == "Pitfalls":
    pitfalls_page()
elif st.session_state.page_selection == "Lot":
    lot_page()
elif st.session_state.page_selection == "NOP":
    nop_page()
elif st.session_state.page_selection == "Short & Long position":
    long_short_page()
elif st.session_state.page_selection == "Swap":
    swap_page()
