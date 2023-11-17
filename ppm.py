def save_image_p6(width, height, fname, pixels):
    max_val = 255

    print(f" Saving image {fname}: {width} x {height}")
    with open(fname, "wb") as fp:
        fp.write(b'P6\n')
        fp.write(f'{width} {height}\n'.encode('ascii'))
        fp.write(f'{max_val}\n'.encode('ascii'))

        for j in range(height):
            fp.write(bytes(pixels[j * width * 3 : (j + 1) * width * 3]))

def save_image_p3(width, height, fname, pixels):
    max_val = 255

    print(f" Saving image {fname}: {width} x {height}")
    with open(fname, "w") as fp:
        fp.write('P3\n')
        fp.write(f'{width} {height}\n')
        fp.write(f'{max_val}\n')

        k = 0
        for j in range(height):
            for i in range(width):
                fp.write(f' {pixels[k]} {pixels[k+1]} {pixels[k+2]}')
                k += 3
            fp.write('\n')
