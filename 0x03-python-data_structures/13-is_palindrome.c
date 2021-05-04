#include "lists.h"

/**
 * is_palindrome - Checks if a function is a palindrome
 * @head: Double pointer to head node
 *
 * Return: 1 if list is palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev_head = NULL, *rev_curr, *curr;

	if (head == NULL || *head == NULL)
		return (1);

	for (curr = *head; curr != NULL; curr = curr->next)
		add_nodeint(&rev_head, curr->n);

	rev_curr = rev_head;
	for (curr = *head; curr != NULL; curr = curr->next)
	{
		if (curr->n != rev_curr->n)
			return (0);
		rev_curr = rev_curr->next;
	}

	free_listint(rev_head);
	return (1);
}

/**
 * add_nodeint - Adds a node at the start
 * @head: Double pointer to head node
 * @n: New node's data value
 *
 * Return: Pointer to hte newly created node
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(*new_node));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	if (*head != NULL)
		new_node->next = *head;
	*head = new_node;

	return (new_node);
}
