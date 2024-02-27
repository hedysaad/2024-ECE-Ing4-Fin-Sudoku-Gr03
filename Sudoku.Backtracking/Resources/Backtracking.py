from timeit import default_timer

#on instancie la structure de données
instance = ((0,0,0,0,9,4,0,3,0),
           (0,0,0,5,1,0,0,0,7),
           (0,8,9,0,0,0,0,4,0),
           (0,0,0,0,0,0,2,0,8),
           (0,6,0,2,0,1,0,5,0),
           (1,0,2,0,0,0,0,0,0),
           (0,7,0,0,0,0,5,2,0),
           (9,0,0,0,6,5,0,0,0),
           (0,4,0,9,7,0,0,0,0))

#fonction pour chercher la prochaine case à remplir
def findNextCellToFill(grid, i, j):
        #on commence a la case (i;j)
        for x in range(i,9):
                for y in range(j,9):
                        # si la case est vide, on renvoit ses coordonnées
                        if grid[x][y] == 0:
                                return x,y
        #si pas de case vide, on reprend
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        #on renvoit ça, quand toutes les cases sont pleines
        return -1,-1
#fonction pour checker si un chiffre est correct dans une case
def isValid(grid, i, j, e):
        #on voit si le chiffre n'est pas dans la ligne
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                #on voit si le chiffre n'est pas dans la colonne
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        #on cherche les coordonnées du point en haut à gauche de la section qui contient la cellule (i;j)
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3)  
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

#fonction pour résoudre la grille sudoku
def solveSudoku(grid, i=0, j=0):
        #on cherche la prochaine case a remplir
        i,j = findNextCellToFill(grid, i, j)
        #si tout est rempli, on a trouvé une solution 
        if i == -1:
                return True
        #on essaie toutes les solutions possibles de 1 à 9 dans la case
        for e in range(1,10):
                #si le chiffre est valide, on l'inclut dans la case
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        #Appel par récursivité pour la prochain case à remplir
                        if solveSudoku(grid, i, j):
                                return True
                        # On revient en arrière - BACKTRACKING - et la case est remise à 0
                        grid[i][j] = 0
        return False

#conversion de notre instance de début en liste de listes pour la travailler
grid_list = [list(row) for row in instance]

#on enregistre le temps pour évaluer la performance
start = default_timer()

#on résout la grille
if(solveSudoku(grid_list)):
    for row in grid_list:
        #si la solution est trouvée, on l'affiche
        print(row)
    r=grid_list
else:
    print("Aucune solution trouvée.")


#on finit le calcul du temps de la performance
execution = default_timer() - start
print("Le temps de resolution est de : ", execution, " seconds as a floating point value")