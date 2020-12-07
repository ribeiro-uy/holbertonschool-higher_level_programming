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
	listint_t *future = list->next;

	if (list == NULL)
		return (0);

	if (list->next == NULL)
		return (0);

	while (current->next != NULL)
	{
		while (future->next != NULL)
		{
			if (current->next == future->next)
				return (1);
			future = future->next;
		}
		current = current->next;
		future = current->next;
	}
	return (0);
}
