#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - func that will be check if a singly-linked list contains a cycle.
 * 
 * @list: A singly-linked list value
 * 
 * Return: return 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr = list;
	while (fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
