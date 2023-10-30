#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

size_t listint_t(const listint_t *h);
listint_t *add_nodeint(listint_ **head, const int n);
void free_listint(listint_t);
int check_cycle(listint_t *list);

#endif
