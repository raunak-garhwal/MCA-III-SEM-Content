
library IEEE;
use IEEE.std_logic_1164.all;

entity adderbench is
--empty
end adderbench;

architecture tb of adderbench is 

component full_adder is
port(
 A : in STD_LOGIC;
 B : in STD_LOGIC;
 Cin : in STD_LOGIC;
 S : out STD_LOGIC;
 Cout : out STD_LOGIC);
end component;

--signal a_in, b_in, c_in, q_out, c_out: std_ulogic;
 
 signal a_in : std_logic := '0';
 signal b_in : std_logic := '0';
 signal c_in : std_logic := '0';
 
 
 signal q_out : std_ulogic;
 signal c_out : std_ulogic;


begin 
DUT : full_adder port map(a_in, b_in , c_in, q_out, c_out);

process
begin


a_in <= '0';
b_in <= '1';
c_in <= '0';
wait for 100 ns;

a_in <= '1';
b_in <= '0';
c_in <= '0';
wait for 100 ns;

a_in <= '1';
b_in <= '1';
c_in <= '0';
wait for 100 ns;


a_in <= '0';
b_in <= '0';
c_in <= '1';
wait for 100 ns;

a_in <= '0';
b_in <= '1';
c_in <= '1';
wait for 100 ns;

a_in <= '1';
b_in <= '0';
c_in <= '1';
wait for 100 ns;

a_in <= '1';
b_in <= '1';
c_in <= '1';
wait for 100 ns;



a_in <= '0';
b_in <= '0';
c_in <= '0';
wait;
end process;
end tb;

