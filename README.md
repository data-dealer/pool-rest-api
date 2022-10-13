# pool-rest-api


To focus on testing, documentation and instructions, I chose Django REST framework as rest-api for these reasons:
- Simplicity, flexibility, quality, and test coverage of source code.
- Compatible with both ORM and non-ORM data sources.
- Provides most of the frameworks as all-inclusive to develop a complete REST API

To focus on clean [architecture and code] + full deliverable, I chose the stack below (I think database is needed):
- Docker + Django REST framework + Nginx + Postgres



# Start guide

run all with "startpoint.sh" or flow each step below:

## 1. Start api with docker-docker-compose
```bash
docker-compose build
docker-compose up -d
```

## 2. Migrate our models
```bash
docker-compose exec restapi python manage.py makemigrations app
docker-compose exec restapi python manage.py migrate app
```



## 3. Run test
restapi/test/test_api.py

```sh
docker-compose exec restapi python manage.py test app
```
the result:
```
Ran 3 tests in 0.022s
OK
```

## 4. Document
http://localhost/doc/



---------
# Endpoint 

> first POST endpoint receives a JSON in the form of a document with two fields: a pool-id (numeric) and a pool-values (array of values) and is meant to append (if pool already exists) or insert (new pool) the values to the appropriate pool (as per the id)


## First endpoint: http://localhost/api/pool

```bash
# first post to create new pool
curl --location --request POST 'localhost/api/pool' \
--header 'Content-Type: application/json' \
--data-raw '{
    "poolId": 1234,
    "poolValues": [
      1,
      2,
      3,
      4
    ]
}'
# return 201 Created
```

```bash
# second post to append pool value
curl --location --request POST 'localhost/api/pool' \
--header 'Content-Type: application/json' \
--data-raw '{
    "poolId": 1234,
    "poolValues": [
      5,
      6
    ]
}'
# return 200 Ok
```

```bash
# get all pool
curl --location --request GET 'localhost/api/pool'
```

## Second endpoint: http://localhost/api/poolQuantile
> second POST is meant to query a pool, the two fields are pool-id (numeric) identifying the queried pool, and a quantile (in percentile form)

```bash
curl --location --request POST 'localhost/api/poolQuantile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "poolId": 1234,
    "percentile": 95.5
}'
```

the quantile function:

```python
def quantile(arr:list, q:float):
    """
    Parameters
    ----------
    arr : Input array.
    q : Quantile in range(1, 100) 
    ----------
    Test
    have the same result with numpy.quantile
    """
    arr = sorted(arr)
    index = (len(arr)-1) * q/100
    floor = int(index//1)
    ceil = int(-(-index//1))
    return arr[floor] * (ceil-index) + arr[ceil] * (index - floor)
```

