# Fit Text to Frame

This Python script is designed to work within the Scribus open-source desktop publishing software. It adjusts the font size of text within a selected frame to fit on a single line.

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

This script should be run from within Scribus. It will check if at least one text frame is selected. If no frame is selected, or if the selected item is not a text frame, the script will display an error message and exit.

For each selected text frame, the script will perform the following actions to make the text fit on a single line:

1.  **Calculate Initial Font Size**: It calculates an initial font size based on the text frame's width and a predefined ratio.
2.  **Handle Multi-line Text**: If the text wraps to more than one line, the script will decrease the font size until all the text fits on a single line.
3.  **Optimize Font Size**: The script then increases the font size incrementally until the text fills the width of the frame without overflowing or wrapping to a new line.
4.  **Final Adjustment**: Finally, it reduces the font size by a very small amount (0.1 points) to ensure a perfect fit within the frame's boundaries.

## Limitations

This script is specifically designed to make text fit on a **single line**. If you apply it to a frame with multiple paragraphs or lines of text, it will shrink the text until it fits onto one line. It only works with text frames; other types of frames are not supported.

## License

This script is released under the MIT license.