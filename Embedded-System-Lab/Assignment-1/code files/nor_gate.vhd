library IEEE;
use IEEE.std_logic_1164.all;
entity norgate is 
port(
a: in std_logic;
b: in std_logic;
q: out std_logic );
end norgate;

architecture art1 of norgate is
begin
process(a,b) is
begin
q <= a nor b;
end process;
end art1;
