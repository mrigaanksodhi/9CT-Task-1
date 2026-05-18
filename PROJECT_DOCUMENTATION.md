# Phase 1: Identifying and Defining
## Requirements Outline

### Functional Requirements
#### Data Loading
- The system must be able to load the CSV file (breakfast.csv) using the Pandas library
- The system must display an error message if the CSV file is missing or in the wrong format
- The system must load the dataset automatically when the program starts, without the user needing to do anything

#### Data Cleaning
- The system must handle any missing values in the dataset without crashing
- The system must allow the user to filter data by country name
- The system must allow the user to filter data by individual food item

#### Data Analysis
- The system must be able to calculate the average price of the breakfast basket for each country
- The system must be able to calculate the average price of each individual food item across all months
- The system must display price changes across the 6 month period (October 2025 to March 2026)

#### Data Visualisation
- The system must display a line graph of all item prices for a selected country using Matplotlib
- The system must display a bar graph comparing the average breakfast basket price across all 20 countries using Matplotlib
- The system must display a line graph showing the price of a single food item across all 20 countries using Matplotlib
- All graphs must have a title, x axis label and y axis label

#### Data Reporting
- The system must print the full dataset to the terminal when requested by the user
- The system must print the hypothesis to the terminal when requested
- The dataset will remain stored in the original breakfast.csv file

---

## Non-Functional Requirements

### Usability
- The system must provide a clear text-based menu that is easy to navigate
- The system must display a list of valid country names and food items before asking the user to type one
- The system must include a README.md file that explains how to run the program and use each menu option
- Menu options must be numbered and the user should only need to type a single number to navigate

### Reliability
- The system must display a clear error message if the user types a country name that does not exist in the dataset
- The system must not crash if the user enters an invalid menu option — instead it should prompt them to try again
- The system must ensure the data loaded from the CSV matches the original dataset without any modifications

---

## Use Case

**Actor:** User

**Goal:** To access and interact with breakfast food price data through the program's text-based user interface.

**Preconditions:**
- The breakfast.csv dataset has already been loaded into the system via data_module.py
- The user has Python installed and is able to run main.py from the terminal

**Main Flow:**
1. User runs main.py and is presented with the text-based menu
2. User selects one of the following options:
   - a. View hypothesis — system prints the project hypothesis to the terminal
   - b. View full dataset — system prints all 120 rows of breakfast.csv to the terminal
   - c. View item prices for a country — user types a country name and system displays a bar graph of all food item prices for that country over 6 months
   - d. View all country basket prices — system displays a bar graph comparing average basket prices across all 20 countries
   - e. Select single food for all countries — user types a food item and system displays a line graph of that item's price across all 20 countries
3. System performs the requested action and outputs the result to the user
4. User is returned to the main menu after each action
5. User selects option 6 to exit the program

**Postconditions:**
- User has viewed and/or interacted with the breakfast price data
- The original dataset remains unchanged
- Data remains available for further queries within the same session

# Phase 2: Researching and Planning

## Research

### Articles and Sources

1. **SBS News (August 2025)**
"Prices don't go back: How did grocery costs see their biggest rise in five years?" [Article 1](https://www.sbs.com.au/news/article/grocery-costs-biggest-rise-five-years-inflation-eases/v8gxqf9zo). This article describes how due to inflation the cost of grocery items is increasing forcing shoppers to change their habits.

2. **Deakin University – Global Centre for Preventive Health and Nutrition (2025)**
"What can Australia do to prevent supermarket price gouging?[Article 2](https://healthyfoodretail.com/what-can-australia-do-to-prevent-supermarket-price-gouging/). "The article argues that recent food price inflation in Australia has been unusually high and may not be explained solely by supply-chain and global economic pressures. It talks about concerns that major supermarkets may have engaged in “greedflation” or excessive pricing by increasing prices beyond what rising costs justified.

## Discuss the findings
**Statement:**
The evidence suggests that Australian supermarkets have been raising prices beyond what inflation alone can justify, placing significant financial pressure on everyday Australian families.
**Explanation:** According to research from Deakin University's Global Centre for Preventive Health and Nutrition, food and beverage prices averaged around 6.6% inflation between 2021 and 2023, more than double the previous two decades. Staple items such as grains, milk and dairy rose even higher at around 10-12%, suggesting that price increases were not evenly distributed across all food categories. SBS News reported in August 2025 that the average weekly grocery bill for a family of four has risen 11% in a single year, from $216 to $240.
**Evidence:** Deakin University's research also highlighted the concept of "greedflation", where a Canadian study found that local farmers' markets raised prices less than mainstream grocery stores during the same period, even though they faced similar supply costs. This suggests that major supermarket chains are choosing to inflate prices rather than being forced to. SBS News further reported that over 80% of Australians have changed their shopping habits in the past year to try to reduce costs, with more than 61% now visiting two or more supermarkets each week.
**Conclusion:** Overall, both sources point to a clear pattern of grocery prices rising faster than general inflation in Australia, with Australian families bearing the financial burden. This supports the hypothesis that supermarkets in Australia are taking advantage of inflation to overcharge consumers on necessary goods.

## Points For and Against the Hypothesis

### For: Supermarkets are overcharging
- The Australia Institute found corporate profits significantly contributed to inflation between 2019 and 2022
- Staple item prices rose far above the general CPI rate — cheese up 27.3%, bread up 24.1%
- The Australian government introduced price gouging legislation specifically targeting Coles and Woolworths
- 77 percent of Australian households experienced food insecurity for the first time in 2023, according to Foodbank
- A Canadian study showed farmers' markets raised prices less than supermarkets despite facing the same costs

### Against: Supermarkets are not deliberately overcharging
- The ACCC's February 2025 inquiry found no direct evidence of price-fixing or collusion between Coles and Woolworths
- Supermarkets have argued that price increases are driven by higher fuel, storage and supply chain costs
- Under Australian law, businesses are legally allowed to set their own prices — raising prices is not inherently illegal
- Global factors such as COVID-19, climate events and international conflict have genuinely driven up food production costs worldwide

---

## Data Dictionary

| Column Name | Data Type | Description | Example |
|---|---|---|---|
| Country | String (Text) | The name of the country where prices were recorded | Australia |
| ISO_Country_Code | String (Text) | The 3-letter international country code | AUS |
| Month | String (Text) | The month the prices were recorded in YYYY-MM format | 2025-10 |
| Breakfast_Basket_USD | Float (Decimal) | The total cost of the full breakfast basket in US dollars | 12.37 |
| Milk (1L) USD | Float (Decimal) | The price of 1 litre of milk in US dollars | 1.73 |
| Bread (500g) USD | Float (Decimal) | The price of 500 grams of bread in US dollars | 2.75 |
| Eggs (12) USD | Float (Decimal) | The price of a dozen eggs in US dollars | 4.83 |
| Bananas (1kg) USD | Float (Decimal) | The price of 1 kilogram of bananas in US dollars | 3.33 |
| Oranges (1kg) USD | Float (Decimal) | The price of 1 kilogram of oranges in US dollars | 3.05 |
| Cheese (1kg) USD | Float (Decimal) | The price of 1 kilogram of cheese in US dollars | 9.86 |
| Tomatoes (1kg) USD | Float (Decimal) | The price of 1 kilogram of tomatoes in US dollars | 7.38 |
| Chicken (1kg) USD | Float (Decimal) | The price of 1 kilogram of chicken in US dollars | 9.35 |

### Dataset Parameters
- **Number of countries:** 20
- **Number of months:** 6 (October 2025 to March 2026)
- **Total rows:** 120 (20 countries x 6 months)
- **Total columns:** 12
- **Source:** Secondary research dataset
- **Currency:** All prices are recorded in US dollars (USD) to allow fair international comparison