tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
tablero =  []
for i in tablero_inicial.split('\n'):
    tablero.append(i.split('\t'))
#print(tablero)

class Piezas:
    def __init__(self, fila, columna, color,tablero):
        self.fila = fila 
        self.columna = columna
        self.color = color
        self.tablero = tablero

    #def __repr__(self):
    #    return str(self.__dict__)

class Peon(Piezas):
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila+2][self.columna] == '' and self.color == 'blanco'):
                self.tablero[self.fila+2][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+2
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila+1][self.columna] == '' and self.color == 'blanco'):
                self.tablero[self.fila+1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila = self.fila+1
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila-2][self.columna] == '' and self.color == 'negro'):
                self.tablero[self.fila-2][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-2
                self.columna = self.columna
            elif (opcion == 3 and self.tablero[self.fila-1][self.columna] == '' and self.color == 'negro'):
                self.tablero[self.fila-1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila-1][self.columna-1] != '' and self.color == 'negro'):
                self.tablero[self.fila-1][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna -1
            elif (opcion == 1 and self.tablero[self.fila-1][self.columna+1] != '' and self.color == 'negro'):
                self.tablero[self.fila-1][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna +1
            elif (opcion == 2 and self.tablero[self.fila+1][self.columna-1] != '' and self.color == 'blanco'):
                self.tablero[self.fila+1][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna -1
            elif (opcion == 3 and self.tablero[self.fila+1][self.columna+1] != ''and self.color == 'blanco'):
                self.tablero[self.fila+1][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna +1
            else:
                MAL=True
                return MAL
                



class Caballo(Piezas):
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + 2][self.columna+1]==''):
                self.tablero[self.fila + 2][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+2
                self.columna = self.columna+1
            elif (opcion == 1 and self.tablero[self.fila + 2][self.columna-1]==''):
                self.tablero[self.fila + 2][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+2
                self.columna = self.columna-1
            elif (opcion == 2 and self.tablero[self.fila - 2][self.columna+1]==''):
                self.tablero[self.fila - 2][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-2
                self.columna = self.columna+1
            elif (opcion == 3 and self.tablero[self.fila - 2][self.columna-1]==''):
                self.tablero[self.fila - 2][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-2
                self.columna = self.columna-1
            elif (opcion == 4 and self.tablero[self.fila + 1][self.columna+2]==''):
                self.tablero[self.fila + 1][self.columna + 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna+2
            elif (opcion == 5 and self.tablero[self.fila - 1][self.columna+2]==''):
                self.tablero[self.fila - 1][self.columna + 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna+2
            elif (opcion == 6 and self.tablero[self.fila + 1][self.columna-2]==''):
                self.tablero[self.fila + 1][self.columna - 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna-2
            elif (opcion == 7 and self.tablero[self.fila - 1][self.columna - 2]==''):
                self.tablero[self.fila - 1][self.columna - 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna-2
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + 2][self.columna+1]!=''):
                self.tablero[self.fila + 2][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+2
                self.columna = self.columna+1
            elif (opcion == 1 and self.tablero[self.fila + 2][self.columna-1]!=''):
                self.tablero[self.fila + 2][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+2
                self.columna = self.columna-1
            elif (opcion == 2 and self.tablero[self.fila - 2][self.columna+1]!=''):
                self.tablero[self.fila - 2][self.columna+1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-2
                self.columna = self.columna+1
            elif (opcion == 3 and self.tablero[self.fila - 2][self.columna-1]!=''):
                self.tablero[self.fila - 2][self.columna-1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-2
                self.columna = self.columna-1
            elif (opcion == 4 and self.tablero[self.fila + 1][self.columna+2]!=''):
                self.tablero[self.fila + 1][self.columna + 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna+2
            elif (opcion == 5 and self.tablero[self.fila - 1][self.columna+2]!=''):
                self.tablero[self.fila - 1][self.columna + 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna+2
            elif (opcion == 6 and self.tablero[self.fila + 1][self.columna-2]!=''):
                self.tablero[self.fila + 1][self.columna - 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna-2
            elif (opcion == 7 and self.tablero[self.fila - 1][self.columna - 2]!=''):
                self.tablero[self.fila - 1][self.columna - 2]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna-2
            else:
                MAL=True
                return MAL


class Alfil(Piezas):
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna + n]==''):
                self.tablero[self.fila + n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna+n
            elif (opcion == 1 and self.tablero[self.fila + n][self.columna - n]==''):
                self.tablero[self.fila + n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna-n
            elif (opcion == 2 and self.tablero[self.fila - n][self.columna + n]==''):
                self.tablero[self.fila - n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila - n][self.columna - n]==''):
                self.tablero[self.fila - n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna-n
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna + n]!=''):
                self.tablero[self.fila + n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna+n
            elif (opcion == 1 and self.tablero[self.fila + n][self.columna - n]!=''):
                self.tablero[self.fila + n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna-n
            elif (opcion == 2 and self.tablero[self.fila - n][self.columna + n]!=''):
                self.tablero[self.fila - n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila - n][self.columna - n]!=''):
                self.tablero[self.fila - n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna-n
            else:
                MAL=True
                return MAL


class Torre(Piezas):  
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna] == ''):
                self.tablero[self.fila + n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - n][self.columna] == ''):
                self.tablero[self.fila - n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + n] == ''):
                self.tablero[self.fila][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila][self.columna - n] == ''):
                self.tablero[self.fila][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna-n
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna] != ''):
                self.tablero[self.fila + n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - n][self.columna] != ''):
                self.tablero[self.fila - n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + n] != ''):
                self.tablero[self.fila][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila][self.columna - n] != ''):
                self.tablero[self.fila][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna-n
            else:
                MAL=True
                return MAL


class Rey(Piezas):
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + 1][self.columna]== ''):
                self.tablero[self.fila + 1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - 1][self.columna]== ''):
                self.tablero[self.fila - 1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + 1]== ''):
                self.tablero[self.fila][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+1
            elif (opcion == 3 and self.tablero[self.fila][self.columna -1]== ''):
                self.tablero[self.fila][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''     
                self.fila=self.fila
                self.columna = self.columna -1
            elif (opcion == 4 and self.tablero[self.fila + 1][self.columna +1]== ''):
                self.tablero[self.fila + 1][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna+1
            elif (opcion == 5 and self.tablero[self.fila + 1][self.columna -1]== ''):
                self.tablero[self.fila + 1][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna-1
            elif (opcion == 6 and self.tablero[self.fila - 1][self.columna + 1]== ''):
                self.tablero[self.fila - 1][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna+1
            elif (opcion == 7 and self.tablero[self.fila - 1][self.columna - 1]== ''):
                self.tablero[self.fila - 1][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna-1
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + 1][self.columna]!= ''):
                self.tablero[self.fila + 1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - 1][self.columna]!= ''):
                self.tablero[self.fila - 1][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + 1]!= ''):
                self.tablero[self.fila][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+1
            elif (opcion == 3 and self.tablero[self.fila][self.columna -1]!= ''):
                self.tablero[self.fila][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''     
                self.fila=self.fila
                self.columna = self.columna -1
            elif (opcion == 4 and self.tablero[self.fila + 1][self.columna +1]!= ''):
                self.tablero[self.fila + 1][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna+1
            elif (opcion == 5 and self.tablero[self.fila + 1][self.columna -1]!= ''):
                self.tablero[self.fila + 1][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+1
                self.columna = self.columna-1
            elif (opcion == 6 and self.tablero[self.fila - 1][self.columna + 1]!= ''):
                self.tablero[self.fila - 1][self.columna + 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna+1
            elif (opcion == 7 and self.tablero[self.fila - 1][self.columna - 1]!= ''):
                self.tablero[self.fila - 1][self.columna - 1]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-1
                self.columna = self.columna-1
            else:
                MAL=True
                return MAL

class Reina(Piezas):
    def mover_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna] == ''):
                self.tablero[self.fila + n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - n][self.columna] == ''):
                self.tablero[self.fila - n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + n] == ''):
                self.tablero[self.fila][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila][self.columna - n] == ''):
                self.tablero[self.fila][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''   
                self.fila=self.fila
                self.columna = self.columna-n  
            elif (opcion == 4 and self.tablero[self.fila + n][self.columna + n] == ''):
                self.tablero[self.fila + n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna+n
            elif (opcion == 5 and self.tablero[self.fila +n][self.columna - n] == ''):
                self.tablero[self.fila + n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna-n
            elif (opcion == 6 and self.tablero[self.fila - n][self.columna + n] == ''):
                self.tablero[self.fila - n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna+n
            elif (opcion == 7 and self.tablero[self.fila - n][self.columna - n] == ''):
                self.tablero[self.fila - n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = '' 
                self.fila=self.fila-n
                self.columna = self.columna -n
            else:
                MAL=True
                return MAL
    def comer_pieza(self,opcion,n=None):
            if (opcion == 0 and self.tablero[self.fila + n][self.columna] != ''):
                self.tablero[self.fila + n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna
            elif (opcion == 1 and self.tablero[self.fila - n][self.columna] != ''):
                self.tablero[self.fila - n][self.columna]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna
            elif (opcion == 2 and self.tablero[self.fila][self.columna + n] != ''):
                self.tablero[self.fila][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila
                self.columna = self.columna+n
            elif (opcion == 3 and self.tablero[self.fila][self.columna - n] != ''):
                self.tablero[self.fila][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''   
                self.fila=self.fila
                self.columna = self.columna-n  
            elif (opcion == 4 and self.tablero[self.fila + n][self.columna + n] != ''):
                self.tablero[self.fila + n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna+n
            elif (opcion == 5 and self.tablero[self.fila +n][self.columna - n] != ''):
                self.tablero[self.fila + n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila+n
                self.columna = self.columna-n
            elif (opcion == 6 and self.tablero[self.fila - n][self.columna + n] != ''):
                self.tablero[self.fila - n][self.columna + n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = ''
                self.fila=self.fila-n
                self.columna = self.columna+n
            elif (opcion == 7 and self.tablero[self.fila - n][self.columna - n] != ''):
                self.tablero[self.fila - n][self.columna - n]=self.tablero[self.fila][self.columna]
                self.tablero[self.fila][self.columna] = '' 
                self.fila=self.fila-n
                self.columna = self.columna -n
            else:
                MAL=True
                return MAL



arreglo_piezas = []
arreglo_piezas.append(Peon(1,0,'blanco',tablero))
arreglo_piezas.append(Peon(1,1,'blanco',tablero))
arreglo_piezas.append(Peon(1,2,'blanco',tablero))
arreglo_piezas.append(Peon(1,3,'blanco',tablero))
arreglo_piezas.append(Peon(1,4,'blanco',tablero))
arreglo_piezas.append(Peon(1,5,'blanco',tablero))
arreglo_piezas.append(Peon(1,6,'blanco',tablero))
arreglo_piezas.append(Peon(1,7,'blanco',tablero))
arreglo_piezas.append(Torre(0,0,'blanco',tablero))
arreglo_piezas.append(Torre(0,7,'blanco',tablero))
arreglo_piezas.append(Caballo(0,1,'blanco',tablero))
arreglo_piezas.append(Caballo(0,6,'blanco',tablero))
arreglo_piezas.append(Alfil(0,2,'blanco',tablero))
arreglo_piezas.append(Alfil(0,5,'blanco',tablero))
arreglo_piezas.append(Reina(0,3,'blanco',tablero))
arreglo_piezas.append(Rey(0,4,'blanco',tablero))

arreglo_piezas.append(Peon(7,0,'negro',tablero))
arreglo_piezas.append(Peon(7,1,'negro',tablero))
arreglo_piezas.append(Peon(7,2,'negro',tablero))
arreglo_piezas.append(Peon(7,3,'negro',tablero))
arreglo_piezas.append(Peon(7,4,'negro',tablero))
arreglo_piezas.append(Peon(7,5,'negro',tablero))
arreglo_piezas.append(Peon(7,6,'negro',tablero))
arreglo_piezas.append(Peon(7,7,'negro',tablero))
arreglo_piezas.append(Torre(7,0,'negro',tablero))
arreglo_piezas.append(Torre(7,7,'negro',tablero))
arreglo_piezas.append(Caballo(7,1,'negro',tablero))
arreglo_piezas.append(Caballo(7,6,'negro',tablero))
arreglo_piezas.append(Alfil(7,2,'negro',tablero))
arreglo_piezas.append(Alfil(7,5,'negro',tablero))
arreglo_piezas.append(Reina(7,3,'negro',tablero))
arreglo_piezas.append(Reina(7,4,'negro',tablero))


n_movimientos=0
while(True):
    x=[]
    for j in tablero:
        x.append("\t".join(j))
    print(("\n".join(x)))


    if n_movimientos % 2 == 0:
        print("Juegan blancas")
        print('')
    else:
        print("Juegan negras")
        print('')
    
    while(True):
        print("Elije tu pieza segun su ubicacion")
        fila=int(input("Ingrese fila: "))
        columna=int(input("Ingrese columna: "))
        if fila>7 or fila<0 or columna>7 or fila<0:
            print('No elejiste una ubicacion valida')
        else:
            print('')
            break

    
    for i in range(len(arreglo_piezas)):
        if arreglo_piezas[i].fila == fila and arreglo_piezas[i].columna == columna:
            print("La pieza a sido elegida: ", type(arreglo_piezas[i]).__name__)
            print('') 
            ubicacion_pieza=i
            break

    while (True):
        print('m:mover -- c:comer')
        accion=input("Elige la accion de la pieza: ")
        if accion == 'm' or accion == 'c':
            print('')
            break
        else: 
            print('No ingresaste una opcion valida')
            print('Vuelve a intentar...')

    MAL=False
    while (True):
        if (accion == 'm'):
            opcion=int(input('Elige el movimiento de tu pieza: '))
            MAL=arreglo_piezas[ubicacion_pieza].mover_pieza(opcion)
        else:
            opcion=int(input('Elige el movimiento de tu pieza: '))
            MAL=arreglo_piezas[ubicacion_pieza].comer_pieza(opcion)
        if(MAL==True):
            print('Tu movimiento no es valido')
            print('Vuelve a probar...')
        else:
            print('')
            break
    n_movimientos=n_movimientos+1        
    

    








