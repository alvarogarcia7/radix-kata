#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "lib.h"
#include "log.h"

void assert_trie_node(trie_t *node, int expected_size, char *expected_word, bool expected_is_final){
	assert (node != NULL);
	assert (node->size == expected_size);
	assert (strcmp(node->word, expected_word) == 0);
	assert (node->is_final == expected_is_final);
}

trie_t* new(){
	trie_t *ret = malloc(sizeof(trie_t));
	ret->size = 0;
	ret->children=NULL;
	ret->word=NULL;
	ret->is_final=false;
	return ret;
}

void insert(trie_t **trie, char *new);


bool test_1_trie_with_0_children() {
	trie_t *t = new();
	assert (t->size == 0);
	assert (t->children == NULL);
	assert (t->word == NULL);
	assert (t->is_final == false);
	return true;
}

bool test_2_children_that_extend_the_parent_exactly() {
	trie_t *t = new();

	insert(&t, "animal");
	insert(&t, "animalada");

	assert_trie_node(t, 1, "animal", true);
	assert_trie_node(t->children[0], 0, "ada", true);
	
	insert(&t, "animaladas");
	assert_trie_node(t->children[0], 1, "ada", true);
	assert_trie_node(t->children[0]->children[0], 0, "s", true);
	
	insert(&t, "animaladasa");
	assert_trie_node(t->children[0]->children[0]->children[0], 0, "a", true);

	return true;
}

bool test_3_several_children_from_the_same_parent() {
	trie_t *t = new();

	insert(&t, "animal");
	insert(&t, "animalada");

	assert_trie_node(t, 1, "animal", true);
	assert_trie_node(t->children[0], 0, "ada", true);

	log_debug("Inserting animales");
	
	insert(&t, "animales");
	// assert_trie_node(t, 2, "animal", true);
	assert_trie_node(t->children[1], 0, "es", true);
	
	return true;
}

int main(int argc, char **argv) {
	assert (test_1_trie_with_0_children() == true);
	assert (test_2_children_that_extend_the_parent_exactly() == true);
	// assert (test_3_several_children_from_the_same_parent() == true);
	return 0;
}

void add_sibling(trie_t *trie, char *new_string) {
	log_debug("add_sibling(trie [%s], %s).", trie->word, new_string);
	debug_print(trie);
	trie_t **c2 = realloc(trie->children, sizeof(trie_t*) * (trie->size + 1));
	int insert_at = 0;
	for (int i = 0; i < trie->size; i++) {
		trie_t *c = trie->children[i];
		log_debug("children word: %s", c->word);
		if (c->word[0] <= new_string[0]) {
			continue;
		} else {
			insert_at = i + 1;
		}
	}
	log_debug("add_sibling. insert_at = %d", insert_at);
	for (int i = 0; i < insert_at; i++) {
		memcpy(&c2[i], &trie->children[i], sizeof(trie_t*));
	}

	trie_t *cc2 = new();
	cc2->children = NULL;
	cc2->word = malloc(strlen(new_string) + 1);
	strcpy(cc2->word, new_string);
	cc2->is_final = true;
	c2[insert_at] = cc2;
	// log_debug("add_sibling, after inserting the new element:");
	// debug_print(trie);
	// debug_print(cc2);

	for (int i = insert_at+1; i < trie->size; i++) {
		memcpy(&c2[i], &trie->children[i-1], sizeof(trie_t*));
	}
	free(trie->children);
	
	trie->children=c2;
	trie->size++;
}



void insert(trie_t **trie, char *new_string) {
	int common = -1;
	trie_t *t = *trie;
	if (NULL != t->word) {
		// there might be a common prefix
		for (int i = 0; i < strlen(t->word) && i < strlen(new_string); i++){
			if (t->word[i] == new_string[i]){
				common = i;
				continue;
			}
			else {
				break;
			}
		}
		log_debug("Found common? %s (common = %d)", common != -1? "true" : "false", common);
		if (common != -1) {
			log_debug("Common prefix: %.*s (len=%d)", common+1, t->word, common ); 
		}

		if (common == -1) {
			add_sibling(t, new_string);
		} else { // common prefix found
			if (t->size > 0) { // already has children: add a sibling
				insert(&t->children[0], &new_string[common+1]);
			} else {
				add_sibling(t, &new_string[common+1]);
			}
		}


		// // prefix found and alraedy has children
		// if(common != -1 && t->size > 0) {
		// 	log_trace("insert at children 0");
		// } else {
		// 	// no prefix 
		// 	log_trace("add_sibling to root");
		// 	add_sibling(t, &new_string[common+1]);
		// }

	} else {
		if (t->is_final) {
			// example: have "animal", insert "jungle": resulting: "" -> ["animal", "jungle"]
			// need to check if need another child
			trie_t *parent = new();
			parent->size = t->size+1;
			trie_t *c2 = realloc(t->children, sizeof(trie_t) * parent->size);

			c2[t->size] = *t;

			*trie = parent;
		} else {
			t->word = malloc(strlen(new_string) + 1);
			strcpy(t->word, new_string);
			t->is_final = true;
			return;
		}
	}

	// int insert_at = -2;
	//
	// for (int cc = 0; cc < t->size; cc++) {
	// 	char *c = t->children[cc]->word;
	// 	for (int k = 0; k < strlen(c); k++) {
	// 		if (new_string[common] == c[k]) {
	// 			insert((&t->children[cc]), &new_string[k]);
	// 		} else if (new_string[common] > c[k]) {
	// 			insert_at = k-1;
	// 		} else {
	// 			continue;
	// 		}
	// 	}
	// }
	//
	// if (insert_at == -2) {
	// 	insert_at = t->size;
	// }

	// trie_t *c2 = realloc(t->children, 100);
}


