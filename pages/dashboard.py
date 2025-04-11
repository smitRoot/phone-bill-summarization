# import streamlit as st

# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background-image: url('file:///C:/Users/smit/Downloads/signupstreamlit/bg.png');  /* Forward slashes */
#         background-size: cover;
#         background-position: center center;
#         height: 100vh;docker run -p 8501:8501 streamlit-auth-app
#     }
#     </style>
#     """, unsafe_allow_html=True)
# if "authenticated" not in st.session_state or not st.session_state.authenticated:
#     st.warning("You must log in first!")
#     st.stop()
# else:       
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         st.write(f"Welcome, {st.session_state.get('username', '')}! 👋")
#     with col2:
#         if st.button("Logout"):
#             st.session_state.clear()
#             st.rerun()
# # Plans data
# # plans = [
# #     {"name": "Essentials Saver", "prices": [50, 80, 100, None], "premium_data": 50, "apple_tv_netflix": "no", "upgrade_ready": "no", "hulu_ads": "no"},
# #     {"name": "Go5G Next", "prices": [100, 170, 180, 225], "premium_data": float("inf"), "apple_tv_netflix": "yes", "upgrade_ready": "1", "hulu_ads": "yes"},
# #     {"name": "Go5G Plus", "prices": [90, 150, 150, 185], "premium_data": float("inf"), "apple_tv_netflix": "yes", "upgrade_ready": "2", "hulu_ads": "no"},
# #     {"name": "Essentials", "prices": [60, 90, 90, 105], "premium_data": 50, "apple_tv_netflix": "no", "upgrade_ready": "no", "hulu_ads": "no"},
# #     {"name": "Go5G", "prices": [75, 130, 130, 155], "premium_data": 100, "apple_tv_netflix": "conditions", "upgrade_ready": "no", "hulu_ads": "no"},
# #     {"name": "Essential4", "prices": [None, None, None, 100], "premium_data": 50, "apple_tv_netflix": "no", "upgrade_ready": "no", "hulu_ads": "no"}
# # ]




# plans = [
#     # T-Mobile Plans
#     {
#         'name': 'Essentials Saver',
#         'carrier': 'T‑Mobile',
#         'cost_per_line': [50, 80],  # Available for 1-2 lines only
#         'premium_data': 50,         # ~50GB premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': 'Go5G Next',
#         'carrier': 'T‑Mobile',
#         'cost_per_line': [90, 170, 225, 225],
#         'premium_data': float('inf'),  # Unlimited premium data
#         'upgrade_ready': True,           # Possibly upgrade-ready (e.g., 1‑yr)
#         'hulu_included': False
#     },
#     {
#         'name': 'Go5G Plus',
#         'carrier': 'T‑Mobile',
#         'cost_per_line': [100, 150, 185, 185],
#         'premium_data': float('inf'),  # Unlimited premium data (per some sources)
#         'upgrade_ready': True,           # Possibly upgrade-ready (e.g., 2‑yr)
#         'hulu_included': False
#     },
#     {
#         'name': 'Essentials',
#         'carrier': 'T‑Mobile',
#         'cost_per_line': [60, 100, 105, 105],
#         'premium_data': 50,         # ~50GB premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': 'Go5G',
#         'carrier': 'T‑Mobile',
#         'cost_per_line': [75, 140, 130, 130],
#         'premium_data': 100,        # ~100GB premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },

#     # Verizon Plans
#     {
#         'name': 'Welcome Unlimited',
#         'carrier': 'Verizon',
#         'cost_per_line': [65, 55, 40, 30],
#         'premium_data': 0,         # No premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': '5G Start',
#         'carrier': 'Verizon',
#         'cost_per_line': [70, 60, 45, 35],
#         'premium_data': 0,         # No premium data (deprioritized)
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': '5G Do More',
#         'carrier': 'Verizon',
#         'cost_per_line': [80, 70, 55, 45],
#         'premium_data': 50,        # 50GB premium data
#         'upgrade_ready': False,
#         'hulu_included': False  # Hulu not included (Disney+ & ESPN+ only)
#     },
#     {
#         'name': '5G Play More',
#         'carrier': 'Verizon',
#         'cost_per_line': [80, 70, 55, 45],
#         'premium_data': 50,        # 50GB premium data
#         'upgrade_ready': False,
#         'hulu_included': True     # Includes Disney+, Hulu, ESPN+
#     },
#     {
#         'name': '5G Get More',
#         'carrier': 'Verizon',
#         'cost_per_line': [90, 80, 65, 55],
#         'premium_data': 100,       # 100GB premium data
#         'upgrade_ready': False,
#         'hulu_included': True     # Includes Disney+, Hulu, ESPN+
#     },

#     # AT&T Plans
#     {
#         'name': 'Unlimited Starter',
#         'carrier': 'AT&T',
#         'cost_per_line': [65, 60, 45, 35],
#         'premium_data': 0,         # Deprioritized premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': 'Unlimited Extra',
#         'carrier': 'AT&T',
#         'cost_per_line': [75, 65, 50, 40],
#         'premium_data': 50,        # 50GB premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     },
#     {
#         'name': 'Unlimited Premium',
#         'carrier': 'AT&T',
#         'cost_per_line': [85, 75, 60, 50],
#         'premium_data': float('inf'),  # Unlimited premium data
#         'upgrade_ready': False,
#         'hulu_included': False
#     }
# ]

# # ------------------------------
# # Helper Functions
# # ------------------------------
# # Function to recommend a plan and get the recommended plan name and price
# # def recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads):
# #     valid_plans = [plan for plan in plans if (plan["premium_data"] >= premium_data_needed or plan["premium_data"] == float("inf")) and
# #                    (plan["apple_tv_netflix"] == apple_tv_netflix) and
# #                    (plan["upgrade_ready"] == upgrade_ready) and
# #                    (plan["hulu_ads"] == hulu_ads)]
    
# #     # Filtering out plans where price is None for the selected number of lines
# #     valid_plans = [plan for plan in valid_plans if plan["prices"][num_lines - 1] is not None]
    
# #     if not valid_plans:
# #         unlimited_plans = [plan for plan in plans if plan["premium_data"] == float("inf") and plan["hulu_ads"] == hulu_ads and plan["prices"][num_lines - 1] is not None]
# #         if unlimited_plans:
# #             cheapest_plan = min(unlimited_plans, key=lambda x: x["prices"][num_lines - 1])
# #             return cheapest_plan['name'], cheapest_plan['prices'][num_lines - 1]
# #         return None, None
    
# #     cheapest_plan = min(valid_plans, key=lambda x: x["prices"][num_lines - 1])
# #     return cheapest_plan['name'], cheapest_plan['prices'][num_lines - 1]
# # recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads)


# def recommend_plan(num_lines, premium_data_needed, upgrade_ready, hulu_ads, apple_tv_netflix):
#     valid_plans = [plan for plan in plans if (plan["premium_data"] >= premium_data_needed or plan["premium_data"] == float("inf"))
#                    and (plan["upgrade_ready"] == upgrade_ready)
#                    and (plan["hulu_included"] == hulu_ads)
#                    and (plan["apple_tv_netflix"] == apple_tv_netflix)]

#     # Ensure plan has pricing for the given number of lines
#     valid_plans = [plan for plan in valid_plans if len(plan["cost_per_line"]) >= num_lines and plan["cost_per_line"][num_lines - 1] is not None]
    
#     # If no exact match, suggest an unlimited data plan with Hulu
#     if not valid_plans:
#         unlimited_plans = [plan for plan in plans if plan["premium_data"] == float("inf")
#                            and plan["hulu_included"] == hulu_ads
#                            and plan["apple_tv_netflix"] == apple_tv_netflix
#                            and len(plan["cost_per_line"]) >= num_lines 
#                            and plan["cost_per_line"][num_lines - 1] is not None]

#         if unlimited_plans:
#             cheapest_plan = min(unlimited_plans, key=lambda x: x["cost_per_line"][num_lines - 1])
#             return cheapest_plan['name'], cheapest_plan['cost_per_line'][num_lines - 1]
        
#         return None, None

#     # Select the cheapest valid plan
#     cheapest_plan = min(valid_plans, key=lambda x: x["cost_per_line"][num_lines - 1])
#     return cheapest_plan['name'], cheapest_plan['cost_per_line'][num_lines - 1]


# # Streamlit UI for user input
# st.title("Plan Recommendation Form")

# # Number of lines with - and + button
# num_lines = st.number_input("Enter premium data needed (in GB)", min_value=1, value=1,max_value=4)

# # Premium data needed textbox
# premium_data_needed = st.number_input("Enter premium data needed (in GB)", min_value=0, value=5)

# # Apple TV/Netflix dropdown
# apple_tv_netflix = st.selectbox("Apple TV+  or Netflix?", ["yes", "no"])

# # Upgrade ready dropdown
# upgrade_ready = st.selectbox("Upgrade Ready?", ["no", "1", "2"])

# # Hulu Ads dropdown
# hulu_ads = st.selectbox("Hulu?", ["yes", "no"])

# # Current bill input
# current_bill = st.number_input("Current bill?", min_value=0, value=50)

# # # Submit button
# # if st.button("Get Recommendation"):
# #     recommended_plan_name, recommended_plan_price = recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads)
    
# #     if current_bill > recommended_plan_price:
# #         if recommended_plan_name is not None:
# #             st.write(f"The recommended plan is: {recommended_plan_name}")
# #             st.write(f"The recommended plan costs: ${recommended_plan_price}")
# #             savings = current_bill - recommended_plan_price
# #             st.write(f"You can save ${savings} by choosing this plan.")
# #     elif current_bill == recommended_plan_price:
# #             st.write("Your current bill is already the same as the recommended plan price.")
# #     elif current_bill<recommended_plan_price:
# #             st.write("You are already saving money.")
# #     else:
# #         st.write("No suitable plan found.")


# if st.button("Get Recommendation"):
#     recommended_plan_name, recommended_plan_price = recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads)

#     if recommended_plan_name is not None and recommended_plan_price is not None:
#         if current_bill > recommended_plan_price:
#             st.write(f"The recommended plan is: {recommended_plan_name}")
#             st.write(f"The recommended plan costs: ${recommended_plan_price}")
#             savings = current_bill - recommended_plan_price
#             st.write(f"You can save ${savings} by choosing this plan.")
#         elif current_bill == recommended_plan_price:
#             st.write("Your current bill is already the same as the recommended plan price.")
#         else:
#             st.write("You are already saving money.")
#     else:
#         st.write("No suitable plan found.")




import streamlit as st

# Original All Carriers Plan Table with proper values
# plans = [
#     {"provider": "T-Mobile", "name": "Essentials Saver", "cost_per_line": [None, 60, 90, 120, 150], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "T-Mobile", "name": "Go5G Next", "cost_per_line": [None, 95, 145, 195, 245], "premium_data": float("inf"), "apple_tv_netflix": False, "upgrade_ready": True, "hulu_included": False},
#     {"provider": "T-Mobile", "name": "Go5G Plus", "cost_per_line": [None, 105, 155, 190, 240], "premium_data": float("inf"), "apple_tv_netflix": False, "upgrade_ready": True, "hulu_included": False},
#     {"provider": "T-Mobile", "name": "Essentials", "cost_per_line": [None, 65, 105, 135, 160], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "T-Mobile", "name": "Go5G", "cost_per_line": [None, 80, 120, 160, 180], "premium_data": 100, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "Verizon", "name": "Welcome", "cost_per_line": [None, 70, 95, 125, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "Verizon", "name": "5G Start", "cost_per_line": [None, 75, 100, 130, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "Verizon", "name": "5G Do More", "cost_per_line": [None, 85, 120, 155, 180], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "Verizon", "name": "5G Play More", "cost_per_line": [None, 90, 130, 160, 190], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": True},
#     {"provider": "Verizon", "name": "5G Get More", "cost_per_line": [None, 100, 130, 170, 200], "premium_data": 100, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": True},
#     {"provider": "AT&T", "name": "Unlimited Starter", "cost_per_line": [None, 70, 95, 120, 150], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "AT&T", "name": "Unlimited Extra", "cost_per_line": [None, 80, 105, 140, 175], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
#     {"provider": "AT&T", "name": "Unlimited Premium", "cost_per_line": [None, 90, 120, 150, 190], "premium_data": float("inf"), "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False}
# ]



plans = [
    # T-Mobile Plans
    {"provider": "T-Mobile", "name": "Essentials Saver", "cost_per_line": [None, 50, 70, 100, 120], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G Next", "cost_per_line": [None, 95, 145, 195, 245], "premium_data": float("inf"), "apple_tv_netflix": True, "upgrade_ready": True, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G Plus", "cost_per_line": [None, 105, 155, 190, 240], "premium_data": float("inf"), "apple_tv_netflix": True, "upgrade_ready": True, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Essentials", "cost_per_line": [None, 65, 105, 135, 160], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G", "cost_per_line": [None, 80, 120, 160, 180], "premium_data": 100, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},

    # Verizon Plans
    {"provider": "Verizon", "name": "Welcome", "cost_per_line": [None, 70, 95, 125, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Start", "cost_per_line": [None, 75, 100, 130, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Do More", "cost_per_line": [None, 85, 120, 155, 180], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Play More", "cost_per_line": [None, 90, 130, 160, 190], "premium_data": 50, "apple_tv_netflix": True, "upgrade_ready": False, "hulu_included": True},
    {"provider": "Verizon", "name": "5G Get More", "cost_per_line": [None, 100, 130, 170, 200], "premium_data": 100, "apple_tv_netflix": True, "upgrade_ready": False, "hulu_included": True},

    # AT&T Plans
    {"provider": "AT&T", "name": "Unlimited Starter", "cost_per_line": [None, 70, 95, 120, 150], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "AT&T", "name": "Unlimited Extra", "cost_per_line": [None, 80, 105, 140, 175], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "AT&T", "name": "Unlimited Premium", "cost_per_line": [None, 90, 120, 150, 190], "premium_data": float("inf"), "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False}
]

# Function to recommend a plan
def recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads):
    valid_plans = [
        plan for plan in plans
        if (plan["premium_data"] >= premium_data_needed or plan["premium_data"] == float("inf"))
        and (plan["apple_tv_netflix"] == apple_tv_netflix)
        and (plan["upgrade_ready"] == upgrade_ready)
        and (plan["hulu_included"] == hulu_ads)
    ]

    # Ensure enough lines exist in the plan
    valid_plans = [plan for plan in valid_plans if len(plan["cost_per_line"]) > num_lines and plan["cost_per_line"][num_lines] is not None]

    if not valid_plans:
        return None, None, None  # No suitable plan found

    # Get the cheapest plan
    cheapest_plan = min(valid_plans, key=lambda x: x["cost_per_line"][num_lines])
    return cheapest_plan['provider'], cheapest_plan['name'], cheapest_plan['cost_per_line'][num_lines]

# Streamlit UI
st.title("📱 Mobile Plan Recommendation System")

# User inputs
num_lines = st.slider("👥 Number of Lines", min_value=1, max_value=4, value=2)
premium_data_needed = st.number_input("🌐 Required Premium Data (GB)", min_value=0, value=50)
apple_tv_netflix = st.checkbox("📺 Need Apple TV+ & Netflix?")
#apple_tv_netflix = st.selectbox("Apple TV+  or Netflix?", ["yes", "no"])
upgrade_ready = st.checkbox("🔄 Need Upgrade-Ready Feature?")
hulu_ads = st.checkbox("🎬 Need Hulu with Ads?")
current_bill = st.number_input("💰 Your Current Monthly Bill ($)", min_value=0, value=100)


# # Number of lines with - and + button
# num_lines = st.number_input("Enter premium data needed (in GB)", min_value=1, value=1,max_value=4)

# # Premium data needed textbox
# premium_data_needed = st.number_input("Enter premium data needed (in GB)", min_value=0, value=5)

# # Apple TV/Netflix dropdown
# apple_tv_netflix = st.selectbox("Apple TV+  or Netflix?", ["yes", "no"])

# # Upgrade ready dropdown
# upgrade_ready = st.selectbox("Upgrade Ready?", ["no", "1", "2"])

# # Hulu Ads dropdown
# hulu_ads = st.selectbox("Hulu?", ["yes", "no"])

# # Current bill input
# current_bill = st.number_input("Current bill?", min_value=0, value=50)






# Submit button
if st.button("🔍 Get Recommendation"):
    recommended_provider, recommended_plan_name, recommended_plan_price = recommend_plan(num_lines, premium_data_needed, apple_tv_netflix, upgrade_ready, hulu_ads)

    if recommended_plan_name is not None and recommended_plan_price is not None:
        if current_bill > recommended_plan_price:
            st.success(f"✅ The best plan for you: **{recommended_plan_name} ({recommended_provider})**")
            st.info(f"💰 Cost: **${recommended_plan_price}/month** for {num_lines} lines.")
            savings = current_bill - recommended_plan_price
            st.success(f"🎉 You can **save ${savings}** per month by switching!")
        elif current_bill == recommended_plan_price:
            st.warning("⚖️ Your current bill is already equal to the recommended plan price.")
        else:
            st.info("✅ You are already on a cheaper plan.")
    else:
        st.error("⚠️ No suitable plan found. Try adjusting your preferences.")
