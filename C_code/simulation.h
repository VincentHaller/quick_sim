// Includes
#include <math.h>
#include "random_dist.h"
// Functions

void simulate(double *ptr_out[], int N, int h, int exp_bool) {

    int i, j;
    double mult;
    double **out;
    **out = &ptr_out;

    if ( exp_bool ) {
        for (j = 0; j < N; j++) {
            out[j][0] = 1;
            for ( i = 1; i < h; i++ ) {
                mult = exp( fabs( get_normal( 1, 0.01 )));
                out[j][i] = out[j][i-1] * mult;
    }}}

    else {
        for ( j = 0; j < N; j++ ) {
            out[j][0] = 1;
            for ( i = 1; i < h; i++ ) {
                mult = fabs( get_normal( 1, 0.01 ));
                out[j][i] = out[j][i-1] * mult;
    }}}

    // for (i = 1; i < h; i++ ) {
    //     for ( j = 0; j < N; j++ ) {
    //         mult = exp_bool == 1 ? exp(abs(get_normal(0, 0.01))) : abs(get_normal(0, 0.01))
    //         out[i][j] = out[i-1][j] * mult
    // }}
}