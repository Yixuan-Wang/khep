import marimo as mo

app = mo.App()

@app.cell
def _():
    import marimo as mo
    return

@app.cell
def _():
    first_button = mo.ui.run_button(label="Option 1")
    second_button = mo.ui.run_button(label="Option 2")
    [first_button, second_button]
    return

@app.cell
def _():
    if first_button.value:
        print("You chose option 1!")
    elif second_button.value:
        print("You chose option 2!")
    else:
        print("Click a button!")
    return
