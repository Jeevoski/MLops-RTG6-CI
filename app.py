import subprocess
import sys

import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx


if __name__ == "__main__" and get_script_run_ctx() is None:
	subprocess.run([sys.executable, "-m", "streamlit", "run", __file__], check=False)
	raise SystemExit(0)

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# Calculate results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")