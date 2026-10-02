struct ListNode* reverseList(struct ListNode* head) {
    int ans[5000];
    int size = 0;

    struct ListNode* curr = head;

    while (curr != NULL) {
        ans[size++] = curr->val;
        curr = curr->next;
    }

    curr = head;

    for (int i = size - 1; i >= 0; i--) {
        curr->val = ans[i];
        curr = curr->next;
    }

    return head;
}