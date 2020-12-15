#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome.
 *
 * @head: pointer to the head of the list
 *
 * Return: Always 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int n = 0;

	if (*head == NULL)
		return (1);

	n = current->n;
	while (current->next != NULL)
		current = current->next;

	if (n == current->n)
		return (1);

	return (0);
}
