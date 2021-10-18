/*
 * 
 * Simple recursive descent parser & interpreter
 * 
 * Example valid input: a=3;b=2;c=+ab;!c.
 * Example invalid input: a=+12;!a.b
 * 
 */
command :
Javac ParserInterpreter.java
java  ParserInterpreter 
input  : 
	testcase-1: a=3;b=2;c=+ab;!c.
	output: 5

	testcase2:  a=+12;!a.b
        output: syntax error

