///Imprimir la suma de N números

#include <iostream>
using namespace std;

int n;
int x, suma=0;


int main()
{
    cout<<"Digite la cantidad de numeros a sumar: ";
    cin>>n;
    for(int i = 1, vueltas = 1; i <= n; i++){
        cout<<"Digite el valor #" <<vueltas <<": ";
        cin>>x;
        suma += x;
        vueltas ++;
    }
    cout<<"El resultado de la suma de sus "<<n<< " valores es: " <<suma;

    return 0;
}
