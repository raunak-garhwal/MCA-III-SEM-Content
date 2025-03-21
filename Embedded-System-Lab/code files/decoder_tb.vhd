LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
ENTITY decoderbench IS
END decoderbench;
 
ARCHITECTURE behavior OF decoderbench IS
 
 COMPONENT decoder
 PORT(
 a : IN std_logic_vector(1 downto 0);
 b : OUT std_logic_vector(3 downto 0)
 );
 END COMPONENT;
 
 
 signal a : std_logic_vector(1 downto 0) := (others => '0');
 
 
 signal b : std_logic_vector(3 downto 0);
 
 
BEGIN
 

 uut: decoder PORT MAP (
 a => a,
 b => b
 );
 

 stim_proc: process
 begin
 
 wait for 100 ns;
 
 a <= "00";
 
 wait for 100 ns;
 
 a <= "01";
 
 wait for 100 ns;
 
 a <= "10";
 
 wait for 100 ns;
 
 a <= "11";
 
 wait;
 end process;
 
END; 


