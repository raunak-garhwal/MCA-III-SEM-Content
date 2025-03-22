library IEEE;
use IEEE.std_logic_1164.all;

-- Entity declaration

entity or_gate is

    port(a: in std_logic;      
         b: in std_logic;     
         c: out std_logic);    

end or_gate;

-- Dataflow Modelling Style
-- Architecture definition

architecture orLogic of or_gate is

begin
process(a,b) is
begin
    
    c<= a or b;
end process;


end orLogic; 
