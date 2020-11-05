#EXO1 :

# Enoncé :
# Donner une définition, avec signature et
# hypothèse(s) éventuelle(s), de la fonction
# compte_mots qui, étant donné une chaîne de
# caractères s, renvoie le nombre de mots que
# contient cette chaîne.
# On considère ici les mots “au sens large” : les mots
# sont séparés par un ou des espaces.

# Exemple :
# >>> compte_mots(’’) => 0
# >>> compte_mots(’il ingurgite impunément un iguane.’) => 5
# >>> compte_mots(’coursdeprogrammation’) => 1
# >>> compte_mots(" Attention aux espaces consécutifs ou terminaux ") => 6

def compte_mots(phrase):
    prec,nb_mots=' ', 0
    for char in phrase:
        nb_mots += int(prec == ' '  and char != ' ')
        prec = char
    return print("il ya ",nb_mots,"mots dans cette phrase")

compte_mots(" j'ai reuse a faire l'exo ")

# >>> il ya 5 mots dans cette phrase



#EXO2 :

# Enoncé :
# Donner une définition, avec signature et
# hypothèse(s) éventuelle(s), de la fonction
# remplace_multiple qui, étant donné
# deux chaînes de caractères s1 et s2, ainsi qu’un
# entier naturel n, renvoie la chaîne obtenue en
# remplaçant le caractère en position n dans s1 par le
# premier caractère de s2, puis le caractère en
# position 2n dans s1 par le deuxième caractère de
# s2, etc.. Le remplacement s’arrête quand il n’y a plus
# de caractères dans s2. Une fois la fin de s1 atteinte,
# s’il reste des caractères dans s2 non utilisés, on les
# ajoute au bout de la chaîne obtenue.

# Exemple :
# >>> remplace_multiple(’’,’’,2) => ‘’
# >>> remplace_multiple(’abacus’,’oiseau’,2) =>’abocisseau’
# >>> remplace_multiple(’hirondelles’,’nid’,3) =>’hirnndillds’

def remplace_multiple(s1, s2, n):
    if len(s1)==0 or len(s2)==0 or n==0:
        return s1
    else:
        t = []
        a = n
        for i in range(len(s1)):
            t.append(a)
            a = a+n
        index_s2 = 0
        t = [e for e in t if e<len(s1)]
        new_str = s1
        for i in t:
            new_str = new_str[:i] + s2[index_s2] + new_str[i+1:]
            if index_s2<len(s2)-1:
                index_s2 = index_s2 + 1
            else:
                break
        return new_str+s2[len(t):]
        return t
		

remplace_multiple('', '', 2)

# >>> ''

remplace_multiple('abacus', 'oiseau', 2)

# >>> 'abocisseau'


#EXO 3 :

# Enoncé 1 :
# Donner une définition de la fonction termeU qui,
# étant donné un entier naturel n, rend la valeur de Un
# correspondante.

# Exemple :
# >>> termeU(0) => 1
# >>> termeU(1) => 3
# >>> termeU(5) => 59013
# >>> termeU(10) => 64885583712887818


from math import pow

def termeU(n):
    if n==0:
        return 1
    else:
        return int(pow(2, n)*termeU(n-1) + n)
		
termeU(0)

# >>> 1

termeU(1)

# >>> 3

termeU(10)

# >>> 64885583712887816


#EXO 4 :

# Enoncé :
# Donner une définition (avec une version
# fonctionnelle et une version non fonctionnel) de la
# fonction factorielle qui, étant donné un entier naturel
# n, rend sa factorielle.

# >>> factorielle(1) => 1
# >>> factorielle(2) => 2
# >>> factorielle(3) => 6
# >>> factorielle(4) => 24


def factorielle(n):
    if n==0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = result*i
        return result
		
factorielle(2)

# >>> 2

factorielle(4)

# >>> 24	
	



