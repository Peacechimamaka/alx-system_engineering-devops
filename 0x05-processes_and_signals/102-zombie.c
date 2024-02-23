#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * create_zombie_processes - Creates 5 zombie processes
 */
void create_zombie_processes() {
    int i;

    for (i = 0; i < 5; i++) {
        pid_t child_pid = fork();

        if (child_pid == -1) {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (child_pid > 0) {
            // Parent process
            printf("Zombie process created, PID: %d\n", child_pid);
        } else {
            // Child process
            exit(EXIT_SUCCESS);
        }
    }

    // Let the parent sleep to allow observing the zombie processes
    sleep(10);
}

int main(void) {
    create_zombie_processes();

    return 0;
}

