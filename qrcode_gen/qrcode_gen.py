import qrcode
import streamlit as st
from PIL import Image
import io

st.title('Streamlit QR Code Web App')

title = st.text_input('Enter text to generate QR code', 'http://mingsung.net')

def load_data(message):
    qr = qrcode.QRCode()
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
img = load_data(title)

buf = io.BytesIO()
img.save(buf)
byte_im = buf.getvalue()
st.image(byte_im, caption='Streamlit QR code Generator Web App')