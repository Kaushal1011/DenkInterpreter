program Main;
var y : real;
procedure Alpha(a : integer; b : integer);
var x : integer;
begin
   x := (a + b ) * 2;
end;
{var x, y : integer;}
begin { Main }
   Alpha(1+2,4);
   Alpha(3,4);
   Alpha(1+2,4); {procedure call}
end.  { Main }
