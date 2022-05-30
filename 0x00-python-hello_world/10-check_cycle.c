#include "lists.h"
/**
 *check_cycle - checks whether a singly linked list has a cycle in it
 *@list:linked list to test
 *Return:0 - no cycle, 1 - cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *front = list, *rear = list;

	while (front && rear && front->next)
	{
		front = hare->next->next;
		rear = rear->next;
		if (front == rear)
			return (1);
	}
	return (0);
}
