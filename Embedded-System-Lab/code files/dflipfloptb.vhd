library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity DFF_tb is
end DFF_tb;

architecture tb of DFF_tb is

component D_FLIPFLOP_SOURCE is
Port ( D, CLOCK: in STD_LOGIC;
Q, Qb : out STD_LOGIC);
end component ;

signal D, CLK,Q, Qb : STD_ULOGIC;

begin
uut: D_FLIPFLOP_SOURCE port map(
D => D,
CLOCK => CLK,

Q => Q,
Qb => Qb);

clock:process
begin
CLK <='0';
wait for 100 ns;
CLK <='1';
wait for 100 ns;
end process;

stim:process
begin

D <='0';
wait for 150 ns;
D <='1';
wait for 150 ns;


end process;
end tb;
