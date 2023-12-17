// Includes

// Functions

int loc_vector( int l_dim, int *dimensions, int *location ){
    int i, vector_loc, mult_value, dim_end;
    
    vector_loc = 0;
    mult_value = 1;

    dim_end = l_dim-1;

    for ( i = 0; i < l_dim; i++ ){
        vector_loc += mult_value * location[dim_end - i];
        mult_value *= dimensions[dim_end - i];
    }

    return vector_loc;
}

void loc_matrix( int *matrix_loc,int l_dim,  int *dimensions, int location ){
    int i, mult_value;

    mult_value = 1;

    for ( i = 0; i < l_dim; i++ ){
        matrix_loc[i] = location/mult_value;
        location %= mult_value;
        if ( i < ( l_dim - 1 )){
            mult_value /= dimensions[i+1];
        }
    }

}