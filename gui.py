import PySimpleGUI as sg

sg.theme("Topanga")

feet_text = sg.Text("Enter feet")
inches_text = sg.Text("Enter inches")
feet_input = sg.InputText(tooltip="Enter feet", key="feets")
inches_input = sg.InputText(tooltip="Enter inches", key="inches")
convert_button = sg.Button("Convert")
result_text = sg.Text(key="result_text")
exit_button = sg.Button("Exit")

layout = [[feet_text, feet_input], [inches_text, inches_input], [convert_button, exit_button, result_text]]

window = sg.Window("Convertor", layout=layout)


while True:

    event, values = window.read()
    print(event, values)

    if event == "Convert":
        result = str(round((float(values['inches']) * 0.0254) + (float(values['feets']) * 0.3048), 2)) + " m"
        window['result_text'].update(value=result)
    elif event == "Exit":
        break
    elif event == sg.WIN_CLOSED:
        break
