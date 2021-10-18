command:
     lex javaToken.l 
     gcc -o jtoken lex.yy.c
     jtoken.exe myJava.java
