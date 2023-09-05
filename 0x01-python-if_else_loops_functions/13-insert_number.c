#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Func that inserts a num into a sorted singly linked list.
 *
 * @head: A pointer to the head of the linked list.
 * @number: The number that will be inserted.
 *
 * Return: return the address of the new node, or NULL if it fails.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!current || new->n < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (!current->next || new->n < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
