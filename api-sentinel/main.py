import requests
from rich import print

url = "https://jsonplaceholder.typicode.com/users"

print("[yellow]Sending API Request...[/yellow]")

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("[green]✓ API Request Successful[/green]")

        data = response.json()

        print("\n[cyan]First User Details:[/cyan]")
        print(f"Name : {data[0]['name']}")
        print(f"Email: {data[0]['email']}")

    else:
        print(f"[red]✗ API Failed[/red]")
        print(f"Status Code: {response.status_code}")

except Exception as e:
    print(f"[bold red]Error:[/bold red] {e}")