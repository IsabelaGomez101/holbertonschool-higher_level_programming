#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle.
 * @list: pointer to head of singly list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *pointer1 = list;
	listint_t *pointer2 = list;

while (pointer1 && pointer2 && pointer2->next)
{
	pointer1 = pointer1->next;
	pointer2 = pointer2->next->next;
	if (pointer1 == pointer2)
	return (1);
}
return (0);
}
