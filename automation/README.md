# Automated Product Registration Bot 🤖📦

This project features a Robotic Process Automation (RPA) bot developed in Python. It automates the tedious task of reading data from a product database and registering them one by one into a web-based ERP system.

## 🚀 Project Overview
The automation emulates human mouse and keyboard actions to navigate a web browser, perform secure user authentication, read a local CSV dataset, and loop through hundreds of inventory items to complete their registration forms.

## 📁 Repository Structure
* **`automacao.py`** (or your file name): The core Python automation script utilizing PyAutoGUI.
* **`produtos.csv`**: The local database containing code, brand, type, category, price, cost, and notes for all inventory products.
* **`ferramentas.txt`**: The requirements file listing the dependencies required to run the environment.

## 🛠️ Technologies & Libraries Used
* **Python 3**
* **PyAutoGUI**: For controlling mouse clicks, keyboard strokes, typing text, and browser page scrolling.
* **Pandas**: For reading, structural parsing, and iterating through the CSV database cleanly.
* **Time**: For handling critical delays and page loading sync steps.

## ⚙️ Key Automation Features
* **Built-in Fail-Safe**: Integrated `pyautogui.FAILSAFE = True`. If the bot behaves unexpectedly, moving the mouse cursor to any corner of the screen immediately triggers a system abort to protect your workstation.
* **Error Handling**: Custom exception layers catch manual user interruptions (`KeyboardInterrupt`) or safety triggers gracefully without crashing the shell.
* **Dynamic Typing Speeds**: Numerical fields (price and cost) utilize custom intervals to guarantee system field rendering without losing characters.

## 🔧 Workflow Architecture
1. **System Wake:** Triggers Windows shortcut menu, opens Microsoft Edge, and navigates to the target ERP address.
2. **Authentication:** Focuses the login element, types pre-configured credentials, and proceeds to the inner dashboard.
3. **Data Fetching:** Reads the `produtos.csv` file using a Pandas DataFrame.
4. **Registration Loop:** 
   * Clicks on the form container.
   * Maps dataset values into respective browser fields (Code, Brand, Type, Category, Price, Cost, Notes).
   * Submits data, triggers database wait timers, and scrolls up to recycle the sequence.

## 📦 How to Run this Project
1. Clone this repository.
2. Ensure you have the `produtos.csv` dataset inside the root folder.
3. Install dependencies from your terminal:
   ```bash
   pip install -r ferramentas.txt
   ```
4. Execute the script:
   ```bash
   python automacao.py
   ```
*⚠️ **Important Warning:** Do not move your mouse or use your keyboard while the automation is actively running, as it mirrors real hardware inputs.*
