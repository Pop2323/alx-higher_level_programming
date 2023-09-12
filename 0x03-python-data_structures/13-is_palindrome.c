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

	while (current != NULL)
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
	listint_t *slow, *fast, *prev_slow, *second_half;
	int is_palindrome = 1;

	slow = fast = *head;
	prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;

	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);
	prev_slow->next = second_half;

	return (is_palindrome);
}
