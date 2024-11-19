import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Solution {
    
    static class SortbyHeight implements Comparator<Struct>
        {
            
        }
    static class Struct{
        int h,ind;
        Struct(int h,int ind){
            this.h=h;
            this.ind=ind;
        }
    }

    public static void main(String[] args) throws java.lang.Exception {
        // your code goes here
        FastReader scn = new FastReader();
        int t, k, i, j, l, f, max=0;
        t=scn.nextInt();
        while(t-->0){
            int n=scn.nextInt();
            int m=scn.nextInt();
            int x=scn.nextInt();
            Struct a[]=new Struct[n];
            for (i=0;i<n;i++){
                a[i]=new Struct(scn.nextInt(),i);
            }
            Arrays.sort(a,new SortbyHeight());
            int b[]=new int[n];
            int ms=1;
            for (i=0;i<n;i++){
                if (ms>m){
                    ms=1;
                }
                b[a[i].ind]=ms;
                ms++;
            }
            System.out.println("YES");
            for (i=0;i<n;i++){
                System.out.print(b[i]+" ");
            }
            System.out.println();
        }   
    }
}
