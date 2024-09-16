#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "cache.h"

#define CACHE_SIZE 100
#define TTL 60

typedef struct CacheEntry {
    char *query;
    char *result;
    time_t timestamp;
} CacheEntry;

static CacheEntry cache[CACHE_SIZE] = { { NULL, NULL, 0 } };

static size_t hash(const char *str) {
    size_t hash = 5381;
    int c;

    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }

    return hash;
}

void init_cache() {
    for (size_t i = 0; i < CACHE_SIZE; i++) {
        cache[i].query = NULL;
        cache[i].result = NULL;
    }
}

void free_cache() {
    for (size_t i = 0; i < CACHE_SIZE; i++) {
        free(cache[i].query);
        free(cache[i].result);
    }
}

char *cache_get(const char *query) {
    time_t now = time(NULL);
    size_t index = hash(query) % CACHE_SIZE;
    
    if (cache[index].query && strcmp(cache[index].query, query) == 0) {
        if (now - cache[index].timestamp < TTL) {
            return cache[index].result;
        } else {
            free(cache[index].query);
            free(cache[index].result);
            cache[index].query = NULL;
            cache[index].result = NULL;
        }
    }
    
    return NULL;
}

void cache_set(const char *query, const char *result) {
    size_t index = hash(query) % CACHE_SIZE;
    free(cache[index].query);
    free(cache[index].result);
    
    cache[index].query = strdup(query);
    cache[index].result = strdup(result);
    cache[index].timestamp = time(NULL);
}
