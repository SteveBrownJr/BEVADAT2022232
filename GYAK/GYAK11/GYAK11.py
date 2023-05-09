import numpy as np

# Hozz létre egy bemeneti "képet" (numpy array-t)  (5x5)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32
picture = np.array([[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0]], dtype=np.float32)
height, width = picture.shape[0], picture.shape[1]
# Hozz létre egy kernelt (numpy array-t)(3x3)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32

# Mentsd el két külön változóba a létrehozott "kép" (5x5)
# dimenzióinak méretét (height,width)
kernel = np.array([[0, 1, 0],[1, 0, 1],[0, 1, 0]],dtype=np.float32)

# Mentsd el két külön változóba a létrehozott kernel (3x3)
# dimenzióinak méretét (height,width)
kernelheight,kernelwidth = kernel.shape[0], kernel.shape[1]

# Számold ki a kimeneti "kép" dimenzióinak a méretét
Padding = 0
Stride = 1
# A magasságot és szélességet két külön változóba mentsd el
# NOTE: használd az előbb kiszámolt "kép" és kernel szélességet és magasságot
OutHeight = (height-kernelheight)+(Padding * 2)+Stride
OutWidth = (width-kernelwidth)+(Padding * 2)+Stride


# Hozz létre egy az előbb kiszámolt kimeneti "kép"
# dimenziójával megegyező 0-kal feltöltött numpy array-t
OutPicture = np.zeros(shape=(OutHeight,OutWidth),dtype=np.float32)

# Hajts végire konvolúciót a bemeneti "képen"
# az eredményt az előbb létrehozott kimeneti "képbe" mentsd el
# NOTE: a kimeneti "kép" 1 db pixel értéke a bemeneti kép n darab értékének összegéből jön létre (n = amennyi nem 0 érték van a kernelben)
for i in range(OutHeight):
    for j in range(OutWidth):
        OutPicture[i,j] = np.sum(picture[i:i+kernelheight,j:j+kernelwidth])


# printeld ki a bemeneti "képet", kernelt és a végeredményül kapott "képet"
print(f'kép:\n{picture}')
print(f'\nkernel:\n{kernel}')
print(f'\noutpicture:\n{OutPicture}')


# Ellenőrizd le, hogy tényleg jó működik a kódod (nem kell semmit írni, csak a printelt értékeket ellenőrizd le)