FROM python:3.10-slim-buster
WORKDIR /cc-rest

ENV JAVA_HOME=/opt/java/openjdk
COPY --from=eclipse-temurin:17-jre $JAVA_HOME $JAVA_HOME
ENV PATH="${JAVA_HOME}/bin:${PATH}"


# We copy just the requirements.txt first to leverage Docker cache
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH .
EXPOSE 5000
CMD [ "python", "./endpoint/__init__.py" ]
