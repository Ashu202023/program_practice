#include <stdio.h>
#include <pthread.h>

void *print_hello_world(void *thread_num_ptr) {
    int thread_num = *((int *)thread_num_ptr);
    for (int i = 0; i < 5; i++) {
        printf("Hello, World (thread %d)\n", thread_num);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[10];
    int thread_nums[10];

    for (int i = 0; i < 10; i++) {
        thread_nums[i] = i;
        pthread_create(&threads[i], NULL, print_hello_world, (void *)&thread_nums[i]);
    }

    // Wait for all threads to complete
    for (int i = 0; i < 10; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}

