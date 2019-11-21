program Main;
var x, y : integer;
procedure PlusXAndY();
begin
    x := x + 1;
    y := y + 1;
end;
begin { Main }
    writeln('enter an integer')
    x := readint();
    y := 2;
    writeln('x+y',x+y)
end.  { Main }
