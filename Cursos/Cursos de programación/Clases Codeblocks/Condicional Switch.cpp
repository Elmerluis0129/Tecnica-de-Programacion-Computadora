/*
Imprimir el mensaje correspondiente a cada número
1-Uno
2-Dos
3-Tres
4-Cuatro
Otro-Equis
*/
#include <iostream>
using namespace std;

int num;

int main(){

    cout<<"Digite el numero: ";
    cin>>num;

    switch( num )
    {
        case 1:
            cout<<"Uno";
        break;
        case 2:
            cout<<"Dos";
        break;
        case 3:
            cout<<"Tres";
        break;
        case 4:
            cout<<"Cuatro";
        break;
        default:
            cout<<"Equis";
        break;
    }


    return 0;
}
