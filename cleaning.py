#%% [markdown]
# ## Visual Assessment: Acquaint Yourself
# This Auralin Phase II clinical trial dataset comes in three tables: `patients`, `treatments`, and `adverse_reactions`. Acquaint yourself with them through visual assessment below.
#%% [markdown]
# ### Gather

#%%
import pandas as pd


#%%
patients = pd.read_csv('patients.csv')
treatments = pd.read_csv('treatments.csv')
adverse_reactions = pd.read_csv('adverse_reactions.csv')

#%% [markdown]
# ### Assess
# In the cells below, each column of each table in this clinical trial dataset is described. To see the table that goes hand in hand with these descriptions, display each table in its entirety by displaying the pandas DataFrame that it was gathered into. This task is the mechanical part of visual assessment in pandas.

#%%
# Display the patients table
patients

#%% [markdown]
# `patients` columns:
# - **patient_id**: the unique identifier for each patient in the [Master Patient Index](https://en.wikipedia.org/wiki/Enterprise_master_patient_index) (i.e. patient database) of the pharmaceutical company that is producing Auralin
# - **assigned_sex**: the assigned sex of each patient at birth (male or female)
# - **given_name**: the given name (i.e. first name) of each patient
# - **surname**: the surname (i.e. last name) of each patient
# - **address**: the main address for each patient
# - **city**: the corresponding city for the main address of each patient
# - **state**: the corresponding state for the main address of each patient
# - **zip_code**: the corresponding zip code for the main address of each patient
# - **country**: the corresponding country for the main address of each patient (all United states for this clinical trial)
# - **contact**: phone number and email information for each patient
# - **birthdate**: the date of birth of each patient (month/day/year). The [inclusion criteria](https://en.wikipedia.org/wiki/Inclusion_and_exclusion_criteria) for this clinical trial is  age >= 18 *(there is no maximum age because diabetes is a [growing problem](http://www.diabetes.co.uk/diabetes-and-the-elderly.html) among the elderly population)*
# - **weight**: the weight of each patient in pounds (lbs)
# - **height**: the height of each patient in inches (in)
# - **bmi**: the Body Mass Index (BMI) of each patient. BMI is a simple calculation using a person's height and weight. The formula is BMI = kg/m<sup>2</sup> where kg is a person's weight in kilograms and m<sup>2</sup> is their height in metres squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. *The [inclusion criteria](https://en.wikipedia.org/wiki/Inclusion_and_exclusion_criteria) for this clinical trial is 16 >= BMI >= 38.*

#%%
# Display the treatments table
treatments

#%% [markdown]
# 350 patients participated in this clinical trial. None of the patients were using Novodra (a popular injectable insulin) or Auralin (the oral insulin being researched) as their primary source of insulin before.  All were experiencing elevated HbA1c levels.
# 
# All 350 patients were treated with Novodra to establish a baseline HbA1c level and insulin dose. After four weeks, which isn’t enough time to capture all the change in HbA1c that can be attributed by the switch to Auralin or Novodra:
# - 175 patients switched to Auralin for 24 weeks
# - 175 patients continued using Novodra for 24 weeks
# 
# `treatments` columns:
# - **given_name**: the given name of each patient in the Master Patient Index that took part in the clinical trial
# - **surname**: the surname of each patient in the Master Patient Index that took part in the clinical trial
# - **auralin**: the baseline median daily dose of insulin from the week prior to switching to Auralin (the number before the dash) *and* the ending median daily dose of insulin at the end of the 24 weeks of treatment measured over the 24th week of treatment (the number after the dash). Both are measured in units (shortform 'u'), which is the [international unit](https://en.wikipedia.org/wiki/International_unit) of measurement and the standard measurement for insulin.
# - **novodra**: same as above, except for patients that continued treatment with Novodra
# - **hba1c_start**: the patient's HbA1c level at the beginning of the first week of treatment. HbA1c stands for Hemoglobin A1c. The [HbA1c test](https://depts.washington.edu/uwcoe/healthtopics/diabetes.html) measures what the average blood sugar has been over the past three months. It is thus a powerful way to get an overall sense of how well diabetes has been controlled. Everyone with diabetes should have this test 2 to 4 times per year. Measured in %.
# - **hba1c_end**: the patient's HbA1c level at the end of the last week of treatment
# - **hba1c_change**: the change in the patient's HbA1c level from the start of treatment to the end, i.e., `hba1c_start` - `hba1c_end`. For Auralin to be deemed effective, it must be "noninferior" to Novodra, the current standard for insulin. This "noninferiority" is statistically defined as the upper bound of the 95% confidence interval being less than 0.4% for the difference between the mean HbA1c changes for Novodra and Auralin (i.e. Novodra minus Auralin).

#%%
# Display the adverse_reactions table
adverse_reactions

#%% [markdown]
# `adverse_reactions` columns:
# - **given_name**: the given name of each patient in the Master Patient Index that took part in the clinical trial and had an adverse reaction (includes both patients treated Auralin and Novodra)
# - **surname**: the surname of each patient in the Master Patient Index that took part in the clinical trial and had an adverse reaction (includes both patients treated Auralin and Novodra)
# - **adverse_reaction**: the adverse reaction reported by the patient
# 
# Additional useful information:
# - [Insulin resistance varies person to person](http://www.tudiabetes.org/forum/t/how-much-insulin-is-too-much-on-a-daily-basis/9804/5), which is why both starting median daily dose and ending median daily dose are required, i.e., to calculate change in dose.
# - It is important to test drugs and medical products in the people they are meant to help. People of different age, race, sex, and ethnic group must be included in clinical trials. This [diversity](https://www.clinicalleader.com/doc/an-fda-perspective-on-patient-diversity-in-clinical-trials-0001) is reflected in the `patients` table.
# - Ensuring column names are descriptive enough is an important step in acquainting yourself with the data. 'Descriptive enough' is subjective. Ideally you want short column names (so they are easier to type and read in code form) but also fully descriptive. Length vs. descriptiveness is a tradeoff and common debate (a [similar debate](https://softwareengineering.stackexchange.com/questions/176582/is-there-an-excuse-for-short-variable-names) exists for variable names). The *auralin* and *novodra* column names are probably not descriptive enough, but you'll address that later so don't worry about that for now.

#%% [markdown]
# ### Quality
# #### `patients` table: 
# - zip code is a float instead of a string
# - zip code has four digits sometimes
# - Tim Neudorf height is 27 in instead of 72 in
# - state names sometimes full name, sometimes abbreviations
# - Dsvid Gustafsson should be David
# - Missing demographic information (address - contact columns)
# - Erroneous datatypes (assigned sex, state zip-code, and birthdate columns)
# - Multiple phone number formats
# - Default John Doe data
# - Multiple records for Jokobsen, Gersten, Taylor
# - kgs instead of lbs for Zaitseva weight
#
# #### `treatments` table: 
# - missing HbA1c changes
# - The letter "u" in starting and ending doses for Auralin and Novodra
# - given names and surnames are lowercase
# - missing records (280 instead of 350)
# - Erroneous datatypes (auralin and novodra columns)
# - Inaccurate HbA1c changes (4s mistaken as 9s)
# - Nulls represented as dashes ("-") in auralin and novodra columns
#
# #### `adverse_reactions` table:
# - given names and surnames are lowercase

#%% [markdown]
# ### Tidiness
# #### `patients` table:
# - `contact` column should be split into email address and phone number
# - `auralin` and `novodra` columns should be split into `treatment`, `start_dose` and `end_dose` columns
#
# #### `treatments` table:
# - `given name` and `surname` columns should be removed, replaced by `patient_id`
#
# #### `adverse_reactions` table:
# - `given name` and `surname` columns should be removed, replaced by `patient_id`
# - `adverse_reaction` column could be moved to `treatments` table, making this table negligible