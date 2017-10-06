

def Cartesion(colors, sizes, sleeveLengths):
    return [[color, size, sleeveL] for color in colors
            for size in sizes
            for sleeveL in sleeveLengths]

if __name__ == '__main__':
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    sleeveOptions = ['short', 'long']

    print(Cartesion(colors,sizes,sleeveOptions))

# Lab exercises two
    print [x*x for x in range(1,25+1)]