# Usar en el problema 3
organigrama = {
    1: {
        'apellido': 'Lobel',
        'padre': None,
        'hijos': {2, 4, 6},
        'nombre': 'Hans Albert',
        'ID': 1,
        'cargo': 'Director',
    },

    2: {
        'apellido': 'Diaz',
        'padre': 1,
        'hijos': {19, 29},
        'nombre': 'Arturo',
        'ID': 2,
        'cargo': 'Bodeguero',
    },

    3: {
        'apellido': 'Fernandez',
        'padre': 9,
        'hijos': {48, 22},
        'nombre': 'Juan',
        'ID': 3,
        'cargo': 'Panadero',
    },

    4: {
        'apellido': 'Blanco',
        'padre': 1,
        'hijos': {17, 42},
        'nombre': 'Hernan',
        'ID': 4,
        'cargo': 'Gerente',
    },

    5: {
        'apellido': 'Alvarez',
        'padre': 17,
        'hijos': {28, 45},
        'nombre': 'Daniela',
        'ID': 5,
        'cargo': 'Bodeguero',
    },

    6: {
        'apellido': 'Alvarez',
        'padre': 1,
        'hijos': {40, 11},
        'nombre': 'Daniela',
        'ID': 6,
        'cargo': 'Reponedor',
    },

    7: {
        'apellido': 'Garcia',
        'padre': 19,
        'hijos': {8, 43},
        'nombre': 'Bastian',
        'ID': 7,
        'cargo': 'Reponedor',
    },

    8: {
        'apellido': 'Gomez',
        'padre': 7,
        'hijos': {9, 10},
        'nombre': 'Cristobal',
        'ID': 8,
        'cargo': 'Vendedor',
    },

    9: {
        'apellido': 'Sanchez',
        'padre': 8,
        'hijos': {3, 13},
        'nombre': 'Bastian',
        'ID': 9,
        'cargo': 'Gerente',
    },

    10: {
        'apellido': 'Martinez',
        'padre': 8,
        'hijos': {41, 39},
        'nombre': 'Arturo',
        'ID': 10,
        'cargo': 'Guardia',
    },

    11: {
        'apellido': 'Blanco',
        'padre': 6,
        'hijos': {18, 36},
        'nombre': 'Camila',
        'ID': 11,
        'cargo': 'Guardia',
    },

    12: {
        'apellido': 'Lopez',
        'padre': 20,
        'hijos': {46, 31},
        'nombre': 'Patricio',
        'ID': 12,
        'cargo': 'Vendedor',
    },

    13: {
        'apellido': 'Diaz',
        'padre': 9,
        'hijos': {34, 23},
        'nombre': 'Hernan',
        'ID': 13,
        'cargo': 'Cajero',
    },

    14: {
        'apellido': 'Lopez',
        'padre': 23,
        'hijos': {24, 15},
        'nombre': 'Hernan',
        'ID': 14,
        'cargo': 'Guardia',
    },

    15: {
        'apellido': 'Fernandez',
        'padre': 14,
        'hijos': {37, 47},
        'nombre': 'Arturo',
        'ID': 15,
        'cargo': 'Panadero',
    },

    16: {
        'apellido': 'Fernandez',
        'padre': 18,
        'hijos': {35, 20},
        'nombre': 'Sebastian',
        'ID': 16,
        'cargo': 'Gerente',
    },

    17: {
        'apellido': 'Alvarez',
        'padre': 4,
        'hijos': {33, 5},
        'nombre': 'Juan',
        'ID': 17,
        'cargo': 'Guardia',
    },

    18: {
        'apellido': 'Garcia',
        'padre': 11,
        'hijos': {16, 25},
        'nombre': 'Felipe',
        'ID': 18,
        'cargo': 'Cajero',
    },

    19: {
        'apellido': 'Gomez',
        'padre': 2,
        'hijos': {30, 7},
        'nombre': 'Cristobal',
        'ID': 19,
        'cargo': 'Cajero',
    },

    20: {
        'apellido': 'Castro',
        'padre': 16,
        'hijos': {12, 21},
        'nombre': 'Andres',
        'ID': 20,
        'cargo': 'Bodeguero',
    },

    21: {
        'apellido': 'Diaz',
        'padre': 20,
        'hijos': {26, 38},
        'nombre': 'Juan',
        'ID': 21,
        'cargo': 'Vendedor',
    },

    22: {
        'apellido': 'Gonzalez',
        'padre': 3,
        'hijos': {27, 44},
        'nombre': 'Andres',
        'ID': 22,
        'cargo': 'Guardia',
    },

    23: {
        'apellido': 'Diaz',
        'padre': 13,
        'hijos': {49, 14},
        'nombre': 'Sebastian',
        'ID': 23,
        'cargo': 'Reponedor',
    },

    24: {
        'apellido': 'Gomez',
        'padre': 14,
        'hijos': {32, 50},
        'nombre': 'Sebastian',
        'ID': 24,
        'cargo': 'Bodeguero',
    },

    25: {
        'apellido': 'Gomez',
        'padre': 18,
        'hijos': set(),
        'nombre': 'Juan',
        'ID': 25,
        'cargo': 'Guardia',
    },

    26: {
        'apellido': 'Perez',
        'padre': 21,
        'hijos': set(),
        'nombre': 'Felipe',
        'ID': 26,
        'cargo': 'Panadero',
    },

    27: {
        'apellido': 'Gonzalez',
        'padre': 22,
        'hijos': set(),
        'nombre': 'Alvaro',
        'ID': 27,
        'cargo': 'Vendedor',
    },

    28: {
        'apellido': 'Perez',
        'padre': 5,
        'hijos': set(),
        'nombre': 'Nicolas',
        'ID': 28,
        'cargo': 'Reponedor',
    },

    29: {
        'apellido': 'Martinez',
        'padre': 2,
        'hijos': set(),
        'nombre': 'Valeria',
        'ID': 29,
        'cargo': 'Guardia',
    },

    30: {
        'apellido': 'Rodriguez',
        'padre': 19,
        'hijos': set(),
        'nombre': 'Andres',
        'ID': 30,
        'cargo': 'Reponedor',
    },

    31: {
        'apellido': 'Garcia',
        'padre': 12,
        'hijos': set(),
        'nombre': 'Patricio',
        'ID': 31,
        'cargo': 'Panadero',
    },

    32: {
        'apellido': 'Lopez',
        'padre': 24,
        'hijos': set(),
        'nombre': 'Felipe',
        'ID': 32,
        'cargo': 'Panadero',
    },

    33: {
        'apellido': 'Perez',
        'padre': 17,
        'hijos': set(),
        'nombre': 'Alvaro',
        'ID': 33,
        'cargo': 'Ejecutivo',
    },

    34: {
        'apellido': 'Blanco',
        'padre': 13,
        'hijos': set(),
        'nombre': 'Juan',
        'ID': 34,
        'cargo': 'Vendedor',
    },

    35: {
        'apellido': 'Perez',
        'padre': 16,
        'hijos': set(),
        'nombre': 'Juan',
        'ID': 35,
        'cargo': 'Reponedor',
    },

    36: {
        'apellido': 'Alvarez',
        'padre': 11,
        'hijos': set(),
        'nombre': 'Agustin',
        'ID': 36,
        'cargo': 'Gerente',
    },

    37: {
        'apellido': 'Martinez',
        'padre': 15,
        'hijos': set(),
        'nombre': 'Constanza',
        'ID': 37,
        'cargo': 'Reponedor',
    },

    38: {
        'apellido': 'Martinez',
        'padre': 21,
        'hijos': set(),
        'nombre': 'Bastian',
        'ID': 38,
        'cargo': 'Bodeguero',
    },

    39: {
        'apellido': 'Alvarez',
        'padre': 10,
        'hijos': set(),
        'nombre': 'Cristobal',
        'ID': 39,
        'cargo': 'Bodeguero',
    },

    40: {
        'apellido': 'Lopez',
        'padre': 6,
        'hijos': set(),
        'nombre': 'Andres',
        'ID': 40,
        'cargo': 'Guardia',
    },

    41: {
        'apellido': 'Gonzalez',
        'padre': 10,
        'hijos': set(),
        'nombre': 'Nicolas',
        'ID': 41,
        'cargo': 'Panadero',
    },

    42: {
        'apellido': 'Blanco',
        'padre': 4,
        'hijos': set(),
        'nombre': 'Daniela',
        'ID': 42,
        'cargo': 'Reponedor',
    },

    43: {
        'apellido': 'Lopez',
        'padre': 7,
        'hijos': set(),
        'nombre': 'Felipe',
        'ID': 43,
        'cargo': 'Panadero',
    },

    44: {
        'apellido': 'Lopez',
        'padre': 22,
        'hijos': set(),
        'nombre': 'Daniela',
        'ID': 44,
        'cargo': 'Panadero',
    },

    45: {
        'apellido': 'Castro',
        'padre': 5,
        'hijos': set(),
        'nombre': 'Patricio',
        'ID': 45,
        'cargo': 'Vendedor',
    },

    46: {
        'apellido': 'Alvarez',
        'padre': 12,
        'hijos': set(),
        'nombre': 'Bastian',
        'ID': 46,
        'cargo': 'Guardia',
    },

    47: {
        'apellido': 'Lopez',
        'padre': 15,
        'hijos': set(),
        'nombre': 'Arturo',
        'ID': 47,
        'cargo': 'Bodeguero',
    },

    48: {
        'apellido': 'Rodriguez',
        'padre': 3,
        'hijos': set(),
        'nombre': 'Sebastian',
        'ID': 48,
        'cargo': 'Ejecutivo',
    },

    49: {
        'apellido': 'Diaz',
        'padre': 23,
        'hijos': set(),
        'nombre': 'Hernan',
        'ID': 49,
        'cargo': 'Guardia',
    },

    50: {
        'apellido': 'Perez',
        'padre': 24,
        'hijos': set(),
        'nombre': 'Hernan',
        'ID': 50,
        'cargo': 'Gerente',
    },

}
