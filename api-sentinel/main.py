import requests
import time
from rich import print
from rich.console import Console
from rich.progress import track

console = Console()


def check_api():

    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments"
    ]

    passed = 0
    failed = 0

    print("""
[green]
 █████╗ ██████╗ ██╗
██╔══██╗██╔══██╗██║
███████║██████╔╝██║
██╔══██║██╔═══╝ ██║
██║  ██║██║     ██║
╚═╝  ╚═╝╚═╝     ╚═╝

      API SENTINEL
[/green]
""")

    with console.status("[bold green]Initializing API Sentinel..."):
        time.sleep(2)

    print("[bold cyan]System Ready[/bold cyan]\n")
    # Startup Spinner
    with console.status("[bold green]Initializing API Sentinel..."):
        time.sleep(2)

    print("[bold cyan]System Ready[/bold cyan]\n")

    # Progress Bar
    for url in track(urls, description="Scanning APIs..."):

        print(f"\n[yellow]Checking:[/yellow] {url}")

        try:

            start_time = time.time()

            response = requests.get(url)

            end_time = time.time()

            response_time = round(end_time - start_time, 3)

            if response.status_code == 200:

                passed += 1

                print("[green]✓ Success[/green]")
                print(f"Status Code : {response.status_code}")
                print(f"Response Time : {response_time} sec")

            else:

                failed += 1

                print("[red]✗ Failed[/red]")
                print(f"Status Code : {response.status_code}")

        except Exception as e:

            failed += 1

            print(f"[bold red]Error:[/bold red] {e}")

        time.sleep(0.5)

    print("\n[bold blue]========== SUMMARY ==========[/bold blue]")
    print(f"[green]Passed:[/green] {passed}")
    print(f"[red]Failed:[/red] {failed}")
    print(f"[cyan]Total APIs:[/cyan] {len(urls)}")


check_api()