program Main;
var x, y : integer;
var a:string;
procedure PlusXAndY();
begin
    x := x + 1;
    y := y + 1;
end;
begin { Main }
    x := readint();
    y := 2;
    a := 'HMM';

    writeln('Hello',x+y,a)
end.  { Main }
