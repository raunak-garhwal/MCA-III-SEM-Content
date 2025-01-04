
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity sync_downcounter_tb is
end entity;

architecture tb of sync_downcounter_tb is
component down_count is
Port ( clk,rst : in STD_LOGIC;
count : out STD_LOGIC_VECTOR (3 downto 0));
end component;

signal clk, rst : STD_LOGIC := '1';
signal count : STD_LOGIC_VECTOR(3 downto 0);

begin

uut: down_count port map(
clk => clk,
rst => rst,
count => count);

clock: process
begin

rst <= '0';

clk <= '0';
wait for 20 ns;
clk <= '1';
wait for 20 ns;

end process;
end tb;