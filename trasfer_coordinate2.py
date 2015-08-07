from PIL import Image
i = Image.open("DOC.png")

pixels = i.load() # this is not a list
width, height = i.size
row_averages = []
for y in range(height):
    cur_row_ttl = 0
    for x in range(width):
        cur_pixel = pixels[x, y]
        cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
        cur_row_ttl += cur_pixel_mono
        print "x=", x, " y=", y, " pixel=", cur_pixel_mono 

    cur_row_avg = cur_row_ttl / width
    row_averages.append(cur_row_avg)

print "Brighest row:",
print max(row_averages)
