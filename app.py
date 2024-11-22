import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openai

# OpenAI API Key for Portion GPT
openai.api_key = "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"

# Phase 1: Core Setup and Proportional Allocation

# Page Title
st.title("Portion Platform: Profit-Sharing Calculator")
st.write("Welcome to Portion! This platform helps you calculate and share profits efficiently, motivating your team to achieve their best.")

# Manager/Admin vs. Employee View Toggle
view_mode = st.sidebar.selectbox(
    "Choose View Mode",
    ["Manager/Admin View", "Employee View"]
)

# Sidebar Mode Selector (Casual vs Fine Dining)
if view_mode == "Manager/Admin View":
    st.sidebar.write("**Choose Venue Type**")
    dining_mode = st.sidebar.radio(
        "Restaurant Level:",
        ["Casual Dining", "Fine Dining"]
    )
else:
    st.sidebar.write("Welcome, Team Member!")
    st.sidebar.write("Your contributions make a big impact.")

# Phase 2: Business Inputs
st.header("Business Inputs")
weekly_revenue = st.number_input("Weekly Revenue ($)", min_value=0, value=80000)
profit_margin = st.slider("Profit Margin (%)", min_value=0, max_value=100, value=10) / 100
bonus_pool_percentage = st.slider("Bonus Pool Percentage (%)", min_value=0, max_value=100, value=10) / 100

# Calculate Profits and Bonus Pool
weekly_profit = weekly_revenue * profit_margin
bonus_pool = weekly_profit * bonus_pool_percentage
st.subheader(f"Weekly Profit: ${weekly_profit:.2f}")
st.subheader(f"Bonus Pool: ${bonus_pool:.2f}")

# Phase 3: Roles and Contributions
st.header("Employee Roles")
roles = [
    {"role": "Host", "hours_worked": 40},
    {"role": "Waiter", "hours_worked": 40},
    {"role": "Section Waiter", "hours_worked": 40},
    {"role": "Front of House Manager", "hours_worked": 50},
]

for role in roles:
    role["hours_worked"] = st.number_input(
        f"Hours Worked ({role['role']})", min_value=0, value=role["hours_worked"]
    )

# Phase 4: Proportional Allocation
total_hours = sum(role["hours_worked"] for role in roles)
results = []
shares = []
labels = []

for role in roles:
    share_percentage = role["hours_worked"] / total_hours if total_hours > 0 else 0
    individual_share = share_percentage * bonus_pool
    results.append({
        "Role": role["role"],
        "Hours Worked": role["hours_worked"],
        "Share (%)": f"{share_percentage * 100:.2f}%",
        "Share ($)": f"${individual_share:.2f}"
    })
    shares.append(share_percentage)
    labels.append(role["role"])

st.write("### Proportional Profit Sharing Table")
st.table(pd.DataFrame(results))

# Dynamic Pie Chart
st.write("### Bonus Pool Distribution (Pie Chart)")
fig, ax = plt.subplots()
ax.pie(shares, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
st.pyplot(fig)

# Phase 5: Team Achievements
if view_mode == "Employee View":
    st.write(f"Your contributions helped the team achieve a ${bonus_pool:.2f} bonus pool this month!")
else:
    st.write("Managers can see detailed team achievements here.")

# Template Management (Manager Only)
if view_mode == "Manager/Admin View":
    st.header("Template Management")
    template_action = st.selectbox("Choose Action", ["Create Template", "Load Template", "Delete Template"])
    if template_action == "Create Template":
        template_name = st.text_input("Template Name:")
        if st.button("Save Template"):
            st.write(f"Template '{template_name}' has been saved.")
    elif template_action == "Load Template":
        st.write("Select a saved template to load.")
    elif template_action == "Delete Template":
        st.write("Choose a template to delete.")

# Portion GPT Chat Functionality (Manager View)
if view_mode == "Manager/Admin View":
    st.header("Ask Portion GPT")
    st.write("Ask for advice or insights to improve profit-sharing!")
    user_query = st.text_input("Your Question:")
    if st.button("Get Suggestion"):
        if user_query:
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",  # Adjust engine version if needed
                    prompt=f"Portion GPT Assistant:\n{user_query}",
                    max_tokens=200,
                    temperature=0.7
                )
                # Display GPT's response
                st.write(f"Suggestion: {response['choices'][0]['text'].strip()}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question.")

# Save and Export Options
st.header("Export Options")
if st.button("Export Report"):
    st.write("Exporting report...")
    # Placeholder for actual export functionality
    st.write("Report exported successfully!")
