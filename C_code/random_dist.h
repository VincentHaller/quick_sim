#include <stdlib.h>
#include <math.h>

double get_uniform() { 
    return ((double)rand() / (double)RAND_MAX); 
    }

double get_normal(double loc, double scale) {
    double u_1, u_2, n;
    
    u_1 = get_uniform();
    u_2 = get_uniform();

    n =  sqrt( -2*log(u_1) ) * cos( 2*M_PI*u_2 )  * scale + loc;

    return n;
}