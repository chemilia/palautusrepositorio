# Login Project Guidelines

- This is a `uv` project. Run project commands with `uv run ...` from the `viikko3/Login` directory.

## Architecture

- `src/app.py` contains the Flask application and route handlers. Routes render Jinja templates or translate service outcomes into redirects and flash messages.
- Business validation belongs in `src/services/user_service.py`. `UserService` validates registration input and checks login credentials before using the repository.
- `src/repositories/user_repository.py` is the in-memory user store used by the application and by the test reset endpoint. Do not add persistence assumptions to the current implementation.
- Templates are in `src/templates/`. Browser acceptance tests are in `src/tests/`; `resource.robot` contains shared Browser setup, URLs, and keywords, while `AppLibrary.py` provides HTTP helpers for test setup.

## Build and Test

Install or synchronize dependencies with:

```bash
uv sync
```

Start the application from the `viikko3/Login` directory. The application listens on port `5001`:

```bash
uv run flask --app src/app.py run --host 127.0.0.1 --port 5001
```

The Robot Framework tests require the application to be running on port `5001`. In a
separate terminal, run all acceptance tests with:

```bash
uv run robot src/tests
```

Run one suite or one test case:

```bash
uv run robot src/tests/register.robot
uv run robot -t "Register With Valid Username And Password" src/tests/register.robot
```

Resolve Robot Framework keywords without opening a browser:

```bash
uv run robot --dryrun src/tests/home.robot src/tests/login.robot src/tests/register.robot
```

Check Python syntax for a changed module:

```bash
uv run python -m py_compile src/services/user_service.py
```

## Conventions

- Browser tests use the `Browser` library with two spaces between Robot Framework keyword arguments. Reuse shared keywords from `src/tests/resource.robot` rather than duplicating browser setup or URL variables.
- Acceptance tests expect the application at `http://localhost:5001`. `AppLibrary.py` resets the in-memory repository through `/tests/reset` and creates setup users through `/register`.
- Username and password validation happens in `UserService.validate` in `src/services/user_service.py`. Login credential checks happen in `UserService.check_credentials` in the same file.
- User-facing validation failures are raised as exceptions in `UserService`, displayed with Flask `flash`, and verified in Robot tests by checking the returned page body. Preserve the existing error-message text when changing validation behavior.
- Registration success redirects to `/welcome`; successful login redirects to `/ohtu`. Keep these route-to-template flows aligned with the corresponding tests and page titles.
- The repository is intentionally in-memory for this exercise. Tests must reset state between cases and should not rely on users created by another test.
