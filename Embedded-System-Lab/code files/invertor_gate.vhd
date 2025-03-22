library IEEE;
use IEEE.std_logic_1164.all;
entity invertorgate is 
port(
a: in std_logic;
q: out std_logic );
end invertorgate;

architecture art1 of invertorgate is
begin
process(a) is
begin
q <= not a;
end process;
end art1;
