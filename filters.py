""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""
import random
from Cimpl import *
def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image
#EX 1
def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = r*0.299 + g*0.587 + b*0.114
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image
# The weighted grayscale has better image quality

#EX 2
def extreme_constrast(image):
    new_image = copy(image)
    for x, y, (r,g,b) in image:
        if r<=127:
            r=0
        else:
            r=255
        if g<=127:
            g=0
        else: 
            g=255
        if b<=127:
            b = 0
        else: 
            b = 255
        new_color = create_color(r ,g, b)
        set_color(new_image, x, y, new_color)    
    return new_image
#EX 3
def sepia_tint(image):
    new_image = copy(image)
    grayscaled_image = grayscale(new_image)
    for x, y, (r,g,b) in grayscaled_image:
        if r<=63:
            b = b*0.9
            r = r*1.1
        elif r>63 and r<=191:
            b = b*0.85
            r = r*1.15
        else:
            b = b*0.93
            r = r*1.08
        new_color = create_color(r ,g, b)
        set_color(grayscaled_image, x, y, new_color)
    return grayscaled_image
#EX 4
def _adjust_component(amount):
    if amount<=63:
        return 31
    elif amount>63 and amount<=127:
        return 95
    elif amount>127 and amount<=191:
        return 159
    elif amount>191 and amount<=255:
        return 233
#EX 5
def posterize(image):
    new_image = copy(image)
    for x, y, (r,g,b) in image:
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_color = create_color(r ,g, b)
        set_color(new_image, x, y, new_color)    
    return new_image    
#Lab 6: EX1
def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range (1, get_height(image) - 1):
        for x in range (1, get_width(image) - 1):
            top_r, top_g, top_b = get_color(image, x, y-1) 
            centre_r, centre_g, centre_b = get_color(image, x,y)
            contrast = math.fabs((top_r + top_g + top_b)/3 - (centre_r + centre_g + centre_b)/3)
            if contrast >= threshold:
                new_color = create_color(0,0,0)
                set_color(new_image, x,y-1,new_color)                
            else:
                new_color = create_color(255,255,255)
                set_color(new_image, x,y-1,new_color)
    return new_image
#Ex 2:
def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range (1, get_height(image) - 1):
        for x in range (1, get_width(image) - 1):
            top_r, top_g, top_b = get_color(image, x, y-1) 
            centre_r, centre_g, centre_b = get_color(image, x,y)
            right_r, right_g, right_b = get_color(image, x+1,y)
            contrast1 = math.fabs((top_r + top_g + top_b)/3 - (centre_r + centre_g + centre_b)/3)
            contrast2 = math.fabs((right_r + right_g + right_b)/3 - (centre_r + centre_g + centre_b)/3)
            if contrast1 >= threshold or contrast2 >= threshold:
                new_color = create_color(0,0,0)
                set_color(new_image, x,y-1,new_color)                
            else:
                new_color = create_color(255,255,255)
                set_color(new_image, x,y-1,new_color)
    return new_image
# this filter does a better job of edge detection compared to the one developed in EX 1
# Ex 3:
def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(image)):
    #     for x in range(0, get_width(image)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            top_left_red, top_left_green, top_left_blue = get_color(image, x-1,y-1)
            top_right_red, top_right_green, top_right_blue = get_color(image, x+1, y-1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(image, x-1,y+1)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(image, x+1, y+1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)

            # Average the red components of the nine pixels
            new_red = (top_red + top_left_red + top_right_red + left_red + bottom_red + bottom_left_red + bottom_right_red +
                       right_red + center_red ) // 9

            # Average the green components of the nine pixels
            new_green = (top_green + top_left_green + top_right_green + left_green + bottom_green + bottom_left_green + bottom_right_green +
                                   right_green + center_green ) // 9

            # Average the blue components of the nine pixels
            new_blue = (top_blue + top_left_blue + top_right_blue + left_blue + bottom_blue + bottom_left_blue + bottom_right_blue +
                                   right_blue + center_blue ) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target
# it does a better job at blurring than the one provided
def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x,y, (r,g,b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        random_row = 0
        random_column = 0
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10,10)
            rand2 = random.randint(-10,10) 
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = y+rand1
            random_row = x+rand2  
            
            # Determine if the random coordinates are in bounds.

            if (random_column >= 0 and random_column < get_height(image) and random_row >= 0 and random_row < get_width(image)):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        
        random_color = get_color(image, random_row, random_column)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, random_color)
                    
    # Return the scattered image.
    return new_image