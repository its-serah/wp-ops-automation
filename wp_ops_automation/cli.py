import typer

from .tasks.demo import demo_login

app = typer.Typer(help="WordPress ops automation toolkit.")


@app.command()
def ping() -> None:
    """
    Quick sanity check command.
    """
    typer.echo("wp-ops-automation is ready.")


@app.command()
def demo_login_task() -> None:
    """
    Run a demo login task against your WordPress site.

    Requires WP_BASE_URL, WP_USERNAME and WP_PASSWORD to be
    configured in your environment or .env file.
    """
    try:
        result = demo_login()
    except Exception as exc:  # noqa: BLE001
        typer.echo(f"[ERROR] Demo login failed: {exc}")
        raise typer.Exit(code=1)

    status = "OK" if result.ok else "FAIL"
    typer.echo(f"[{status}] {result.message}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()

