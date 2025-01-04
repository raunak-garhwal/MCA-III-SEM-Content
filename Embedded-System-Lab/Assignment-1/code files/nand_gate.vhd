library IEEE;
use IEEE.std_logic_1164.all;
entity nandgate is 
port(
a: in std_logic;
b: in std_logic;
q: out std_logic );
end nandgate;

architecture art1 of nandgate is
begin
process(a,b) is
begin
q <= a nand b;
end process;
end art1;
