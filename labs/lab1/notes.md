Calculate formatting penalty & apply

a special Line is annotated, (AnnotatedLine)
WhitespaceManger is introduced to the Line
UnwrappedLineFormatter (& other classes) analyze the Line and modify Whitespacemanger

! grep 'return Penalty *'
! some things are parsed UnwrappedLineParser (<>, sth else?)
! Swift has a Lexer.cpp that is ready for use with LLVM
! need to also implement DryRun mode (identify the required modifications/violations but do not fix them)