library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
entity down_count is
    Port ( clk,rst : in  STD_LOGIC;
           count : out  STD_LOGIC_VECTOR (3 downto 0));
end down_count;

architecture Behavioral of down_count is

signal temp:std_logic_vector(3 downto 0);
begin
process(clk,rst)
begin

if(rst='1')then
temp<="1111";
elsif(rising_edge(clk))then
temp<=temp-1;
end if;
end process;

count<=temp;
end Behavioral;
