#include<stdio.h>

int a1, b1, c1, a2, b2, c2, producto_escalar;   /* Componentes de los vectores y resultado*/

#define m 100
int main()
{
    int C, i, j, k;
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

        /* Lectura de datos */
        
        printf("Componentes del primer vector (separadas por espacios): ");
        scanf("%d %d %d", &a1, &b1, &c1);

        printf("\n\nComponentes del segundo vector (separadas por espacios): ");
        scanf("%d %d %d", &a2, &b2, &c2);
        
        /* Procesamiento de información */
        startwtime = omp_get_wtime();
        
        producto_escalar = a1*a2 + b1*b2 + c1*c2;

        endwtime = omp_get_wtime(); // Termina de medir el tiempo Total
        double dt = (endwtime - startwtime);
        
        /* Impresión de resultados */
        
        printf("\n\nEl producto escalar es como sigue: ");
        printf("(%d,%d,%d) · (%d,%d,%d) = %d", a1, b1, c1, a2, b2, c2, producto_escalar);

        printf("\n\nTerminación normal del programa.\n");

        return 0;
}