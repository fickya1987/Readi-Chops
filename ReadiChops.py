import pandas as pd 
import streamlit as st
import time
import joblib 
import warnings
warnings.filterwarnings('ignore')

# Define a dictionary to map items to their prices
item_prices = {
    "Chicken & chips": 2500,
    "Shawarma(single)": 2000,
    "Shawarma(double)": 2500,
    "Croaker Fish & Chips": 6000,
    "Spaghetti & Turkey": 3000,
    "Spaghetti & Chicken": 2500
}


# Define delivery locations and their prices
delivery_locations = {
    "Within Yaba": 1000,
    "Mainland": 2000,
    "Island": 4000
}

# Define your menu items
menu_items = ["Chicken & chips", "Shawarma(single)", "Shawarma(double)", "Croaker Fish & Chips", "Spaghetti & Turkey", "Spaghetti & Chicken"]

#Add Header and Sub Header
st.markdown("<h1 style = 'color: #337357 text-align: center; font-size: 55px; font-family: Cambria'>READI CHOPS GRILL SPOT</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Discover Flavor, Indulge In Quality</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

#Add An Image
st.image('Readichops logo-1-1.png', width = 600,  caption = 'Built By Joshua')

st.header('Description of Business',divider = True)
st.write("Readi Chops is a vibrant grill and food business that prides itself on serving up delicious, hearty meals with a modern twist. Specializing in grills and flavorful sides, Readi Chops offers a diverse menu featuring everything from succulent Grilled fish, Turkey and Chicken to mouthwatering Shawarma and Stir Fry Spaghetti. With an emphasis on quality ingredients and innovative flavor combinations, Readi Chops is dedicated to providing customers with a memorable dining experience that leaves them coming back for more. Whether you're craving a classic barbecue feast or seeking out bold new flavors, Readi Chops has something to satisfy every appetite.")

st.markdown("<h2 style = 'color: #132043; text-align: center; font-family: montserrat '>Menu Overview</h2>", unsafe_allow_html = True)

# Create a scrolling marquee for menu items
menu_text = " | ".join(menu_items)
marquee_html = f"<marquee style='font-size: 20px; color: #132043; font-family: montserrat;' scrollamount='5'>{menu_text}</marquee>"
st.markdown(marquee_html, unsafe_allow_html=True)


#To add anything to the side bar of the page
st.sidebar.image('pngwing.com (3).png')

#To add space to the sidebar before adding writeup to give line spaace
st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)



# Selectbox to choose menu items while Multiselect to choose more than one item 
# Multiselect to choose menu items
selected_item = st.sidebar.multiselect("Select Items To Order", ["Chicken & chips", "Shawarma(single)", "Shawarma(double)", "Croaker Fish & Chips", "Spaghetti & Turkey", "Spaghetti & Chicken"])

# Display the price of the selected item in the sidebar
# if selected_item:
#     st.sidebar.write(f"Price: {item_prices[selected_item]}")  ........This is to make a selection and show the price alone on sidebar

# Delivery or Pickup option
delivery_option = st.sidebar.radio("Delivery or Pickup", ("Delivery", "Pickup"))

# If delivery is chosen, display dropdown for delivery locations
if delivery_option == "Delivery":
    delivery_location = st.sidebar.selectbox("Select Delivery Location", list(delivery_locations.keys()))

# Display the selected items and their prices in the main section
if selected_item:
    st.subheader("Selected Items")
    total_price = 0
    for item in selected_item:
        # Check if the selected item exists in the item_prices dictionary
        if item in item_prices:
            price = item_prices[item]
            st.write(f"- {item}:_________________________#{price}")
            total_price += price
        else:
            st.write(f"- {item}: Item not available")

 # Add delivery cost if applicable
    if delivery_option == "Delivery":
        delivery_cost = delivery_locations.get(delivery_location, 0)
        st.write(f"- Delivery ({delivery_location}):________________________#{delivery_cost}")
        total_price += delivery_cost

 #This is the Total Price which is inclusive of The selected items and delivery if applicable     
    st.subheader("Total Price")
    st.write(f"#{total_price}")


st.markdown("<br>", unsafe_allow_html= True)

# Feedback and Reviews
st.header('Feedback and Reviews', divider=True)

# Flag to control the visibility of the feedback form
show_feedback_form = st.checkbox("Leave Feedback")

# Display feedback form if checkbox is checked
if show_feedback_form:
    feedback = st.text_area("Leave your feedback or review here:")
    submit_button = st.button("Submit")

    if submit_button and feedback:
        # You can store the feedback in a database or simply display it
        st.success("Thank you for your feedback! Your review has been submitted.")
        # Clear the feedback form
        show_feedback_form = ""


st.markdown("<br>", unsafe_allow_html= True)

# Contact Information
st.header('Contact Information', divider=True)
st.write("For any inquiries or to place an order, feel free to contact us:")
st.write("- Phone: +2349073793284")
st.write("- Instagram: [Instagram](https://www.instagram.com/readichops.ng)")
st.write("- Email: readichops@gmail.com")
st.write("- Address: 12 Connal Road, Yaba, Lagos")