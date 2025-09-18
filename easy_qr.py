import qrcode
import matplotlib.pyplot as plt

def generar_qr(texto, nombre_archivo="qr.png"):
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(texto)
    qr.make(fit=True)


    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)
    print(f"Código QR guardado como {nombre_archivo}")

    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    texto = input("Ingrese el texto o URL para generar el código QR: ")
    generar_qr(texto, "mi_codigo_qr.png")