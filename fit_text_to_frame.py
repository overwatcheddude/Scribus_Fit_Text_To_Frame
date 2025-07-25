import sys

try:
    import scribus
except ImportError:
    print("This script only works from within Scribus.")
    sys.exit(1)


try:
    scribus.haveDoc()
except NameError:
    print("This script only works from within Scribus.")
    sys.exit(1)


baselineWidth = 100.0  # mm
baselineFontSize = 47.6  # pt
ratio = baselineFontSize / baselineWidth


count = scribus.selectionCount()
if count == 0:
    scribus.messageBox("Error", "No frame selected")
    sys.exit(1)


for i in range(count):
    frame = scribus.getSelectedObject(i)
    try:
        scribus.getTextLength(frame)
    except scribus.WrongFrameTypeError:
        scribus.messageBox("Error", "Only text frames are supported")
        continue

    # get current frame width
    frameWidth, frameHeight = scribus.getSize(frame)

    desiredSize = frameWidth * ratio
    scribus.setFontSize(desiredSize, frame)

    while scribus.getTextLines(frame) > 1 and desiredSize > 0:
        desiredSize -= 0.1
        scribus.setFontSize(desiredSize, frame)
    # grow
    while scribus.textOverflows(frame) == 0 and scribus.getTextLines(frame) == 1:
        desiredSize += 0.1
        scribus.setFontSize(desiredSize, frame)

    desiredSize -= 0.1
    scribus.setFontSize(desiredSize, frame)

# refresh view
scribus.redrawAll()
