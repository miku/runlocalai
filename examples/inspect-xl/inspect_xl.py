#!/usr/bin/env -S uv run --script
#
# /// script
# dependencies = [
#   "openpyxl>=3.1",
#   "xlrd>=2.0",
#   "rich>=13",
# ]
# ///

import sys
from pathlib import Path

import openpyxl
import xlrd
from rich.console import Console  # type: ignore
from rich.table import Table  # type: ignore
from rich.panel import Panel  # type: ignore
from rich.text import Text  # type: ignore

console = Console()


def inspect_xlsx(filepath: Path) -> None:
    wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)

    file_size = filepath.stat().st_size
    size_str = (
        f"{file_size / 1024:.1f} KB"
        if file_size < 1024 * 1024
        else f"{file_size / (1024 * 1024):.2f} MB"
    )

    console.print(
        Panel(
            f"[bold]File:[/] {filepath}\n"
            f"[bold]Format:[/] XLSX (Office Open XML)\n"
            f"[bold]Size:[/] {size_str}\n"
            f"[bold]Sheets:[/] {len(wb.sheetnames)}",
            title="📊 XLSX File Info",
            border_style="blue",
        )
    )

    for name in wb.sheetnames:
        ws = wb[name]
        max_row = ws.max_row or 0
        max_col = ws.max_column or 0

        console.print()
        console.print(f'  📋 [bold cyan]Sheet: "{name}"[/]')
        console.print(f"     Dimensions : {max_row} rows × {max_col} cols")
        console.print(f"     Cells      : ~{max_row * max_col:,}")

        # Preview first rows
        if max_row > 0 and max_col > 0:
            table = Table(show_header=True, header_style="bold magenta")
            for col_idx in range(1, min(max_col + 1, 11)):
                table.add_column(f"Col {col_idx}", max_width=30)

            for row_idx, row in enumerate(
                ws.iter_rows(min_row=1, max_row=min(max_row, 10), values_only=True), 1
            ):
                if row_idx > 10:
                    break
                table.add_row(
                    *[str(c) if c is not None else "[dim]None[/]" for c in row[:10]]
                )

            console.print(table)
            if max_col > 10:
                console.print(f"     [dim]... {max_col - 10} more columns[/]")
            if max_row > 10:
                console.print(f"     [dim]... {max_row - 10} more rows[/]")

    wb.close()


def inspect_xls(filepath: Path) -> None:
    wb = xlrd.open_workbook(str(filepath))

    file_size = filepath.stat().st_size
    size_str = (
        f"{file_size / 1024:.1f} KB"
        if file_size < 1024 * 1024
        else f"{file_size / (1024 * 1024):.2f} MB"
    )

    console.print(
        Panel(
            f"[bold]File:[/] {filepath}\n"
            f"[bold]Format:[/] XLS (BIFF{wb.biff_version})\n"
            f"[bold]Size:[/] {size_str}\n"
            f"[bold]Sheets:[/] {wb.nsheets}",
            title="📊 XLS File Info",
            border_style="green",
        )
    )

    for idx in range(wb.nsheets):
        sheet = wb.sheet_by_index(idx)
        console.print()
        console.print(f'  📋 [bold cyan]Sheet: "{sheet.name}"[/]')
        console.print(f"     Dimensions : {sheet.nrows} rows × {sheet.ncols} cols")
        console.print(f"     Cells      : ~{sheet.nrows * sheet.ncols:,}")

        if sheet.nrows > 0 and sheet.ncols > 0:
            table = Table(
                show_header=True, header_style="bold magenta", max_col_width=30
            )
            for col_idx in range(min(sheet.ncols, 10)):
                table.add_column(f"Col {col_idx + 1}")

            for row_idx in range(min(sheet.nrows, 10)):
                row_vals = []
                for col_idx in range(min(sheet.ncols, 10)):
                    cell = sheet.cell(row_idx, col_idx)
                    val = str(cell.value) if cell.value != "" else "[dim]None[/]"
                    row_vals.append(val)
                table.add_row(*row_vals)

            console.print(table)
            if sheet.ncols > 10:
                console.print(f"     [dim]... {sheet.ncols - 10} more columns[/]")
            if sheet.nrows > 10:
                console.print(f"     [dim]... {sheet.nrows - 10} more rows[/]")


def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Usage:[/] uv run inspect_xl.py <file.xls|xlsx>")
        console.print(
            "Displays information and a preview of XLS/XLSX spreadsheet files."
        )
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        console.print(f"[bold red]Error:[/] File not found: {filepath}")
        sys.exit(1)

    suffix = filepath.suffix.lower()

    if suffix == ".xlsx":
        inspect_xlsx(filepath)
    elif suffix == ".xls":
        inspect_xls(filepath)
    else:
        console.print(
            f"[bold red]Error:[/] Unsupported format '{suffix}'. Use .xls or .xlsx files."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
