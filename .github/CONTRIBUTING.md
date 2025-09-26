# Contributing

1. [Fork the repository.][fork]  
2. [Create a topic branch.][branch]  
3. Install the necessary dependencies using `uv sync` (please note that you'll also require [uv](https://github.com/astral-sh/uv) installed).  
4. Implement your feature or bug fix.  
5. Don't forget to add tests and make sure they pass by running `uv run pytest`. Tests will be linted automatically.  
6. Make sure your code complies with the style guide by running `uv run ruff check`. You can also auto-fix issues with: `uv run ruff check --fix` and `uv run black .`.
7. We use type hinting so check if everything is okay by running `uv run pyright`.
8. If necessary, add documentation for your feature or bug fix.
9. Commit and push your changes.
10. [Submit a pull request.][pr]

[fork]: http://help.github.com/fork-a-repo/
[branch]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches
[pr]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
