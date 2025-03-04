import streamlit as st
import numpy as np
import base64

def normalize_image(image):
    """Ensure the image is in the correct range [0, 255] and uint8 format."""
    if image.dtype != np.uint8:
        image = np.clip(image, 0, 255).astype(np.uint8)
    return image

def display_images(original, processed, filter_name):
    """Display original and processed images side by side."""
    processed = normalize_image(processed)  # Normalize before displaying

    col1, col2 = st.columns(2)
    with col1:
        st.image(original, caption="Original Image", width=300)
    with col2:
        st.image(processed, caption=f"{filter_name} Applied", width=300, clamp=True)

def get_download_link(file_path, text):
    """Generate a download link for the processed image."""
    with open(file_path, "rb") as file:
        file_bytes = file.read()
    encoded_file = base64.b64encode(file_bytes).decode()
    return f'<a href="data:file/image;base64,{encoded_file}" download="{file_path}">{text}</a>'


