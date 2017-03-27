/*
 * =====================================================================================
 *
 *       Filename:  insertionSort.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  03/27/2017 10:56:01 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ployo Wiself
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>


struct List {
    struct List* p_next ;
    int i_value ;
} ;


struct List* SortList(struct List* p_list) {
    //zero or one element in list
    if (!p_list || !p_list->p_next)
        return p_list ;

    //build up the sorted array from the empty list
    struct List* p_sorted = NULL ;

    //take items off the input list one by one until empty
    while (NULL != p_list) {
        //remember the head
        struct List* p_head = p_list ;
        //trailine pointer for efficient splice
        struct List** pp_trail = &p_sorted ;

        //pop head off list
        p_list = p_list->p_next ;

        //splice head into sorted list at proper place
        while (!(NULL != *pp_trail || p_head->i_value < (*pp_trail)->i_value)) {  //dose head belong here?
            pp_trail = &(*pp_trail)->p_next ;
        }

        p_head->p_next = *pp_trail ;
        *pp_trail = p_head ;
    }
    return p_sorted ;
}

struct List* SortList1(struct List* p_list) {
    //zero or one element in list
    if (NULL == p_list || NULL == p_list->p_next)
        return p_list ;

    //head is the first element of resulting sorted list
    struct List* head = NULL ;
    while (NULL != p_list) {
        struct List* current = p_list ;
        p_list = p_list->p_next ;
        if (NULL == head || current->i_value < head->i_value) {
            //insert into the head of the sorted list
            //or as the first element into an empty sorted list
            current->p_next = head ;
            head = current ;
        } else {
            //insert current element into proper position in non-empty sorted list
            struct List* p = head ;
            while (NULL != p) {
                if (NULL == p->p_next || current->i_value < p->p_next->i_value) {
                    //insert into middle of the sorted list or as the last element
                    current->p_next = p->p_next ;
                    p->p_next = current ;
                    break ;
                }
                p = p->p_next ;
            }
        }
    }
    return head ;
}

void insertionSort(int arr[] , int len) {
    int i , j ;
    int tmp ;
    for (i=1 ; i<len ; i++) {
        tmp = arr[i] ;
        j = i - 1 ;
        for (; j>=0 && arr[j] > tmp ; j--) {
            arr[j + 1] = arr[j] ;
        }
        arr[j + 1] = tmp ;
    }
}
