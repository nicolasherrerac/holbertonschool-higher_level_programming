#include <list.h>
/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: struct
 * Return: 0 if there is no cycle, 1 if there is a cylce
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	for (; first && second && second->next;)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
