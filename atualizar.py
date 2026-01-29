import requests

# Suas 3 fontes atualizadas
URLS_FONTES = [
    "http://168.205.55.2:8000/playlist.m3u8",
    "http://189.73.8.73:8000/playlist.m3u8",
    "http://177.126.18.20:8000/playlist.m3u8"
]

def atualizar_lista():
    final_m3u = ["#EXTM3U\n"]
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in URLS_FONTES:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                linhas = r.text.splitlines()
                # Pula o cabeçalho para não duplicar
                if linhas and "#EXTM3U" in linhas[0]:
                    linhas = linhas[1:]
                final_m3u.extend(linhas)
                final_m3u.append("\n")
        except:
            print(f"Erro ao acessar {url}")

    with open("lista_leve.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(final_m3u))

if __name__ == "__main__":
    atualizar_lista()
