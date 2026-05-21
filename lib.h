#include <stdbool.h>

typedef struct trie_t {
	int size;
	struct trie_t *children;
	char *word;
	bool is_final;
} trie_t;



