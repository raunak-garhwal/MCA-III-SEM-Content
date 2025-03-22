library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity comparator is
    Port ( A,B : in std_logic;
           G,S,E: out std_logic);
end comparator;

architecture comp_arch of comparator is
  begin
   G <= A and (not B);
   S <= (not A) and B;
   E <= A xnor B;
end comp_arch;

