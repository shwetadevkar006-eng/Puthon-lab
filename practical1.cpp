#include<iostream>
using namespace std;

struct Student
{
	int roll;
	string name;
	float marks;
};

void display(Student*s,int n)
{
	for(int i=0; i<n; i++)
	{
		cout<<"\nRoll No: "<<(s+i)->roll;
		cout<<"\nName: "<<(s+i)->name;
		cout<<"\nMarks: "<<(s+i)->marks
	    << endl;
	
	}
}

int main()
{
	Student s[10];
	int n;
	cout<<"Enter number of students: ";
	cin>>n;
	
	for(int i=0; i<n; i++)
	{
		cout<<"\nEnter Roll No: ";
		cin>>s[i].roll;
		
		cout<<"\nEnter Name: ";
		cin>>s[i].name;
		
		cout<<"\nEnter Marks: ";
		cin>>s[i].marks;
		
		
	}
	
	cout<<"\n-*-*-Students Record-*-*-";
	display(s,n);
	
	
	return 0;
	
	
}








