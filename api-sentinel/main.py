import requests
import time
from rich import print


def check_api():

    url = "https://jsonplaceholder.typicode.com/users"

    print("[yellow]Sending API Request...[/yellow]")

    try:
        # Start Timer
        start_time = time.time()

        # Send Request
        response = requests.get(url)

        # End Timer
        end_time = time.time()

        # Calculate Response Time
        response_time = round(end_time - start_time, 3)

        # Validate Status Code
        if response.status_code == 200:

            print("[green]✓ API Request Successful[/green]")

            data = response.json()

            print("\n[cyan]First User Details:[/cyan]")
            print(f"Name : {data[0]['name']}")
            print(f"Email: {data[0]['email']}")

            print(
                f"\n[bold blue]Response Time:[/bold blue] {response_time} seconds"
            )

        else:

            print("[red]✗ API Request Failed[/red]")
            print(f"Status Code: {response.status_code}")

    except Exception as e:

        print(f"[bold red]Error:[/bold red] {e}")



check_api()