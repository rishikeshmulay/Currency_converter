import streamlit as st
import requests

st.title("Currency converter")
st.image("https://m.media-amazon.com/images/I/510WmeXkLXL.png",width=200)

#geeting full list of functions from api
def get_currency():
    url="https://open.er-api.com/v6/latest/USD"
    response=requests.get(url)
    data=response.json()

    if response.status_code==200 and data['result']=='success':
        return sorted(data['rates'].keys())
    else:
        return[]
    
currency=get_currency()

# UI Elements
amount=st.number_input("Enter the amount:", min_value=1,step=5)
from_currency=st.selectbox("From Currency", currency)
to_currency=st.selectbox("To Currency", currency)

#conversion logic
if st.button("convert"):
    if from_currency==to_currency:
        st.warning("Chooose diff currencies")
    else:
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response=requests.get(url)
        data=response.json()

        if response.status_code==200 and data['result']=="success":
            rate=data['rates'][to_currency]
            converted=amount*rate
            st.success(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
        else:
            st.error("target currency not found")
        
