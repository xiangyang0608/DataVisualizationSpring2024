import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data

def load_data():
    data = pd.read_csv("cardio_train.csv", delimiter=';')
    # Convert age from days to years
    data['age_years'] = data['age'] / 365.25
    # Calculate BMI: weight (kg) / (height (m))^2
    data['bmi'] = data['weight'] / ((data['height'] / 100) ** 2)
    return data

df = load_data()
st.title("Cardiovascular Disease (CVD) Risk Factor Analysis")

# Sidebar filters
st.sidebar.title("Filters")
gender = st.sidebar.selectbox("Gender", options=[0, 1, 2], format_func=lambda x: "Male" if x == 2 else "Female" if x == 1 else "All")
age = st.sidebar.slider("Age Range", int(df['age_years'].min()), int(df['age_years'].max()), (50, 60))
# Add a BMI slider
bmi = st.sidebar.slider("BMI Range", float(df['bmi'].min()), float(df['bmi'].max()), (18.5, 24.9))

# Filter data based on selections
df_filtered = df[df['age_years'].between(age[0], age[1])]
if gender != 0:
    df_filtered = df_filtered[df_filtered['gender'] == gender]

# Now, also filter based on the BMI range
df_filtered = df_filtered[df_filtered['bmi'].between(bmi[0], bmi[1])]

colors = ['#374B4A', '#88D9E6'] 

# Blood Pressure Analysis with Bar Charts
st.header("Blood Pressure Analysis")
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Calculate the average blood pressure for each group
avg_bp = df_filtered.groupby('cardio')[['ap_hi', 'ap_lo']].mean().reset_index()

# Bar chart for Systolic and Diastolic using the updated colors
sns.barplot(x='cardio', y='ap_hi', data=avg_bp, ax=ax[0], palette=colors)
ax[0].set_title('Average Systolic Blood Pressure')
ax[0].set_xlabel('CVD')
ax[0].set_ylabel('Average Systolic BP (mmHg)')

sns.barplot(x='cardio', y='ap_lo', data=avg_bp, ax=ax[1], palette=colors)
ax[1].set_title('Average Diastolic Blood Pressure')
ax[1].set_xlabel('CVD')
ax[1].set_ylabel('Average Diastolic BP (mmHg)')

st.pyplot(fig)

color_dict = {0: '#374B4A', 1: '#88D9E6'}

# Cholesterol Bar Chart
st.header("Cholesterol Levels")
cholesterol_counts = df_filtered.groupby(["cholesterol", "cardio"]).size().unstack().fillna(0)
cholesterol_counts.plot(kind='bar', stacked=True, color=[color_dict[x] for x in cholesterol_counts.columns])
plt.title('Distribution of Cholesterol Levels')
plt.xlabel('Cholesterol Level')
plt.ylabel('Number of People')
plt.xticks(ticks=[0, 1, 2], labels=['Normal', 'Above Normal', 'Well Above Normal'], rotation=0)
st.pyplot(plt)

# Glucose Bar Chart
st.header("Glucose Levels")
glucose_counts = df_filtered.groupby(["gluc", "cardio"]).size().unstack().fillna(0)
glucose_counts.plot(kind='bar', stacked=True, color=[color_dict[x] for x in glucose_counts.columns])
plt.title('Distribution of Glucose Levels')
plt.xlabel('Glucose Level')
plt.ylabel('Number of People')
plt.xticks(ticks=[0, 1, 2], labels=['Normal', 'Above Normal', 'Well Above Normal'], rotation=0)
st.pyplot(plt)



