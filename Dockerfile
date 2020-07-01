FROM python:3.7

RUN apt-get update \
    && apt-get upgrade -y \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pipのアップデート
    && pip install --upgrade pip

RUN mkdir /python_test
