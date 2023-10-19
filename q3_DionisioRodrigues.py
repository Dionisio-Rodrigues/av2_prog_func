from PIL import Image

factor = -100

img = Image.open('img.webp')
width, height = img.size

get_img_pixels = lambda width, height : [[img.getpixel((x, y)) for y in range (height)] for x in range (width)]
modified_img_pixels = lambda f, pixels: [
    [
        tuple(map(f, pixels[x][y]))

        if not (
            max(pixels[x][y], key=int) + factor > 255
            or min(pixels[x][y], key=int) + factor < 0
        )
        else pixels[x][y]

        for y in range(len(pixels[x]))
    ]
    for x in range(len(pixels))
]
m = modified_img_pixels (lambda x : x + factor, get_img_pixels (width, height))
put_pixels = lambda imginf : [[img.putpixel((x, y), imginf[x][y]) for y in range(len(imginf[x]))] for x in range (len(imginf))]
put_pixels(m)
img.save(f'img.webp')
