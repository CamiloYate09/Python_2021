import PySimpleGUI as sg
import vlc

controls = [sg.Button("Play"), sg.Button("Pause"), sg.Button("Stop")]

layout = [[sg.FileBrowse(key="-MP3-", enable_events=True)], controls]
player = None

window = sg.Window("MP3 Player", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WINDOW_CLOSED:
        break
    if event == "-MP3-":
        player = vlc.MediaPlayer(values['-MP3-'])
    if event == "Play" and player is not None:
        player.play()
    if event == "Pause" and player is not None:
        player.pause()
    if event == "Stop" and player is not None:
        player.stop()
window.close()

# # This is a sample Python script.
#
# # Press Mayús+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
