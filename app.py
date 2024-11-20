import streamlit as st

# Page Title
st.title("Comprehensive Profit-Sharing Calculator")
st.write("""
This tool helps you calculate profit-sharing bonuses for employees across all key roles in hospitality, 
including Front of House, Back of House, and Bartending teams.
""")

# Business Inputs
st.header("Business Inputs")
weekly_revenue = st.number_input("Weekly Revenue ($)", min_value=0, value=49000)
profit_margin = st.slider("Profit Margin (%)", min_value=0, max_value=100, value=30) / 100
bonus_pool_percentage = st.slider("Bonus Pool Percentage (%)", min_value=0, max_value=100, value=10) / 100

# Calculate profits and bonus pool
weekly_profit = weekly_revenue * profit_margin
bonus_pool = weekly_profit * bonus_pool_percentage

st.subheader(f"Weekly Profit: ${weekly_profit:.2f}")
st.subheader(f"Bonus Pool: ${bonus_pool:.2f}")

# Employee Role Inputs
st.header("Employee Roles and Contributions")
roles = [
    # Front of House Roles
    {"role": "Host", "weight": 1.0, "hours_worked": 40, "performance_score": 90},
    {"role": "Waiter", "weight": 1.1, "hours_worked": 40, "performance_score": 90},
    {"role": "Section Waiter", "weight": 1.2, "hours_worked": 40, "performance_score": 90},
    {"role": "Front of House Manager", "weight": 1.5, "hours_worked": 50, "performance_score": 90},
    # Back of House Roles
    {"role": "Head Chef", "weight": 1.5, "hours_worked": 50, "performance_score": 90},
    {"role": "Sous Chef", "weight": 1.3, "hours_worked": 45, "performance_score": 90},
    {"role": "Line Cook", "weight": 1.2, "hours_worked": 40, "performance_score": 90},
    {"role": "Dishwasher", "weight": 1.0, "hours_worked": 35, "performance_score": 85},
    # Bartending Roles
    {"role": "Bartender", "weight": 1.1, "hours_worked": 40, "performance_score": 90},
    {"role": "Barback", "weight": 1.0, "hours_worked": 35, "performance_score": 85},
    {"role": "Dispense", "weight": 1.0, "hours_worked": 30, "performance_score": 80},
]

# Dynamic Role Customization
for role in roles:
    role["hours_worked"] = st.number_input(
        f"Hours Worked: {role['role']}", min_value=0, max_value=60, value=role["hours_worked"]
    )
    role["weight"] = st.slider(
        f"Weight Factor: {role['role']}", min_value=0.5, max_value=2.0, step=0.1, value=role["weight"]
    )
    role["performance_score"] = st.slider(
        f"Performance Score: {role['role']}", min_value=0, max_value=100, step=5, value=role["performance_score"]
    )

# Calculate Total Score
total_score = sum(
    role["weight"] * role["hours_worked"] * role["performance_score"] for role in roles
)

# Calculate Shares and Display Results
st.header("Profit Sharing Results")
st.write("The bonus pool is distributed based on each role's contribution.")

results = []
for role in roles:
    weighted_score = role["weight"] * role["hours_worked"] * role["performance_score"]
    share_percentage = weighted_score / total_score
    individual_share = share_percentage * bonus_pool
    results.append({"Role": role["role"], "Share ($)": f"${individual_share:.2f}"})

# Display Results as a Table
st.table(results)