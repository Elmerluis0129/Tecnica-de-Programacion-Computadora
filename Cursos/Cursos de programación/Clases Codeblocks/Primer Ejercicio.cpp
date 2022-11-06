///Dada la edad de una persona, indica si es mayor o menor de edad.

#include <iostream>
using namespace std;

int edad;
string nombre;

int main()
{
    cout<<"Digite su nombre:";
    cin>>nombre;
    cout<<"Digite su edad:";
    cin>>edad;

    if (edad < 18){
        cout<<nombre << " eres menor de edad";
    }


    if (edad >= 18 && edad <= 130)
        {
            cout<<nombre << " eres mayor de edad";
    }

    if (edad > 130){
        cout<<"Wow "<< nombre << ", eres el anciano mas viejo del mundo o me estas mientiendo";
    }

    return 0;
}
