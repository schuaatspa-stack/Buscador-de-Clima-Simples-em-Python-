import customtkinter as ctk
import requests

def buscar_clima(event=None):
    cidade = campo_cidade.get()
    
    if not cidade:
        texto_resultado.configure(text="Por favor, digite uma cidade.")
        return

    try:
        url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
        resposta_geo = requests.get(url_geo).json()
        
        if not resposta_geo.get('results'):
            texto_resultado.configure(text="Cidade não encontrada.")
            return

        lat = resposta_geo['results'][0]['latitude']
        lon = resposta_geo['results'][0]['longitude']
        nome_real = resposta_geo['results'][0]['name']

        url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        resposta_clima = requests.get(url_clima).json()
        temperatura = resposta_clima['current_weather']['temperature']

        texto_resultado.configure(text=f"📍 {nome_real}\n🌡️ Temperatura: {temperatura}°C")
        
    except Exception as e:
        texto_resultado.configure(text="Erro ao buscar o clima.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("350x500")
janela.title("App de Clima")

titulo = ctk.CTkLabel(janela, text="Consulta de Clima", font=("Arial", 24, "bold"))
titulo.pack(pady=40)

campo_cidade = ctk.CTkEntry(janela, placeholder_text="Digite a cidade", width=250)
campo_cidade.pack(pady=10)

janela.bind('<Return>', buscar_clima)

botao_buscar = ctk.CTkButton(janela, text="Buscar Temperatura", command=buscar_clima)
botao_buscar.pack(pady=20)

texto_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 20))
texto_resultado.pack(pady=30)

janela.mainloop()
