

def space_transformation(space):
    #Transformar de bytes a Gb
    space_transform = int(space / 1073741824)
    space_transform = f'{space_transform}Gb'
    return space_transform