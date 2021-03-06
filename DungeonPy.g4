grammar DungeonPy;

/*
 * Parser Rules
 */
game                    : setup+ start EOF;

setup                   : entity action+ done;

start                   : START idenity CAMPAIGN;

entity                  : command idenity cmd_type ;

action                  : key value ;

done                    : DONE ;

command                 : ( BEGIN | SET ) ; 

cmd_type                : ( CAMPAIGN | REALM | LOCATION | NPC | PLAYER | LOOT | CREATURE | SHOP | ) ;

key                     : '-'idenity;

value                   : '(' ( STRING',' )+ STRING ')' | STRING | INT ;         

idenity                      : WORD ;

/*
 * Lexer Rules
 */
fragment A              : ('A'|'a') ;
fragment B              : ('B'|'b') ;
fragment C              : ('C'|'c') ;
fragment D              : ('D'|'d') ;
fragment E              : ('E'|'e') ;
fragment G              : ('G'|'g') ;
fragment H              : ('H'|'h') ;
fragment I              : ('I'|'i') ;
fragment L              : ('L'|'l') ;
fragment M              : ('M'|'m') ;
fragment N              : ('N'|'n') ;
fragment O              : ('O'|'o') ;
fragment P              : ('P'|'p') ;
fragment R              : ('R'|'r') ;
fragment S              : ('S'|'s') ;
fragment T              : ('T'|'t') ;
fragment U              : ('U'|'u') ;
fragment Y              : ('Y'|'y') ;
fragment DIGIT          : [0-9] ;
fragment LETTER         : [a-zA-Z_];

BEGIN                   : B E G I N ;

SET                     : S E T ;

START                   : S T A R T ;

LOCATION                : L O C A T I O N ;

CAMPAIGN                : C A M P A I G N ;

PLAYER                  : P L A Y E R ;

LOOT                    : L O O T ;

CREATURE                : C R E A T U R E ;

SHOP                    : S H O P ;

NPC                     : N P C ;

REALM                   : R E A L M ;

DONE                    : D O N E ;

INT                     : DIGIT+ ;

STRING                  : '"'( LETTER | DIGIT )*'"'; 

WORD                    : LETTER+;

WHITESPACE              : [ \r\n]+ -> skip ;  