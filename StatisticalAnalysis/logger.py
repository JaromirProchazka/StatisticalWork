import StatisticalAnalysis.StatisticalAnalysis
from tabulate import tabulate
from typing import Self

class _StatLogger:
    def __init__(self) -> None:
        self._rows: list = list()
        self._add_header()
    
    def _add_header(self):
        self._rows.append(['Line Count', 'Block size [B]', 'Associativity', 'Lambda'])
    
    def log(self) -> None:
        print(tabulate(self._rows))
    
    def add_row(self, line_cont: int, bloc_size: int, associativity: int, lambda_res: float) -> Self:
        self._rows.append([line_cont, bloc_size, associativity, lambda_res])
        return self
    
    def clear_rows(self) -> Self:
        self._rows.clear()
        self._add_header()
        return self
