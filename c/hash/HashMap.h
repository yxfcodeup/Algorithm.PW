#ifndef HASH_MAP_H
#define HASH_MAP_H

typedef struct __hash_map_node {
    void* key;
    void* value;
    int hash;
    Entry* next;    // ָ����һ�����
} Entry;

typedef struct _hash_map {

} HashMap;

#endif // !HASH_MAP_H
