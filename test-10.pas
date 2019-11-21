program Main;
var x, y : integer;
procedure PlusXAndY();
begin
    x := x + 1;
    y := y + 1;
end;
begin { Main }
    x := 1;
    y := 0;
    PlusXAndY();
    writeln('x|y',x|y,'1<<2',1<<2)
end.  { Main }
