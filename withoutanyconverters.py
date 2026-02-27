from PIL import Image

OUTPUT_COLS = 200

img = Image.open("hitler.jpg")  # PNG/JPG supported
img_width, img_height = img.size

OUTPUT_ROWS = int(OUTPUT_COLS * img_height / img_width * 0.55)

row = 0
while row < OUTPUT_ROWS:

    col = 0
    while col < OUTPUT_COLS:

        x = int(col * img_width / OUTPUT_COLS)
        y = int(row * img_height / OUTPUT_ROWS)

        if x >= img_width:
            x = img_width - 1
        if y >= img_height:
            y = img_height - 1

        pixel = img.getpixel((x, y))

        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        # Distance-based intensity (NOT grayscale conversion)
        brightness = int(((r*r + g*g + b*b) ** 0.5) / 3)

        if brightness < 30:
            char = "@"
        elif brightness < 60:
            char = "#"
        elif brightness < 90:
            char = "%"
        elif brightness < 120:
            char = "+"
        elif brightness < 150:
            char = "="
        elif brightness < 180:
            char = "-"
        elif brightness < 210:
            char = "."
        else:
            char = " "

        print(char, end="")
        col += 1

    print()
    row += 1