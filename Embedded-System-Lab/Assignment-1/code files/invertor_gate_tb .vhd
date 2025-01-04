library IEEE;
use IEEE.std_logic_1164.all;

entity invertorgatetb is
end invertorgatetb;

architecture tb of invertorgatetb is 

component invertorgate is
port(
a: in std_logic;
q: out std_logic);
end component;

signal a_in, q_out: std_ulogic;

begin 
DUT : invertorgate port map(a_in, q_out);

process
begin
a_in <= '0';
wait for 100 ns;


a_in <= '1';
wait for 100 ns;


a_in <= '0';
wait;
end process;
end tb;
