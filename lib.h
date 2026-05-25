#include <stdbool.h>
#include <stdio.h>

typedef struct trie_t {
	int size; // how many direct children this node has
	struct trie_t **children; // size == 0 <-> children == NULL
	char *word; // NULL means no word
	bool is_final;
} trie_t;

void debug_print_indented(trie_t *trie, int indentation_level) {
	printf("%.*s[%s] %s, %d children:\n", indentation_level, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", trie->is_final? "F" : " ", trie->word, trie->size);
	for (int i = 0; i < trie->size; i++) {
		debug_print_indented(trie->children[i], indentation_level + 1);
	}
}

void debug_print(trie_t *trie) {
	debug_print_indented(trie, 0);
}



