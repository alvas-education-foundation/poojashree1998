/*monk watching fight*/
#include <stdio.h>
struct node{
	int value;
	struct node *left;
	struct node *right;
};
struct node *newnode(int value){
	struct node *makenode = (struct node*)malloc(sizeof(struct node));
	makenode->value = value;
	makenode->left = NULL;
	makenode->right = NULL;
	return makenode;
}
 
struct node *bst(struct node *root,int value){
	if(root == NULL ){
		return newnode(value);
	}
	else{
		if(value <= root->value){
			root->left = bst(root->left,value);
		}
		else{
			root->right = bst(root->right, value);
		}
	return root;
	}
}
 
void traverse(struct node *root){
	if(root == NULL){
		return;
	}
	traverse(root->left);
	printf("%d\n",root->value);
	traverse(root->right);
}
 
int max(int a, int b){return (a>b)?a:b;}
int height(struct node *root){
	if(root == NULL){
		return 0;
	}
	return 1+max(height(root->left), height(root->right));
}
 
 
int main(){
int n, i, j;
struct node *lulu;
scanf("%d",&n);
int *array = (int*)malloc(n*sizeof(int));
for(i=0;i<n;i++){
	scanf("%d",&array[i]);
}
for(j=0;j<n;j++){
	if(j==0){
		lulu = newnode(array[0]);
	}
	else{
		bst(lulu,array[j]);
	}
}
 
printf("%d",height(lulu));
}
