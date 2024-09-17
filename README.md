# BMI Calculator App
## Overview
The BMI Calculator App is a Kivy-based application developed in Python that calculates and manages Body Mass Index (BMI). It features BMI calculation, data storage, and retrieval with classifications.
## Features
- **Calculate BMI**: Compute BMI from weight (in pounds) and height (in inches)
- **Store BMI Data**: Save and manage BMI data associated with individual names
- **Retrieve BMI Data**: Search and display stored BMI values and their classifications
- **Error Handling**: Effectively handles empty inputs, non-numeric values, and zero division errors
- **Custom Interface**: Utilizes Kivy for a clean, user-friendly interface
## Technologies
- **Python**: Programming language used for application logic.
- **Kivy**: Framework used for building the graphical user interface.
- **JSON**: Data format for storing and retrieving BMI information.
## Installation
### Prerequisites
- **Python 3.x**
- **Kivy library**
### Steps
1. **Clone the Repository:**
 `git clone https://github.com/yourusername/bmi-calculator-app.git`


2. **Navigate to the Project Directory:**
 `cd bmi-calculator-app`


3. **Install Dependencies:**
`pip install kivy`


4. **Run the Application:**
  `python main.py`


## Usage
1. **Input Data:**
   - Enter weight (in pounds) and height (in inches).
   - Click **Calculate BMI** to compute and display the BMI.
2. **Store BMI Data:**
    - Enter your name and click **Save BMI** to save the BMI.
3. **Retrieve BMI Data:**
    - Enter your name in the search bar and click **Search BMI** to view the stored BMI and its classification.
4. **Error Handling:**
    - **ZeroDivisionError:** Alerts if height is zero.
    - **TypeError:** Displays error for non-numeric inputs.
    - **Empty Input:** Notifies if any input fields are empty.
## Code Structure
- **main.py:** Contains the application logic and user interface
    - **build():** Configures the app’s title and background color.
    - **clickMe():** Calculates BMI from user inputs.
    - **accumulateBMI():** Saves BMI data to a JSON file.
    - **searchBMIWithName():** Retrieves and displays stored BMI data.
## Future Enhancements
- Add graphical representations of BMI ranges.
- Enable users to update or delete existing BMI records.
- Support additional units (kilograms and meters).
## License
This project is licensed under the MIT License. See [LICENSE](https://github.com/Nkhanal2002/BMICalculatorApp?tab=MIT-1-ov-file) for more information.

