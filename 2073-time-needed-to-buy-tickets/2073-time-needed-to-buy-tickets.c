int timeRequiredToBuy(int* t, int tSize, int k) {
    int res = 0;

    for (int i = 0; i < tSize; i++) {
        int x = t[k] - (i > k);

        if (x < t[i]) {
            res += x;
        } else {
            res += t[i];
        }
    }

    return res;
}