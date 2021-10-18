
Command:
 		lex lexer.l

		yacc -d grammer.y

		gcc -o valStm lex.yy.c grammer.tab.c -w

testCase-1 : 	valStm.exe sample.txt     

NOUN    ==>Sachin
VERB    ==>is
NOUN    ==>student

SIMPLE SENTENCE

testCase-2 : valStm.exe sample.txt
NOUN    ==>Sachin
VERB    ==>is
NOUN    ==>boy
CONJUNCTION     ==>and
PRONOUN ==>he
VERB    ==>is
NOUN    ==>student

COMPOUND SENTENCE

