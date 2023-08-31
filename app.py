import streamlit as st


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def main():
    st.title("Temperature Converter")

    option = st.selectbox("Enter conversion direction", ('Fahrenheit to Celsius', 'Celsius to Fahrenheit'))

    if option == 'Fahrenheit to Celsius':
        f_temp = st.number_input("Enter Fahrenheit Temperature")
        c_temp = fahrenheit_to_celsius(f_temp)
        st.write(f"{f_temp:.2f} °F is equal to {c_temp:.2f} °C")
    else:
        c_temp = st.number_input("Enter Celsius Temperature")
        f_temp = celsius_to_fahrenheit(c_temp)
        st.write(f"{c_temp:.2f} °C is equal to {f_temp:.2f} °F")


if __name__ == "__main__":
    main()
