#include <stdlib.h>
#include <stdbool.h>

typedef struct TrieNode {
    struct TrieNode* trie[26];
    bool flag;
} TrieNode;

typedef struct {
    TrieNode* root;
} Trie;


TrieNode* createNode() {
    TrieNode* node = (TrieNode*)malloc(sizeof(TrieNode));

    node->flag = false;

    for (int i = 0; i < 26; i++) {
        node->trie[i] = NULL;
    }

    return node;
}


Trie* trieCreate() {
    Trie* obj = (Trie*)malloc(sizeof(Trie));

    obj->root = createNode();

    return obj;
}


void trieInsert(Trie* obj, char* word) {

    TrieNode* head = obj->root;

    for (int i = 0; word[i] != '\0'; i++) {

        int index = word[i] - 'a';

        if (head->trie[index] == NULL) {
            head->trie[index] = createNode();
        }

        head = head->trie[index];
    }

    head->flag = true;
}


bool trieSearch(Trie* obj, char* word) {

    TrieNode* head = obj->root;

    for (int i = 0; word[i] != '\0'; i++) {

        int index = word[i] - 'a';

        if (head->trie[index] == NULL) {
            return false;
        }

        head = head->trie[index];
    }

    return head->flag;
}

bool trieStartsWith(Trie* obj, char* prefix) {

    TrieNode* head = obj->root;

    for (int i = 0; prefix[i] != '\0'; i++) {

        int index = prefix[i] - 'a';

        if (head->trie[index] == NULL) {
            return false;
        }

        head = head->trie[index];
    }

    return true;
}


void trieFree(Trie* obj) {

    free(obj);
}