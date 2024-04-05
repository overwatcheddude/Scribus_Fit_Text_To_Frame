import sys
try:
   import scribus
except ImportError:
   print("This script only works from within Scribus")
   sys.exit(1)

# check that the selection is one text frame and get that frame
frame_n = scribus.selectionCount()
if frame_n == 0 :
    scribus.messageBox('Error:', 'No frame selected')
    sys.exit(1)
elif frame_n > 1 :
    scribus.messageBox('Error:', 'You may select only one frame')
    sys.exit(1)

frame = scribus.getSelectedObject(0)
try:
    char_n = scribus.getTextLength(frame)
except scribus.WrongFrameTypeError:
    scribus.messageBox('Error:', 'You may only adjust text frames')
    sys.exit(1)

if char_n == 0:
    scribus.messageBox('Error:', 'You can\'t adjust an empty frame')
    sys.exit(1)

# get the current font size
font_size = scribus.getFontSize(frame)

# if the frame overflows, decrease the font size until it fits
while scribus.textOverflows(frame) > 0 and font_size > 0:
    font_size -= 1
    scribus.setFontSize(font_size, frame)

# if the frame doesn't overflow, increase the font size until it just fits
while scribus.textOverflows(frame) == 0 and font_size < 100:  # assuming 100 as the maximum reasonable font size
    font_size += 1
    scribus.setFontSize(font_size, frame)

# undo the latest 1pt step to ensure the text fits the frame
font_size -= 1
scribus.setFontSize(font_size, frame)