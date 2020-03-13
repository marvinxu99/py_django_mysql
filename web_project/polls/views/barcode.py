# https://blog.jonasneubert.com/2019/01/23/barcode-generation-python/

# https://www.ghostscript.com/

# (1) pip install treepoem
#     it will install treepoem 3.3.1 and Pillow 7.0.0

# (2) Install ghostscript    - 32bit


# Another solution is to (1) edit the 
# C:\Users\Windows.UserName\AppData\Local\Programs\Python\Python37\Lib\site-packages\treepoem__init__.py
# the script is looking for gs.exe, change to gswin32.exe as shown below.
# (2) Then add the GhostScriptInstallDir\bin in the PATH in windows.

# def _get_ghostscript_binary():
#     binary = "gswin32c" # changed from 'gs' to 'gswin32c'

#     if sys.platform.startswith("win"):
#         binary = EpsImagePlugin.gs_windows_binary
#         if not binary:
#             raise TreepoemError(
#                 "Cannot determine path to ghostscript, is it installed?"
#             )

#     return binary

#

from django.shortcuts import render
from django.conf import settings
import datetime
import os

import treepoem


def generate_barcode(text=None, file_name=None, code_type="datamatrix"):
    if text is not None:
        data = text
    else:
        data = 'Winter WinnPy'
    
    image = treepoem.generate_barcode(
        barcode_type = code_type,
        data = data
    )

    if file_name is None:
        # /generated_barcode/
        f_path = os.path.join(settings.BASE_DIR, 'generated_codes')
        # f_name = 'barcode_' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.png'
        f_name = 'barcode.png'
        img_file = f_path + "\\" + f_name
    else:
        img_file = file_name

    print(img_file)
    image.convert('1').save(img_file)
    # image.convert('1').save('barcode.png')


def barcode_req(request):
    # barcode_types = ['QR Code', 'other code']    
    
    barcode_types = [
        ("datamatrix", "Data Matrix"),
        ("qrcode", "QR Code"),
    ]    
      
    context = {
            'barcode_types': barcode_types,
        }
    return render(request, 'polls/barcode_req.html', context)


def barcode_disp(request):
    print(request.POST['barcode_type'])
    print(request.POST['barcode_data'])
    print(settings.BASE_DIR)

    text = request.POST['barcode_data']
    code_type = request.POST['barcode_type']

    generate_barcode(text=text, code_type=code_type)

    f_path = os.path.join(settings.BASE_DIR, 'generated_codes')
    f_name = 'barcode.png'
    file_name = f_path + "\\" + f_name

    context = {
            'barcode_url': file_name,
            'barcode_data': text,
            'code_type': code_type,
        }

        
    return render(request, 'polls/barcode_disp.html', context)


if __name__ == "__main__":
    generate_barcode()


