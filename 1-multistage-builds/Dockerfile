FROM gcc:latest as build
WORKDIR /app
COPY hello.c .
RUN gcc -o hello hello.c

FROM alpine:latest
WORKDIR /app
RUN apk add --no-cache libc6-compat && rm -rf /var/cache/apk/*
COPY --from=build /app/hello .
ENTRYPOINT ["./hello"]