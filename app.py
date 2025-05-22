import streamlit as st
import pandas as pd
from spread import spread_page
from equity import equity_page
from margin import margin_page
from Arbitrage import arbitrage_page
from TOO import pending_order_page
from SST import scalping_vs_swing_trading_page
from Pitfalls import pitfalls_page

# Language switcher
if 'language' not in st.session_state:
    st.session_state.language = 'en'  # Default language is English

# Function to toggle language
def toggle_language():
    if st.session_state.language == 'en':
        st.session_state.language = 'zh'
    else:
        st.session_state.language = 'en'

# Add a language toggle button in the sidebar

with st.sidebar:
    # Display Company logo
    st.image('https://www.sequoiacap.com/wp-content/uploads/sites/6/2021/12/Upway_Logo_RGB_Electric_Blue.png', use_container_width=True)  # Company logo

    # Welcome text and links
    st.write("### Welcome to Upway Global!")  
    st.write("Upway Global is a leading company in financial technologies. We provide cutting-edge solutions for trading and market analysis.")
    st.markdown("[Visit our website](https://www.upwaygroup.com)")  # Website link
    st.markdown("[Follow us on LinkedIn](https://www.linkedin.com/company/upwayglobal)")  # LinkedIn link
    st.markdown("[Follow us on Twitter](https://twitter.com/upwayglobal)")  # Twitter link


st.sidebar.button("Switch to 中文" if st.session_state.language == 'en' else "Switch to English", on_click=toggle_language)

page_selection = st.sidebar.selectbox(
    "Select Page" if st.session_state.language == 'en' else "选择页面",
    ["Spread", "Balance & Equity", "Margin", "Swap", "Types of Orders", "Scalping vs. Swing Trading", "Pitfalls","NOP","Short & Long position", "Arbitrage","Lot"]  
)

if page_selection == "Spread":
    spread_page()

elif page_selection == "Equity":
    equity_page()  

elif page_selection == "Margin":
    margin_page() 

elif page_selection == "Arbitrage":
    arbitrage_page()

elif page_selection == "Type of Orders":
    pending_order_page()

elif page_selection == "Scalping vs. Swing Trading":
    scalping_vs_swing_trading_page()

elif page_selection == "Pitfalls":
    pitfalls_page()

