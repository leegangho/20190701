#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 10 //ť ������� 5

typedef int element;
typedef struct {
	int front; //ť�� front �� rear �� �ִ�.
	int rear;
	element data[MAX_QUEUE_SIZE];
}QueueType;

void error(char *message) {
	fprintf(stderr, "%s\n", message);
	exit(1);
}

void init_queue(QueueType *q) {
	q->rear = -1; //ť�� ���´� rear =-1, front =-1 �� �ʱ�ȭ 
	q->front = -1;
}

void queue_print(QueueType *q) { //ť�� ���Ҹ� ����Ʈ �Ѵ�.
	for (int i = 0; i < MAX_QUEUE_SIZE; i++) { //ť ������ ��ŭ �ݺ��Ѵ�.
		if (i <= q->front || i > q->rear) //front �޺κ�, rear �պκ��� ����ִ�.
			printf(" |"); // ���� ����ִ� �κ��� ����Ѵ�.
		else
			printf("%d|", q->data[i]); //front �� rear ���� �ȿ� �ִ� ���Ҹ� ����Ѵ�.
	}                                  // data[i] �� ���� �ȿ� �ִ� ���ҵ��̴�.
	printf("\n");
}

int is_full(QueueType *q) {
	if (q->rear == MAX_QUEUE_SIZE - 1) //rear�� ť������-1 �� �Ǹ� ���� �� ����
		return 1;
	else
		return 0;
}

int is_empty(QueueType *q) {
	if (q->front == q->rear) //front�� rear�� �������� empty
		return 1;
	else
		return 0;
}

void enqueue(QueueType *q, int item) {
	if (is_full(q)) {
		error("ť�� ��ȭ�����Դϴ�.");
		return;
	}
	q->data[++(q->rear)] = item; // ť�� �������� rear�� �����̸鼭 �ִ´�.
}                                // ť�� rear,front �� -1�� �ʱ�ȭ �̹Ƿ� ++(q->rear)�� �Ѵ�.

int dequeue(QueueType *q) {
	/*if (is_empty(q)) {
		error("ť�� ��������Դϴ�.");
		return -1;
	}*/
	int item = q->data[++(q->front)]; // front�� �����̸鼭 ����Ѵ�.
	return item;                      // dequeue�Լ� ��ȯ�� �Ѵ�.
}




int compare(const void *a, const void *b)
{
	return *(int *)a - *(int *)b;
}

int suffle(int a, int b)
{
	int suffle_scoville;
	suffle_scoville = a + (b * 2);

	return suffle_scoville;
}



int main(void)
{
	QueueType q;
	init_queue(&q);

	int scoville[] = {1,2,3,9,10,12};
	int K = 7;
	int N=6; // �迭 ����

	int result;
	int count=0;
	
	for (int i = 0; i < 6; i++)
	{
		enqueue(&q, scoville[i]);
	}
	qsort(q.data, N, sizeof(int), compare);
	
	while (1)
	{
		if (q.data[(q.front + 1)] < K) {
			result = suffle(dequeue(&q), dequeue(&q));
			enqueue(&q, result);
			qsort(q.data, N, sizeof(int), compare);
			count++;
		}
		else
			break;

	}
	printf("%d", count);
	return 0;
}