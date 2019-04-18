NB. run with:
NB. j asm.ijs filename.asm

NB.                     setup
NB. Initialize Symbol Table (ST) with builtin keywords
NB. each row of this array is (key;address)
ST =: ('SCREEN';dfh'4000'),:'KBD';dfh'6000'                      NB. screen and keyboard
ST =: ST, (<"0 i.5),.~;:'SP LCL ARG THIS THAT'                   NB. keywords
ST =: ST, (<"0 i.16),.~'R'&,@":&.>i.16                           NB. R0-R15


NB.                     symbol resolution
NB. Pass #1, labels
NB. Scan the file and for each (LABEL), append to a label look-up table the key-value pair
NB. where LABEL is the key and the value is the address of the next instruction.

ins =: a:-.~((' ',TAB,CR)-.~'/'&taketo) each cutLF fread 2{ARGV  NB. remove comment/whitespace lines
isl =: '('e.S:0]                                                 NB. is a label?
labels =: ((}.@}:)each #~ isl) ins                               NB. just the labels
laddr =: <"0 (-i.@#)I. isl ins                                   NB. address of instruction after (label)
ST =: ST,labels,.laddr
ac =: ins #~ -. isl ins                                          NB. A and C instructions - need symbol resolution

NB. Pass #2, variables
NB. Scan the file and for each new variable name found, append (key;address) to ST, starting at address 16.

num =: '0123456789'
nn =: }.each(#~(num -.@e.~ {.)@}.&>)~.(#~'@'e.&>]) ac            NB. @name might be LABEL or variable
ST =: ST,(,.<"0@(16+i.@#)) (#~ ({."1 ST) -.@e.~]) nn             NB. filter out existing ST names, only vars remain


NB.                     code generation
NB. C instruction
NB. lookup tables for jmp, dst:
'jmp dst' =: <"2(<"1 #:i.8),.~"1]_8&{.@;:"1 'JGT JEQ JGE JLT JNE JLE JMP',:'M D MD A AM AD AMD'
comptab =: cut&>cutLF (0 :0)                                     NB. lookup table for cmp
0    1 0 1 0 1 0
1    1 1 1 1 1 1
-1   1 1 1 0 1 0
D    0 0 1 1 0 0
A    1 1 0 0 0 0  M
!D   0 0 1 1 0 1
!A   1 1 0 0 0 1  !M
-D   0 0 1 1 1 1
-A   1 1 0 0 1 1  -M
D+1  0 1 1 1 1 1
A+1  1 1 0 1 1 1  M+1
D-1  0 0 1 1 1 0
A-1  1 1 0 0 1 0  M-1
D+A  0 0 0 0 1 0  D+M
D-A  0 1 0 0 1 1  D-M
A-D  0 0 0 1 1 1  M-D
D&A  0 0 0 0 0 0  D&M
D|A  0 1 0 1 0 1  D|M
)
compbits =: ".&>(}.@}:)"1 comptab
ca1 =: compbits (4 :'(y,.<"1 (1 1 1 1,"1 x))#~(a:~:y)') {:"1 comptab
ca0 =: (<"1]1 1 1 0,"1 compbits),.~{."1 comptab
cmp =: ca0,ca1
lookup =: 4 :' ({:"1 x) {~ (<,y) ss {."1 x'
cproc =: (3 :0)                                                  NB. @ccut
c =. cmp lookup '=' taketo    &.|.   ';' taketo y
d =. dst lookup '=' takeafter &.|. y
j =. jmp lookup ';' takeafter y
;c,d,j
)
NB. Pass #3, replace symbols with addresses
NB. Replace @name with value based on lookup from symbol table
aproc =: ST&(4 :'>({:"1 x) {~ ({."1 x) i. <y') :: ".

proc =: cproc`((_16{.#:)@aproc@}.)@.('@'e.])
code =: proc each ac
hack =: LF,~LF joinstring(' '-.~":) each code

(3 :0) ARGV
if. 4=#y do.
 hack fwrite 3{y
 exit''
else.
 echo hack
                                                                 NB. exit''
end.
)

NB. $ time j asm.ijs pong/Pong.asm  # 28375 lines, about 60kLOC/s 
NB. (intel i7 workstation)
NB. real    0m0.497s
NB. user    0m0.459s
NB. sys     0m0.020s
NB. (arm64 laptop)
NB. real    0m1.214s
NB. user    0m1.174s
NB. sys     0m0.039s
