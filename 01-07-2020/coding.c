1.	#include<stdio.h>    
2.	#include<stdlib.h>  
3.	int main(){  
4.	  int ch=65;    
5.	    int i,j,k,m;    
6.	  system("cls");  
7.	    for(i=1;i<=5;i++)    
8.	    {    
9.	        for(j=5;j>=i;j--)    
10.	            printf(" ");    
11.	        for(k=1;k<=i;k++)    
12.	            printf("%c",ch++);    
13.	            ch--;    
14.	        for(m=1;m<i;m++)    
15.	            printf("%c",--ch);    
16.	        printf("\n");    
17.	        ch=65;    
18.	    }    
19.	return 0;  
20.	}  

