import java.util.Scanner;
public class Demo
{	
	public static void main(String[] args)
  	{	
		Scanner sc= new Scanner(System.in);	
		System.out.print("enter first string :");
     		String str1 = sc.nextLine(); 
     		System.out.print("enter second string :");
     		String str2 =sc.nextLine();
		if(str1.equals(str2))	
		{	
			System.out.println("both string are equal");	
		}
		else
		{
   			System.out.println("both stings are not equal");
		}
 	}
}
