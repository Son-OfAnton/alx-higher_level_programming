#include "lists.h"
#include <stdlib.h>
/**
 *reverse_listint - reverses a linked list
 *@head:pointer to first node
 *Return:address of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current_node = *head, *next = NULL, *prev = NULL;

	while (current_node)
	{
		next = current_node->next;
		current_node->next = prev;
		prev = current_node;
		current_node = next;
	}
	*head = prev;
	return (*head);
}
/**
 *is_palindrome - checks whether a linked list is palindrome
 *@head:pointer to first node
 *Return:1 - on success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t size = 0, i;
	listint_t *tmpo, *reve, *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmpo = *head;

	for (size = 0; tmp; size++)
		tmpo = tmpo->next;
	tmpo = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmpo = tmpo->next;
	if ((size % 2) == 0 && tmpo->n != tmpo->next->n)
		return (0);
	tmpo = tmpo->next->next;
	reve = reverse_listint(&tmpo);
	mid = reve;

	tmpo = *head;
	while (reve)
	{
		if (tmpo->n != reve->n)
			return (0);
		tmpo = tmpo->next;
		reve = reve->next;
	}
	reverse_listint(&mid);

	return (1);
}
