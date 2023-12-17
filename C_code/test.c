#include <stdio.h>
#include "location_helpers.h"

int main(){
    int i, j, l_dim;
    l_dim = 2;
    int dimensions[2] = {3, 3};
    int matrix_loc[2];
    int loc_vec;

    int arr[3][3] = {{1,2,3}, {4,5,6}, {7, 8, 9}};

    for ( i = 0; i < 3; i++ ){
        for ( j = 0; j < 3; j ++ ){
            matrix_loc[0] = i;
            matrix_loc[1] = j;
            loc_vec = loc_vector(l_dim, dimensions, matrix_loc);
            printf("location is = %d\n", loc_vec);
            printf("array_value = %d\n\n", arr[i][j]);
        }
    }

}