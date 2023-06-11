import requests

# ID del video de Twitch
video_id = "123456789"

# Token de acceso de la API de Twitch (obtenido de Twitch Developer Portal)
access_token = "TU_ACCESS_TOKEN"

# URL de la API de Twitch para obtener información del video
url = f"https://api.twitch.tv/helix/videos?id={video_id}"

# Encabezados de la solicitud con el token de acceso
headers = {
    "Client-ID": "TU_CLIENT_ID",
    "Authorization": f"Bearer {access_token}"
}

# Realiza la solicitud GET a la API de Twitch
response = requests.get(url, headers=headers)

# Obtiene los datos de la respuesta JSON
data = response.json()

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el título y la descripción del video
    video_title = data["data"][0]["title"]
    video_description = data["data"][0]["description"]

    # Imprime el título y la descripción
    print("Título del video:", video_title)
    print("Descripción del video:", video_description)

    # Descarga el video
    video_url = data["data"][0]["url"]
    video_data = requests.get(video_url)

    # Guarda el video en un archivo
    with open(f"{video_id}.mp4", "wb") as file:
        file.write(video_data.content)

    print("Video descargado y guardado correctamente.")
else:
    print("Error al obtener la información del video:", data["message"])
