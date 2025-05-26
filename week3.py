import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, pearsonr
import matplotlib.pyplot as plt

# 1. Data Generation
np.random.seed(42)
n = 100

# Define position categories with mean salary and standard deviation\ npositions = {
    'Doctor': (150000, 10000),
    'Engineer': (120000, 15000),
    'Manager': (100000, 10000),
    'Nurse': (80000, 8000),
    'Teacher': (60000, 7000)
}

# Education levels and conditional probabilities by position
edulevels = ['Bachelor', 'Master', 'PhD']
edup = {
    'Doctor': [0.1, 0.2, 0.7],
    'Engineer': [0.2, 0.6, 0.2],
    'Manager': [0.7, 0.3, 0.0],
    'Nurse': [0.8, 0.2, 0.0],
    'Teacher': [0.9, 0.1, 0.0]
}

# Generate random ages and positions\ nages = np.random.randint(25, 66, size=n)
pos_choices = np.random.choice(
    list(positions.keys()), size=n,
    p=[0.2, 0.3, 0.2, 0.2, 0.1]
)

# Assign education and compute salary incorporating age effect
education = []
salary = []
for i, p in enumerate(pos_choices):
    # Sample education level
    education.append(np.random.choice(edulevels, p=edup[p]))
    # Base salary adjustment for age
    base_mean, base_sd = positions[p]
    adjusted_mean = base_mean + (ages[i] - 45) * 1000
    salary.append(int(np.random.normal(adjusted_mean, base_sd)))

# Assemble DataFrame\ n
df = pd.DataFrame({
    'Age': ages,
    'Position': pos_choices,
    'Education': education,
    'Salary': salary
})

# 2. Contingency Analysis\ nct = pd.crosstab(df['Position'], df['Education'])
chi2, p_val, dof, expected = chi2_contingency(ct)
print(f"Chi-square = {chi2:.2f}, p = {p_val:.4e}")

# 3. Correlation Analysis\ nr, p_corr = pearsonr(df['Age'], df['Salary'])
print(f"Pearson r = {r:.2f}, p = {p_corr:.4e}")

# 4. Visualization\ nplt.figure()
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter Plot of Age vs. Salary')
plt.tight_layout()
plt.savefig('scatter_plot.png')