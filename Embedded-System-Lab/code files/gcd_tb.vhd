
library ieee;
use ieee.std_logic_1164.all;
USE ieee.numeric_std.ALL;

entity gcd_tb is
end gcd_tb;

architecture tb of gcd_tb is

component gcd_4bit is
port (a,b: in STD_LOGIC_vector(3 downto 0);
gcd:OUT STD_LOGIC_vector(3 downto 0));
end component;

signal a: std_logic_vector(3 downto 0);
signal b:  std_logic_vector(3 downto 0);
signal gcd_out:STD_LOGIC_vector(3 downto 0);
begin
uut : gcd_4bit port map (

a=>a,
b=>b,
gcd => gcd_out);



process
constant period: time := 100 ns;
begin
a <= "1100";
b <="1000";
wait for period;


a <= "0110";
b <="1001";
wait for period;
wait;
end process;
end tb;
