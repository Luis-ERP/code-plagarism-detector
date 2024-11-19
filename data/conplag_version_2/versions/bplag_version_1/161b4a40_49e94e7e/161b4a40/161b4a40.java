import java.io.BufferedReader;
import java.io.IOException;
import java.lang.*;
import java.io.InputStreamReader;
import static java.lang.Math.*;
import static java.lang.System.out;
import java.util.*;
import java.io.File;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.math.BigInteger;
public class Main {
 
	
	/* 10^(7) = 1s.
	 * ceilVal = (a+b-1) / b */
	
	static final int mod = 1000000007;
	static final long temp = 998244353;
	static final long MOD = 1000000007;
	static final long M = (long)1e9+7;
 
	
	static class Pair implements Comparable<Pair> 
	{
		int first, second;
		
		public Pair(int first, int second) 
		{
			this.first = first;
			this.second = second;
		}
		
		public int compareTo(Pair ob) 
		{
			return (int)(first - ob.first);
		}
	}
	
	
	static class Tuple implements Comparable<Tuple>
	{
		int first, second,third;
		public Tuple(int first, int second, int third)
		{
			this.first = first;
			this.second = second;
			this.third = third;
		}
		public int compareTo(Tuple o)
		{
			return (int)(o.third - this.third);
		}
	}
	
	public static class DSU
	{
		int[] parent;
		int[] rank; //Size of the trees is used as the rank
		public DSU(int n)
		{
			parent = new int[n];
			rank = new int[n];
			Arrays.fill(parent, -1);
			Arrays.fill(rank, 1);
		}
		
		public int find(int i) //finding through path compression
		{
			return parent[i] < 0 ? i : (parent[i] = find(parent[i]));
		}
		
		public boolean union(int a, int b) //Union Find by Rank 
		{
			a = find(a);
			b = find(b);
			
			if(a == b) return false; //if they are already connected we exit by returning false.
			
			// if a's parent is less than b's parent
			if(rank[a] < rank[b])
			{
				//then move a under b
				parent[a] = b;
			}
			//else if rank of j's parent is less than i's parent
			else if(rank[a] > rank[b])
			{
				//then move b under a
				parent[b] = a;
			}
			//if both have the same rank.
			else
			{
				//move a under b (it doesnt matter if its the other way around.
				parent[b] = a;
				rank[a] = 1 + rank[a];
			}
			return true;
		}	
	}

	static class Reader 
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		
		int[] readArray(int n) throws IOException {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		
		long[] longReadArray(int n) throws IOException {
			long[] a=new long[n];
			for (int i=0; i<n; i++) a[i]=nextLong();
			return a;
		}
		
		long nextLong() {
			return Long.parseLong(next());
		}
		double nextDouble() {
			return Double.parseDouble(next());
		}
	}
	
	public static int gcd(int a, int b)
	{
		if(b == 0)
		 return a;
		
		else
		return gcd(b,a%b);
	} 
 
		public static long lcm(long a, long b)
	    {
	        return (a / LongGCD(a, b)) * b;
	    }
	
	public static long LongGCD(long a, long b)
	{
		if(b == 0)
			 return a;
			
			else
			return LongGCD(b,a%b);
	}
	
		public static long LongLCM(long a, long b)
	    {
	        return (a / LongGCD(a, b)) * b;
	    }
	
		//Count the number of coprime's upto N
		public static long phi(long n)  //euler totient/phi function
	    { 
	       long ans = n;
//	       for(long i = 2;i*i<=n;i++)
//	       {
//	    	   if(n%i == 0)
//	    	   {
//	    		   while(n%i == 0) n/=i;
//	    		   ans -= (ans/i);
//	    	   }
//	       }
//	       
//	       if(n > 1)
//	       {
//	    	   ans -= (ans/n);
//	       }
	       
	       for(long i = 2;i<=n;i++)
	       {
	    	   if(isPrime(i))
	    	   {
	    		   ans -= (ans/i);
	    	   }
	       }
	       
	       return ans;
	       
	    }	
	
	public static long fastPow(long x, long n) 
	{
		if(n == 0)
			return 1;
		else if(n%2 == 0)
			return fastPow(x*x,n/2);
		else
			return x*fastPow(x*x,(n-1)/2);
	}
	
	   public static long modPow(long x, long y, long p)
	    {
	        long res = 1;
	        x = x % p;
	 
	        while (y > 0) {
	            if (y % 2 == 1)
	                res = (res * x) % p;
	 
	            y = y >> 1; 
	            x = (x * x) % p;
	        }
	        return res;
	    }
	   
	   static long modInverse(long n, long p)
	    {
	        return modPow(n, p - 2, p);
	    }
	 
	    // Returns nCr % p using Fermat's little theorem.
	    
	    public static long nCrModP(long n, long r,long p)
	    {
	    	if (n<r) 
	              return 0;
	          
	        if (r == 0)
	            return 1;
	 
	        long[] fac = new long[(int)(n) + 1];
	        fac[0] = 1;
	 
	        for (int i = 1; i <= n; i++)
	            fac[i] = fac[i - 1] * i % p;
	 
	        return (fac[(int)(n)] * modInverse(fac[(int)(r)], p)
	                % p * modInverse(fac[(int)(n - r)], p)
	                % p)
	            % p;
	    }
	    
	    public static long fact(long n) 
	    {
	    	  long[] fac = new long[(int)(n) + 1];
		        fac[0] = 1;
		 
		        for (long i = 1; i <= n; i++)
		            fac[(int)(i)] = fac[(int)(i - 1)] * i;
		        
		        return fac[(int)(n)];
		}
	    
	    public static long nCr(long n, long k) 
	    {
			long ans = 1;
			for(long i = 0;i<k;i++)
			{
				ans *= (n-i);
				ans /= (i+1);
			}
			return ans;
		}
 
		//Modular Operations for Addition and Multiplication. 
		   public static long perfomMod(long x)
		   {
		        return ((x%M + M)%M);
		    }
		   public static long addMod(long a, long b)
		   {
		        return perfomMod(perfomMod(a)+perfomMod(b));
		    }
		  
		   public static long subMod(long a, long b)
		   {
		        return perfomMod(perfomMod(a)-perfomMod(b));
		   }
		   
		   public static long mulMod(long  a, long b)
		   {
		        return perfomMod(perfomMod(a)*perfomMod(b));
		   }
		   
		   public static boolean isPrime(long n) 
			{
				if(n == 1)
				{
					return false;
				}
				
				//check only for sqrt of the number as the divisors 
				//keep repeating so only half of them are required. So,sqrt.
				for(int i = 2;i*i<=n;i++)
				{
					if(n%i == 0)
					{
						return false;
					}
				}
				return true;
			}
			
			public static List<Integer> SieveList(int n)
			{
				boolean prime[] = new boolean[(int)(n+1)];
				Arrays.fill(prime, true);
				
				List<Integer> l = new ArrayList<>();
				for (int p = 2; p*p<=n; p++) 
				{ 
					if (prime[p] == true) 
					{ 	
					    for(int i = p*p; i<=n; i += p) 
						{
						    prime[i] = false; 
						}	
					} 
				} 
		 
				for (int p = 2; p<=n; p++) 
				{
				    if (prime[p] == true)
				    {
				       l.add(p); 
				    }
				}
				
				return l;
			}
			
			public static int countDivisors(int x)
			{
				int c = 0;
				for(int i = 1;i*i<=x;i++)
				{
					if(x%i == 0)
					{
						if(x/i != i)
						{
							c+=2;
						}
						else 
						{
							c++;
						}
					}
				}
				return c;
			}
			
			public static long log2(long n)
		    {
				 long ans = (long)(log(n)/log(2));
				 return ans;
			}
			   
			public static boolean isPow2(long n)
			{
				 return (n  != 0 && ((n & (n-1))) == 0);
			}	
		   
		   public static boolean isSq(int x)  
		   {
			    long s = (long)Math.round(Math.sqrt(x));
			    return s*s==x;
		   }
		
			   /*
			    * 
			    * >=         <=
			   0 1 2 3 4 5 6 7  
			   5 5 5 6 6 6 7 7
			   lower_bound for 6 at index 3 (>=)
			   upper_bound for 6 at index 6(To get six reduce by one) (<=)
			   */

		   public static int LowerBound(int a[], int x) 
		   {
			      int l=-1,r=a.length;
				  while(l+1<r) 
				  {
				    int m=(l+r)>>>1;
				    if(a[m]>=x) r=m;
				    else l=m;
				  }
				  return r;
			}
		   
			public static int UpperBound(long a[], long x) 
			{
				int l=-1, r=a.length;
			    while(l+1<r) 
			    {
			       int m=(l+r)>>>1;
			       if(a[m]<=x) l=m;
			       else r=m;
			    }
			    return l+1;
			}
			
			public static void Sort(long[] a) 
			{
				List<Long> l = new ArrayList<>();
				for (long i : a) l.add(i);
				Collections.sort(l);
//				Collections.reverse(l);  //Use to Sort decreasingly 
				for (int i=0; i<a.length; i++) a[i]=l.get(i);
			}
			
			public static void ssort(char[] a)
			{
				List<Character> l = new ArrayList<>();
				for (char i : a) l.add(i);
				Collections.sort(l);
				for (int i=0; i<a.length; i++) a[i]=l.get(i);
			}
	
	
	public static void main(String[] args) throws Exception 
	{
		Reader sc = new Reader();
		PrintWriter fout = new PrintWriter(System.out); 
		
		int tt = sc.nextInt();
		while(tt-- > 0)
		{
	       int n = sc.nextInt();
	       char[] a = sc.next().toCharArray(), b = sc.next().toCharArray();
	       
	       int c00 = 0, c01 = 0, c10 = 0, c11 = 0;
	       for(int i = 0;i<n;i++)
	       {
	    	   if(a[i] == '0' && b[i] == '0')
	    	   {
	    		   c00++;
	    	   }
	    	   else if(a[i] == '0' && b[i] == '1')
	    	   {
	    		   c01++;
	    	   }
	    	   else if(a[i] == '1' && b[i] == '0')
	    	   {
	    		   c10++;
	    	   }
	    	   else if(a[i] == '1' && b[i] == '1')
	    	   {
	    		   c11++;
	    	   }
	       }
	       
	       int ans = mod;
	       if(c01 == c10) ans = min(ans, c01 + c10);
	       if(c11 == c00 + 1) ans = min(ans, c11 + c00);
	       
	       fout.println((ans == mod) ? -1 : ans);
		}
		
		fout.close();
	}
}