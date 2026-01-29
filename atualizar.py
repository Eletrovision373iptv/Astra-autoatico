import requests
import re

# Suas URLs fontes
URLS_FONTES = [
    "http://168.205.55.2:8000/playlist.m3u8",
    "http://189.73.8.73:8000/playlist.m3u8",
    "http://177.126.18.20:8000/playlist.m3u8"
]

LOGO_URL = "https://i.imgur.com/dPaFa7x.png"
CATEGORIA = "CANAIS.4K"

def processar_listas():
    playlist_final = ["#EXTM3U"]
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in URLS_FONTES:
        try:
            print(f"Lendo: {url}")
            response = requests.get(url, headers=headers, timeout=20)
            if response.status_code == 200:
                linhas = response.text.splitlines()
                
                for i in range(len(linhas)):
                    # Verifica se a linha é de informação do canal
                    if linhas[i].startswith("#EXTINF"):
                        # Extrai o nome do canal (tudo que vem após a última vírgula)
                        partes = linhas[i].split(',')
                        nome_canal = partes[-1].strip() if len(partes) > 1 else "Canal sem nome"
                        
                        # Cria a nova linha EXTINF com sua logo e categoria
                        nova_linha = f'#EXTINF:-1 tvg-logo="{LOGO_URL}" group-title="{CATEGORIA}",{nome_canal}'
                        playlist_final.append(nova_linha)
                        
                        # A próxima linha geralmente é o link (URL)
                        if i + 1 < len(linhas):
                            link = linhas[i+1].strip()
                            if link.startswith("http"):
                                playlist_final.append(link)
            
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")

    # Salva o arquivo final
    with open("playlist_personalizada.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(playlist_final))
    print("✅ Lista personalizada criada com sucesso!")

if __name__ == "__main__":
    processar_listas()
