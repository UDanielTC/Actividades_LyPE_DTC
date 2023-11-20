// Actividad 3 | Daniel Trejo Camacho | Universidad del Valle de México | Ciencia de Datos

# include <iostream>
using namespace std;

// EJERCICIO 1: CREAR UNA FUNCIÓN QUE DETERMINE SI UN NÚMERO ES PAR O IMPAR

int par_o_impar(); // Se declara la función

int main() {
    par_o_impar(); // Se llama a la función
    return 0;
}

/// Se crea la función para determinar si el número ingresado es par o impar
int par_o_impar(){
    int n;

    // Se solicita al usuario ingresar un número
    std::cout << "Ingresa un número:";
    std::cin >> n;

    // Se determina si el número ingresado es par o impar
    if((n%2) == 0){
        std::cout << "El número es par" << std::endl;
    } else{
        std::cout << "El número es impar" << std::endl;
    }
    
    return 0;
}


// EJERCICIO 2: CREAR UNA FUNCIÓN QUE DETERMINE SI UN ALUMNO SE ENCUENTRA ACREDITADO O NO

int calificación(); // Se declara la función

int main() {
    calificación(); // Se llama a la función
    return 0;
}

/// Se crea la función para determinar si un alumno se encuentra acreditado o no
int calificación(){
    int g;

    // Se solicita al usuario ingresar un número
    std::cout << "Ingresa una calificación:";
    std::cin >> g;

    // Se determina si el número ingresado es par o impar
    if(g == 10){
        std::cout << "Excelente" << std::endl;
    } else if(g == 9){
        std::cout << "Muy bien" << std::endl;
    } else if (g == 8) {
        std::cout << "Bien" << std::endl;
    } else if (g == 7) {
        std::cout << "Regular" << std::endl;
    } else if ( g >= 0 && g <= 6) {
        std::cout << "No acreditado" << std::endl;
    } else {
        std::cout << "Error" << std::endl;
    }
    return 0;
}