#include <stdio.h>

#define MAX_STACK_SIZE 100

typedef char element;

typedef struct {
	element data[MAX_STACK_SIZE];
	int top;
}StackType;


void init_stack(StackType *s)
{
	s->top = -1;
}

int is_empty(StackType *s) {
	return (s->top == -1);
}

int is_full(StackType *s)
{
	return (s->top == (MAX_STACK_SIZE - 1));
}

void push(StackType *s, element item)
{
	if (is_full(s)) {
		fprintf(stderr, "push_error");
		return;
	}
	else
		s->data[++(s->top)] = item;
}

element pop(StackType *s)
{
	if (is_empty(s)) {
		fprintf(stderr, "pop_error");
		exit(1);
	}
	else
		return s->data[(s->top)--];
	//return s->data[(s->top)--];
}

int main(void)
{
	// Stack ������ �����
	StackType s;

	// Stack�� �ʱ�ȭ ���ѳ���
	init_stack(&s);

	// ������ �ϵ��ڵ�..�� 
	char bar[] = { '(',')','(','(','('
	,'(',')','(',')',')',
	'(','(',')',')','(',')' ,')',')','(','(',')',')' };

	int count = 0;

	//for ���� ������ ��ȣ ������ŭ ���ƿ�
	// ��ȣ ������ 21
	for (int i = 0; i <= 21; i++)
	{	
		// '('�� ������ stack�� �־��
		if (bar[i] == '(') {
			push(&s, bar[i]);
		}

		// ')'�� ������ ���������� ������ �������� �Ǵ�

		else {
			// ')' �ٷ� �տ��� ������.
			pop(&s);
			//�������� stack�� ����ִ� '('��ŭ ������ ����.
			if (bar[i-1] == '(')
				// stack�� top�� =-1�� �����߱⶧����
				// +1�� �մϴ�. 
				// ���� ���鶧 top�� 0���� �ϴ°Ͱ� ���ƿ�
				count += s.top+1;
			else {
				// �������� �ƴ� �׳� ����� ���̸�
				// �ѹ��� �����ָ� �ǿ�~
				count++;
			}
		}
	}
	//������ ��� ��� 
	printf("%d", count);
	
	return 0;
}