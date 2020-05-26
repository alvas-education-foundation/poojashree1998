
# Function to check if linked list is palindrome or not
def checkPalin(head):
	return checkPalindrome(head, head)[0]


if __name__ == '__main__':

	# input keys
	keys = [1, 3, 5, 3, 1]

	head = None
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	if checkPalin(head):
		print("Linked list is Palindrome")
	else:
		print("Linked list is not Palindrome")
