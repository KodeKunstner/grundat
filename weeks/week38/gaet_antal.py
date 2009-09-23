# -*- coding: utf-8 -*-
def antal_vi_kan_skelne_imellem(n):
    """Funktion der retunere hvor mange  tal vi kan ...."""
    if n == 1:
        return 1
    else:
        return antal_vi_kan_skelne_imellem(n-1)*2 + 1

for i in range(1, 21):
    print("Antal gæt: " + str(i) + ", intervalstørrelse: " + str(antal_vi_kan_skelne_imellem(i)))
