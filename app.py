import streamlit as st

st.set_page_config(layout="wide")
st.title("FAC ROADMAP and SECRETARY RECRUITMENT")
st.title("🍪 Cookie Policy")
st.write("We use cookies to improve your experience. Do you accept?")

if st.button("Yes, I accept cookies 🍪"):
    st.markdown(f"""
    <div style="text-align:center;">
        <h2> Get PRANKED! 😄</h2>
        <img src="https://i.imgflip.com/4/9txq7s.jpg" style="max-width:300px;">
        <p>ACCHA LAUNDE!</p>
        <video id="prank-video" width="100%" autoplay>
            <source src="https://shattereddisk.github.io/rickroll/rickroll.mp4" type="video/mp4">
        </video>
        <br><br>
        
    </div>
    <script>
    const vid = document.getElementById('prank-video');
    vid.muted = true; // start muted
    setTimeout(() => {{
        vid.muted = false; // unmute after 200ms
    }}, 200);
    </script>
    """, unsafe_allow_html=True)
