# Step-by-step
# Step 1: Import database
# Step 2: View database
# Step 3: Fix database issues/errors
# Step 4: Churn analysis
# Step 5: Analysis of churn causes (how do columns impact churn?)

# Project step-by-step
# Step 1: Import the database
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")

# Step 2: View the database
tabela = tabela.drop(columns="CustomerID")
print(tabela)  # Changed from display to print
# useless columns - information that doesn't help you, it gets in the way

# Step 3: Fix database issues/errors
print(tabela.info())  # Changed from display to print
# empty values - delete rows containing empty values
tabela = tabela.dropna()

print(tabela.info())  # Changed from display to print

# Step 4: Initial churn analysis

# how many people canceled and how many did not
print(tabela["cancelou"].value_counts())  # Changed from display to print

# in percentage
print(tabela["cancelou"].value_counts(normalize=True))  # Changed from display to print

# Step 5: Analysis of churn causes (how database columns impact churn)
# charts/dashboards
import plotly.express as px
import plotly.io as pio

# Forces Plotly to open the charts in your default internet browser
pio.renderers.default = "browser"

# create the chart
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    # display the chart
    grafico.show()

# ALL monthly contract customers churn
    # offer discounts on annual and quarterly plans
# customers who call the call center more than 4 times churn
    # create a process to resolve customer issues in a maximum of 3 calls
# customers who delayed payment for more than 20 days churned
    # policy to resolve late payments within 10 days (finance team)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts())  # Changed from display to print
# in percentage
print(tabela["cancelou"].value_counts(normalize=True))  # Changed from display to print
