#include  <iostream>
using namespace std;

int x = 0, contador  = 1, vueltas = 0;
int suma=0;

int main()
{
    while(suma<100)
    {
        cout<<"Ingresa el valor #" <<contador << ": ";
        cin>>x;
        suma += x;
        contador++;
        vueltas++;

    }
    cout<<"Se ha ejecutado: "<<vueltas<< " veces";
}
