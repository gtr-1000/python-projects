# Customer Churn Analysis 📊❌

This project focuses on analyzing a customer database to identify the main reasons for cancellations (churn) and propose data-driven solutions to improve customer retention.

## 🚀 Project Overview
The main goal of this analysis is to find patterns among customers who canceled their services and establish actions to reduce the churn rate. By filtering out high-risk customer profiles, we simulated a significant reduction in the company's cancellation rate.

## 📁 Repository Structure
* **`dados.py`**: The clean Python script developed in VS Code with English documentation.
* **`analise_dados.ipynb`**: The Interactive Jupyter Notebook (Google Colab) displaying the data structures and outputs.
* **`cancelamentos.csv`**: The dataset containing customer metrics (contract type, calls, payment delays, etc.).
* **`ferramentas.txt`**: The requirements file containing all dependencies and libraries needed to run the project.

## 🛠️ Technologies & Libraries Used
* **Python 3**
* **Pandas**: For data manipulation and cleaning.
* **Plotly Express**: For data visualization and interactive histograms.

## 🔍 Key Insights & Business Rules Discovered
After analyzing the interactive charts, three major pain points were identified as the root causes of customer churn:

1. **Contract Type**: **100% of customers with Monthly contracts canceled their subscription.**
   * *Action:* Offer special discounts to migrate these users to Quarterly or Annual plans.
2. **Call Center Interaction**: **Customers who called the call center more than 4 times churned.**
   * *Action:* Implement a priority system to resolve customer support issues within a maximum of 3 calls.
3. **Payment Delays**: **Customers with late payments exceeding 20 days canceled their services.**
   * *Action:* Set a financial team trigger to resolve billing delays within 10 days.

## 📈 Results
By applying these three business rules to filter out high-risk profiles, the database simulation showed a massive drop in the cancellation rate, proving the impact of data-driven decisions on customer retention.

## 🔧 How to Run this Project
1. Clone this repository.
2. Create and activate your virtual environment (`venv`).
3. Install the required dependencies using the terminal:
   ```bash
   pip install -r ferramentas.txt
   ```
4. Run the script:
   ```bash
   python dados.py
   ```
