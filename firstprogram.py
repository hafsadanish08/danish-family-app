import streamlit as st

# Title
st.title("👩‍👧 Danish Family Info Viewer")

# Name input
name = st.text_input("Enter name")

# Info input
operation = st.text_input(f"What info do you want of {name} (e.g., Age, Hobbies):")

# Data dictionary
data = {
    "Gulshan Azher": {
        "Age": 70,
        "Gender": "Female",
        "Date of Birth:": "13-April-1955",
        "Hobbies": ["Reading", "Gardening", "Photography"]
    },
    "Danish Wajih": {
        "Age": 43,
        "Gender": "Male",
        "Date of Birth:": "22-August-1982",
        "Hobbies": ["Gym", "Playing Cricket"]
    }
}

# Show result only if both inputs are filled
if name in data and operation in data[name]:
    result = data[name][operation]
    if isinstance(result, list):
        st.write(", ".join(result))
    else:
        st.write(result)
elif name and operation:
    st.error("Sorry! Name or info type not found.")