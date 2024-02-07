from selenium import webdriver
from selenium.webdriver.common.by import By
import clipboard
import pyautogui
from time import sleep
import json

# Importation de la base de données des coordonnées
with open('db.json') as f:
    data = json.load(f)

# Sélection des coordonnées en fonction de la distribution Linux et de la résolution d'écran
db = data["mint"]["1920x1080"]

# Demande du lien de l'anime et du nombre d'épisodes
link = input("Entrez le lien de l'anime disponible sur anime-sama.fr : ")
serv = int(input("Entrez le numero du serveur (1 ; 2 ; 3 ; 4) : "))
ep_start = int(input("Le téléchargement commencera de l'épisode : "))
ep_end = int(input("A l'épisode : "))

# Lancement de Firefox avec les addons
driver = webdriver.Firefox()
driver.install_addon('./adblock.xpi')
driver.install_addon('./xdm.xpi')
driver.maximize_window()
driver.get(link)
sleep(5)

# Ferme la page d'adblock
driver.switch_to.window(driver.window_handles[2])
driver.close()

# Va sur la page de xdm et clique sur accepter
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.CSS_SELECTOR, "#accept").click()

# Resélectionne la page de l'anime
driver.switch_to.window(driver.window_handles[0])

# Ouvre la base de données
with open('db.json') as f:
    data = json.load(f)

# Sélection des coordonnées en fonction de la distribution Linux et de la résolution d'écran
db = data["mint"]["1920x1080"]

# Définition des coordonnées pour chaque point
start = db["start"]
video_list = db["video-list"]
video = db["video"]
close_video_list = db["close-video-list"]
start_download = db["start-download"]
close_finished_download = db["close-finished-download"]
video_title = db["video-title"]

# Raccourci pour pyautogui.click()
def click_coordinates(x, y):
    pyautogui.click(x, y)
    sleep(1)

# Ferme la video_list qui apparaît au démarrage
click_coordinates(close_video_list["x"], close_video_list["y"])

# Accepte les cookies
driver.find_element(By.CSS_SELECTOR, ".css-k8o10q").click()

# Sélectionne l'épisode de début
driver.find_element(By.CSS_SELECTOR, f"#selectEpisodes > option:nth-child({ep_start})").click()
sleep(2)
# Sélectionne le serveur
driver.find_element(By.CSS_SELECTOR, f"#selectLecteurs > option:nth-child({serv})").click()
sleep(2)

for i in range(ep_start, ep_end + 1):
    current_ep = i
    # Lance et relance l'épisode tant que le video_list n'est pas apparu
    while pyautogui.pixel(video_list["x"], video_list["y"]) != (50, 50, 50):
        click_coordinates(start["x"], start["y"])

    # Clique sur le video_list
    click_coordinates(video_list["x"], video_list["y"])

    # Clique sur la vidéo à télécharger
    click_coordinates(video["x"], video["y"])

    # Ferme le video_list
    click_coordinates(close_video_list["x"],close_video_list["y"])

    # Récupère le nom de l'anime et la saison
    name = driver.find_element(By.CSS_SELECTOR, "#titreOeuvre").text
    season = driver.find_element(By.CSS_SELECTOR, "#avOeuvre").text

    # Change le titre
    click_coordinates(video_title["x"], video_title["y"])
    pyautogui.hotkey('ctrl', 'a')
    sleep(.5)

    # Crée et écrit le titre de l'épisode
    ep_number = f"0{current_ep}" if current_ep < 10 else str(current_ep)
    ep_title = clipboard.copy(f"Ep {ep_number} {name} {season}.mp4")
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    print(ep_title)

    # Passe au prochain épisode
    if current_ep < ep_end : 
        next_ep_button = driver.find_element(By.CSS_SELECTOR, "#nextEpisode")
        sleep(0.5)
        next_ep_button.click()
        sleep(1)
    elif current_ep == ep_end :
        # Sélectionne l'épisode 1
        driver.find_element(By.CSS_SELECTOR, f"#selectEpisodes > option:nth-child(1").click()

    # Sélectionne le serveur
    driver.find_element(By.CSS_SELECTOR, f"#selectLecteurs > option:nth-child({serv})").click()
    sleep(2)

    # Clique sur le bouton DOWNLOAD VIDEO
    click_coordinates(start_download["x"], start_download["y"])

    # Affiche l'épisode en télechargement
    print(f"Téléchargement de {ep_title}")

    # Attend que le téléchargement soit terminé
    while pyautogui.pixel(close_finished_download["x"], close_finished_download["y"]) != (255, 255, 255):
        sleep(1)

    # Clique sur la fenêtre de fermeture de fin de téléchargement
    click_coordinates(close_finished_download["x"], close_finished_download["y"])

driver.close()
print("Terminé!")
