#include <iostream>
#include <cmath>
using namespace std;

///FUNCIONES POPULARES CON <cmath>
/*
pow(base, exponente) ///  Elevar a una potencia
sqrt(x) /// Raíz cuadrada
abs(x) /// Valor absoluto
min(x, y) /// Menor de dos números
max (x, y) /// Mayor de dos números
*/

int x, y, a, l, m, z, i, j;
float r;


int main()
{
    cin>>x>>y>>l>>m>>z>>i>>j;
    a = max(x, max(y, max(z, max(l, max(m, max(j, i))))));
    cout<<a;


    return 0;
}
