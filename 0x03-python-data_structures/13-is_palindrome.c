#include "lists.h"

/**
 * is_palindrome - Checks if a function is a palindrome
 * @head: Double pointer to head node
 *
 * Return: 1 if list is palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *start;

	if (head == NULL || *head == NULL)
		return (1);

	start = *head;
	return (check_palindrome(&start, start));
}

/**
 * check_palindrome - Check if a list is a palindrome
 * @start: Double pointer to head node
 * @end: Pointer to compare with start
 *
 * Return: 1 if the list is palindrome, 0 otherwise
*/
int check_palindrome(listint_t **start, listint_t *end)
{
	int res = 1;

	if (end == NULL)
		return (1);

	res = check_palindrome(start, end->next);
	res = res && ((*start)->n == end->n);
	*start = (*start)->next;

	return (res);
}
