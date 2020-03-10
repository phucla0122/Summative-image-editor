# SYSC 1005 A Fall 2018 Lab 7

from filters import *
from Cimpl import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """
    
    
    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

if __name__ == "__main__":
    check = False
    condition = True
    while condition ==True:
        print("L)oad")
        print("B)lur        E)dge detect      P)osterize        S)catter      T)int sepia")
        print("W)eighted grayscale      X)treme constrast")
        print("Q/uit")
        option = input(': ')        
        if option in ['L', 'B', 'E', 'P', 'S', 'T', 'W', 'X', 'Q']:
            if option =="L":
                img = get_image()
                show(img)
                check = True
            elif option =="B":
                if(check != True):
                    print('No image loaded')
                else:
                    img = blur(img)
                    show(img)
            elif option =='P':
                if(check != True):
                    print('No image loaded')
                else:
                    img = posterize(img)
                    show(img)            
            elif option == 'S':
                if(check != True):
                    print('No image loaded')
                else:
                    img = scatter(img)
                    show(img)
            elif option == 'T':
                if(check != True):
                    print('No image loaded')
                else:            
                    img = sepia_tint(img)
                    show(img)
            elif option == 'E':
                if(check != True):
                    print('No image loaded')
                else:            
                    threshold = int(input('Threshold?: '))
                    img = detect_edges_better(img, threshold)
                    show(img)
            elif option == 'T':
                if (check !=True):
                    print('No image loaded')
                else:
                    img = sepia_tint(img)
                    show(img)
            elif option == 'W':
                if (check != True):
                    print('No image loaded')
                else:
                    img = weighted_grayscale(img)
                    show(img)
            elif option == 'X':
                if (check != True):
                    print('No image loaded')
                else:
                    img = extreme_constrast(img)
                    show(img)
            else:
                condition = False
        else:
            print('No such command')
           
    
