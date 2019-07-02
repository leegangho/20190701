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
	// Stack 구조를 만든다
	StackType s;

	// Stack을 초기화 시켜놓음
	init_stack(&s);

	// 문제를 하드코딩..ㅠ 
	char bar[] = { '(',')','(','(','('
	,'(',')','(',')',')',
	'(','(',')',')','(',')' ,')',')','(','(',')',')' };

	int count = 0;

	//for 문을 문제의 괄호 갯수만큼 돌아요
	// 괄호 갯수는 21
	for (int i = 0; i <= 21; i++)
	{	
		// '('를 만나면 stack에 넣어요
		if (bar[i] == '(') {
			push(&s, bar[i]);
		}

		// ')'를 만나면 레이저인지 끝나는 지점인지 판단

		else {
			// ')' 바로 앞에는 빼내요.
			pop(&s);
			//레이저면 stack에 들어있는 '('만큼 갯수를 세요.
			if (bar[i-1] == '(')
				// stack의 top을 =-1로 설정했기때문에
				// +1를 합니다. 
				// 구조 만들때 top을 0으로 하는것과 같아요
				count += s.top+1;
			else {
				// 레이저가 아닌 그냥 막대기 끝이면
				// 한번만 더해주면 되요~
				count++;
			}
		}
	}
	//마지막 결과 출력 
	printf("%d", count);
	
	return 0;
}