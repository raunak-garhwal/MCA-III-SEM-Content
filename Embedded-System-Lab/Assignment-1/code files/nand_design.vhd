library ieee;
use ieee.std_logic_1164.all;

entity nand_design is
 port(
    a : in std_logic;
    b : in std_logic;
    c : out std_logic);
end nand_design;

architecture data_nand of nand_design is
begin 
  c <= a nand b;
end data_nand;
