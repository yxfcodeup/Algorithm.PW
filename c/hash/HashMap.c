#include "HashMap.h"

Entry* initEntry(void* k , void* v , int h , Entry* n) {
    Entry* entry;
    entry->key = k;
    entry->value = v;
    entry->hash = h;
    entry->next = n; 
    return entry;
}

bool equals(void* obj) {

}