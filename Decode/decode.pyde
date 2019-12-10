immagine= loadImage("code.tiff") #carico l'immagine output di code
image(immagine,0,0) #posiziona l'immagine a cordinate x,y =0
loadPixels()                                  #funzione che converte la matrice dell'immagine in un vettore di pixel


frase=[]                                      
dimQuad=50                                 
lato_img=500                                 
size(500,500)


i=49                                          #metto l'indice del vettore a 49 perchè la matrice parte da 0
while pixels[i] != color(204,204,204):        #il ciclo continua finche non incontra il grigio di default 
    if pixels[i] != color(204,204,204):
        r=int(red(pixels[i]))                 #carico in r il numero del rosso
    if pixels[i] != color(204,204,204):
        g=int(green(pixels[i]))               #carico in g il numero del verde
    if pixels[i] != color(204,204,204):
        b=int(blue(pixels[i]))                #carico in b il numero del blu
    if pixels[i] != color(204,204,204):
        i=i+dimQuad                       #incremento i di 50 per passare al pixel successivo
    if(i%(lato_img-1)==0):                    #se la riga è finita carico il prossimo pixel nella riga successiva
        i=i+(lato_img*(dimQuad-1))
    frase.append(chr(r))                      #aggiungo alla lista frase i valori del codice ASCII convertiti in lettere
    frase.append(chr(g))
    frase.append(chr(b))

stringa=""
for ele in frase:                             #converto il vettore in una stringa e la stampo
    stringa += ele
print stringa
