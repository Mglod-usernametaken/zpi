# dwa zadania

- co to ścieżka krytyczna
- istota ścieżki krytycznej
- czym jest zadanie wirtualne
- 


## wyznaczanie ścieżki metodą PERT

| zadanie | poprzednik | A | M  | B  | T(pert) | sigma | sigma2 |
| A       | -          | 1 | 2  | 3  | 2       |       |        |
| B       | A          | 4 | 6  | 8  | 6       |       |        |
| C       | -          | 3 | 4  | 6  | 4.17    |       |        |
| D       | A C        | 4 | 8  | 12 | 8       |       |        |
| E       | D          | 2 | 4  | 6  | 4       |       |        |
| F       | D E        | 5 | 7  | 9  | 7       |       |        |
| G       | B          | 6 | 8  | 10 | 8       |       |        |
| H       | F          | 5 | 9  | 12 | 8,83    |       |        |
| I       | G          | 4 | 6  | 9  | 6,17    |       |        |
| J       | H          | 7 | 10 | 12 | 9.83    |       |        |

t(pert) - liczymy jako *(a+4m+b)/6*

sigma - *b-a/6*

### tworzymy graf

dla każdego węzła grau tworzymy:
| t(min)R  | T     | t(min)Z       |
| t(n) - T | zapas | t(następnika) |

- wyznaczamy ścieżkę
- (wypisujemy wszystkie i sumujemy czasy T(pert), zostaje najdłuższa)
- następnie dla ścieżki liczymy odchylenie i wariancję
- 

### dla grfu

---> największą wybieramy
<--- najmniejszą wybieramy
