grammar c;

org: line+;

line: '#+TITLE:' one params? NEWLINE  # title
      |'#+CSS: ' path # css
      | HEADER1 WS? one params? NEWLINE  # header1
      | HEADER2 WS? one params? NEWLINE  # header2
      | HEADER3 WS? one params? NEWLINE  # header3
      | content+     # con
      | NEWLINE                 # newline
      ;

path: (ID | '/' | '.')+ # p ;

content: (WS* ID)+ NEWLINE       # con2
         ;

params : '[' exprlist ']' # Para;

exprlist: ID '=' ID # expr ;

one: (WS* ID)+;


NEWLINE : '\r'? '\n' ;
HEADER1: '*' ;
HEADER2: '**' ;
HEADER3: '***' ;
WS : [ \t]+ ;
ID : [0-9a-zA-Z]+;
