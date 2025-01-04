library ieee;
use ieee.std_logic_1164.all;
entity orgate_tb id
end orgate_tb;
architecture behavioral or orgate_tb is
component orgate is
port(x,y : in std_logic;
     z : out std_logic);
end component;
signal X,Y,Z : std_ulogic;
begin
DUT : orgate port map(x,y,z);
stim_proc : process
begin
wait for 10ns;
x_in <= '0';
y_in <= '0';
wait for 10 ns;

x_in <= '0';
y_in <= '1';
wait for 10  ns;

x_in <= '1';
y_in <= '0';
wait for 10 ns;

x_in <= '1';
y_in <= '1';
wait for 10 ns;
end process;
end behavioral;
