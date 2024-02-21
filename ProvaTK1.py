import  tkinter as tk

def converter_para_metros(event=None):
    centimetros_str = entrada_centimetros.get()

    if centimetros_str.replace('.', '', 1).isdigit():  
        centimetros = float(centimetros_str)
        metros = centimetros / 100
        resultado_var.set(f"{centimetros} centímetros é igual a {metros} metros.")
    else:
        resultado_var.set("Por favor, insira um valor válido.")

janela = tk.Tk()
janela.title ('Conversor de Centimetros para Metros')       

resultado_var = tk.StringVar()

label_instrucao = tk.Label(janela,text='Insira a quantidade em centimetros: ')
entrada_centimetros = tk.Entry(janela)
botao_converter = tk.Button(janela,text='Converter', command=converter_para_metros)
label_resultado = tk.Label(janela,textvariable = resultado_var)
entrada_centimetros.bind('<Return>',converter_para_metros)

label_instrucao.pack(pady=10)
entrada_centimetros.pack(pady=10)
botao_converter.pack(pady=10)
label_resultado.pack(pady=10)

janela.mainloop()