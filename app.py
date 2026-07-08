import streamlit as st
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing import image
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Pet Face Classification",
    page_icon="🐾",
    layout="centered"
)

st.sidebar.title("🐾 Pet Face Classification")

st.sidebar.info(
"""
### About

This AI model classifies pet images into five classes.

Supported Pets

🐱 Cats
🐶 Dogs
🦦 Ferrets
🐹 Hamsters
🐰 Rabbits

Built using

• TensorFlow
• MobileNetV2
• Streamlit
• NumPy
• Pillow
"""
)

model = tf.keras.models.load_model("pet_classifier.keras")

with open("class_names.pkl", "rb") as file:
    class_names = pickle.load(file)

st.title("🐾 Pet Face Classification")

st.write(
"""
Upload a pet image or capture one using your camera.

The AI model will identify the pet and display its confidence score.
"""
)

st.divider()

option = st.radio(
    "Choose Image Source",
    ["📁 Upload Image", "📷 Take Photo"]
)

uploaded_file = None

if option == "📁 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

else:

    uploaded_file = st.camera_input("Take a Photo")

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")

    st.image(
        img,
        caption="Selected Image",
        use_container_width=True
    )

    img_resize = img.resize((224, 224))

    img_array = image.img_to_array(img_resize)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = img_array / 255.0

    with st.spinner("AI is analyzing the image..."):

        prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = np.max(prediction) * 100

    st.success(f"🐾 Prediction : {predicted_class.capitalize()}")

    st.info(f"🎯 Confidence : {confidence:.2f}%")

    st.balloons()

    st.divider()

    st.subheader("Prediction Probability")

    probability = prediction[0]

    for i, name in enumerate(class_names):

        st.write(f"**{name.capitalize()}**")

        st.progress(float(probability[i]))

        st.write(f"{probability[i]*100:.2f}%")

    st.divider()

    st.subheader("Probability Table")

    df = pd.DataFrame({
        "Pet": class_names,
        "Probability (%)": [round(i * 100, 2) for i in probability]
    })

    st.dataframe(
        df,
        use_container_width=True
    )

st.divider()

st.markdown(
"""
<div style="
background-color:#f8f9fa;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 2px 10px rgba(0,0,0,0.1);
">

<h2 style="color:#2E86C1;">👨‍💻 Developed By</h2>

<h3 style="color:#000000;">
K. Rakesh Reddy
</h3>

<p style="font-size:18px;">
B.Tech - Computer Science & Engineering
</p>

<hr>

<h3 style="color:#2E86C1;">🛠️ Technologies Used</h3>

<p style="font-size:18px;">
🐍 Python <br>
🤖 TensorFlow <br>
🧠 MobileNetV2 <br>
🌐 Streamlit <br>
📊 NumPy <br>
🐼 Pandas <br>
🖼️ Pillow
</p>

<hr>

<p style="font-size:16px;color:gray;">
© 2026 K. Rakesh Reddy. All Rights Reserved.
</p>

</div>
""",
unsafe_allow_html=True
)