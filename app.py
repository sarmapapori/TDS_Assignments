import streamlit as st

def app():
    st.title("Find the largest number")
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
    num3 = st.number_input("Enter the third number")
    if st.button("Find largest number"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is {largest_number}")
        
def find_largest_number(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3
