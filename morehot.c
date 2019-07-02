#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 10 //큐 사이즈는 5

typedef int element;
typedef struct {
	int front; //큐는 front 와 rear 가 있다.
	int rear;
	element data[MAX_QUEUE_SIZE];
}QueueType;

void error(char *message) {
	fprintf(stderr, "%s\n", message);
	exit(1);
}

void init_queue(QueueType *q) {
	q->rear = -1; //큐의 상태는 rear =-1, front =-1 로 초기화 
	q->front = -1;
}

void queue_print(QueueType *q) { //큐의 원소를 프린트 한다.
	for (int i = 0; i < MAX_QUEUE_SIZE; i++) { //큐 사이즈 만큼 반복한다.
		if (i <= q->front || i > q->rear) //front 뒷부분, rear 앞부분은 비어있다.
			printf(" |"); // 따라서 비어있는 부분을 출력한다.
		else
			printf("%d|", q->data[i]); //front 와 rear 범위 안에 있는 원소를 출력한다.
	}                                  // data[i] 가 범위 안에 있는 원소들이다.
	printf("\n");
}

int is_full(QueueType *q) {
	if (q->rear == MAX_QUEUE_SIZE - 1) //rear이 큐사이즈-1 이 되면 가득 찬 상태
		return 1;
	else
		return 0;
}

int is_empty(QueueType *q) {
	if (q->front == q->rear) //front가 rear와 같아지면 empty
		return 1;
	else
		return 0;
}

void enqueue(QueueType *q, int item) {
	if (is_full(q)) {
		error("큐가 포화상태입니다.");
		return;
	}
	q->data[++(q->rear)] = item; // 큐에 넣을때는 rear을 움직이면서 넣는다.
}                                // 큐를 rear,front 는 -1로 초기화 이므로 ++(q->rear)로 한다.

int dequeue(QueueType *q) {
	/*if (is_empty(q)) {
		error("큐가 공백상태입니다.");
		return -1;
	}*/
	int item = q->data[++(q->front)]; // front를 움직이면서 출력한다.
	return item;                      // dequeue함수 반환을 한다.
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
	int N=6; // 배열 개수

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