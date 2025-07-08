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
        "Date of Birth": "13-August-1980",
        "Hobbies": ["Reading", "Gardening", "Photography"]
    },
    "Danish Wajih": {
        "Age": 43,
        "Gender": "Male",
        "Date of Birth": "22-August-1982",
        "Hobbies": ["Gym", "Playing Cricket"],
    "Saira Danish":{
       "Age": 37,
        "Gender": "Female",
        "Date of Birth": "19-February- 1988",
        "Hobbies": ["Cooking", "Making YouTube videos"] ,
        "Hafsa Danish":
        "Age": 17
        "Gender" : "Female"
        "Date of Birth" : "3-April-2008"
        "Hobbies": ["Painting","Photography","Overthinking"],
         "Fatima Danish":
        "Age": 15
        "Gender" : "Female"
        "Date of Birth" : "14-July-2010"
        "Hobbies": ["Playing Roblox","Wasting time"
    ,"Making Pasta"],
    "Zainab Danish":
        "Age": 11
        "Gender" : "Female"
        "Date of Birth" : "25-June-2014"
        "Hobbies": ["Reading",""
    ,"Coding", "Cycling"],
      "Khadija Danish":
        "Age": 7 
        "Gender" : "Female"
        "Date of Birth" : "11-Nov-2017"
        "Hobbies": ["Playing with yahya",
    ,"Sleeping", "Drawing"],
      "Yahya Wajih":
        "Age": 3
        "Gender" : "Male"
        "Date of Birth" : "12-June-2021"
        "Hobbies": ["Cycling","Eating"
    ,"Teasing mother"]
        
        
        
    }

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
