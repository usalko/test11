# Environment variables list

Environment variables list:

```:bash
# enable debug mode
DEBUG=True
# disable anonymous user if not empty
# if is empty or false you could connect
# to the service without BPLEX as anonymous user (user with id = 0)
DISABLE_ANONYMOUS_USER=
# enable mass import/export
ENABLE_SHARING_DATA_BETWEEN_ACCOUNTS=True
# enable api exceptions logging
API_EXCEPTIONS_REPORTING=True

# database params
DATABASE_TMS_HOST=pg
DATABASE_TMS_NAME=tms
DATABASE_TMS_USER=tms
DATABASE_TMS_PASSWORD=tms

# BPlex endpoints
BPLEX_ENDPOINT=http://172.17.0.1:8000
BPLEX_PUBLIC_URL=

# Swagger first option for connection
PREFER_HTTP_PROTOCOL=True

# kafka url
KAFKA_URL=kafka1:9092,kafka2:9094

# Loki connection (changes history storage)
LOKI_WRITE_URL=http://loki2:3100
LOKI_READ_URL=http://loki1:3100

# Mobile logs collector
MOBILE_LOGS_URL=http://molog:8804

# S3 Object storage connection (file storage)
S3_URL=minio:9000
S3_PUBLIC_URL=minio:9001

# Redis connection (cache)
REDIS_URL=redis://redis:6379/0

# Chat bot settings
# Wnen settings is empty read from /home/deploy/apps/.chat-bot-token
CHAT_BOT_PUBLIC_URL=https://t.me/<bot name>
CHAT_BOT_TOKEN=
CHAT_BOT_INTERNAL_WEBHOOK_URL=
CHAT_BOT_EXTERNAL_WEBHOOK_URL=
CHAT_BOT_TTL_IN_MINUTES=

# Anonymous mobile login for pass google-play checking
ANONYMOUS_EMPLOYEE_PHONE=+7
ANONYMOUS_REGISTRATION_CODE=908235
DISABLE_ANONYMOUS_EMPLOYEE=

# Integration settings
TRAFFIC_ONLINE_GET_TOKEN_ENDPOINT=https://demo.traffic.online/api/v1/auth/token
CONTINUOUS_INTEGRATION=
CONTINUOUS_INTEGRATION_MINIMAL_TIME_BETWEEN_GET_USER_DATA=60
```
