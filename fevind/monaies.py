def brut(a):
    a = a.replace("{", "")
    a = a.replace("}", "")
    a = a.replace('\"',"")
    a = a.replace("A","")
    a = a.replace("B", "")
    a = a.replace("C", "")
    a = a.replace("D", "")
    a = a.replace("E", "")
    a = a.replace("F", "")
    a = a.replace("G", "")
    a = a.replace("H", "")
    a = a.replace("I", "")
    a = a.replace("J", "")
    a = a.replace("K", "")
    a = a.replace("L", "")
    a = a.replace("M", "")
    a = a.replace("N", "")
    a = a.replace("O", "")
    a = a.replace("P", "")
    a = a.replace("Q", "")
    a = a.replace("R", "")
    a = a.replace("S", "")
    a = a.replace("T", "")
    a = a.replace("U", "")
    a = a.replace("V", "")
    a = a.replace("W", "")
    a = a.replace("X", "")
    a = a.replace("Y", "")
    a = a.replace("Z", "")
    a = a.replace("_", "")
    a = a.replace(":", "")

    return a

def request(d_un,d_deux):
    url = 'https://free.currconv.com/api/v7/convert?q=' + d_un + '_' + d_deux + '&compact=ultra&apiKey=8374f8c80936aec0e5aa'
    r = requests.get(url)
    r = r.text
    r = brut(r)
    r = float(r)
    return r

import requests
print("Veuillez Patienter...")
#PND


cadeur = request("CAD", "EUR")
cadusd = request("CAD", "USD")
chfeur = request("CHF", "EUR")


#FCD

chfgbp = request("CHF", "GBP")
audsgd = request("AUD", "SGD")
gipeur = request("GIP", "EUR")

#EVC

eurxpf = request("EUR", "XPF")
eurxpf = eurxpf*50
dkkisk = request("DKK", "ISK")
dkkisk = dkkisk
noksek = request("NOK", "SEK")
noksek = noksek*1000
krweur = request("KRW", "EUR")


#Resultats

pndchf = cadusd + cadeur
pnd = pndchf*chfeur
print("Un ducat de Piton des Neiges équivaut à", pnd, "EUR")


fcdgip = pndchf - chfgbp - cadeur + audsgd
fcd = fcdgip*gipeur
print("Un Cadeau Flavenien équivaut à", fcd, "EUR")


evckrw = eurxpf - dkkisk + noksek
milevc = evckrw*krweur
evc = (evckrw*krweur)/1000
print("1000 Couronne Evrestienne équivalent à", milevc, "EUR")

print("\n")
convert = 0
while convert != "STOP":
    convert =  input("Quelle devise voulez vous convertir ?")
    convert = convert.upper()
    if convert == "PND":
        secondstep = input("En quoi souhaitez vous le convertir ?")
        secondstep = secondstep.upper()
        if secondstep == "EUR":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  pnd*somme
            print(sommeconvertie)
        elif secondstep == "FCD":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  pnd/fcd*somme
            print(sommeconvertie)

        elif secondstep == "EVC":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  pnd/evc*somme
            print(sommeconvertie)

        else:
            print("Commande invalide :/")

    elif convert == "FCD":
        secondstep = input("En quoi souhaitez vous le convertir ?")
        secondstep = secondstep.upper()
        if secondstep == "EUR":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  fcd*somme
            print(sommeconvertie)

        elif secondstep == "PND":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  fcd/pnd*somme
            print(sommeconvertie)

        elif secondstep == "EVC":
            somme = float(input("Quelle somme ?"))
            sommeconvertie = fcd/evc*somme
            print(sommeconvertie)

        else:
            print("Commande invalide :/")

    elif convert == "EVC":
        secondstep = input("En quoi souhaitez vous le convertir ?")
        secondstep = secondstep.upper()
        if secondstep == "EUR":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  evc*somme
            print(sommeconvertie)
        elif secondstep == "PND":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  evc/pnd*somme
            print(sommeconvertie)

        elif secondstep == "FCD":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  evc/fcd*somme
            print(sommeconvertie)

        else:
            print("Commande invalide :/")
	
    elif convert == "EUR":
        secondstep = input("En quoi souhaitez vous le convertir ?")
        secondstep = secondstep.upper()
        if secondstep == "EVC":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  (1/evc)/somme
            print(sommeconvertie)
        elif secondstep == "PND":
            somme = float(input("Quelle somme ?"))
            sommeconvertie = (1/pnd)*somme
            print(1/pnd)
            print(sommeconvertie)

        elif secondstep == "FCD":
            somme = float(input("Quelle somme ?"))
            sommeconvertie =  (1/fcd)*somme
            print(sommeconvertie)

        else:
            print("Commande invalide :/")
    else:
        print("Commande invalide :/")
