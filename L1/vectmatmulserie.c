#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <omp.h>

float **Matrix=NULL;
float *Vector=NULL;
float *Result=NULL;

void create_matrix_vector(uint32_t n){
	uint32_t i=0;
	uint32_t j=0;
	Matrix=(float **)calloc(n,sizeof(float *));
	Vector=(float *)calloc(n,sizeof(float));
	Result=(float *)calloc(n,sizeof(float));
        for(i=0;i<n;i++){
                Matrix[i]=(float *)calloc(n,sizeof(float));

		for(j=0;j<n;j++){
			Matrix[i][j]=rand()%100;
		}
	Vector[i]=rand()%100;
        }
}

void freeMatrix(uint32_t n){
uint32_t i=0;
for(i=0;i<n;i++){
        free(Matrix[i]);
       }
        free(Matrix);
	free(Vector);
	free(Result);
}

void multiply_vector_matrix_serial(uint32_t n){
	uint32_t column=0;
	uint32_t row=0;

	for(column=0;column<n;column++){
		for(row=0;row<n;row++){
			Result[column]+=Matrix[row][column]*Vector[row];
		}
	}
}


int main(int argc,char *argv[]){
	uint32_t N=0;
	uint32_t j=0;
	uint32_t i=0;
	double t[2]={};
	if(argc<2)N=2;
	else
		N=atoi(argv[1]);

	
	create_matrix_vector(N);
	t[1]=omp_get_wtime();
	multiply_vector_matrix_serial(N);
	t[0]=omp_get_wtime();
	printf("Time: %.4lf\n",t[0]-t[1]);
	
	printf("\nVector\n");

        for(j=0;j<N;j++){
                printf("%.2f\t",Vector[j]);
        }

	printf("\nMatrix\n");
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			printf("%.2f\t",Matrix[i][j]);
		}

		printf("\n");

	}
	
	
	printf("\nResult\n");

	for(j=0;j<N;j++){
		printf("%.2f\t",Result[j]);
	}

	freeMatrix(N);
	return 0;
}
