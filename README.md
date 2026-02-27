# ASCII Image Generation (Without Using Converters)

## Project Description

This project demonstrates how to generate an ASCII image from any uploaded `.jpg` or `.png` file **without using any external ASCII converter libraries**.

The image is processed manually by:

- Reading image width and height
- Converting pixels to grayscale
- Measuring brightness (intensity distance)
- Mapping brightness values to ASCII characters
- Printing structured ASCII output

---

## How It Works

1. Convert image to grayscale  
2. Extract pixel brightness values (0–255)  
3. Map darker pixels → denser characters (`@`, `#`, `%`)  
4. Map lighter pixels → thinner characters (`.`, ` `)  
5. Adjust output width to maintain aspect ratio  


---

## Why This Approach?

- No external ASCII converter libraries  
- Full control over brightness-to-character mapping  
- Adjustable width scaling  
- Terminal friendly  
- GitHub Markdown compatible  
