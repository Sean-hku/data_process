import os

txt_folder = '/media/hkuit164/WD20EJRX/basket/txt'
for name in os.listdir(txt_folder):
    print(name)
    used_name = txt_folder + '/' + name
    x = name.replace('.xml.', '.')
    new_name = txt_folder + '/' + x
    # used_name = txt_folder + name
    os.rename(used_name,new_name)