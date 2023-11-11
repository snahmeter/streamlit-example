import streamlit as st
import pandas as pd


def main():
    st.title("skill_views")
    st.dataframe(pd.read_csv('./players.csv'))

if __name__ == "__main__":
    main()
