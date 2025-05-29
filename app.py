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

SIDEBAR_TEXT = {
    "en": {
        "welcome": "### Welcome to Upway Global!",
        "desc": "Upway Global is a leading company in financial technologies. We provide cutting-edge solutions for trading and market analysis.",
        "website": "Visit our website",
        "linkedin": "Follow us on LinkedIn",
        "twitter": "Follow us on Twitter",
        "switch": "Switch to 中文",
        "select": "Select Page"
    },
    "zh": {
        "welcome": "### 欢迎来到 Upway Global!",
        "desc": "Upway Global 是金融科技领域的领先公司，专注于为交易和市场分析提供前沿解决方案。",
        "website": "访问我们的网站",
        "linkedin": "关注我们的领英",
        "twitter": "关注我们的推特",
        "switch": "切换到 English",
        "select": "选择页面"
    }
}

if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'page_selection' not in st.session_state:
    st.session_state.page_selection = "Spread"

def toggle_language():
    st.session_state.language = 'zh' if st.session_state.language == 'en' else 'en'

with st.sidebar:
    st.image(
        'https://www.sequoiacap.com/wp-content/uploads/sites/6/2021/12/Upway_Logo_RGB_Electric_Blue.png', 
        use_container_width=True
    )
    lang = st.session_state.language
    st.write(SIDEBAR_TEXT[lang]['welcome'])
    st.write(SIDEBAR_TEXT[lang]['desc'])
    st.markdown(f"[{SIDEBAR_TEXT[lang]['website']}](https://www.upwaygroup.com)")
    st.markdown(f"[{SIDEBAR_TEXT[lang]['linkedin']}](https://www.linkedin.com/company/upwayglobal)")
    st.markdown(f"[{SIDEBAR_TEXT[lang]['twitter']}](https://twitter.com/upwayglobal)")
    st.button(SIDEBAR_TEXT[lang]['switch'], on_click=toggle_language)

    st.selectbox(
        SIDEBAR_TEXT[lang]['select'],
        PAGE_KEYS,
        format_func=lambda x: PAGE_NAMES[lang][PAGE_KEYS.index(x)],
        key="page_selection"
    )

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
