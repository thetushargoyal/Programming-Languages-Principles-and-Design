#include<stdio.h> 
#define ROWS 5

int main() {
    int meru[ROWS][ROWS];
    for (int i=0; i<ROWS; i++) meru[i][0]=1;
    
    for (int i=0; i<ROWS; i++) 
        for (int j=1; j<=i; j++)
            meru[i][j]=meru[i-1][j-1]+meru[i-1][j];

    for (int i=0; i<ROWS; i++) { 
        for (int j=0; j<=i; j++)
            printf(meru[i][j]%2? "*":" "); 
            printf("\n");
    }
}