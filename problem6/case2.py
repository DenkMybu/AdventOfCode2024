from multiprocessing import Pool, cpu_count
from functools import partial

def lire_tableau_depuis_fichier(nom_fichier):
    tableau = []
    garde = []
    with open(nom_fichier, 'r') as fichier:
        for i, ligne in enumerate(fichier):
            tableau.append(list(ligne.strip()))
            for j, line in enumerate(ligne) :
                if line == '^' :
                    garde = (i, j, 'n')
    return tableau, garde

def tester_position(tableau, garde) :
    try :
        value_tab = tableau[garde[0]][garde[1]]
        if value_tab == '#' :
            return False
        elif (value_tab == '.') or (value_tab == '^') :
            return True
    except :
        return -1

def check_direction(garde) :
    if  'n' in garde[2] :
        return(garde[0]-1, garde[1], garde[2])
    elif 'e' in garde[2] :
        return(garde[0], garde[1]+1, garde[2])
    elif 's' in garde[2]:
        return(garde[0]+1, garde[1], garde[2])
    elif 'o' in garde[2] :
        return(garde[0], garde[1]-1, garde[2])
    else :
        print('PROBLEM')
        return -1

def check_boucle(liste_old_positions_garde, garde) :
    if garde in liste_old_positions_garde :
            return True
    return False

def bouger_garde(tableau, garde):

    list_direction = ('n', 'e', 's', 'o') # Nord, Est, Sud, Ouest
    list_positions_garde = []
    while tester_position(tableau, garde) != -1 :
        new_garde = check_direction(garde)
        result_test_pos = tester_position(tableau, new_garde)
        # Le garde avance
        if result_test_pos :
            garde = new_garde
        # Le garde change de direction
        elif not result_test_pos :
            index_dir = list_direction.index(garde[2])
            garde = (garde[0], garde[1], list_direction[(index_dir+1)%4])
        # Le garde est sorti de la map
        else :
            return False

        # Vérification de la boucle du garde par rapport à ses précédentes trajectoires
        if check_boucle(list_positions_garde, garde) :
            return True
        else :
            list_positions_garde.append(garde)

    print('PROBLEM')
    return -1

# Création d'un tableau indenté avec piège
def create_trap(tableau, garde) :
    # Calculs parallèles
    counter_trap = 0
    for i, ligne in enumerate(tableau):
        for j, valeur in enumerate(ligne):
            print("position : ", i, " ", j)
            if tableau[i][j] == '.' :
                tableau[i][j] = '#'
                if(bouger_garde(tableau,garde)):
                    counter_trap+=1
                tableau[i][j] = '.'

    print("Counter tap = {}".format(counter_trap))
    return counter_trap

def main():
    # Lire le tableau depuis le fichier
    nom_fichier = "input1.txt"
    tableau, garde = lire_tableau_depuis_fichier(nom_fichier)

    # Calculs parallèles
    p = Pool(cpu_count())


if __name__ == '__main__' :
    main()