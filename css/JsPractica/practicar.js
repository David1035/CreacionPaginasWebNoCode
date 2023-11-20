/*
Ejercicio: Suma de números pares en un rango

Crea una función llamada sumaNumerosParesque tome dos argumentos: inicioy fin, que representan el rango de números a considerar.

Dentro de la función, utilice un bucle for para iterar a través inicio hasta fin.

En cada iteración, verifica si el número actual es pa%(módulo) para verificar si el número es divisible por 2 sin dejar un r

Si el número es par, agregue una llamada variable suma.

Al finalizar el bucle, la variable `susumacontendrá la suma de todos los números pares dentro del rango.

La función debe devolver el valor de suma.

Llama a la función sumaNumerosParescon un rango específico, por ejemplo, inicio = 1y fin = 10, y debe
*/

function sumaNumerosPares(inicio, fin) {
    let suma = 0;    
        for(let numero = inicio; numero <= fin; numero++) {
            if (numero % 2 === 0){
                suma += numero;
        }
        return suma;
    }
}

const resultado = sumaNumerosPares(1,10);
console.log(`La suma de números pares en el rango es: ${resultado}`);