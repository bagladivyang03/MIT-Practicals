/*
 * 
 * Simple recursive descent parser & interpreter
 * 
 * Example valid input: a=3;b=2;c=+ab;!c.
 * Example invalid input: a=+12;!a.b
 * 
 */
import java.util.Scanner;

// CFG
/* Program = Stmtlist .
 * StmtList = Stmt NextStmt
 * NextStmt = ; Stmtlist | E
 * Stmt = Assign | Print
 * Assign = Id = Expr
 * Print = ! Id
 * Expr = + Expr Expr
 * 		| - Expr Expr
 * 		| * Expr Expr 
 * 		| / Expr Expr
 * 		| Id
 * 		| Const
 * Id = a | b | c
 * Const = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
 * 
 */



public class ParserInterpreter {
	
	  private static char token;
	  private static String input;
	  private static int a = -99, b = -99,c = -99;
	  private static int index;
	  
	  public static void main(String argv[]) {
		  
		Scanner scanner = new Scanner(System.in);
		input = scanner.next();
		scanner.close();
		
		index = 0;
		updateToken();
		
		/* Parse input and check if matches grammar, recursive descent*/
		program();
	
		/* Evaluates input */
		index = -1;
	    while (index < input.length()) {
	    	eval();
	    }
	    
	  }
	  
	public static void program () {
			stmtlist();
			if (token == '.') {
			match('.');
			if (index != input.length()) {
				System.out.println("syntax error\n");
				System.exit(-1);
			}
			}
			else {
			    System.out.println("syntax error\n");
				System.exit(-1);
			}
		}
	
	public static void stmtlist () {
		stmt();
		nextstmt();
	}
	
	public static void nextstmt() {
		if (token == ';') {
		match(';');
		stmtlist();
		}
		else {
			//epsilon
		}
		
	}
	
	public static void stmt () {
		assign();
		print();
	}
	
	public static void assign() {
		if (token >= 'a' && token <= 'c') {
		match('v'); //should be variable
		match('=');
		expr();
		}
	}
	
	public static void print() {
		if (token == '!') {
		match('!');
		match('v'); //should be variable
		}
	}
	
	public static void expr() {
		if (token == '+') {
			match('+');
			expr();
			expr();
		}
		else if (token == '-') {
			match('-');
			expr();
			expr();
		}
		else if (token == '*') {
			match('*');
			expr();
			expr();
		}
		else if (token == '/') {
			match('/');
			expr();
			expr();
		}
		else if (token - '0' >= 0 && token -'0' <= 9){
			match('n');
		}
		else if (token >= 'a' && token <= 'c') {
			match('v');
		}
		else {
			System.out.println("exception");
			System.exit(-1);
		}
	}
	
	public static void match (char c) {
		if (token == '!' || token == '+' || token == ';' || token == '/' || token == '*' || token == '-' || token == '=' || token == '.') {
			getToken();
		}
		else if (c == 'v' && token >= 'a' && token <= 'c') {
		    getToken();
		}
		else if (c == 'n' && token - '0' >= 0 && token -'0' <= 9) {
			getToken();
		}
		else {
			System.out.println("synxtax error");
		}
	}
	  
	  // getToken - advance to the next token on the input
	  private static void getToken()  {
		index++;
		if (index >= input.length()) {
			return;
		}
	    token = input.charAt(index);
	  }

	  
	  private static int eval() {
		  
		getToken();
		  
	    if (token == '-') { //check for operator, consume next two inputs
	      return eval() - eval();
	    }
	    
	    else if (token == '+') {
		     return eval() + eval();
	    }
	    else if (token == '!')
	    {
	      int ret = eval();
	      System.out.println(ret);
	      return ret;
	      //print out value of lookahead token, needs to be moved to own method
	    }
	    else if (token == '/')
	    {
	      if (input.charAt(index+=2) == '0') {
	    	 System.out.println("exception");
	    	 System.exit(-1);
	      }
		  return eval() / eval();
	    }
	    
	    else if (token == '*') {
	    	return eval() * eval();
	    }
	    

	   else if (token >= 'a' && token <= 'c') {
		   if (lookAhead() == '=')
			   return assignVal();
		   else {
			   if (token == 'a') {
				   if (a == -99) {
					   System.out.println("exception");
					   System.exit(0);
				   }
				   else {
					   return a;
				   }
			   }
			   if (token == 'b') {
					if (b == -99) {
					   System.out.println("exception");
					   System.exit(0);
					   }
					   else {
						   return b;
					   }
			   }
			  if (token == 'c') {
					if (c == -99) {
					  System.out.println("exception");
					  System.exit(0);
						   }
						   else {
							   return c;
						   }
			  		}
		   	  }
	   }
	       
	    else if (token - '0' <= 9) {
	      return token - '0';
	    }
	    
	    else if (token == ';') {
	    	return 0;
	    }
	    
	      System.out.println("exception");
	      System.exit(-1);
	      return -1;
	  }
	
	  
	 public static int assignVal() {
		 
		    	if (token == 'a') {
		    		index+=1;
		    		updateToken();
		    		a = eval();
		    		return a;
		    	}
		    	else if (token == 'b') {
		    		index+=1;
		    		updateToken();
		    		b = eval();
		    		return b;
		    	}
		    	else if (token == 'c') {
		    		index+=1;
		    		updateToken();
		    		c = eval();
		    		return c;
		    	}
		    	
			return -1;
		}
	  
	  private static void updateToken() {
		  token = input.charAt(index);
	  }
	  
	  private static char lookAhead () {
		  if (index + 1 < input.length()) {
			  return input.charAt(index+1);
		  }
		  else {
			  System.out.println("syntax error");
			  System.exit(-1);
			  return '0';
		  }
	  }
	}