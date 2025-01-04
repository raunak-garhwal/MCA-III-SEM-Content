library ieee;
use ieee.std_logic_1164.all;
entity and_gaate_tb is
--  Port ( );
end and_gaate_tb;

architecture tb of and_gaate_tb is

component and_gaate is
  Port (A,B:in std_logic;
  Y: out std_logic );
end component;
signal a_in,b_in,c_out:std_ulogic;
begin
DUT: and_gaate port map(a_in,b_in,c_out);

stim_proc:process
begin
a_in <= '0';
b_in <= '0';
wait for 10ns;
a_in <= '1';
b_in <= '0';
wait for 10ns;
a_in <= '0';
b_in <= '1';
wait for 10ns;

a_in <= '1';
b_in <= '1';
wait for 10ns;
end process;
end tb;
