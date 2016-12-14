from math import sqrt
import csv

def as_orientation(x, y, is_portrait=False):
    """Given an x and y, return in orientation specified by `is_portrait`."""
    if is_portrait:
        return (y, x) if x > y else (x, y)
    else:
        return (x, y) if x > y else (y, x)

def as_portrait(x, y):
    """Given a dimensions, return that pair in portrait orientation"""
    return as_orientation(x, y, is_portrait=True)

def as_landscape(x, y):
    """Given a dimensions, return that pair in landscape orientation"""
    return as_orientation(x, y, is_portrait=False)

def calc_hypotenuse(a, b):
    """Calculate length of hypotenuse using Pythagorian theorem"""
    return sqrt(a**2 + b**2)

def calc_ppi(width_px, height_px, hypotenuse_in):
    """
    Given the diagnonal measurement of the screen in inches (`hypotenuse_in`),
    calculate the pixels-per-inch (ppi) offered by the screen.
    """
    hypotenuse_px = calc_hypotenuse(width_px, height_px)
    return hypotenuse_px / hypotenuse_in

def calc_screen_dimensions_in(width_px, height_px, ppi):
    """
    Calculate screen dimensions (width, height) in inches given dimensions
    in px and pixels-per-inch (ppi).
    """
    return (width_px / float(ppi), height_px / float(ppi))

def calc_screen_size_in(x_px, y_px, ppi):
    """
    Calculate diagonal screen size given dimensions in pixels and
    pixels-per-inch (ppi)
    """
    a, b = calc_screen_dimensions_in(x_px, y_px, ppi)
    return calc_hypotenuse(a, b)

def read_aspect_ratios(file_csv):
    """
    Given a CSV file full of (x, y, name) aspect ratio descriptions, compile
    a tuple of Python tuples.
    """
    with open(file_csv) as f:
      reader = csv.reader(f, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
      next(reader, None)  # skip the header row
      return tuple(tuple(row) for row in reader)

# @TODO port to CSV
ASPECT_RATIOS = read_aspect_ratios('./aspect_ratios.csv')

def find_aspect_ratio(x, y):
    """
    Given an aspect ratio, find an aspect ratio description using a list
    of common aspect ratios.
    """
    ratio = x / y
    for cx, cy, name in ASPECT_RATIOS:
      if ratio == (cx/cy):
        return (ratio, cx, cy, name)
    return (ratio, ratio, 1, "")