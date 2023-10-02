#include <iostream>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode() {
        child[0] = nullptr;
        child[1] = nullptr;
    }
    TrieNode* child[2];
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    void insert(int n) {
        TrieNode* temp = root;
        int i = 31;

        while (i >= 0) {
            int bit = (n >> i) & 1;

            if (!temp->child[bit]) {
                temp->child[bit] = new TrieNode();
            }

            temp = temp->child[bit];
            i--;
        }
    }

    int maxXorHelper(int value) {
        TrieNode* temp = root;
        int curr = 0;
        int i = 31;
        
        while (i >= 0) {
            int bit = (value >> i) & 1;
            int toggleBit = bit ^ 1;
            
            if (temp->child[toggleBit]) {
                temp = temp->child[toggleBit];
                curr += (1 << i);
            } else {
                temp = temp->child[bit];
            }
            
            i--;
        }
        return curr;
    }

private:
    TrieNode* root;
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int maxVal = 0;
        trie.insert(nums[0]);

        for (size_t i = 1; i < nums.size(); i++) {
            maxVal = max(trie.maxXorHelper(nums[i]), maxVal);
            trie.insert(nums[i]);
        }

        return maxVal;
    }
};