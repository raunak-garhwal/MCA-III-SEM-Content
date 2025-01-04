library IEEE;
use IEEE.std_logic_1164.all;

-- Entity declaration

entity and_gaate is

    port(A : in std_logic;      
         B : in std_logic;     
         Y : out std_logic);    

end and_gaate;

-- Dataflow Modelling Style
-- Architecture definition

architecture andLogic of and_gaate is

begin
process(A,B) is
begin
    
    Y <= A AND B;
end process;


end andLogic; 
