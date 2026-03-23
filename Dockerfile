FROM python:3.10-slim

ARG RUN_ID

RUN echo "Simulating model download for Run ID: ${RUN_ID}"

CMD ["sh", "-c", "echo Container started for Run ID: ${RUN_ID}"]
