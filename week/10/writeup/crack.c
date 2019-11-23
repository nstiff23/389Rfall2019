#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

//helper function to print hashes for debugging
void print_hash(unsigned char *hash, size_t len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("%c", hash[i]);
	}
}

int main(int argc, char **argv) {
	unsigned char key[2];
	unsigned char *hash;
	unsigned char fd_key_hash[16];
	unsigned char good_key[2];
	char collision[4];
	char test_collision[3];
	int fd;

	memset(collision, 0, 4);

	fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
	read(fd, fd_key_hash, 16);
	//printf("Stored key hash: ");
	//print_hash(fd_key_hash, 16);
	//printf("\n");

	//use brute force to find the two characters that hash to the stored hash
	for (int i = 0; i < 256; i++) {
		for (int j = 0; j < 256; j++) {
			key[0] = i;
			key[1] = j;
			hash = md5_hash(key, 2);

			//printf("Tried: ");
			//print_hash(key, 2);
			//printf("\nHash: ");
			//print_hash(hash, 16);
			if (memcmp(hash, fd_key_hash, 16) == 0) {
				memcpy(good_key, key, 2);
				//printf(" - Success!\n");
			//} else {
				//printf(" - Failure\n");
			}
			//fflush(stdout);
			free(hash);
		}
	}

	//use brute force again to find something that hashes to those two characters
	for (int i = 32; i < 127; i++) {
		for (int j = 32; j < 127; j++) {
			for (int k = 32; k < 127; k++) {
				test_collision[0] = i;
				test_collision[1] = j;
				test_collision[2] = k;
				unsigned char *test_hash = md5_hash(test_collision, 3);
				if (memcmp(test_hash, good_key, 2) == 0) {
					memcpy(collision, test_collision, 3);
				}
				free(test_hash);
			}
		}
	}

	printf("%s\n", collision);

	close(fd);

	return 0;
}
