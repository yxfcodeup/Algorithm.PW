/*
 * =====================================================================================
 *
 *       Filename:  insertionSort.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  03/27/2017 11:37:44 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>


template<typename T>
void insertionSort(T arr[] , int len) {
    int i , j ;
    T tmp ;
    for (i = 1 ; i < len ; i++) {
        tmp = arr[i] ;
        j = i - 1 ;
        for (; j >= 0 && arr[j] > tmp ; j--) {
            arr[j + 1] = arr[j] ;
        }
        arr[j + 1] = tmp ;
    }
}
