#include "lists.h"

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
	listint_t *current = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!current || new_node->n < current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current)
	{
		if (!current->next || new_node->n < current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (NULL);
}
