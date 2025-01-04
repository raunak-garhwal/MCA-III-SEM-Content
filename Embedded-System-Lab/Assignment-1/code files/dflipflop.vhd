library ieee;
use ieee. std_logic_1164.all;
use ieee. std_logic_arith.all;
use ieee. std_logic_unsigned.all;
 
entity D_FLIPFLOP_SOURCE is
PORT( D,CLOCK: in std_logic;
Q,Qb: out std_logic);
end D_FLIPFLOP_SOURCE;
 
architecture behavioral of D_FLIPFLOP_SOURCE is
begin
process(CLOCK)
begin
if(CLOCK='1') then
Q <= D;
Qb<= not D;


	
--elsif(RST='1') THEN
--Q <= '0';
--Qb <= '1';
end if;
end process;
end behavioral;
