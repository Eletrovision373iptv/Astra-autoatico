import requests

# Adicione quantas URLs quiser dentro dos colchetes, separadas por vírgula
URLS_FONTES = [
    "http://168.205.55.2:8000/playlist.m3u8",
    "http://189.73.8.73:8000/playlist.m3u8",
    "https://terceira_lista.net/futebol.m3u"
]

def baixar_e_unir():
    playlist_final = ["#EXTM3U\n"] # Cabeçalho obrigatório
    
    header = {'User-Agent': 'Mozilla/5.0'}

    for url in URLS_FONTES:
        try:
            print(f"Baixando: {url}")
            response = requests.get(url, headers=header, timeout=30)
            
            if response.status_code == 200:
                linhas = response.text.splitlines()
                # Pula a primeira linha se for #EXTM3U para não repetir no meio do arquivo
                if linhas and "#EXTM3U" in linhas[0]:
                    linhas = linhas[1:]
                
                playlist_final.extend(linhas)
                playlist_final.append("\n") # Espaço entre listas
                print(f"✅ Sucesso!")
            else:
                print(f"❌ Erro {response.status_code} ao baixar {url}")
        except Exception as e:
            print(f"❌ Falha crítica em {url}: {e}")

    # Salva o resultado final unindo tudo
    with open("playlist_atualizada.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(playlist_final))

if __name__ == "__main__":
    baixar_e_unir()
