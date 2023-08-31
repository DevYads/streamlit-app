import streamlit as st


def find_largest(num1, num2, num3):
    if num1 > num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3


def main():
    st.title("Largest Number App")

    st.write("Enter three number and Get largest among them.")

    n1 = st.number_input("Enter the first number:")
    n2 = st.number_input("Enter the second number:")
    n3 = st.number_input("Enter the third number:")

    if st.button('Get Largest'):
        largest = find_largest(n1, n2, n3)
        st.write(f"The largest number among {n1}, {n2}, {n3} is: {largest}")


if __name__ == "__main__":
    main()
