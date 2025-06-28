import streamlit as st

st.title('Basic app for Power calculation')

st.write('Enter number to calculate its square, Cube and 5th power')

number = st.number_input('Enter an Integer', value=1, step=1)

square = number**2
cube = number**3
fifth_power = number**5

st.write(f'Square of the {number} is:  {square}.')
st.write(f'Cube of the {number} is:  {cube}.')
st.write(f'Fifth power of the {number} is:  {fifth_power}.')