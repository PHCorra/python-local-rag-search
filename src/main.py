from fastapi import FastAPI
from infra.pg_config import test_add_data, test_show_data

app = FastAPI(
    title="RAG local LLM Server",
    version="1.0",
    description="Sample API with local LLM, RAG and FastAPI"
)


def main():
    test_add_data()

    test_show_data()


if __name__ == "main":
    main()
