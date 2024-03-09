# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7
ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Install Tesseract OCR, PortAudio library and its dependencies
RUN --mount=type=cache,target=/root/.cache/apt-get \
    apt-get update
RUN --mount=type=cache,target=/root/.cache/apt-get \
    apt-get install -y --no-install-recommends \
    curl \
    tesseract-ocr \
    libtesseract-dev \
    libportaudio2 \
    portaudio19-dev \
    alsa-utils \
    mpg123

# Set the TESSDATA_PREFIX environment variable
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

# Download the Telugu language data file if it's not included in the package
RUN --mount=type=cache,target=/root/.cache/tesseract \
    curl -L -o ${TESSDATA_PREFIX}/te.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/tel.traineddata

ARG REPOSITORY_NAME=image2speech_te
ARG REPOSITORY_PATH=/${REPOSITORY_NAME}

# Copy the source code into the container.
COPY . ${REPOSITORY_PATH}

# Change the current working directory to the copied source code directory.
WORKDIR ${REPOSITORY_PATH}

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install poetry

# Install poetry packages globally inside docker
RUN poetry config virtualenvs.create false

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/poetry to speed up subsequent builds.
# Leverage a bind mount to pyproject.toml to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/poetry \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    poetry install

# Clean up
RUN apt-get clean
