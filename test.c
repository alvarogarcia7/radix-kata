#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "lib.h"


trie_t* new(){
	trie_t *ret = malloc(sizeof(trie_t));
	ret->size = 0;
	ret->children=NULL;
	ret->word=NULL;
	ret->is_final=false;
	return ret;
}

void insert(trie_t *trie, char *new);


bool test_1_trie_with_0_children() {
	trie_t *t = new();
	assert (t->size == 0);
	assert (t->children == NULL);
	assert (t->word == NULL);
	assert (t->is_final == false);
	return true;
}

bool test_2_empty_trie_with_1_child_hence_1_level() {
	trie_t *t = new();

	insert(t, "animal");

	assert (t->size == 0);
	assert (t->children == NULL);
	assert (strcmp(t->word, "animal") == 0);
	assert (t->is_final == true);

	return true;
}


int main(int argc, char **argv) {
	assert (test_1_trie_with_0_children() == true);
	assert (test_2_empty_trie_with_1_child() == true);
	return 0;
}


void insert(trie_t *trie, char *new) {
	int common = -1;
	trie_t *t = trie;
	if (NULL != t->word) {
		for (int i = 0; i < strlen(t->word); i++){
			if (t->word[i] == new[i]){
				common = i;
				continue;
			}
			else {
				break;
			}
		}
	} else {
		t->word = malloc(strlen(new) + 1);
		strcpy(t->word, new);
		t->is_final = true;
		return;
	}

	int insert_at = -2;

	for (int cc = 0; cc < t->size; cc++) {
		char *c = t->children[cc].word;
		for (int k = 0; k < strlen(c); k++) {
			if (new[common] == c[k]) {
				insert(&t->children[cc], &new[k]);
			} else if (new[common] > c[k]) {
				insert_at = k-1;
			} else {
				continue;
			}
		}
	}

	if (insert_at == -2) {
		insert_at = t->size;
	}

	// trie_t *c2 = realloc(t->children, 100);
}


