FROM python:3.7.8-slim as base
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gcc libffi-dev g++ libpq-dev python3-venv python3-wheel git curl telnet
#RUN git config --global --unset https.proxy || true
#RUN git config --global --unset http.proxy || true
WORKDIR /store
FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN python -m venv /venv

# RUN . /venv/bin/activate && pip install -U "pip"
RUN . /venv/bin/activate && curl https://bootstrap.pypa.io/get-pip.py | python -

RUN . /venv/bin/activate && pip install cython wheel
RUN . /venv/bin/activate && pip install --upgrade pip

# copies the current directory to the container
COPY . .
RUN . /venv/bin/activate && pip install --no-deps -r ./requirements.txt

FROM base as final
COPY --from=builder /venv /venv

COPY ./docker/local/docker-entrypoint.sh ./

RUN bash -c "chmod +x ./docker-entrypoint.sh"

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait

# adds some nice formatting to the bash terminal
ENV TERM xterm-256color
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
# sources the django env, activates the venv, adds some color
RUN bash -c "mkdir /root/.oh-my-bash/themes/meld-shell"
COPY ./docker/local/store/term/bash.rc /root/.bashrc
COPY ./docker/local/store/term/meld-shell.theme.sh /root/.oh-my-bash/themes/meld-shell

RUN chmod +x /wait