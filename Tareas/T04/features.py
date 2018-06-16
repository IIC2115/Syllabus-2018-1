import os
import numpy
import mahotas
from skimage import color, io, transform, feature


def get_img_feature(path):
    '''
    Recibe el path de una imagen y retorna un diccionario con los siguientes datos:
    image: la imagen original
    category: categoria a la que pertenece
    {R, G, B}_hist: histograma de intensidad por canal de color
    hog: histograma gradientes orientados
    lbp: patrones binarios locales
    haralick: texturas de haralick
    '''
    # Leemos la imagen.
    image = io.imread(path)
    label = path.split("/")[-2]

    # Trabajamos un poco la imagen: la llevamos a gris y le ponemos un tamaño estandar a todas.
    image_grey = color.rgb2gray(image)
    image_grey = transform.resize(image_grey, (225, 167), mode='constant')
    image_grey.reshape(image_grey.shape[0], image_grey.shape[1])

    # Histograma de colores rgb.
    rhist = numpy.histogram(image[:, :, 0])
    ghist = numpy.histogram(image[:, :, 1])
    bhist = numpy.histogram(image[:, :, 2])

    # Calculamos hog de imagen completa.
    fd_hog = feature.hog(image_grey, orientations=9, pixels_per_cell=(30, 30), cells_per_block=(1, 1), transform_sqrt=True, block_norm='L2-Hys')

    # Calculamos local binary patterns de imagen completa.
    fd_lbp = mahotas.features.lbp(image_grey, 1, 8)

    # Calculamos haralick.
    fd_har = mahotas.features.haralick(image_grey.astype(int), return_mean=True)

    return {'image': image, 'category': label, 'red_hist': rhist, 
            'green_hist': ghist, 'blue_hist': bhist, 'hog': fd_hog, 
            'lbp': fd_lbp, 'haralick': fd_har}


def get_features(global_path="./"):
    '''
    Recibe el path raiz del directorio de imagenes (por defecto, "./", 
    la carpeta donde estan las carpetas de los productos), 
    y retorna el diccionario descrito en el enunciado.
    '''
    features = {}
    for category in os.listdir(global_path):
        if len(category.split(".")) < 2:
            category_path = "{}/{}".format(global_path, category)
            for img in os.listdir(category_path):
                if img.split(".")[-1] in ["png", "h4n5", "hans"]:
                    img_path = "{}/{}".format(category_path, img)
                    print("Extrayendo features de {}...".format(img))
                    features[img] = get_img_feature(img_path)

    print("Diccionario creado.")
    return features

