// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Scanner;
class revStr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
       // System.out.println(str);
        String nstr="",res="";
        char ch;
        String[] words = str.split(" ");
        //System.out.println(words[0]);
        for(int i =0;i<words.length;i++){
             for (int j=0;j<words[i].length(); j++)
            {
                ch= words[i].charAt(j); 
                nstr= ch+nstr;
             }
       // System.out.println(words[i]);
       res = res+" "+nstr;
       System.out.println(res);
        }
       // System.out.println(res.substring(1)+"\n");
    }
}