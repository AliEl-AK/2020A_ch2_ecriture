#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        lettre_min = ord(lettre)
        lettre_majiscule = lettre_min - 32
        M = chr(lettre_majiscule)
        resultat += M
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
    word = 'fuck you'
print(word.upper())
print(word)
message  = 'python is fun'
print(message.title())

#INV de l'exercice du prof


def majuscule (mot):
    resultat=""
    for lettre in mot:
        lettre_majuscule= ord(lettre)
        lettre_min= lettre_majuscule + 32
        J= chr(lettre_min)
        resultat += J
    return resultat
if __name__ == '__main__':
    mots = [
        'RIZ',
        'COURS',
        'VOITURE',
        'OISEAU',
        'BONJOUR',
        'ÉGLANTIER',
        'ARBRE'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)