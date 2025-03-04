import streamlit as st
import numpy as np
import cv2
from PIL import Image
from image_processing import process_image, compress_image
from ui_helpers import display_images, get_download_link

# Streamlit UI
st.title("🖼️ Image Filtering and Enhancement App")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Convert uploaded image to OpenCV format
    image = Image.open(uploaded_file)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Select Filter
    filter_option = st.sidebar.radio(
        "Select Image Processing Technique:",
        ("Original", "Gaussian Blur", "Median Blur", "Histogram Equalization", "Sobel Edge Detection", "Canny Edge Detection")
    )

    # Process Image
    processed_image = process_image(image, filter_option)

    # Compression Options
    st.sidebar.header("Compression & Resizing")
    target_width = st.sidebar.number_input("Width", min_value=50, value=image.shape[1])
    target_height = st.sidebar.number_input("Height", min_value=50, value=image.shape[0])
    target_size_kb = st.sidebar.number_input("Target File Size (KB)", min_value=10, value=100)
    output_format = st.sidebar.selectbox("Output Format", ["JPEG", "PNG"], index=0)

    # Compress & Resize
    if st.sidebar.button("Apply & Download"):
        compressed_path = compress_image(image, target_width, target_height, target_size_kb, output_format)
        st.success("✅ Image Processed Successfully!")
        st.markdown(get_download_link(compressed_path, f"Download {output_format} Image"), unsafe_allow_html=True)

    # Display Images
    display_images(image, processed_image, filter_option)
