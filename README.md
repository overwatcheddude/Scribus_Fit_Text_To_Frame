# Fit Text to Frame

This Python script is designed to work within the Scribus open-source desktop publishing software. It adjusts the font size of selected text frames to ensure the text fits within the frame boundaries.

## Requirements

- [Scribus](https://www.scribus.net/)

## How to Run
To run this script on Scribus, you need to follow these steps:
1. Download the script file `fit_text_to_frame.py` to your computer.
2. Open Scribus and create a new document or open an existing one.
3. Add a text frame to the document and enter some text.
4. Select the text frame by clicking on it with the mouse.
5. Click on `Script > Execute Script` in the Scribus menu.
6. In the file dialog that opens, select the `fit_text_to_frame.py` script file that you downloaded.

## How it Works

This script should be run from within Scribus. It will check if at least one text frame is selected. If no frame is selected, or if the selected frame is not a text frame, the script will display an error message and exit.

For each selected text frame, the script will:

1. Check if the frame is empty. If it is, an error message is displayed and the script moves on to the next frame.
2. Get the current font size of the text in the frame.
3. If the text overflows the frame, the script will decrease the font size until the text fits within the frame.
4. If the text does not overflow the frame, the script will increase the font size until it just fits within the frame. The maximum font size is assumed to be 1000 points.
5. The script will then decrease the font size by 1 point to ensure the text fits within the frame.

## Limitations

This script only works with text frames. Other types of frames are not supported. The script assumes that a maximum font size of 1000 points is reasonable. If your use case requires larger font sizes, you will need to modify the script.

## License

This script is released under the MIT license.