import pandas as pd

def calculate_demographic_data(/workspace/boilerplate-demographic-data-analyzer/.vscode
/workspace/boilerplate-demographic-data-analyzer/.gitignore
/workspace/boilerplate-demographic-data-analyzer/.gitpod.yml
/workspace/boilerplate-demographic-data-analyzer/adult.data.csv
/workspace/boilerplate-demographic-data-analyzer/demographic_data_analyzer.py
/workspace/boilerplate-demographic-data-analyzer/main.py
/workspace/boilerplate-demographic-data-analyzer/README.md
/workspace/boilerplate-demographic-data-analyzer/renovate.json
/workspace/boilerplate-demographic-data-analyzer/requirements.txt
/workspace/boilerplate-demographic-data-analyzer/test_module.py, print_data=True):
    # Read data from file
    df = pd.read_csv(/workspace/boilerplate-demographic-data-analyzer/.vscode
/workspace/boilerplate-demographic-data-analyzer/.gitignore
/workspace/boilerplate-demographic-data-analyzer/.gitpod.yml
/workspace/boilerplate-demographic-data-analyzer/adult.data.csv
/workspace/boilerplate-demographic-data-analyzer/demographic_data_analyzer.py
/workspace/boilerplate-demographic-data-analyzer/main.py
/workspace/boilerplate-demographic-data-analyzer/README.md
/workspace/boilerplate-demographic-data-analyzer/renovate.json
/workspace/boilerplate-demographic-data-analyzer/requirements.txt
/workspace/boilerplate-demographic-data-analyzer/test_module.py)

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[advanced_education]['salary'] == '>50K').mean() * 100

    # What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~advanced_education
    lower_education_rich = (df[no_advanced_education]['salary'] == '>50K').mean() * 100

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_people = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (min_hours_people['salary'] == '>50K').mean() * 100

    # 7. What country has the highest percentage of people that earn >50K?
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    country_total = df['native-country'].value_counts(normalize=True) * 100
    percentage_by_country = (country_salary / country_total).fillna(0) * 100
    highest_earning_country = percentage_by_country.idxmax()
    highest_earning_country_percentage = percentage_by_country.max()

    # 8. Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_salary['occupation'].mode()[0]

    # Print results if print_data is True
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", round(average_age_men, 1))
        print(f"Percentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: {round(higher_education_rich, 1)}%")
        print(f"Percentage without higher education that earn >50K: {round(lower_education_rich, 1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }