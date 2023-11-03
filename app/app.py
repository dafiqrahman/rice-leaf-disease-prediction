import streamlit as st
import keras
from functions.predict import predict
from PIL import Image
from functions.disease_desc import disease_desc
import os
# make it center
st.markdown("""
<style>
.center {
    text-align: center;
}
            
.fs-2 {
    font-size: 2rem;
}
.green {
    color: #3ECF0E;
}
.red {
    color: #CD0E3E;
}
</style>
""", unsafe_allow_html=True)
coll1, coll2, coll3 = st.columns([1, 1, 1])
with coll1:
    st.write("")
with coll2:
    logo = Image.open('app/assets/logo app.png')
    st.image(logo,)
with coll3:
    st.write("")
st.markdown('<h2 class="center"> Aplikasi Deteksi Penyakit pada Tanaman Padi </h2>',
            unsafe_allow_html=True)


@st.cache_resource
def load_model():
    model = keras.models.load_model('app/mobilenetv2')
    return model


model = load_model()
# Add a selectbox to the sidebar:
img_input = st.file_uploader("Upload Image", type=["jpg", "png"])

if img_input is not None:
    # make image centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        st.image(img_input, width=300)
    with col3:
        st.write("")
    # img_input to image
    image = Image.open(img_input)
    prediction, class_name = predict(model, image)
    st.markdown(prediction, unsafe_allow_html=True)
    if class_name != 'Padi Sehat':
        st.markdown(
            f"<h3> <br> Deskripsi {class_name}", unsafe_allow_html=True)
        description, solution, reference = disease_desc(class_name)
        st.markdown(description, unsafe_allow_html=True)
        st.markdown(
            f"<h3> <br> Solusi", unsafe_allow_html=True)
        st.markdown(solution, unsafe_allow_html=True)
        st.markdown(
            f"<h3> <br> Referensi", unsafe_allow_html=True)
        st.markdown(reference, unsafe_allow_html=True)
