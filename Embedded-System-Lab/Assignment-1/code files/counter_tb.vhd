library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity sync_upcounter_tb is
end entity;

architecture tb of sync_upcounter_tb is
component SOURCE is
Port ( CLK,RST : in STD_LOGIC;
COUNT : inout STD_LOGIC_VECTOR (3 downto 0));
end component;

signal CLK,RST : STD_LOGIC := '1';
signal COUNT : STD_LOGIC_VECTOR(3 downto 0);

begin

uut: SOURCE port map(
CLK => CLK,
RST => RST,
COUNT => COUNT);

clock: process
begin

RST <= '0';

CLK <= '0';
wait for 20 ns;
CLK <= '1';
wait for 20 ns;

end process;
end tb;

