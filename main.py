import Tkinter as tk

window = tk.Tk()
window.title("Joonas Project")

greeting = tk.Label(text = "Welcome, user! Would you like to contribute\nto this free and open source project?\n\n" \
"Please feel free to do so.\n\nRegards,\nJoonas, the creator of this project",
height = 9,
anchor = "w",
justify = "left")
greeting.grid(row = 0, column = 0)

calculatorInfo = tk.Label(text = "Below is my calculator which converts meters into \"Weird Joonas Units\".\n" \
"Weird Joonas Unit is my own weird unit of measurement that is\n" \
"basically meters divided by 256. The result must be an integer. If the\n" \
"last Weird Joonas Unit of the result is less than 256 m, then this must\n" \
"be indicated with the notification \"last unit not full\".\n" \
"Eg. 200 m = 1 WJU, because the result is 0.78125 but WJU must be\n" \
"an integer. For 200 m we need 1 WJU which is less than 256 m and\n" \
"therefore not a full unit.",
anchor = "w",
justify = "left")
calculatorInfo.grid(row = 1, column = 0, sticky = "w")

entry = tk.Entry(width = 10)
entry.grid(row = 2, column = 0)

calculationResult = tk.Label(text = "", anchor = "w", justify = "left")
calculationResult.grid(row = 3, column = 0, sticky = "w")

def enterMeterValue(event):
    metersInputText = entry.get()
    try:
        lastUnit = ""
        meters = float(metersInputText)
        WJUmodulo = meters % 256
        WJU = meters / 256
        if WJUmodulo != 0:
            if meters < 0:
                WJU = WJU - 1
            else:
                WJU = WJU + 1
            lastUnit = "\n(last unit not full)"
        WJU = int(WJU)
        WJUText = str(WJU)
        calculationResult["text"] = metersInputText + " m =\n" + WJUText + " Weird Joonas Units" + lastUnit
    except ValueError:
        print("invalid value")

entry.bind("<Return>", enterMeterValue)

window.mainloop()
