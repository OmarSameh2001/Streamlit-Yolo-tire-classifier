from ultralytics import YOLO
from PIL import Image
from torchvision import transforms
import numpy as np
import streamlit as st
import webbrowser
from style import style


# Load Styling
style()

# Load the YOLO model
model = YOLO('v:/last.pt')

# Define the transformation
transform = transforms.Compose([transforms.Resize((640, 640)), transforms.ToTensor(), ])

# Create the Streamlit app
st.title("Tire Defects Classifier")

# Allow user to upload an image
file = st.file_uploader("Choose an image")


if file is not None:
    try:
        # Open and convert the image to RGB
        image = Image.open(file).convert('RGB')
        resize = transform(image)

        if image is not None:
            # Perform image classification
            results = model.predict(resize)

            # Grab the output from results
            classified = np.argmax(results[0].probs.data.tolist())
            tire_condition = results[0].names[classified]
            confidence = results[0].probs.data[classified] * 100

            # Display the detected tire class as a warning
            st.warning(f"Your tire is: {tire_condition}, With confidence: {confidence:.2f}%")

            # Display redirecting link
            if tire_condition == 'Defected':
                if st.button("Press here to be redirected to a specialist"):
                    webbrowser.open_new_tab("https://www.fitandfix.com")

            # Display the image
            print_image = image.resize((704, 500))
            st.image(print_image)

        else:
            st.warning("Unable to decode the uploaded image. Please upload a valid image file.")

    except Exception as e:
        st.warning(f"Error during image decoding: {e}")

else:
    st.warning("Please upload an image.")
