from hashlib import sha256


def empreinte_mdp(chaine: str) -> str:
    """ Renvoie l'empreinte SHA256 de la chaine de caractère sous forme hexadécimale."""
    return sha256(chaine.encode('UTF-8')).hexdigest()
