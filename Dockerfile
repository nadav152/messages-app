# pull official python base image
FROM python:3.10-slim

# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r $APP_USER && useradd --no-log-init -r -g $APP_USER $APP_USER

# set environment variables
# 1st variable -> Prevents Python from writing pyc files to disc (equivalent to python -B option)
# 2nd variable -> Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED=1

# Install packages needed to run your application (not build deps):
RUN set -ex \
    && RUN_DEPS=" \
    libpcre3 \
    mime-support \
    binutils \
    gdal-bin \
    python3-gdal \
    libgdal-dev \
    libproj-dev \
    libpq-dev \ 
    postgresql-client \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

# set work directory
# create the appropriate directories
ENV APP_HOME=/code
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
RUN pip install --upgrade pip
COPY requirements.txt /$APP_HOME/
RUN pip install -r requirements.txt

# copy project and install project dependencies
COPY . $APP_HOME

# Change to a non-root user
RUN chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER:$APP_USER
