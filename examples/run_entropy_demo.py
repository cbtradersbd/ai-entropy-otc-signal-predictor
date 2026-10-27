import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from src.signals.predictor_service import PredictorService

console = Console()

def main():
    console.print(Panel("[bold cyan]🔮 AI ENTROPY OTC MARKET MICROSTRUCTURE PREDICTOR[/bold cyan]\n"
                        "[green]Official Telegram Channel:[/green] https://t.me/+R_kEsY9yqkA1NDI1\n"
                        "[magenta]Custom Deep-Learning Bot Orders:[/magenta] @YouKnowWho_am (Telegram)\n"
                        "[yellow]Interactive API Docs:[/yellow] https://api1.api.cbtradersbd.com/docs",
                        title="2027-2030 Viral Machine Learning Technology"))
    
    console.print("[dim]Simulating synthetic OTC tick streams and computing rolling Shannon Entropy...[/dim]\n")
    
    test_runs = [
        ("EURUSD_otc", [1.0850, 1.0852, 1.0855, 1.0858, 1.0862, 1.0865, 1.0870]),
        ("GBPUSD_otc", [1.2650, 1.2648, 1.2651, 1.2649, 1.2652, 1.2647, 1.2650]),
        ("BTCUSD_otc", [64500, 64550, 64620, 64700, 64810, 64950, 65100]),
        ("USDJPY_otc", [155.20, 155.15, 155.18, 155.14, 155.19, 155.13, 155.16])
    ]
    
    table = Table(title="Live OTC Entropy & Markov Regime Output")
    table.add_column("Asset", style="bold")
    table.add_column("Shannon Entropy", justify="right")
    table.add_column("Market Regime", style="cyan")
    table.add_column("Predicted Direction", style="bold green")
    table.add_column("Confidence Winrate", justify="right")
    table.add_column("Signal Action", style="yellow")
    
    for asset, ticks in test_runs:
        res = PredictorService.evaluate(ticks)
        table.add_row(
            asset,
            str(res["entropy"]),
            res["regime"],
            f"[bold green]{res['direction']} 🟢[/bold green]" if res["direction"] == "CALL" else f"[bold red]{res['direction']} 🔴[/bold red]",
            f"{res['winrate_probability']}%",
            f"[bold green]{res['signal_status']}[/bold green]" if "DISPATCH" in res["signal_status"] else "[dim]MUTED[/dim]"
        )
        
    console.print(table)
    console.print("\n[bold green]✓ OTC Entropy simulation completed successfully![/bold green]")

if __name__ == "__main__":
    main()
