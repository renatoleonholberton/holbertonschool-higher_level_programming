#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a linked list has a cycle
 * @head: Head node of linked list
 *
 * Return: 1 if the lists has a cycle, 0 otherwise
*/
int check_cycle(listint_t *head)
{
	listint_t *slow, *fast;

	if (head == NULL)
		return (0);

	slow = fast = head;

	while (slow != NULL)
	{
		slow = slow->next;
		if (fast == NULL || fast->next == NULL)
			return (0);

		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
