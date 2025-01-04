library IEEE;
use IEEE.std_logic_1164.all;
entity xnorgate is 
port(
a: in std_logic;
b: in std_logic;
q: out std_logic );
end xnorgate;

architecture art1 of xnorgate is
begin
process(a,b) is
begin
q <= a xnor b;
end process;
end art1;

