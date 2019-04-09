  // c_2.asm file
  @0
D=M
@INFINITE_LOOP
  D;JLE
  @counter

  M=D  // test
  @SCREEN
D=A

  @address
M=D
   	0;JMP
