import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Placeholder data for demonstration
team_data = {
    "Name": ["Person 1", "Person 2", "Person 3", "Person 4"],
    "Role": ["Waiter", "Chef", "Bartender", "Host"],
    "Hours Worked": [35, 40, 30, 20],
    "Contribution (%)": [25, 30, 20, 15],
    "Bonus Earned ($)": [250, 300, 200, 150],
}

# Helper functions
def show_owner_dashboard():
    st.title("Owner Dashboard")
    st.subheader("Revenue and Profit Summary")
    revenue = 10000
    profit = 7500
    cog = 2500
    st.metric("Revenue", f"${revenue}")
    st.metric("Profit", f"${profit}")
    st.metric("Cost of Goods (COG)", f"${cog}")
    
    # Team Performance Summary
    st.subheader("Team Performance Overview")
    st.bar_chart(pd.DataFrame({
        "Team Contribution (%)": [25, 30, 20, 15],
    }, index=["Person 1", "Person 2", "Person 3", "Person 4"]))
    st.button("Download Report")

def show_manager_dashboard():
    st.title("Manager Dashboard")
    st.subheader("Team Analytics")
    df = pd.DataFrame(team_data)
    st.table(df)
    
    # Bonus Allocation
    st.subheader("Manage People")
    for i in range(len(df)):
        name = df.loc[i, "Name"]
        st.slider(f"Adjust Bonus Percentage for {name}", min_value=0, max_value=100, value=int(df.loc[i, "Contribution (%)"]))
        st.checkbox(f"Grant Manager Access to {name}")
    
    # Visualization
    st.subheader("Bonus Distribution")
    fig, ax = plt.subplots()
    ax.pie(df["Contribution (%)"], labels=df["Name"], autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

def show_employee_dashboard():
    st.title("Employee Dashboard")
    st.subheader("Your Contribution")
    st.metric("Hours Worked", "35 hours")
    st.metric("Contribution (%)", "25%")
    st.metric("Bonus Earned", "$250")
    
    # Team Progress
    st.subheader("Team Progress")
    st.progress(75)  # Team has reached 75% of their profit goal
    
    # Motivation
    st.success("You’ve reached 90% of your target hours this week. Great job!")
    st.info("Your team is 80% toward the bonus pool goal!")

# Main Application
def main():
    st.sidebar.title("Portion Dashboard")
    role = st.sidebar.selectbox("Select Your Role", ["Owner", "Manager", "Employee"])
    
    if role == "Owner":
        show_owner_dashboard()
    elif role == "Manager":
        show_manager_dashboard()
    elif role == "Employee":
        show_employee_dashboard()

if __name__ == "__main__":
    main()
