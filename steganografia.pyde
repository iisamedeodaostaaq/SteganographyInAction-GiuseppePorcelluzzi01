dimQuad=50
altezzaImg=500
larghezzaImg=500
img=createImage(altezzaImg,larghezzaImg,RGB)
img.loadPixels()

def setup():
    size(altezzaImg,larghezzaImg)
    frase=[]
    frase= input('scrivi una frase')
    creaImmagine(frase)
    
#Apro una finestra di input per inserire una frase
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame,message)

    
def creaImmagine(frase):
    loadPixels() #funzione chiamata per caricare i pixel in un'immagine tramite un array
    pixel=0
    i=0
    lunghezza=len(frase) #variabile contenente la lunghezza dell'array
    while(i<lunghezza): #scorro l'array contenente la frase
        if(i<lunghezza): #con questi 3 if controllo se il numero di caratteri è multiplo di 3
            r=ord(frase[i]) # se lo è assegno alle variabili (r,g,b) il carattere corrispondente nella tabella ASCII
        else: 
            r=255   #altrimenti assegno il valore 255 della tabella ascii
        if(i+1<lunghezza):
            g=ord(frase[i+1])
        else:
            g=255
        if(i+2<lunghezza):
            b=ord(frase[i+2])
        else:
            b=255
        i=i+3 #ogni tre caratteri formano un pixel
        for j in range(dimQuad):
            for k in range(dimQuad):
                pixels[pixel+k+(larghezzaImg*j)] = color(r, g, b)   #inserisco ad ogni pixel il suo colore
        pixel=pixel+dimQuad                                         #ripeto quest' operazione per 50 volte
        if(pixel%larghezzaImg==0):                
            pixel=pixel+(larghezzaImg*(dimQuad-1))    #se ho finito una riga , il prossimo quadrato va posizionato alla riga successiva
        print r                                  
        print g
        print b
        
    while ((pixel/dimQuad)%larghezzaImg):
        for i in range(dimQuad):
                #per righe immagine
            for j in range(dimQuad):
                    #per  colonne immagine
                pixels[pixel+k+(larghezzaImg*j)]=color(0,0,0)
        pixel=pixel+dimQuad
        if (pixel%larghezzaImg==0):
                #se ho finito una riga , il prossimo quadrato va posizionato alla riga successiva 
            pixel=pixel+larghezzaImg*(dimQuad-1)
    updatePixels()                 #tramite questa funzione carico i pixel
    save("code.tiff")               #salvo l'immagine col nome out.tiffss
                


    


    



    

    
    

    
