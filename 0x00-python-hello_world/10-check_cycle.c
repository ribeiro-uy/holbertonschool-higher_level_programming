#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head  of the list
 *
 * Return: 1 if the linked list has a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *future = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (current && future)
	{
		current = current->next;
		future = future->next->next;
		if (current->next == future->next)
			return (1);
	}
	return (0);
}
