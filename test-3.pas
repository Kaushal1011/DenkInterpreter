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
    x:=x+2;
    y:=y+2;

end.  { Main }
