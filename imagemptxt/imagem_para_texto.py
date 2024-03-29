from PIL import Image
def textconvert(imagem, type, s, scala):
    scala = int(scala)

    # Abre a imagem e redimensiona
    img = Image.open(imagem)
    w, h = img.size
    nova_largura = w // scala
    nova_altura = h // scala
    img = img.resize((nova_largura, nova_altura))

    #l ista o tamanho correto
    grade = []

    # Mapeia os valores RGB para caracteres
    mapeamento = {0: '#',  # Preto
                  1: 'X',
                  2: '%',
                  3: '&',
                  4: '*',
                  5: '+',
                  6: '/',
                  7: '(',
                  8: "'"}
    

    for y in range(nova_altura):
        linha = []
        for x in range(nova_largura):
            pixel = img.getpixel((x, y))
            intensidade = sum(pixel) // 100  # Valor entre 0 e 7
            caractere = mapeamento.get(intensidade, ' ')
            linha.append(caractere)
        grade.append(linha)

    # Escreve no arquivo de texto
    with open(s, "w") as arte:
        for linha in grade:
            arte.write("".join(linha) + "\n")

if __name__ == "__main__":
    textconvert("imagem.jpg", "jpg", "imagem.txt", "3")
