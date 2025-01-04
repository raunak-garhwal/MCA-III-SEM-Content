library IEEE;
use IEEE.std_logic_1164.all;
entity full_adder is 
port(
 A : in STD_LOGIC;
 B : in STD_LOGIC;
 Cin : in STD_LOGIC;
 S : out STD_LOGIC;
 Cout : out STD_LOGIC );
end full_adder;

architecture rt1 of full_adder is
begin
process(A,B, Cin) is
begin

 S <= A XOR B XOR Cin ;
 Cout <= (A AND B) OR (Cin AND A) OR (Cin AND B) ;

end process;
end rt1;
