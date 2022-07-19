import streamlit as st
from streamlit_image_comparison import image_comparison

st.image("img/telescope.png", width=78)
"# Webb Compare"
"### Southern Ring Nebula 💍"
image_comparison("img/hubble/southern_nebula_1400.jpg", "img/webb/southern_nebula_1400.jpg", "Hubble", "Webb")
"### Carina Nebula 💃"
image_comparison("img/hubble/carina_1400.png", "img/webb/carina_1400.jpg", "Hubble", "Webb")
"### Galaxy Cluster SMACS 0723 🏘"
image_comparison("img/hubble/deep_field_1400.jpg", "img/webb/deep_field_1400.jpg", "Hubble", "Webb")
"### Stephan's Quintet 🖐"
image_comparison("img/hubble/stephans_quintet_1400.jpg", "img/webb/stephans_quintet_1400.jpg", "Hubble", "Webb")


# Alternative – smaller but more complicated
# st.image("img/telescope.png", width=78)
# st.title("Webb Compare")
# for name in ["southern_nebula", "carina", "deep_field", "stephans_quintet"]:
#     st.subheader(" ".join([part.capitalize() for part in name.split("_")]))
#     image_comparison(f"img/hubble/{name}_700.{'png' if name == 'carina' else 'jpg'}", f"img/webb/{name}_700.jpg")
    
