#ifndef CACHE_H
#define CACHE_H

void init_cache();
void free_cache();
char *cache_get(const char *query);
void cache_set(const char *query, const char *result);

#endif // CACHE_H
