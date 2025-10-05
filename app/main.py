def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        # "errors" to lista przeformatowanych błędów
        "errors": [
            {
                # przenosimy numer linii do klucza "line"
                "line": e["line_number"],
                "column": e["column_number"],
                "message": e["text"],
                "name": e["code"],
                "source": "flake8"
            } for e in errors
        ],
        # dodajemy ścieżkę do pliku
        "path": file_path,
        # status passed jeśli nie ma błędów, failed jeśli są błędy
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # tworzymy listę słowników, po jednym dla każdego pliku w raporcie
    return [
        {
            # "errors" to lista przeformatowanych błędów dla tego pliku
            "errors": [
                {
                    # numer linii w nowym kluczu "line"
                    "line": e["line_number"],
                    # numer kolumny w nowym kluczu "column"
                    "column": e["column_number"],
                    # Treść błędu w kluczu "messege"
                    "message": e["text"],
                    # Kod błędu w kluczu "name"
                    "name": e["code"],
                    # Źródło błędu stałe "flake8"
                    "source": "flake8"
                }
                # literujemy po wszystkich błędach dla danego pliku
                for e in errors
            ],
            # ścieżka do pliku
            "path": file_path,
            # status pliku: passed jeśli brak błędów, failed jeśli są
            "status": "passed" if not errors else "failed"
        }
        # literujemy po wszystkich plikach w linter_report
        for file_path, errors in linter_report.items()
    ]
