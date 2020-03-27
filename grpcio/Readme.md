# grps

Instalar las dependencias de requirements.txt y generar el código con:

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. get_value.proto
```

