import Image
import numpy as np
img = Image.open("DOC.jpeg")
a = np.array(img.convert(mode "1"))
blockLengthX = np.argmin(a[0]==a[0,0])
blockLengthY = np.argmin(a[:,0]==a[0,0])
result = a[::blockLengthX, ::blockLengthY]
np.savetxt('test.txt', result)
