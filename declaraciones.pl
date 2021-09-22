padre_de(juan,maria).
padre_de(pablo,juan).
padre_de(pablo,marcela).
padre_de(carlos,debora).

hijo_de(A,B):-padre_de(B,A).
abuelo_de(A,B):-padre_de(A,C),padre_de(C,B).
hermano_de(A,B):-padre_de(C,A),padre_de(C,B),A\==B.
familiar_de(A,B):-padre_de(A,B).
familiar_de(A,B):-hijo_de(A,B).
familiar_de(A,B):-hermano_de(A,B).