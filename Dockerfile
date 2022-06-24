FROM jbenjoseph/nevua:base-latest
LABEL maintainer="JJ Ben-Joseph (jj@memoriesofzion.org)" \
      description="This project contains a dashboard and forecasting algorithms tuned currently for the COVID-19 outbreak. [Application Container]"
EXPOSE 8080
CMD uwsgi --http :8080 --module nevua.app:SERVER
COPY nevua /app/nevua
WORKDIR /app
