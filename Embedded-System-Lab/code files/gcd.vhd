LIBRARY IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity gcd_4bit is
Port (a : in STD_LOGIC_VECTOR(3 downto 0);
      b : in STD_LOGIC_VECTOR(3 downto 0);
      gcd : out STD_LOGIC_VECTOR(3 downto 0));
end gcd_4bit;
architecture Behavioral of gcd_4bit is
begin
process(a,b)
variable x,y: STD_LOGIC_VECTOR(3 downto 0);
begin
x := a;
y := b;
while (x/=y) loop
    if (x<y) then
        y := y-x;
    else
        x := x-y;
    end if;
end loop;
gcd<=x;
end process;
end Behavioral;


