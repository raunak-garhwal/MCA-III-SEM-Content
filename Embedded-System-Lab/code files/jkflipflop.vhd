library ieee;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity JK_FF is
	port( J, K, clk : in std_logic;
		Q, Qbar : out std_logic);
end JK_FF;

architecture behavioral of JK_FF is
begin
process(clk)
variable qn : std_logic;
begin

if(clk'event and clk = '1')then
if(J='0' and K='0')then
qn := qn;
elsif(J='0' and K='1')then
qn := '0';
elsif(J='1' and K='0')then
qn := '1';
elsif(J='1' and K='1')then
qn := not qn;
else
null;
end if;
else
null;
end if;
Q <= qn;
Qbar <= not qn;

end process;
end behavioral;
