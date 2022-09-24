int min(int a[],int n)
{
    int i,min=a[0],index=0;
    for(i=1;i<n;i++)
    {
        if(a[i]<min)
        {
            min=a[i];
            index=i;
        }
    }
    return index+1;
}
int max(int a[],int n)
{
    int i,max=a[0],index=0;
    for(i=1;i<n;i++)
    {
        if(a[i]>max)
        {
            max=a[i];
            index=i;
        }
    }
    return index+1;
}
int avg(int a[],int n)
{
    int i,sum=0;
    for(i=0;i<n;i++)
    {
        if(a[i]>0)
        {
            sum=sum+a[i];
        }
    }
    return sum/n;
}
int sum(int a[],int n)
{
    int i,sum=0;
    for(i=0;i<n;i++)
    {
        sum=sum+a[i];
    }
    return sum;
}
int main()
{
    int n=12,i;
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Total rainfall : %d\n",sum(a,n));
    printf("Average rainfall : %d\n",avg(a,n));
    printf("Lowest rainfall month : %d\n",min(a,n));  
    printf("Highest rainfall month: %d\n",max(a,n));
    return 0;
   
}