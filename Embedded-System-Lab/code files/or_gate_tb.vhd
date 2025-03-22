library IEEE;
use IEEE.std_logic_1164.all;

entity or_gate_tb is
end or_gate_tb ;

architecture t of or_gate_tb is 

component or_gate is
port(
a: in std_logic;
b: in std_logic;
c: out std_logic);
end component;

signal a_in, b_in, q_out: std_ulogic;

begin 
DUT : or_gate port map(a_in, b_in , q_out);

process
begin
a_in <= '0';
b_in <= '0';
wait for 100 ns;

a_in <= '0';
b_in <= '1';
wait for 100 ns;

a_in <= '1';
b_in <= '0';
wait for 100 ns;

a_in <= '1';
b_in <= '1';
wait for 100 ns;


end process;
end t;