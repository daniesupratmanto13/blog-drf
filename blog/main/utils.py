

def cke_pic_path(filename, request):

    cke_pic_dir = f'{request.user.id}_{request.user.username}/{filename}'

    return cke_pic_dir
