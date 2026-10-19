
import pyautogui
import pandas as pd
import time


# Safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


try:
    # Open Microsoft Edge
    pyautogui.press("win")
    time.sleep(1)

    pyautogui.write("edge")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)

    # Open the website
    pyautogui.write(
        "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    )
    pyautogui.press("enter")
    time.sleep(3)

    # Log in
    pyautogui.click(x=895, y=531)
    pyautogui.write(123@123.com")
    pyautogui.press("tab")
    pyautogui.write("sua senha")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

    # Load the products table
    tabela = pd.read_csv("produtos.csv")

    # Register the products
    for linha in tabela.index:

        # Click the product code field
        pyautogui.click(x=758, y=360)

        # Enter the product code
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

        # Enter the brand
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")

        # Enter the product type
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")

        # Enter the category
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")

        # Enter the unit price
        preco = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.write(preco, interval=0.05)
        pyautogui.press("tab")
        time.sleep(0.3)

        # Enter the cost
        custo = str(tabela.loc[linha, "custo"])
        pyautogui.write(custo, interval=0.05)
        time.sleep(0.3)
        pyautogui.press("tab")

        # Enter the notes, if available
        obs = tabela.loc[linha, "obs"]

        if pd.notna(obs):
            pyautogui.write(str(obs))

        # Submit the product
        pyautogui.press("tab")
        pyautogui.press("enter")

        # Wait for the website to process the submission
        time.sleep(1)

        # Scroll up the page
        pyautogui.scroll(5000)
        

except pyautogui.FailSafeException:
    print("Automation stopped by the fail-safe mechanism.")

except KeyboardInterrupt:
    print("Automation stopped by the user.")
