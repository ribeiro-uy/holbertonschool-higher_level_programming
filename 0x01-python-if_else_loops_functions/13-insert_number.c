#include "lists.h"

/**
 * insert_node - Checks if a singly linked list has a cycle in it.
 * @head: pointer to head
 * @number: number
 *
 * Return: 0 (no cycle)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	temp = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	else
	{
		if (node->n < (*head)->n)
		{
			node->next = *head;
			*head = node;
			return (node);
		}
		else
		{
			temp = temp->next;
			while (temp->next != NULL)
			{
				if (number >= temp->n && number <= temp->next->n) 
				{
					node->next = temp->next;
					temp->next = node;
					return (node);
				}
				temp = temp->next;
			}
			temp->next = node;
			return (node);
		}
	}
}
