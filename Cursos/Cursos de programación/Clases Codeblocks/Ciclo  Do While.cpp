#include <iostream>
using namespace std;

int contador = 1, vueltas = 1;
int x, suma=0;

int main()
{
    do{
      cout<<"Ingresa el valor #" <<contador << ": ";
      cin>>x;
      suma+=x;
      contador++;
      vueltas++;
    }while(suma<100);

    cout<<"Se ha ejecutado: "<<vueltas<< " veces";

    return 0;
}
