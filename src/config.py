# src/config.py

import numpy as np

def get_birth_values(df_pivot):
    human_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Human"].values[0]
    mouse_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Mouse"].values[0]
    rat_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Rat"].values[0]
    return human_birth, mouse_birth, rat_birth


# Model 4: quarter-power with constant, y = b*x^(1/4) + c
def mod_quarter_const(x, b, c):
    return b * x**0.25 + c

# # Paleta personalizada

colors = {
    'Human': '#67ba6a',
    'Mouse': '#42a5f5',
    'Mouse_O':"#04AF98",
    'Mouse_WO':"#7434DB",
    'Brain': '#ffca28',  # ejemplo
    'Rat': '#ef5351',
    'Body': '#6A0DAD'
    
}

# Export settings
TIFF_DPI = 300

# Shared configuration for subplot letter annotations across panels.
panel_subplot_letters = {
    'labels': list('abcdefghijklmnopqrstuvwxyz'),
    'x': -0.11,
    'y': 1.03,
    'fontsize': 11,
    'fontweight': 'bold',
    'ha': 'left',
    'va': 'bottom',
}


params_quarter_plus_c = {
    "rat": {
        "b": 10.3716,
        "c": -12.4535
    },
    "mouse": {
        "b": 8.7156,
        "c": -9.5489
    }
}
