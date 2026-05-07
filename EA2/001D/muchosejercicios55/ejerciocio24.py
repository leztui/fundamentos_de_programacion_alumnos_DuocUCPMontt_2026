chat = ['hola', 'noob', 'genial', 'manco']
palabra = ""
for palabra in chat:
    if palabra in ['noob', 'manco']:
        print('[CENSURADO]')
    else : 
        print(palabra)