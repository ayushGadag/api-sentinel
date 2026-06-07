import requests
import time
from rich import print


def check_api():

    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments"
    ]

    passed = 0
    failed = 0

    print("\n[bold cyan]API Sentinel Started[/bold cyan]\n")

    for url in urls:

        print(f"[yellow]Checking:[/yellow] {url}")

        try:
            start_time = time.time()

            response = requests.get(url)

            end_time = time.time()

            response_time = round(end_time - start_time, 3)

            if response.status_code == 200:

                passed += 1

                print("[green]✓ Success[/green]")
                print(f"Status Code : {response.status_code}")
                print(f"Response Time : {response_time} sec\n")

            else:

                failed += 1

                print("[red]✗ Failed[/red]")
                print(f"Status Code : {response.status_code}\n")

        except Exception as e:

            failed += 1

            print(f"[bold red]Error:[/bold red] {e}\n")

    print("[bold blue]========== SUMMARY ==========[/bold blue]")
    print(f"[green]Passed:[/green] {passed}")
    print(f"[red]Failed:[/red] {failed}")
    print(f"[cyan]Total APIs:[/cyan] {len(urls)}")


check_api()