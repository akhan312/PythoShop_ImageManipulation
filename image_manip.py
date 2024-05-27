from pythoshop_exports import create_bmp, export_filter, export_tool, get_height, get_pixel_rgb, get_width, set_pixel_rgb
import random

@export_tool
def change_pixel(image, clicked_coordinate, color, **kwargs):
    x, y = clicked_coordinate
    set_pixel_rgb(image, (x, y), (color))

@export_filter
def mark_middle(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    mid_width= int(w/2)
    mid_height = int(h/2)
    change_pixel(image, (mid_width, mid_height), color, **kwargs)
    return

@export_filter
def mark_four_corners(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    set_pixel_rgb(image, (w - 1, h - 1), color)
    set_pixel_rgb(image, (w-1, 0), color)
    set_pixel_rgb(image, (0, h - 1), color)
    set_pixel_rgb(image, (0,0), color)

@export_filter
def mark_middle_with_t(image, color, **kwargs):
    w = int(get_width(image) / 2)
    h = int(get_height(image) / 2)
    for i in range(1, 2):
        set_pixel_rgb(image, (w, h),  color)
        set_pixel_rgb(image, (w+i, h), color)
        set_pixel_rgb(image, (w-i, h), color)
        set_pixel_rgb(image, (w, h-i), color)
        set_pixel_rgb(image, (w, h+i), color)

@export_tool
def draw_t(image, clicked_coordinate, color, **kwargs):
    x, y = clicked_coordinate
    set_pixel_rgb(image, (x,y), color)

    for i in range(1, 2):
        set_pixel_rgb(image, (x, y + i), color)
        set_pixel_rgb(image, (x, y -i), color)
        set_pixel_rgb(image, (x-i, y), color)
        set_pixel_rgb(image, (x+i, y), color)

@export_tool
def draw_hline(image, clicked_coordinate, color, **kwargs):
    w = get_width(image) - 1
    h = get_height(image) - 1
    x, y = clicked_coordinate
    for x in range (w):
        set_pixel_rgb(image, (x, y), color)

@export_tool
def draw_vline(image, clicked_coordinate, color, extra, **kwargs):
    w = get_width(image) - 1
    h = get_height(image) - 1
    x, y = clicked_coordinate
    for y in range (h):
        set_pixel_rgb(image, (x, y), color)

@export_filter
def draw_centered_hline(image, color, extra, **kwargs):
    w = get_width(image) - 1
    h = get_height(image) - 1
    mid_h = int(h / 2)
    thickness = int(extra)/2
    for x in range (w):
        for y in range(int(thickness)):
            set_pixel_rgb(image, (x, int(mid_h + y)), color)
            set_pixel_rgb(image, (x, mid_h), color)
            set_pixel_rgb(image, (x, int(mid_h - y)), color)

@export_filter
def draw_centered_vline(image, color, extra, **kwargs):
    w = get_width(image) - 1
    h = get_height(image) - 1
    mid_w = int(w / 2)
    thickness = int(extra)/2
    for x in range (h):
        for y in range(int(thickness)):
            set_pixel_rgb(image, (int(mid_w + y) , x), color)
            set_pixel_rgb(image, (mid_w, x), color)
            set_pixel_rgb(image, (int(mid_w - y), x), color)

@export_filter
def draw_bisecting_diagonals(image, color, **kwargs):
    return

@export_filter
def make_red(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            set_pixel_rgb(image, (row, pixel), (255, 0, 0))

@export_filter
def make_static(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            set_pixel_rgb(image, (row, pixel), (r, g, b))

@export_filter
def remove_red(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range (h):
        for pixel in range(w):
            r , g, b = get_pixel_rgb(image, (row, pixel))
            set_pixel_rgb(image, (row, pixel), (0, g, b))

@export_filter
def remove_blue(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range (h):
        for pixel in range(w):
            r , g, b = get_pixel_rgb(image, (row, pixel))
            set_pixel_rgb(image, (row, pixel), (r, g, 0))

@export_filter
def remove_green(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range (h):
        for pixel in range(w):
            r , g, b = get_pixel_rgb(image, (row, pixel))
            set_pixel_rgb(image, (row, pixel), (r, 0, b))

@export_filter
def lighten(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b, = get_pixel_rgb(image, (row, pixel))
            r = int(r*1.5)
            if r > 255:
                r = 255
            g = int(g * 1.5)
            if g > 255:
                g = 255
            b = int(b * 1.5)
            if b > 255:
                b = 255
            set_pixel_rgb(image, (row, pixel), (r, g, b))

@export_filter
def make_gray(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b = get_pixel_rgb(image, (pixel, row))
            s = round((r + g + b)/3)
            set_pixel_rgb(image, (pixel, row), (s, s, s))

@export_filter
def negate(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b = get_pixel_rgb(image, (pixel, row))
            r = (255-r)
            g = (255-g)
            b = (255-b)
            set_pixel_rgb(image, (pixel, row), (r, g, b))

@export_filter
def intensify(image,color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b = get_pixel_rgb(image, (pixel, row))
            if r > 255/2:
                r = 255
            elif r < 255/2:
                r = 0
            if g > 255/2:
                g = 255
            elif g < 255/2:
                g = 0
            if b > 255/2:
                b = 255
            elif b < 255/2:
                b = 0
            set_pixel_rgb(image, (pixel, row), (r, g, b))

@export_filter
def make_two_tones(image, color, **kwargs):

    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b = get_pixel_rgb(image, (pixel,row))
            if (r + g + b) / 3 > 122.5:
                r = 255
                g = 255
                b = 255
            if (r + g + b) / 3  < 122.5:
                r = 0
                g = 0
                b = 0
            set_pixel_rgb(image, (pixel, row), (r, g, b))
            
@export_filter
def make_four_tones(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    for row in range(h):
        for pixel in range(w):
            r, g, b = get_pixel_rgb(image, (pixel,row))
            if 186.25 < ((r + g + b) / 3) <= 255:
                r = 255
                g = 255
                b = 255
            if 122.5 < ((r + g + b) / 3) < 186.25:
                r = 170
                g = 170
                b = 170
            if 63.75 < ((r + g + b) / 3) < 122.5:
                r = 85
                g = 85
                b = 85
            if (r + g + b) / 3  < 63.75:
                r = 0
                g = 0
                b = 0
            set_pixel_rgb(image, (pixel, row), (r, g, b))

@export_filter
def make_better_two_tone(image, color, **kwargs):
    width = get_width(image)
    height = get_height(image)
    total_brightness = 0
    for row in range(height):
        for pixel in range(width):
            r, g, b = get_pixel_rgb(image, (pixel, row))
            total_brightness += (r+g+b) /3    
    total_pix = height * width
    average_brightness =  total_brightness / total_pix
    for row in range(height):
        for pixel in range(width):
            r, g, b = get_pixel_rgb(image, (pixel, row))
            if int((r+g+b)/3) > average_brightness:
                set_pixel_rgb(image, (pixel,row), (255,255,255))
            else:
                set_pixel_rgb(image, (pixel, row), (0,0,0))

@export_filter
def blend_other(image, other_image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    blended_image = create_bmp(w, h)
    for row in range(h):
        for pixel in range(w):
            r1, g1, b1 = get_pixel_rgb(image, (pixel,row))
            r2, g2, b2 = get_pixel_rgb(other_image, (pixel,row))
            blended_red = int((r1 + r2) / 2)
            blended_green = int((g1 + g2) / 2)
            blended_blue = int((b1 + b2) / 2)
            set_pixel_rgb(blended_image, (pixel, row), (blended_red, blended_green, blended_blue))

    return blended_image

@export_filter
def chroma_overlay(image, other_image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    blended_image = create_bmp(w, h)
    for row in range(h):
        for pixel in range(w):
            r1, g1, b1 = get_pixel_rgb(image, (pixel, row))
            r2, g2, b2 = get_pixel_rgb(other_image, (pixel, row))
            
            if r1 <=5 and b1<=5 and g1>=250:
                set_pixel_rgb(blended_image, (pixel, row), (r2, g2, b2))
            else:
                set_pixel_rgb(blended_image, (pixel, row,), (r1, g1, b1))
    return blended_image
            
@export_filter
def make_line_drawing(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    new_image = create_bmp(w-1, h)
    for y in range(h):
        for x in range(w-1):
            r, g, b = get_pixel_rgb(image, (x, y))
            r1, g1, b1 = get_pixel_rgb(image, ((x+1), y))
            
            if abs((int(r1+g1+b1)/3)-(int(r+g+b)/3)) >=10:
                set_pixel_rgb(new_image, (x,y), (0,0,0))
            else:
                set_pixel_rgb(new_image, (x,y), (255,255,255))
    return new_image
    

@export_filter
def mirror_left_horizontal(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    new_image = create_bmp(w, h)
    for x in range(int(w/2)):
        for y in range(h):
            r, g, b = get_pixel_rgb(image, (x,y))
            set_pixel_rgb(new_image, (x,y),(r,g,b))
            set_pixel_rgb(new_image, (w-1-x, y), (r,g,b))

    return new_image


@export_filter
def shrink(image, color, **kwargs):
    w = get_width(image)
    h = get_height(image)
    new_image = create_bmp(int(w/2), int(h/2))
    for x in range(0, w,2):
        for y in range(0, h,2):
            r, g, b = get_pixel_rgb(image, (x,y))
            set_pixel_rgb(new_image, (int(x/2),int(y/2)), (r, g, b))
    return new_image




    