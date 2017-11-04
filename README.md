Steps for execution:

1. install rabbitMQ
2. create "celery_out" exchange and bind "outgoing" queue to it
2. install Celery
3. run "celery -A tasks worker --loglevel=info"
4. run "python run.py 1000"