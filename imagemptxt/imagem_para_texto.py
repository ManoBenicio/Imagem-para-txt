from PIL import Image

def textconvert(imagem, tipo, s, largura, altura):
    largura = int(largura)
    altura = int(altura)

    # Abre a imagem e redimensiona
    img = Image.open(imagem)
    img = img.resize((largura, altura))

    # Lista para armazenar a representação em texto da imagem
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

    for y in range(altura):
        linha = []
        for x in range(largura):
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
    #só mudar o nome antes do .jpg para o nome do arquivo desejado
    textconvert("imagem.jpg", "jpg", "imagem.txt", largura=200, altura=300)
