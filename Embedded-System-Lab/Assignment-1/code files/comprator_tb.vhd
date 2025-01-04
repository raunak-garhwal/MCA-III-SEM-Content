library IEEE;
use IEEE.std_logic_1164.all;

entity comparatorbench is
--empty
end comparatorbench;

architecture tb of comparatorbench is 

component comparator is
port(
 A : in STD_LOGIC;
 B : in STD_LOGIC;
 G : out STD_LOGIC;
 S : out STD_LOGIC;
 E : out STD_LOGIC);
end component;

--signal a_in, b_in, c_in, q_out, c_out: std_logic;
 
 signal a_in : std_logic := '0';
 signal b_in : std_logic := '0';
 

 signal g_out : std_ulogic;
 signal s_out : std_ulogic;
 signal e_out : std_ulogic;


begin 
DUT : comparator port map(a_in, b_in , g_out, s_out, e_out);

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

a_in <= '0';
b_in <= '0';

wait;
end process;
end tb;

