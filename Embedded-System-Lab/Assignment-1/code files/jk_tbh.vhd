library ieee;
use ieee.std_logic_1164.all;

entity JK_FF_tb is
end JK_FF_tb;

architecture testbench of JK_FF_tb is

component JK_FF is
port(J, K, clk: in std_logic;
Q, Qbar : out std_logic
);
end component;

signal J, K, clk: std_logic;
signal Q, Qbar : std_ulogic;

begin
uut: JK_FF port map(
J => J,
K => K,
clk => clk,

Q => Q,
Qbar => Qbar);

clock: process
begin
clk <= '0';
wait for 200 ns;
clk <= '1';
wait for 200 ns;
end process;

Force: process
begin
J <= '0';
K <= '0';

wait for 200 ns;

J <= '0';
K <= '1';

wait for 200 ns;

J <= '1';
K <= '0';

wait for 200 ns;

J <= '1';
K <= '1';

wait for 200 ns;

J <= '1';
K <= '1';

wait for 200 ns;




end process;
end testbench;
