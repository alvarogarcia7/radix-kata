# Trie Kata - C

ORGANIC: O

## Learning goals

Learning goals for this kata:

1. Practice C, low level, unaided by and IDE, debugger, or AI
2. Implement a data structure using TDD
3. Practice recursion
4. C-Specific goals: manual memory management, strings

## Implementation notes

1. Each trie /tri/ node will have a variable-size number of children
2. In each trie node will be compact: as many characters in the `word` as possible, compacting levels.
3. Any node can be a word, indicated by the `is_final` flag

