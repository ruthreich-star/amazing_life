import streamlit as st
import pandas as pd
import numpy as np

def show_pets():
    st.write("Really this is working!")
    
    # Generate a sample DataFrame
    np.random.seed(42)
    pet_types = ["Panda", "Cat", "Dog", "Rabbit"]
    names = ["Mochi", "Luna", "Rex", "Bun", "Bamboo", "Fluffy", "Socks", "Hopper"]
    df = pd.DataFrame({
        "Pet Name": np.random.choice(names, 30),
        "Type": np.random.choice(pet_types, 30, p=[0.3, 0.2, 0.3, 0.2]),
        "Age": np.random.randint(1, 15, 30),
        "Cuteness": np.round(np.random.uniform(7, 10, 30), 1)
    })

    # User filter
    pet_type = st.multiselect("Choose pet type(s):", pet_types, default=pet_types)
    filtered = df[df["Type"].isin(pet_type)]

    st.dataframe(filtered, use_container_width=True)

    # Show stats and plot
    st.markdown(f"**Total pets shown:** {len(filtered)}")
    if not filtered.empty:
        st.bar_chart(filtered.groupby("Type")["Cuteness"].mean())

    if st.button("Show a random pet!"):
        pet = filtered.sample(1)
        st.success(
            f"Meet {pet['Pet Name'].values[0]}, a {pet['Age'].values[0]}-year-old {pet['Type'].values[0]}!"
        )
