
library ieee;
use ieee.std_logic_1164.all;

entity multiply_behav is 
  port (A, B : in bit_vector(1 downto 0);
        P : out bit_vector(3 downto 0)
    );
end multiply_behav;

architecture behavioral of multiply_behav is
begin
	process(A,B) is
	begin
		case A is
			when "00" =>
				if B="00" then P<="0000";
                                elsif B="01" then P<="0000";
				elsif B="10" then P<="0000";
				else P<="0000";
				end if;
			when "01" =>
				if B="00" then P<="0000";
				elsif B="01" then P<="0001";
				elsif B="10" then P<="0010";
				else P<="0011";
				end if;
			when "10" =>
				if B="00" then P<="0000";
				elsif B="01" then P<="0010";
				elsif B="10" then P<="0100";
				else P<="0110";
				end if;
			when "11" =>
                                if B="00" then P<="0000";
				elsif B="01" then P<="0011";
				elsif B="10" then P<="0110";
				else P<="1001";
				end if;
		end case;
end process;
end architecture;
