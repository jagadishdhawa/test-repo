import streamlit as st
def multiply_numbers(num1,num2):
    return num1*num2
def main():
    st.title("Multiplication App")
             
num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')

button_clicked = st.button("Multiply")

if button_clicked:
    result = multiply_numbers(num1,num2)
    st.write(f"The result of multiplying {num1} and {num2} is: {result}")

if __name__== "__main__":
    main()
