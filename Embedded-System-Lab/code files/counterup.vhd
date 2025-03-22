library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity SOURCE is
    Port ( CLK,RST : in  STD_LOGIC;
             COUNT : inout  STD_LOGIC_VECTOR (3 downto 0));
end SOURCE;

architecture Behavioral of SOURCE is

begin
process (CLK,RST)
begin

if (RST = '1')then
COUNT <= "0000";
elsif(rising_edge(CLK))then
COUNT <= COUNT+1;

end if;
end process;
end Behavioral;

