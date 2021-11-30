// Producto Escalar de 2 vectores
// Calculo en Paralelo con OMP. (Program SPMD)
#include <omp.h>
#include <stdio.h>
#include <math.h>
//#include <iostream.h>
//#include <iomanip.h>
//using namespace std;

#define m 100                   // Dimension del Vector A y del Vector B
int main(int argc, char **argv) // Declaracion de variables
{
    int myid, nthreads; // Id, cantidad de hilos
    int C, i, j, k;
    nthreads = omp_get_num_threads();
    double a[m], b[m];
    double *A = a; // Definimos los vectores en forma dinamica
    double *B = b;
    float dt;
    double startwtime = 0.0, endwtime; // Variables de tiempo
    // ARMADO DE VECTORES
    // Armado del Vector A
    for (i = 0; i < m; i++)
        A[i] = i + 1;
    // Armado del Vector B
    for (j = 0; j < m; j++)
        B[j] = 2 * (j + 1);
    // Armado del Escalar C
    C = 0;
    // Iniciamos el producto
    startwtime = omp_get_wtime(); // Comienza a medir el tiempo Total
// Paralelizamos
#pragma omp parallel shared(A, B, C, nthreads) private(myid, i, j, k)
    {
        myid = omp_get_thread_num();
        nthreads = omp_get_num_threads();
        for (i = myid; i < m; i += nthreads)
#pragma omp critical // Declaramos una zona critica
        {
            C = C + A[i] * B[i];
        }
    }                           // Fin paralelismo
    endwtime = omp_get_wtime(); // Termina de medir el tiempo Total
    dt = (endwtime - startwtime);
    printf("\n");
    printf("PRODUCTO ESCALAR DE 2 VECTORES");
    printf("\n");
    printf(" Resultado del producto escalar: %d \n", C);
    printf("\n");
    //// Para verificar mostramos las matrices y vectores
    //// Vector A
    // printf('\n';
    // printf("Vector A" << '\n';
    // for (i = 0; i < m; i++)
    // {
    // printf(A[i] << '\t';
    // }
    // printf('\n';
    //
    //// Vector B
    // printf('\n';
    // printf("Vector B" << '\n';
    // for (j = 0; j < m; j++)
    // {
    // printf(B[j] << "\t \n";
    // }
    // printf('\n';
    printf("El tiempo de calculo Total fue: %.9f seg\n", dt);
    printf("\n");
    return 0;
}