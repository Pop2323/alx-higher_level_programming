#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a singly linked list
 * @head: double pointer to the head of the list
 *
 * Return: return return the ptr for the first node
 */
void reverse_list(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;
	next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *temp, *second_half;

	slow = *head;
	fast = *head;
	temp = *head;
	second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			second_half = slow->next;
			break;
		}
		if (!fast->next)
		{
			second_half = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&second_half);

	while (second_half && temp)
	{
		if (temp->n != second_half->n)
			return (0);

		second_half = second_half->next;
		temp = temp->next;
	}
	return (!second_half);
