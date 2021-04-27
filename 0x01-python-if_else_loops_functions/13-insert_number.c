#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list
 * @head: Double pointer to list's head
 * @number: Value as a number
 *
 * Return: Pointer to the inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev = NULL, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(*new_node));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/* Add to the begining */
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (curr = *head; curr != NULL && curr->n < number ; curr = curr->next)
		prev = curr;

	new_node->next = prev->next;
	prev->next = new_node;

	return (new_node);
}
