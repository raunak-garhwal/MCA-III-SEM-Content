library ieee;
use ieee.std_logic_1164.all;

entity multiply_behav_tb is
end multiply_behav_tb;

architecture tb of multiply_behav_tb is

component multiply_behav is
port (A, B : in bit_vector(1 downto 0);
P : out bit_vector(3 downto 0)
);
end component;
signal A, B : bit_vector(1 downto 0);
signal P : bit_vector(3 downto 0);
begin
UUT : multiply_behav port map (
A => A,
B => B,
P => P);


Force:process
constant period: time := 20 ns;
begin
A <= "00";
B <= "00";
wait for period;

A <= "00";
B <= "01";
wait for period;

A <= "00";
B <= "10";
wait for period;

A <= "00";
B <= "11";
wait for period;

A <= "01";
B <= "00";
wait for period;

A <= "01";
B <= "01";
wait for period;

A <= "01";
B <= "10";
wait for period;

A <= "01";
B <= "11";
wait for period;

A <= "10";
B <= "00";
wait for period;

A <= "10";
B <= "01";
wait for period;

A <= "10";
B <= "10";
wait for period;

A <= "10";
B <= "11";
wait for period;

A <= "11";
B <= "00";
wait for period;

A <= "11";
B <= "01";
wait for period;

A <= "11";
B <= "10";
wait for period;

A <= "11";
B <= "11";
wait for period;
wait;
end process;
end tb;








