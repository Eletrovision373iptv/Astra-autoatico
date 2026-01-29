import requests

# COLOQUE SEU LINK FIXO AQUI DENTRO DAS ASPAS
URL_FONTE = "http://168.205.55.2:8000/playlist.m3u8"

def baixar_lista():
    try:
        header = {'User-Agent': 'Mozilla/5.0'} # Simula um navegador
        response = requests.get(URL_FONTE, headers=header, timeout=30)
        
        if response.status_code == 200:
            # Salva o conteúdo no arquivo m3u
            with open("playlist_atualizada.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✅ Playlist atualizada com sucesso!")
        else:
            print(f"❌ Erro: Servidor retornou status {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

if __name__ == "__main__":
    baixar_lista()
