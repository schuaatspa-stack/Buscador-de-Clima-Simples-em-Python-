import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()
janela.geometry("350x600") 
janela.title("App de Clima")


titulo = ctk.CTkLabel(janela, text="Consulta de Clima", font=("Arial", 24, "bold"))
titulo.pack(pady=40) 


campo_cidade = ctk.CTkEntry(janela, placeholder_text="Digite a cidade", width=250)
campo_cidade.pack(pady=10)


botao_buscar = ctk.CTkButton(janela, text="Buscar Temperatura")
botao_buscar.pack(pady=20)


janela.mainloop()
