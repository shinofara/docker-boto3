docker-boto3
===============

alpine 3.4


## Usage

```
$ docker run --rm -t \
    -v ~/.aws:/home/worker/.aws:ro \
    -v /path/to/src/dir:/work \
    shinofara/docker-boto3 <commnad>
```

### Example

```
$ docker run --rm -t \
    -v $HOME/.aws:/home/worker/.aws:ro \
    -v ${pwd}/example:/work \
    shinofara/docker-boto3 python example.py
```
