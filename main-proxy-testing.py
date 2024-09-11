import requests

def test_proxy(proxy):
    # Extraire les informations du proxy
    proxy_parts = proxy.split(":")
    ip_port = f"{proxy_parts[0]}:{proxy_parts[1]}"
    username = proxy_parts[2]
    password = proxy_parts[3]

    # Reformatage du proxy avec authentification
    proxies = {
        "http": f"http://{username}:{password}@{ip_port}",
        "https": f"http://{username}:{password}@{ip_port}"
    }

    url = "http://httpbin.org/ip"  # Ce site renvoie votre adresse IP publique

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

def tester_proxies(fichier_proxies, fichier_proxies_ok, fichier_proxies_ko):
    with open(fichier_proxies, 'r') as file:
        liste_proxies = [line.strip() for line in file.readlines()]

    proxy_ok = []  # Liste pour les proxies qui fonctionnent
    proxy_ko = []  # Liste pour les proxies qui échouent

    for proxy in liste_proxies:
        if test_proxy(proxy):
            proxy_ok.append(proxy)
        else:
            proxy_ko.append(proxy)

    # Écrire les proxies fonctionnels dans un fichier
    with open(fichier_proxies_ok, 'w') as file_ok:
        for proxy in proxy_ok:
            file_ok.write(f"{proxy}\n")

    # Écrire les proxies échoués dans un autre fichier
    with open(fichier_proxies_ko, 'w') as file_ko:
        for proxy in proxy_ko:
            file_ko.write(f"{proxy}\n")

# Utilisation
fichier_proxies = 'liste_proxies.txt'  # Fichier contenant la liste des proxies à tester
fichier_proxies_ok = 'proxies_fonctionnels.txt'  # Fichier où stocker les proxies fonctionnels
fichier_proxies_ko = 'proxies_echoues.txt'  # Fichier où stocker les proxies échoués

tester_proxies(fichier_proxies, fichier_proxies_ok, fichier_proxies_ko)
